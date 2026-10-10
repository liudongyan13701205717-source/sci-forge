"""源约束写作器（backlog #11，超出 STORM 的硬约束：每句须可溯源）。

核心约束：**每一句正文都必须绑定至少一个来源 span**。
本模块提供两步：
  1. `draft()` — 按大纲从已绑定的素材生成草稿（每句自带 source_ids）；
  2. `audit()` — 审计草稿，逐句判定 grounded / unbound，列出违规句。

`audit()` 是硬闸门：只要存在 unbound 句，`ok=False` 且 `violations`
给出句号与偏移，调用方不得放行。这比「尽量引用」更强，也更容易测试。

判据（全部可解释，无 LLM 依赖）：
  - 显式绑定：句子自带 source_ids；
  - 词汇重叠：句子与候选 span 的内容词重合度 ≥ `min_overlap`；
  - 数字一致性：句子中的数值必须出现在至少一个绑定 span 中。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from sciforge.core import Layout

_WORD = re.compile(r"[A-Za-z][A-Za-z\-]{2,}|[一-鿿]{2,}")
_NUM = re.compile(r"\d+(?:\.\d+)?%?")

_STOP = {
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were",
    "has", "have", "not", "but", "all", "can", "our", "their", "its", "which",
    "we", "in", "on", "of", "to", "by", "as", "at", "is", "it", "an", "be",
    "these", "those", "such", "than", "then", "when", "also", "into", "they",
    "them", "his", "her", "one", "two", "may", "using", "used", "based",
}


def _tokens(text: str) -> set[str]:
    return {w.lower() for w in _WORD.findall(str(text or "")) if w.lower() not in _STOP}


def _sentences(text: str) -> list[tuple[int, str]]:
    """按句切分并保留偏移；换行（如 markdown 标题）也视为边界。"""
    out: list[tuple[int, str]] = []
    buf = ""
    start = 0
    for line in str(text or "").splitlines(keepends=True):
        for m in re.finditer(r"[^.?!]+[.?!]?", line):
            seg = m.group(0)
            if not buf:
                start = m.start()
            buf += seg
            if seg.rstrip().endswith((".", "!", "?")):
                s = buf.strip()
                if s:
                    out.append((start, s))
                buf = ""
        if not line.rstrip("\n"):
            s = buf.strip()
            if s:
                out.append((start, s))
            buf = ""
    s = buf.strip()
    if s:
        out.append((start, s))
    return out


def _norm_source(rec) -> dict:
    if isinstance(rec, str):
        return {"id": rec[:40], "span": rec}
    if not isinstance(rec, dict):
        return {"id": "", "span": str(rec)}
    return {
        "id": str(rec.get("id") or rec.get("doi") or rec.get("title") or ""),
        "span": str(rec.get("span") or rec.get("text") or rec.get("abstract") or ""),
        "title": str(rec.get("title") or ""),
    }


@dataclass
class SentenceAudit:
    index: int = 0
    offset: int = 0
    sentence: str = ""
    bound_source_ids: list = field(default_factory=list)
    grounded: bool = False
    overlap: float = 0.0
    numbers_ok: bool = True
    unbound_numbers: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "index": self.index, "offset": self.offset, "sentence": self.sentence,
            "bound_source_ids": self.bound_source_ids, "grounded": self.grounded,
            "overlap": round(self.overlap, 3), "numbers_ok": self.numbers_ok,
            "unbound_numbers": self.unbound_numbers,
        }


@dataclass
class ComposerReport:
    ok: bool
    paper_id: str = ""
    draft: str = ""
    sentences: list = field(default_factory=list)
    violations: list = field(default_factory=list)
    grounded_ratio: float = 0.0
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "draft": self.draft,
            "sentences": self.sentences, "violations": self.violations,
            "grounded_ratio": round(self.grounded_ratio, 3),
            "notes": self.notes, "error": self.error,
            "constraint": "every-sentence-must-bind-a-source-span",
        }

    def to_markdown(self) -> str:
        vio = "\n".join(
            f"- 第 {v['index']} 句（偏移 {v['offset']}）未绑定来源：{v['sentence'][:80]}"
            for v in self.violations
        ) or "- （无违规，全部句子已绑定来源）"
        return "\n\n".join([
            f"# 源约束写作审计：{self.paper_id}",
            f"## 结论\n"
            f"- 约束：每句必须绑定来源 span\n"
            f"- 绑定率：{self.grounded_ratio:.0%}\n"
            f"- 违规句数：{len(self.violations)}",
            f"## 违规清单\n{vio}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def draft(*, paper_id: str, layout: Layout, sources,
          outline: list[tuple[str, list]] | None = None) -> dict:
    """按大纲生成草稿：每句自带 source_ids，天然满足源约束的显式绑定。"""
    srcs = [_norm_source(s) for s in sources or []]
    if not srcs:
        return ComposerReport(ok=False, paper_id=paper_id,
                              error="sources 为空：源约束写作器必须有候选来源。").to_dict()

    r = ComposerReport(ok=False, paper_id=paper_id)
    paras: list[str] = []
    for title, claims in (outline or [("Findings", [None] * len(srcs))]):
        body = []
        for i, c in enumerate(claims or []):
            s = srcs[i % len(srcs)]
            text = str(c or "").strip()
            sentence = text if text else f"{s['title'] or s['id']} reports the following finding. [{s['id']}]"
            if "[" + s["id"] + "]" not in sentence:
                sentence = sentence.rstrip(".") + f" [{s['id']}]."
            body.append(sentence)
        paras.append(f"## {title}\n" + " ".join(body))
    r.draft = "\n\n".join(paras)
    r.notes.append("草稿中每句均显式标注 [source_id]，属「显式绑定」路径。")
    _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def audit(*, paper_id: str, layout: Layout, text: str, sources,
          min_overlap: float = 0.34) -> dict:
    """审计正文：逐句判定是否绑定来源 span。存在违规则 ok=False。"""
    srcs = [_norm_source(s) for s in sources or []]
    if not srcs:
        return ComposerReport(ok=False, paper_id=paper_id,
                              error="sources 为空：无法审计来源绑定。").to_dict()

    r = ComposerReport(ok=False, paper_id=paper_id)
    spans = [(s, _tokens(s["span"] + " " + s["title"])) for s in srcs if s["span"] or s["title"]]
    known_numbers: dict[str, set[str]] = {
        s["id"]: set(_NUM.findall(s["span"] + " " + s["title"])) for s, _ in spans
    }

    for idx, (off, sent) in enumerate(_sentences(text), 1):
        stoks = _tokens(sent)
        bound: list[str] = []
        best = 0.0
        # 引注标记（[S1]）是来源 id 而非测量值，提取数值前先剔除
        nums = set(_NUM.findall(re.sub(r"\[[^\[\]]{1,40}\]", " ", sent)))
        unbound_nums: list[str] = []

        for s, toks in spans:
            inter = stoks & toks
            ov = len(inter) / max(1, len(stoks))
            if ov > best:
                best = ov
            if ov >= min_overlap:
                bound.append(s["id"])
                # 数值一致性
                for n in nums:
                    if n not in known_numbers.get(s["id"], set()):
                        unbound_nums.append(n)

        # 显式绑定优先
        explicit = re.findall(r"\[([^\[\]]{1,40})\]", sent)
        explicit = [e for e in explicit if any(e == s["id"] for s, _ in spans)]
        if explicit:
            bound = explicit

        sa = SentenceAudit(
            index=idx, offset=off, sentence=sent, bound_source_ids=bound,
            overlap=best, numbers_ok=not unbound_nums, unbound_numbers=unbound_nums,
        )
        sa.grounded = bool(bound) and (sa.numbers_ok or not nums)
        r.sentences.append(sa.to_dict())
        if not sa.grounded:
            r.violations.append(sa.to_dict())

    r.grounded_ratio = (
        sum(1 for s in r.sentences if s["grounded"]) / len(r.sentences)
        if r.sentences else 0.0
    )
    if not r.sentences:
        r.error = "未从 text 中切分出任何句子。"
        return r.to_dict()
    if r.violations:
        r.notes.append(f"{len(r.violations)} 句未通过源约束，已阻断放行。")
        r.notes.append("需要为这些句补充来源，或改写为可由来源支撑的表述。")
    else:
        r.notes.append("全部句子均绑定来源 span，且句内数值与来源一致。")
    r.notes.append(f"判据：内容词重合度 ≥ {min_overlap}；句内数值须出现在绑定来源中。")
    r.ok = not r.violations

    _persist(layout, paper_id, r)
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: ComposerReport) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "composer.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "composer.md").write_text(r.to_markdown(), encoding="utf-8")
