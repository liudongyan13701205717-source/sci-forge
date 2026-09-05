"""研究计划书：把选题扩展成一份可执行的完整研究计划（研究计划书）。

对齐 RESEARCH_PLANNING：产出
  - 选题与标题
  - 研究问题（RQ）与假设
  - 目标与贡献
  - 方法路线
  - 数据集与基线
  - 评估指标
  - 消融
  - 里程碑与进度表
  - 风险与预期结果
统一落盘 projects/{paper_id}/research/research_plan.json + markdown 片段。
无 LLM 时确定性回退（可复用 ideate/experiment plan 的产物）。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm


@dataclass
class ResearchPlan:
    ok: bool
    title: str = ""
    topic: str = ""
    question: str = ""
    hypotheses: list = field(default_factory=list)
    objectives: list = field(default_factory=list)
    contributions: list = field(default_factory=list)
    methodology: list = field(default_factory=list)
    datasets: list = field(default_factory=list)
    baselines: list = field(default_factory=list)
    metrics: list = field(default_factory=list)
    ablation: list = field(default_factory=list)
    milestones: list = field(default_factory=list)
    risks: list = field(default_factory=list)
    expected: list = field(default_factory=list)
    compute: str = ""
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "title", "topic", "question", "hypotheses", "objectives",
            "contributions", "methodology", "datasets", "baselines", "metrics",
            "ablation", "milestones", "risks", "expected", "compute",
            "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （待补充）"

        mets = "\n".join(
            f"- {m if isinstance(m, str) else m.get('name', '')}"
            for m in self.metrics
        ) or "- （待补充）"
        return "\n\n".join([
            f"# 研究计划书：{self.title or '未命名'}",
            f"**研究方向：** {self.topic or '—'}\n**研究问题：** {self.question or '—'}",
            f"## 假设\n{bullet(self.hypotheses)}",
            f"## 目标\n{bullet(self.objectives)}",
            f"## 贡献\n{bullet(self.contributions)}",
            f"## 方法路线\n{bullet(self.methodology)}",
            f"## 数据集\n{bullet(self.datasets)}",
            f"## 基线\n{bullet(self.baselines)}",
            f"## 评估指标\n{mets}",
            f"## 消融\n{bullet(self.ablation)}",
            f"## 里程碑与进度\n{bullet(self.milestones)}",
            f"## 风险\n{bullet(self.risks)}",
            f"## 预期结果\n{bullet(self.expected)}",
            f"## 计算资源\n{self.compute or '待评估'}",
        ])


def _load_ideation(layout: Layout, paper_id: str) -> dict:
    p = layout.project_dir(paper_id) / "research" / "ideation.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}
    return {}


def _load_plan(layout: Layout, paper_id: str) -> dict:
    p = layout.project_dir(paper_id) / "research" / "experiment_plan.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}
    return {}


def research_plan(
    topic: str,
    *,
    paper_id: str,
    layout: Layout,
) -> ResearchPlan:
    r = ResearchPlan(ok=False, topic=topic)
    notes: list = []
    ide = _load_ideation(layout, paper_id)
    ex = _load_plan(layout, paper_id)

    # 标题/问题来源：优先已存在的 ideation/experiment plan
    cands = ide.get("candidates") or []
    title = ""
    if cands:
        title = cands[0].get("title", "") if isinstance(cands[0], dict) else str(cands[0])
    r.title = title or ex.get("title") or topic
    r.question = (
        (ide.get("questions") or [""])[0]
        or ex.get("question")
        or f"针对「{topic}」，当前方法的瓶颈与更优方案是什么？"
    )

    if llm.configured():
        try:
            _llm_plan(r, topic, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 计划书不可用，回退模板：{e}")

    if not r.hypotheses:
        _template_plan(r, ide, ex, notes)

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _llm_plan(r: ResearchPlan, topic: str, notes: list) -> None:
    sys = "你是资深科研项目规划者。基于主题输出一份完整研究计划书。输出严格 JSON，不编造数据。"
    prompt = (
        f"研究方向：{topic}\n拟用标题：{r.title}\n研究问题：{r.question}\n\n"
        "输出 JSON（键必须包含）：\n"
        "{\"hypotheses\":[\"...\"],\"objectives\":[\"...\"],\"contributions\":[\"...\"],"
        "\"methodology\":[\"...\"],\"datasets\":[\"公开数据+来源\"],\"baselines\":[\"...\"],"
        "\"metrics\":[\"...\"],\"ablation\":[\"...\"],\"milestones\":[\"M1..M4 各一句\"],"
        "\"risks\":[\"...\"],\"expected\":[\"...\"],\"compute\":\"资源估计一句\"}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.6, max_tokens=2000)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，回退模板。")
        return
    for k in ("hypotheses", "objectives", "contributions", "methodology",
              "datasets", "baselines", "metrics", "ablation", "milestones",
              "risks", "expected"):
        setattr(r, k, [str(x) for x in data.get(k, []) if x])
    r.compute = data.get("compute", "")


def _template_plan(r: ResearchPlan, ide: dict, ex: dict, notes: list) -> None:
    if not r.hypotheses:
        cands = [(c.get("hypothesis") if isinstance(c, dict) else "") for c in (ide.get("candidates") or [])]
        r.hypotheses = [c for c in cands if c] or [f"「{r.topic}」可被轻量/更优方法在有限开销内解决"]
    if not r.objectives:
        r.objectives = [
            "明确 {topic} 的核心瓶颈与机会点".format(topic=r.topic),
            "设计并验证一种资源友好、可复现的方法",
            "与现有基线在公开基准上做公平对比",
        ]
    if not r.contributions:
        r.contributions = [f"提出面向「{r.topic}」的新方法/框架", "开源可复现实验与指标"]
    if not r.methodology:
        r.methodology = ["文献与基线梳理", "构建方案与实现", "消融与敏感性分析", "结果整理与撰写"]
    if not r.datasets:
        r.datasets = ex.get("datasets") or ["公开基准数据集（视领域而定）"]
    if not r.baselines:
        r.baselines = ex.get("baselines") or ["最简基线", "当前 SOTA"]
    if not r.metrics:
        r.metrics = ex.get("metrics") or [{"name": "准确率/损失", "direction": "minimize"}]
    if not r.ablation:
        r.ablation = ex.get("ablation") or ["去除核心组件", "关键超参敏感性"]
    if not r.milestones:
        r.milestones = ["M1 文献与选题收敛", "M2 原型与基线复现", "M3 实验与消融", "M4 撰写与交付"]
    if not r.risks:
        r.risks = ["数据/标签稀缺", "基线复现难度高于预期", "指标提升不显著（时间窗内）"]
    if not r.expected:
        r.expected = ex.get("expected") or ["相对基线有可量化提升，且开销可控"]
    if not r.compute:
        r.compute = ex.get("compute") or "单卡 CPU/GPU 即可完成小规模验证。"
    notes.append("无 LLM，使用确定性模板生成研究计划书（回填 ideation/experiment_plan）。")


def _strip_json_obj(raw: str) -> dict:
    s = raw.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
    i, j = s.find("{"), s.rfind("}")
    if i == -1 or j == -1 or j < i:
        return {}
    try:
        d = json.loads(s[i : j + 1])
        return d if isinstance(d, dict) else {}
    except (ValueError, TypeError):
        return {}


def _persist(layout: Layout, paper_id: str, r: ResearchPlan) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / "research_plan.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / "research_plan.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p
