"""参考文献工具：DOI 核验 → BibTeX 生成 → 批量导出。

全部走免 key 公开接口（Crossref / OpenAlex）。离线模式返回模板占位。
"""
from __future__ import annotations

import re
from sciforge.research import lit


_DOI_RE = r"10\.\d{4,9}/[^\s,)]+"


def _doi_from_input(s: str) -> str | None:
    m = re.search(_DOI_RE, s or "", re.IGNORECASE)
    return m.group(0) if m else None


def ref_to_bibtex(doi: str) -> dict:
    """通过 Crossref 免 key API 获取 DOI 对应 BibTeX。"""
    import urllib.parse
    import urllib.request
    import json

    clean = _doi_from_input(doi)
    if not clean:
        return {"ok": False, "error": "无法从输入中提取 DOI"}

    if lit._offline():
        return _fallback_bibtex(clean)

    url = "https://api.crossref.org/works/" + urllib.parse.quote(clean)
    req = urllib.request.Request(url, headers={"User-Agent": lit._USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        msg = data.get("message", {})
        authors = []
        for a in msg.get("author", []):
            given = a.get("given", "")
            family = a.get("family", "")
            if given or family:
                authors.append(f"{family}, {given}".strip(", "))
        title = (msg.get("title") or [""])[0]
        year = msg.get("published-print", msg.get("published-online", {})).get("date-parts", [[0]])[0][0]
        venue = msg.get("container-title", [""])[0] if msg.get("container-title") else ""
        bib = f"@article{{ref,\n"
        bib += f"  author = {{{' and '.join(authors)}}},\n"
        bib += f"  title = {{{title}}},\n"
        bib += f"  journal = {{{venue}}},\n"
        bib += f"  year = {{{year}}},\n"
        bib += f"  doi = {{{clean}}}\n"
        bib += "}\n"
        return {"ok": True, "doi": clean, "bibtex": bib}
    except Exception as e:
        return {"ok": False, "doi": clean, "error": f"Crossref API 错误: {e}"}


def _fallback_bibtex(doi: str) -> dict:
    """离线模板占位。"""
    return {"ok": True, "doi": doi, "bibtex":
            f"@article{{placeholder,\n"
            f"  author = {{Unknown}},\n"
            f"  title = {{(离线模式，请联网获取）}},\n"
            f"  year = {{????}},\n"
            f"  doi = {{{doi}}}\n"
            f"}}\n", "offline": True}


def batch_ref_export(text: str) -> dict:
    """从文本中提取所有 DOI，批量生成 BibTeX。"""
    dois = list(dict.fromkeys(re.findall(_DOI_RE, text, re.IGNORECASE)))
    if not dois:
        return {"ok": False, "error": "文本中未找到 DOI", "bibtex": ""}
    entries = []
    missing = []
    for doi in dois:
        r = ref_to_bibtex(doi)
        if r["ok"]:
            entries.append(r["bibtex"])
        else:
            missing.append(doi)
    return {
        "ok": True,
        "count": len(dois),
        "bibtex": "\n".join(entries),
        "missing": missing,
    }
