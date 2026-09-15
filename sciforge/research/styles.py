"""引用样式转换：解析后的引用（dict 或 BibTeX 字符串）→ 五样式渲染。

样式：APA 7.0、Chicago（Notes 与 Author-Date 两种）、MLA 9、IEEE、Vancouver。
确定性正则解析，stdlib only。作者/年份/标题/期刊/卷期页字段缺失时优雅降级
（渲染标注 (missing)，结果同时返回 missing 字段清单）。
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

STYLES = ["apa", "chicago-notes", "chicago-author-date", "mla", "ieee", "vancouver"]

_MISSING = "(missing)"

_FIELDS = ["author", "title", "journal", "year", "volume", "number",
           "pages", "doi", "url", "publisher"]


@dataclass
class Citation:
    """规范化引用：authors 为 [{family, given}]，given 为完整名（可空）。"""
    authors: list = field(default_factory=list)
    year: str = ""
    title: str = ""
    journal: str = ""
    volume: str = ""
    number: str = ""
    pages: str = ""
    doi: str = ""
    url: str = ""
    publisher: str = ""
    missing: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "authors", "year", "title", "journal", "volume", "number",
            "pages", "doi", "url", "publisher", "missing",
        )}


def _norm_cit(cit) -> Citation:
    """Citation / dict 统一为 Citation。"""
    if isinstance(cit, Citation):
        return cit
    if isinstance(cit, dict):
        authors = []
        for a in cit.get("authors", []):
            authors.append(a if isinstance(a, dict) else _parse_name(a))
        return Citation(
            authors=authors, year=str(cit.get("year", "") or ""),
            title=cit.get("title", ""), journal=cit.get("journal", "")
            or cit.get("venue", ""), volume=str(cit.get("volume", "") or ""),
            number=str(cit.get("number", "") or cit.get("issue", "") or ""),
            pages=str(cit.get("pages", "") or ""), doi=cit.get("doi", ""),
            url=cit.get("url", ""), publisher=cit.get("publisher", ""),
        )
    raise TypeError(f"不支持的引用类型: {type(cit).__name__}")


def parse_bibtex(text: str) -> Citation:
    """确定性正则解析 BibTeX 条目 → Citation。无字段时全部标 missing。"""
    cit = Citation()
    if not text or not text.strip():
        cit.missing = list(_FIELDS)
        return cit
    for name in _FIELDS:
        m = re.search(
            rf"\b{name}\s*=\s*[{{\"](.*?)[}}\"]\s*,?\s*\n", text,
            re.IGNORECASE | re.DOTALL,
        )
        if not m:
            m = re.search(rf"\b{name}\s*=\s*(\d+)", text, re.IGNORECASE)
            if not m:
                continue
            setattr(cit, name, m.group(1))
            continue
        val = re.sub(r"\s+", " ", m.group(1)).strip().strip("{}")
        if not val:
            continue
        if name == "author":
            cit.authors = [
                _parse_name(a.strip()) for a in re.split(r"\s+and\s+", val) if a.strip()
            ]
        else:
            setattr(cit, name, val)
    cit.missing = _missing_fields(cit)
    return cit


def from_hit(hit: dict) -> Citation:
    """OpenAlex 精简结构（survey/lit 检索结果）→ Citation。"""
    return _norm_cit(hit)


def _parse_name(s: str) -> dict:
    """解析单个作者名：'Family, Given' 或 'Given Family' 或 'Family'。"""
    s = (s or "").strip()
    if not s:
        return {"family": "", "given": ""}
    if "," in s:
        family, _, given = s.partition(",")
        return {"family": family.strip(), "given": given.strip()}
    toks = s.split()
    if len(toks) >= 2:
        return {"family": toks[-1], "given": " ".join(toks[:-1])}
    return {"family": s, "given": ""}


def _initials(given: str) -> str:
    return " ".join(f"{t[0]}." for t in given.split() if t and t[0].isalpha())


def _missing_fields(cit: Citation) -> list[str]:
    req = {"year": cit.year, "title": cit.title, "journal": cit.journal,
           "volume": cit.volume, "number": cit.number, "pages": cit.pages}
    out = [k for k, v in req.items() if not str(v or "").strip()]
    if not cit.authors:
        out.insert(0, "authors")
    return out


def _authors_apa(cit: Citation) -> str:
    names = [f"{a['family']}, {_initials(a['given'])}".strip(", ")
             for a in cit.authors]
    if not names:
        return _MISSING
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} & {names[1]}"
    return ", ".join(names[:-1]) + f", & {names[-1]}"


def _authors_chicago(cit: Citation) -> str:
    if not cit.authors:
        return _MISSING
    first = f"{cit.authors[0]['family']}, {cit.authors[0]['given']}".strip(", ")
    rest = []
    for a in cit.authors[1:]:
        rest.append(f"{a['given']} {a['family']}".strip() or a["family"])
    if not rest:
        return first
    if len(rest) == 1:
        return f"{first}, and {rest[0]}"
    return f"{first}, {', '.join(rest[:-1])}, and {rest[-1]}"


def _authors_mla(cit: Citation) -> str:
    if not cit.authors:
        return _MISSING
    first = f"{cit.authors[0]['family']}, {cit.authors[0]['given']}".strip(", ")
    if len(cit.authors) == 1:
        return first
    if len(cit.authors) == 2:
        second = f"{cit.authors[1]['given']} {cit.authors[1]['family']}".strip()
        return f"{first}, and {second}"
    return f"{first}, et al."


def _authors_ieee(cit: Citation) -> str:
    names = [f"{_initials(a['given'])} {a['family']}".strip() for a in cit.authors]
    if not names:
        return _MISSING
    return " and ".join(names)


def _authors_vancouver(cit: Citation) -> str:
    names = [f"{a['family']} {_initials(a['given']).replace('. ', ' ').rstrip('.')}"
             for a in cit.authors]
    if not names:
        return _MISSING
    if len(names) > 6:
        return ", ".join(names[:6]) + ", et al."
    return ", ".join(names)


def _pages(text: str) -> str:
    p = str(text or "").strip()
    if not p:
        return _MISSING
    return re.sub(r"\s*--\s*|\s*-\s*", "–", p)


def render(cit, style: str) -> dict:
    """渲染为指定样式。返回 {ok, style, citation, missing}；样式未知/引用为空/输入为空时失败。"""
    if not str(cit or "").strip() and not isinstance(cit, Citation):
        # 空字符串/None 等直接失败（兼容测试 render("", "apa")）
        return {"ok": False, "error": "引用为空"}
    if not str(style or "").strip():
        return {"ok": False, "error": "样式不能为空"}
    style = style.strip().lower()
    if style not in STYLES:
        return {"ok": False, "error": f"未知样式: {style}（可选: {', '.join(STYLES)}）"}
    c = _norm_cit(cit)
    if not any((c.title, c.journal, c.authors, c.doi)):
        return {"ok": False, "error": "引用为空（无标题/作者/期刊/DOI）",
                "style": style, "citation": "", "missing": c.missing}
    fn = {
        "apa": _apa, "chicago-notes": _chicago_notes,
        "chicago-author-date": _chicago_ad, "mla": _mla,
        "ieee": _ieee, "vancouver": _vancouver,
    }[style]
    return {"ok": True, "style": style, "citation": fn(c), "missing": c.missing}


def render_all(cit) -> dict:
    """一次渲染全部样式。返回 {ok, styles: {style: rendered}, missing}。"""
    c = _norm_cit(cit)
    out: dict[str, str] = {}
    for s in STYLES:
        r = render(c, s)
        out[s] = r.get("citation", "") if r["ok"] else ""
    return {"ok": True, "styles": out, "missing": c.missing}


def _year(c: Citation) -> str:
    return str(c.year or "").strip() or _MISSING


def _title(c: Citation) -> str:
    return (c.title or "").strip() or _MISSING


def _journal(c: Citation) -> str:
    return (c.journal or "").strip() or _MISSING


def _apa(c: Citation) -> str:
    s = f"{_authors_apa(c)} ({_year(c)}). {_title(c)}. {_journal(c)}"
    if c.volume:
        s += f", {c.volume}"
        if c.number:
            s += f"({c.number})"
    if c.pages:
        s += f", {_pages(c.pages)}"
    s += "."
    if c.doi:
        s += f" https://doi.org/{c.doi}"
    elif c.url:
        s += f" {c.url}"
    return s


def _chicago_notes(c: Citation) -> str:
    s = f"{_authors_chicago(c)}. “{_title(c)}.” {_journal(c)}"
    if c.volume:
        s += f" {c.volume}"
        if c.number:
            s += f", no. {c.number}"
    s += f" ({_year(c)})"
    if c.pages:
        s += f": {_pages(c.pages)}"
    return s + "."


def _chicago_ad(c: Citation) -> str:
    s = f"{_authors_chicago(c)}. {_year(c)}. “{_title(c)}.” {_journal(c)}"
    if c.volume:
        s += f" {c.volume}"
        if c.number:
            s += f" ({c.number})"
    if c.pages:
        s += f": {_pages(c.pages)}"
    s += "."
    if c.doi:
        s += f" doi:{c.doi}"
    return s


def _mla(c: Citation) -> str:
    s = f"{_authors_mla(c)}. “{_title(c)}.” {_journal(c)}"
    if c.volume:
        s += f", vol. {c.volume}"
        if c.number:
            s += f", no. {c.number}"
    s += f", {_year(c)}"
    if c.pages:
        s += f", pp. {_pages(c.pages)}"
    return s + "."


def _ieee(c: Citation) -> str:
    s = f"{_authors_ieee(c)}, “{_title(c)},” {_journal(c)}"
    if c.volume:
        s += f", vol. {c.volume}"
        if c.number:
            s += f", no. {c.number}"
    if c.pages:
        s += f", pp. {_pages(c.pages)}"
    s += f", {_year(c)}."
    if c.doi:
        s += f" doi: {c.doi}."
    return "[1] " + s


def _vancouver(c: Citation) -> str:
    s = f"{_authors_vancouver(c)}. {_title(c)}. {_journal(c)}."
    s += f" {_year(c)}"
    if c.volume:
        s += f";{c.volume}"
        if c.number:
            s += f"({c.number})"
    if c.pages:
        s += f":{_pages(c.pages)}"
    if c.doi:
        s += f". doi:{c.doi}"
    return s + "."
