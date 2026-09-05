"""假设多视角辩论 + 评审排序。

对齐 HYPOTHESIS_GEN（multi-agent debate）：对候选方向从三个视角
（新颖性 / 严谨性 / 可行性）交叉评审，输出加权分并排序，给出推荐。
无 LLM 时确定性回退（仅按难度/预设可行性排序）。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm

_DIMS = ["novelty", "rigor", "feasibility"]
_DIM_CN = {"novelty": "新颖性", "rigor": "严谨性", "feasibility": "可行性"}


@dataclass
class Review:
    title: str = ""
    hypothesis: str = ""
    scores: dict = field(default_factory=dict)  # dim -> 1..10
    strengths: list = field(default_factory=list)
    weaknesses: list = field(default_factory=list)
    weighted: float = 0.0
    rank: int = 0

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "hypothesis": self.hypothesis,
            "scores": self.scores,
            "strengths": self.strengths,
            "weaknesses": self.weaknesses,
            "weighted": round(self.weighted, 2),
            "rank": self.rank,
        }


@dataclass
class DebateResult:
    ok: bool
    reviews: list = field(default_factory=list)
    recommendation: str = ""
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "reviews": [rv.to_dict() for rv in self.reviews],
            "recommendation": self.recommendation,
            "notes": self.notes,
            "error": self.error,
            "llm_used": self.llm_used,
        }


def _norm(x) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return 3.0
    return max(1.0, min(10.0, v))


def debate(candidates: list[dict], *, layout, paper_id: str) -> DebateResult:
    r = DebateResult(ok=False)
    if not candidates:
        r.error = "缺少候选方向，无法辩论。"
        return r
    # 1) LLM 三角色评审（可选）
    notes: list[str] = []
    if llm.configured():
        try:
            reviews = _llm_debate(candidates)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 辩论不可用，回退模板：{e}")
            reviews = _template_debate(candidates)
    else:
        reviews = _template_debate(candidates)
    # 2) 加权分 + 排序
    weights = {"novelty": 0.4, "rigor": 0.3, "feasibility": 0.3}
    for rv in reviews:
        tot = 0.0
        for d in _DIMS:
            tot += _norm(rv.scores.get(d)) * weights.get(d, 0)
        rv.weighted = tot
    reviews.sort(key=lambda x: x.weighted, reverse=True)
    for rank, rv in enumerate(reviews, 1):
        rv.rank = rank
    best = reviews[0] if reviews else None
    r.reviews = reviews
    r.recommendation = (
        f"推荐第 1 名「{best.title}」（加权 {best.weighted:.2f}）"
        if best else "无可推荐方向"
    )
    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _template_debate(candidates: list[dict]) -> list[Review]:
    reviews = []
    for c in candidates:
        diff = _norm(c.get("difficulty"))
        feasibility = max(3.0, 10.0 - diff)  # 难度越低可行性越高
        title = c.get("title", "")
        reviews.append(
            Review(
                title=title,
                hypothesis=c.get("hypothesis", ""),
                scores={
                    "novelty": 6.0,
                    "rigor": 5.5,
                    "feasibility": feasibility,
                },
                strengths=[c.get("approach", "") or "有方法路线"],
                weaknesses=["未经验证，需实验支撑"],
            )
        )
    return reviews


def _llm_debate(candidates: list[dict]) -> list[Review]:
    sys = (
        "你是科研评审委员会，从三个独立视角评审：新颖性(novelty)、严谨性(rigor)、"
        "可行性(feasibility)。仅基于给定候选信息，不编造。输出严格 JSON 数组。"
    )
    cand_blk = _cand_block(candidates)
    weight_desc = _DIM_CN
    prompt = (
        "候选方向：\n" + cand_blk + "\n\n"
        f"请模拟三视角逐个评审每个候选，输出 JSON 数组：\n"
        "[{\"title\":\"与候选 title 一致\",\"scores\":{\"novelty\":1-10,"
        "\"rigor\":1-10,\"feasibility\":1-10},\n"
        "\"strengths\":[\"...\"],\"weaknesses\":[\"...\"]调用}]\n"
        f"维度含义：{weight_desc}。必须有与输入完全一致的 title。"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.6, max_tokens=2000)
    data = _parse_reviews(raw)
    if not data:
        return _template_debate(candidates)
    out = []
    for d in data:
        out.append(
            Review(
                title=d.get("title", ""),
                hypothesis=_find_hyp(candidates, d.get("title", "")),
                scores={
                    "novelty": _norm(d.get("scores", {}).get("novelty")),
                    "rigor": _norm(d.get("scores", {}).get("rigor")),
                    "feasibility": _norm(d.get("scores", {}).get("feasibility")),
                },
                strengths=[str(x) for x in d.get("strengths", []) if x],
                weaknesses=[str(x) for x in d.get("weaknesses", []) if x],
            )
        )
    return out


def _find_hyp(candidates, title: str) -> str:
    for c in candidates:
        if (c.get("title") or "").strip() == title.strip():
            return c.get("hypothesis", "")
    return ""


def _parse_reviews(raw: str) -> list[dict]:
    s = raw.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
    i, j = s.find("["), s.rfind("]")
    if i == -1 or j == -1 or j < i:
        return []
    try:
        data = json.loads(s[i : j + 1])
    except (ValueError, TypeError):
        return []
    return data if isinstance(data, list) else []


def _cand_block(candidates: list[dict]) -> str:
    lines = []
    for i, c in enumerate(candidates, 1):
        lines.append(
            f"{i}. 标题：{c.get('title','')}\n"
            f"   假设：{c.get('hypothesis','')}\n"
            f"   方法：{c.get('approach','')}\n"
            f"   新意：{c.get('novelty','')}\n"
            f"   难度：{c.get('difficulty','')}"
        )
    return "\n".join(lines)


def _persist(layout: Layout, paper_id: str, r: DebateResult) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    f = root / "debate.json"
    f.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    return f
