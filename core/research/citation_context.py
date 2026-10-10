"""引文上下文立场分类（backlog #1，Scite Smart Citations 对等能力）。

输入含引注标记的句子/段落，判定每条引注在当前语境是
**支持( supporting ) / 对比( contrasting ) / 提及( mentioning )**，
并给出可解释的触发线索与置信度。

判据全部为「表层线索词 + 结构化特征」：
  - supporting：确认、扩展、复现、一致、支持类措辞
  - contrasting：但是、然而、相反、未能、矛盾、反驳类措辞
  - mentioning：仅陈述存在/背景，无立场措辞（默认档）
纯启发式、离线可跑；不伪造语义理解，``method`` 字段如实标注启发式来源。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from sciforge.core import Layout

_CITE = re.compile(r"\[(?P<bracket>[^\[\]]{1,40})\]\s*")
_NUM_CITE = re.compile(r"\[(?P<num>\d{1,4}(?:\s*[-,]\s*\d{1,4})*)\]")

_SUPPORT = (
    "support", "confirms", "confirm", "consistent with", "in agreement",
    "corroborat", "reproduc", "replicat", "in favour", "in favor",
    "also shows", "similarly", "as expected", "validat", "extend",
    "improves upon", "builds on", "demonstrat", "show that", "found that",
    "we agree", "consistent",
)
_CONTRAST = (
    "however", "but ", "in contrast", "contrast", "by contrast",
    "nevertheless", "nonetheless", "on the other hand", "whereas", "while",
    "although", "though", "despite", "in spite of", "unlike",
    "conversely", "instead", "rather than", "contradict", "refut",
    "fail to", "failed to", "did not", "does not", "cannot", "unable to",
    "disagree", "challenge", "question the", "overstate", "limitation of",
    "shortcom", "no evidence", "contrary to", "conflict",
)

_REF_TAIL = re.compile(r"et\s+al\.?,?\s*\[", re.IGNORECASE)


@dataclass
class ContextSpan:
    reference: str = ""
    sentence: str = ""
    stance: str = "mentioning"
    confidence: float = 0.5
    cues: list = field(default_factory=list)
    offset: int = 0

    def to_dict(self) -> dict:
        return {
            "reference": self.reference, "sentence": self.sentence,
            "stance": self.stance, "confidence": round(self.confidence, 3),
            "cues": self.cues, "offset": self.offset,
        }


@dataclass
class CitationContext:
    ok: bool
    paper_id: str = ""
    spans: list = field(default_factory=list)
    counts: dict = field(default_factory=dict)
    verdict: str = ""
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "spans": self.spans,
            "counts": self.counts, "verdict": self.verdict,
            "notes": self.notes, "error": self.error,
            "method": "surface-cue-heuristic",
        }

    def to_markdown(self) -> str:
        rows = "\n".join(
            f"- **{s['stance']}**（{s['confidence']:.2f}） {s['reference']} — "
            f"{s['sentence'][:80]}"
            + (f"  \n  线索：{'；'.join(s['cues'])}" if s["cues"] else "")
            for s in self.spans
        ) or "- （无引注）"
        c = self.counts
        return "\n\n".join([
            f"# 引文上下文分类：{self.paper_id}",
            f"## 结论\n{self.verdict or '（无）'}",
            "## 统计\n"
            f"- supporting {c.get('supporting', 0)} | "
            f"contrasting {c.get('contrasting', 0)} | "
            f"mentioning {c.get('mentioning', 0)}",
            f"## 明细\n{rows}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def _sentences(text: str) -> list[tuple[int, str]]:
    """按句切分并保留偏移。"""
    out: list[tuple[int, str]] = []
    if not text:
        return out
    for m in re.finditer(r"[^.?!]+[.?!]?", text):
        seg = m.group(0).strip()
        if seg:
            out.append((m.start(), seg))
    return out


def _classify_sentence(sent: str) -> tuple[str, float, list]:
    low = sent.lower()
    con = [c for c in _CONTRAST if c in low]
    sup = [c for c in _SUPPORT if c in low]
    # 对比优先：出现对比词时更可能是在与引注工作对比
    if con and (len(con) >= len(sup) or "however" in con or "in contrast" in con):
        return "contrasting", min(0.95, 0.55 + 0.12 * len(con)), con[:4]
    if sup:
        return "supporting", min(0.95, 0.55 + 0.12 * len(sup)), sup[:4]
    return "mentioning", 0.5, []


def classify(sentences, *, paper_id: str = "", layout: Layout | None = None) -> dict:
    """对含引注的句子列表做立场分类，返回 dict（可持久化）。"""
    spans: list[ContextSpan] = []
    for raw in sentences or []:
        if not isinstance(raw, str) or "[" not in raw:
            continue
        for offset, sent in _sentences(raw):
            for m in _CITE.finditer(sent):
                ref = m.group("bracket").strip()
                if not ref:
                    continue
                stance, conf, cues = _classify_sentence(sent)
                spans.append(ContextSpan(
                    reference=ref, sentence=sent.strip(), stance=stance,
                    confidence=conf, cues=cues, offset=offset,
                ))

    counts = {
        "supporting": sum(1 for s in spans if s.stance == "supporting"),
        "contrasting": sum(1 for s in spans if s.stance == "contrasting"),
        "mentioning": sum(1 for s in spans if s.stance == "mentioning"),
    }
    r = CitationContext(
        ok=False, paper_id=paper_id, spans=[s.to_dict() for s in spans],
        counts=counts,
    )
    if not spans:
        r.error = "未在输入中检测到 [..] 形式的引注标记。"
        r.notes.append("请使用方括号数字引注（如 [1]）或作者-年份方括号引注。")
        return r.to_dict()

    total = len(spans)
    r.verdict = (
        f"共 {total} 处引注：支持 {counts['supporting']}、"
        f"对比 {counts['contrasting']}、提及 {counts['mentioning']}。"
    )
    r.notes.append("方法为表层线索词启发式（method=surface-cue-heuristic），"
                   "不等同于语义级引文意图识别。")
    if counts["contrasting"] == 0:
        r.notes.append("未检出对比性引注；若全文确无对立证据，"
                       "请在综述中说明检索到的局限。")
    if layout is not None:
        _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: CitationContext) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "citation_context.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "citation_context.md").write_text(r.to_markdown(), encoding="utf-8")
