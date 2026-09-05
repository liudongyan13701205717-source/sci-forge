"""实验设计：把选定的研究方向/假设，展开成可执行的实验计划。

对齐 EXPERIMENT_DESIGN / RESOURCE_PLANNING：产出
  - 数据集（公开基准）
  - 基线（含最简基线）
  - 指标（含主指标与方向）
  - 消融设计
  - 预期结果与计算资源估计
产物同时序列化为 markdown 片段，可直接作为 writing 线 experiments/results 素材。
无 LLM 时确定性回退。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm


@dataclass
class ExperimentPlan:
    ok: bool
    title: str = ""
    question: str = ""
    datasets: list = field(default_factory=list)
    baselines: list = field(default_factory=list)
    metrics: list = field(default_factory=list)
    ablation: list = field(default_factory=list)
    expected: list = field(default_factory=list)
    compute: str = ""
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "title": self.title,
            "question": self.question,
            "datasets": self.datasets,
            "baselines": self.baselines,
            "metrics": self.metrics,
            "ablation": self.ablation,
            "expected": self.expected,
            "compute": self.compute,
            "notes": self.notes,
            "error": self.error,
            "llm_used": self.llm_used,
        }

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （待补充）"

        parts = [
            f"## 实验设计：{self.title or '未命名'}",
            f"**研究问题：** {self.question or '—'}",
            "### 数据集",
            bullet(self.datasets),
            "### 基线方法",
            bullet(self.baselines),
            "### 评估指标",
            bullet(self.metrics),
            "### 消融实验",
            bullet(self.ablation),
            "### 预期结果",
            bullet(self.expected),
            f"### 计算资源\n{self.compute or '待评估'}",
        ]
        return "\n\n".join(parts)


def design(
    candidate: dict | None,
    *,
    layout: Layout,
    paper_id: str,
    ideation: dict | None = None,
) -> ExperimentPlan:
    r = ExperimentPlan(ok=False)
    c = candidate or {}
    r.title = c.get("title", "")
    r.question = (ideation or {}).get("questions", [""])[0] if (ideation or {}).get("questions") else r.title
    notes: list = []
    if llm.configured():
        try:
            _llm_design(r, c, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 设计不可用，回退模板：{e}")
    if not r.metrics:
        _template_design(r, c, notes)
    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _llm_design(r: ExperimentPlan, c: dict, notes: list) -> None:
    sys = "你是资深实验设计者。基于给定研究方向设计可执行实验计划，不编造数据集。输出严格 JSON。"
    prompt = (
        f"研究方向：{r.title}\n假设：{c.get('hypothesis','')}\n"
        f"方法：{c.get('approach','')}\n研究问题：{r.question}\n\n"
        "输出 JSON：\n"
        "{\"datasets\":[\"公开数据集+来源\"],\"baselines\":[\"SOTA与最简基线\"],"
        "\"metrics\":[{\"name\":\"主指标\",\"direction\":\"minimize|maximize\"}],"
        "\"ablation\":[\"消融项\"],\"expected\":[\"预期结果\"],"
        "\"compute\":\"资源估计一句话\"}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.6, max_tokens=1400)
    data = _strip_json_obj(raw)
    if data:
        r.datasets = [str(x) for x in data.get("datasets", []) if x]
        r.baselines = [str(x) for x in data.get("baselines", []) if x]
        r.metrics = _norm_metrics(data.get("metrics"))
        r.ablation = [str(x) for x in data.get("ablation", []) if x]
        r.expected = [str(x) for x in data.get("expected", []) if x]
        r.compute = data.get("compute", "")
    else:
        notes.append("LLM 输出非合法 JSON，回退模板。")


def _norm_metrics(metrics) -> list:
    out = []
    for m in metrics or []:
        if isinstance(m, dict):
            out.append(
                {"name": m.get("name", ""), "direction": m.get("direction", "minimize")}
            )
        elif isinstance(m, str):
            out.append({"name": m, "direction": "minimize"})
    return out


def _template_design(r: ExperimentPlan, c: dict, notes: list) -> None:
    if not r.datasets:
        r.datasets = ["公开基准数据集（如 MNIST/CIFAR-10 等，视方法领域而定）"]
    if not r.baselines:
        r.baselines = ["最简基线（零样本/启发式）", "当前 SOTA 方法"]
    if not r.metrics:
        r.metrics = [{"name": "准确率/损失", "direction": "minimize"}]
    if not r.ablation:
        r.ablation = ["去除核心组件（消融）", "改变关键超参敏感性"]
    if not r.expected:
        r.expected = ["相对基线有可量化提升，且开销可控"]
    if not r.compute:
        r.compute = "单卡 CPU/GPU 即可完成小规模验证（可先降采样）。"
    notes.append("无 LLM，使用确定性模板生成实验计划。")


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


def _persist(layout: Layout, paper_id: str, r: ExperimentPlan) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    f = root / "experiment_plan.json"
    f.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    return f
