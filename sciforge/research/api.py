"""研究线 API 编排：构思→辩论→实验计划→注入论文 的聚合入口。

供 MCP 层（server.py）调用，产出 unified result：
  - ok / error / notes
  - paper_id
  - ideation（gap/RQ/candidates）
  - debate（评审排序 + recommendation）
  - plan（实验计划 + markdown 片段）
  - artifacts（落盘的 research/*.json 路径）
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sciforge.research.design as design
import sciforge.research.hypoth as hypoth
import sciforge.research.ideate as ideate
import sciforge.research.inject as inject

from sciforge.core import Layout


@dataclass
class ResearchResult:
    ok: bool
    paper_id: str = ""
    topic: str = ""
    ideation: dict = field(default_factory=dict)
    debate: dict = field(default_factory=dict)
    plan: dict = field(default_factory=dict)
    plan_markdown: str = ""
    artifacts: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "paper_id": self.paper_id,
            "topic": self.topic,
            "ideation": self.ideation,
            "debate": self.debate,
            "plan": self.plan,
            "plan_markdown": self.plan_markdown,
            "artifacts": self.artifacts,
            "notes": self.notes,
            "error": self.error,
            "llm_used": self.llm_used,
        }


def ideate_paper(
    topic: str,
    *,
    paper_id: str,
    layout: Layout,
    papers: list | None = None,
) -> ResearchResult:
    r = ResearchResult(ok=False, paper_id=paper_id, topic=topic)
    notes: list[str] = []

    # 1) 构思 + 选题漏斗
    ir = ideate.ideate(topic, layout=layout, paper_id=paper_id, papers=papers)
    r.llm_used = ir.llm_used
    if not ir.ok:
        r.error = ir.error
        r.notes = ir.notes
        r.ok = False
        return r
    r.ideation = ir.to_dict()
    notes += list(ir.notes)

    # 2) 假设多视角辩论 + 排序
    dr = hypoth.debate(ir.candidates, layout=layout, paper_id=paper_id)
    r.llm_used = r.llm_used or dr.llm_used
    r.debate = dr.to_dict()
    notes += list(dr.notes)

    # 3) 实验计划（选 top 候选）
    top = None
    if dr.reviews:
        top = next(
            (c for c in ir.candidates if (c.get("title") or "").strip()
             == dr.reviews[0].title.strip()),
            None,
        )
    er = design.design(top, layout=layout, paper_id=paper_id, ideation=ir.to_dict())
    r.llm_used = r.llm_used or er.llm_used
    r.plan = er.to_dict()
    r.plan_markdown = er.to_markdown()
    notes += list(er.notes)

    # 4) artifacts
    root = layout.project_dir(paper_id) / "research"
    for fn in ("ideation.json", "debate.json", "experiment_plan.json"):
        p = root / fn
        if p.exists():
            r.artifacts.append(str(p))

    r.notes = notes
    r.ok = True
    return r


def inject_results(
    *,
    paper_id: str,
    task_id: str,
    layout: Layout,
    section: str = "results",
) -> dict:
    """把复现任务产物注入论文章节。"""
    try:
        res = inject.inject_results(
            layout=layout, paper_id=paper_id, task_id=task_id, section=section
        )
    except inject.InjectError as e:
        return {"ok": False, "error": str(e), "paper_id": paper_id, "task_id": task_id}
    res["ok"] = True
    return res


def decision_readout(*, task_id: str, layout: Layout) -> dict:
    """结果分析自旋门：读复现产物给出 PROCEED/REFINE/PIVOT 建议。

    对齐 RESEARCH_DECISION：基于指标完整度、是否含图、是否有非可信指标。
    """
    root = layout.task_dir(task_id)
    data = {}
    p = root / "results.json"
    if p.exists():
        try:
            import json

            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    metrics = data.get("metrics", [])
    plots = data.get("plots", [])
    ok = bool(data.get("ok"))
    if not ok:
        return {"ok": False, "verdict": "PIVOT", "reason": data.get("error", "结果缺失"),
                "task_id": task_id}
    if not metrics:
        return {"ok": True, "verdict": "REFINE", "reason": "无可用指标", "task_id": task_id}
    all_conf = all(m.get("conf", True) for m in metrics)
    has_plot = bool(plots)
    if all_conf and has_plot and len(metrics) >= 1:
        verdict, reason = "PROCEED", "指标齐备且含曲线，可进入论文写作。"
    elif not all_conf:
        verdict, reason = "REFINE", "存在低可信指标，建议精调后重跑。"
    else:
        verdict, reason = "REFINE", "缺少曲线/指标，建议补充。"
    return {"ok": True, "verdict": verdict, "reason": reason, "task_id": task_id,
            "metrics_count": len(metrics), "has_plot": has_plot}
