"""主动学习式筛选分流（backlog #13，ASReview LAB v2 对等）。

不训练模型，而是用**可解释的启发式信息量**给未筛记录排序，让筛选人先看
最可能改变结论的条目：

  - 分歧度：多名筛选人决定不一致 → 信息量高
  - 不确定性：关键词命中弱、题名/摘要短、无 DOI → 把握低
  - 多样性：与已纳入集合主题重合低 → 可能带来新证据
  - 影响面：被引/年份等元数据完备度高 → 若翻转结论影响大

同时给停止建议：连续 `window` 条被排除时，提示「可能已饱和」——
这是建议，不是自动停止（终决权在筛选人）。

纯启发式、离线可跑；`method` 字段如实标注为启发式（非模型概率）。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from sciforge.core import Layout

_WORD = re.compile(r"[A-Za-z][A-Za-z\-]{2,}|[一-鿿]{2,}")
_STOP = {
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were",
    "has", "have", "not", "but", "all", "can", "our", "their", "its", "which",
    "we", "in", "on", "of", "to", "by", "as", "at", "is", "it", "an", "be",
    "a", "study", "using", "based", "method", "methods", "result", "results",
}


def _toks(text: str) -> set[str]:
    return {w.lower() for w in _WORD.findall(str(text or "")) if w.lower() not in _STOP}


@dataclass
class TriageItem:
    id: str = ""
    title: str = ""
    score: float = 0.0
    reasons: list = field(default_factory=list)
    decisions: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id, "title": self.title, "score": round(self.score, 3),
            "reasons": self.reasons, "decisions": self.decisions,
        }


@dataclass
class TriageReport:
    ok: bool
    paper_id: str = ""
    queue: list = field(default_factory=list)
    included_count: int = 0
    excluded_count: int = 0
    unresolved_count: int = 0
    saturation_note: str = ""
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "queue": self.queue,
            "included_count": self.included_count,
            "excluded_count": self.excluded_count,
            "unresolved_count": self.unresolved_count,
            "saturation_note": self.saturation_note, "notes": self.notes,
            "error": self.error, "method": "heuristic-informativeness",
        }

    def to_markdown(self) -> str:
        rows = "\n".join(
            f"{i}. **{q['score']:.2f}** {q['title'] or q['id']}"
            f"（{'；'.join(q['reasons'])}）"
            for i, q in enumerate(self.queue[:20], 1)
        ) or "- （无待筛条目）"
        return "\n\n".join([
            f"# 筛选分流队列：{self.paper_id}",
            f"## 状态\n- 已纳入 {self.included_count} | 已排除 {self.excluded_count} | "
            f"待筛 {self.unresolved_count}\n- 饱和提示：{self.saturation_note or '（无）'}",
            f"## 建议先看\n{rows}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def _norm_decision(v) -> str:
    s = str(v or "").strip().lower()
    if s in ("in", "include", "i", "yes", "y", "1"):
        return "include"
    if s in ("out", "exclude", "e", "no", "n", "0"):
        return "exclude"
    return "maybe"


def triage(*, paper_id: str, layout: Layout, records,
           saturation_window: int = 10) -> dict:
    """给未决记录排「先看谁」的启发式队列 + 饱和建议。"""
    r = TriageReport(ok=False, paper_id=paper_id)
    items = [x for x in (records or []) if isinstance(x, dict)]
    if not items:
        r.error = "records 为空。"
        return r.to_dict()

    included: list[set] = []
    excluded_run = 0
    max_excluded_run = 0
    pending: list[dict] = []

    for it in items:
        decs = [ _norm_decision(d) for d in (it.get("decisions") or []) ]
        text = str(it.get("title") or "") + " " + str(it.get("abstract") or "")
        toks = _toks(text)
        if decs and all(d == "include" for d in decs):
            r.included_count += 1
            included.append(toks)
        elif decs and all(d == "exclude" for d in decs):
            r.excluded_count += 1
            excluded_run += 1
            max_excluded_run = max(max_excluded_run, excluded_run)
        else:
            r.unresolved_count += 1
            pending.append({"rec": it, "decs": decs, "toks": toks})

    excluded_run = 0
    for it in items:
        decs = [ _norm_decision(d) for d in (it.get("decisions") or []) ]
        if decs and all(d == "exclude" for d in decs):
            excluded_run += 1
        elif decs:
            excluded_run = 0
    max_excluded_run = max(max_excluded_run, excluded_run)

    queue: list[TriageItem] = []
    for p in pending:
        it, decs, toks = p["rec"], p["decs"], p["toks"]
        score = 0.0
        reasons: list[str] = []
        if len(set(decs)) > 1:
            score += 3.0
            reasons.append("筛选人分歧（分歧度高）")
        if not toks or len(toks) < 5:
            score += 2.0
            reasons.append("题名/摘要信息稀疏，把握低")
        if not it.get("doi"):
            score += 1.0
            reasons.append("无 DOI，定位不稳")
        # 多样性：与已纳入集合的平均重合度低
        if included:
            avg = sum(len(toks & s) / max(1, len(toks | s)) for s in included) / len(included)
            if avg < 0.15:
                score += 2.0
                reasons.append(f"与已纳入集合重合度低（{avg:.2f}），可能带来新证据")
        if it.get("cited_by") is not None or it.get("year"):
            score += 1.0
            reasons.append("元数据完备，若翻转结论影响面大")
        queue.append(TriageItem(
            id=str(it.get("id") or ""), title=str(it.get("title") or ""),
            score=score, reasons=reasons, decisions=decs,
        ))

    queue.sort(key=lambda x: x.score, reverse=True)
    r.queue = [q.to_dict() for q in queue]

    if max_excluded_run >= max(1, int(saturation_window)):
        r.saturation_note = (f"连续 {max_excluded_run} 条被一致排除，"
                             f"可能已接近筛选饱和（建议抽检最新记录）")
    else:
        r.saturation_note = (f"当前最长连续排除 {max_excluded_run}/{saturation_window}，"
                             f"尚未达到饱和提示阈值")

    r.notes.append("分流分数为启发式信息量（非模型概率），仅决定查看顺序。")
    r.notes.append("饱和提示不自动停止筛选；停止须由筛选人决定并记录理由。")

    _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: TriageReport) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "triage.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    (root / "triage.md").write_text(r.to_markdown(), encoding="utf-8")
