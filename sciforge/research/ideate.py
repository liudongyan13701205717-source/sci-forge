"""构思 + 选题漏斗：研究方向 → 文献 → 研究缺口 → 研究问题 → 候选假设。

对齐 SciForge/AutoResearchClaw 的 Phase A–C：
  Topic → PROBLEM_DECOMPOSE → LITERATURE → SYNTHESIS → HYPOTHESIS_GEN
本实现轻量化：
  1) 用 OpenAlex（免 key）检索相关文献；
  2) 交给内部 LLM 提炼研究缺口（gap）与研究问题（RQ）;
  3) 输出结构化候选方向，供 hypoth.py 进一步辩论与排序。
无 LLM 时回退到确定性模板，保证功能不缺失。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm
from sciforge.research import lit


@dataclass
class IdeationResult:
    ok: bool
    topic: str = ""
    papers: list = field(default_factory=list)
    gaps: list = field(default_factory=list)
    questions: list = field(default_factory=list)
    candidates: list = field(default_factory=list)  # 候选方向
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "topic": self.topic,
            "papers_count": len(self.papers),
            "gaps": self.gaps,
            "questions": self.questions,
            "candidates": self.candidates,
            "notes": self.notes,
            "error": self.error,
            "llm_used": self.llm_used,
        }


def ideate(
    topic: str,
    *,
    layout: Layout,
    paper_id: str,
    papers: list | None = None,
    lit_limit: int = 8,
) -> IdeationResult:
    r = IdeationResult(ok=False, topic=topic)
    if not topic or not topic.strip():
        r.error = "研究方向（topic）不能为空。"
        r.notes.append("L1: topic 为空")
        return r
    if len(topic.strip()) < 4:
        r.error = "研究方向过短，请给出更具体的主题/关键词。"
        r.notes.append("L1: topic 过短")
        return r

    # 1) 文献检索（可外部注入，避免测试联网）
    if papers is None:
        papers = lit.search_openalex(topic, limit=lit_limit)
        if lit.search_arxiv(topic, limit=3):
            papers += lit.search_arxiv(topic, limit=3)
    papers = lit.dedupe(papers or [])
    r.papers = papers

    # 2) LLM 提炼 gap / RQ / 候选方向
    notes: list[str] = []
    if llm.configured():
        try:
            _llm_ideate(r, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 不可用，回退模板：{e}")
    if not r.questions:
        _template_ideate(r, notes)

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _paper_block(papers: list[dict]) -> str:
    lines = []
    for i, p in enumerate(papers[:8], 1):
        authors = ", ".join(p.get("authors", [])[:3])
        lines.append(
            f"{i}. {p.get('title','')} ({p.get('year')}) "
            f"venue={p.get('venue')} cited={p.get('cited_by')} "
            f"authors=[{authors}] doi={p.get('doi')}"
        )
    return "\n".join(lines) or "（未检索到相关文献）"


def _llm_ideate(r: IdeationResult, notes: list) -> None:
    sys = (
        "你是一位严谨的科研选题顾问。请仅从给定文献与主题出发提炼研究缺口，"
        "不得凭空编造文献或数据。输出严格 JSON。"
    )
    prompt = (
        f"研究方向：{r.topic}\n\n"
        "检索到的相关文献：\n" + _paper_block(r.papers) + "\n\n"
        "请输出 JSON（无多余文字）：\n"
        "{\n"
        '  "gaps": ["2-4 条研究缺口，每条一句话"],\n'
        '  "questions": ["2-3 条可检验的研究问题"],\n'
        '  "candidates": [{"title":"候选方向标题","hypothesis":"可检验假设",'
        '"approach":"拟采用方法简述","novelty":"新意点","difficulty":1..5}]\n'
        "}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.7, max_tokens=1600)
    try:
        data = json.loads(_strip_json(raw))
        r.gaps = [str(x) for x in data.get("gaps", []) if x]
        r.questions = [str(x) for x in data.get("questions", []) if x]
        r.candidates = [c for c in data.get("candidates", []) if isinstance(c, dict)]
    except (ValueError, TypeError) as e:
        notes.append(f"LLM 输出非合法 JSON，回退模板：{e}")


def _template_ideate(r: IdeationResult, notes: list) -> None:
    if not r.questions:
        r.questions = [
            f"针对「{r.topic}」，当前方法的性能/效率/泛化/可解释性瓶颈是什么？",
            f"「{r.topic}」在何种约束(数据规模/计算/标签稀缺)下表现最差？",
        ]
    if not r.gaps:
        cited = sorted({p.get("cited_by", 0) for p in r.papers}, reverse=True)[:3]
        r.gaps = [
            f"现有「{r.topic}」相关工作总体引用不高（top3 被引 {cited}），"
            "说明仍缺公认基准与强基线。",
            "文献多为单一数据集验证，跨领域泛化证据不足。",
        ]
    if not r.candidates:
        r.candidates = [
            {
                "title": f"{r.topic}：面向资源受限场景的高效方法",
                "hypothesis": f"在同等精度下，针对「{r.topic}」的轻量化方案能大幅降低计算/参数开销",
                "approach": "设计紧凑结构并用公开基准对比基线",
                "novelty": "解决小规模场景下的实用性缺口",
                "difficulty": 3,
            }
        ]
    notes.append("无 LLM，使用确定性模板生成缺口/RQ/候选方向。")


def _strip_json(raw: str) -> str:
    s = raw.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
    i, j = s.find("{"), s.rfind("}")
    return s[i : j + 1] if (i != -1 and j != -1 and j >= i) else s


def _persist(layout: Layout, paper_id: str, r: IdeationResult) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    f = root / "ideation.json"
    f.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    return f
