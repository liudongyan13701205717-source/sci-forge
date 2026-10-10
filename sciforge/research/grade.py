"""证据权重层（backlog #16）：RoB2 / ROBINS-I + GRADE 确定性分级。

GRADE 起始确定性按研究设计给出，再按五个降级因素与三个升级因素调整：
  - 起始：RCT = high(-0)；观察性 = low(-2)；病例系列/病例报告 = very low(-3)
  - 降级：偏倚风险、不一致性、间接性、不精确性、发表偏倚（每项 -1）
  - 升级：效应量大、剂量-反应、混杂会削弱结论（每项 +1）
确定性四档：high / moderate / low / very low。

RoB 侧只做**结构化录入 + 分级**，不替代 RoB2/ROBINS-I 的领域判断：
调用方给出 signalling-question 答案，本模块按官方汇总规则改成 overall。

规则本身写在这里、可复算；不引入任何黑箱评分。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from sciforge.core import Layout

CERTAINTY = ("high", "moderate", "low", "very_low")

# 设计 → 起始确定性（GRADE 手册默认）
_DESIGN_START = {
    "rct": "high",
    "randomized": "high",
    "randomised": "high",
    "randomized controlled trial": "high",
    "nrs": "low",
    "observational": "low",
    "cohort": "low",
    "case-control": "low",
    "cross-sectional": "low",
    "quasi-experimental": "low",
    "case series": "very_low",
    "case report": "very_low",
    "expert opinion": "very_low",
    "narrative": "very_low",
}

_RANK = {"high": 3, "moderate": 2, "low": 1, "very_low": 0}

# RoB2 五个领域（随机试验）
_ROB2 = ["D1_randomization", "D2_deviations", "D3_missing_data",
         "D4_outcome_measurement", "D5_reported_result"]
# ROBINS-I 七个领域（非随机研究）
_ROBINS_I = ["D1_confounding", "D2_selection", "D3_classification",
             "D4_deviations", "D5_missing_data", "D6_outcome_measurement",
             "D7_reported_result"]

_ANSWER_MAP = {
    "y": "low", "yes": "low", "low": "low", "pn": "some", "probably": "some",
    "py": "some", "some": "some", "some concerns": "some",
    "n": "high", "no": "high", "high": "high", "ni": "unclear",
    "no information": "unclear", "unclear": "unclear",
}


def _norm_answer(v) -> str:
    s = str(v or "").strip().lower()
    return _ANSWER_MAP.get(s, "unclear")


def rob_overall(domain_answers: dict, tool: str = "rob2") -> str:
    """按官方汇总规则从领域答案推 overall。

    rob2: 任一 high → high；任一 some concerns → some concerns；否则 low
          （unclear 不降级，但会出现在 notes）
    robins-i: 同理，领域更多
    """
    answers = [ _norm_answer(v) for v in (domain_answers or {}).values() ]
    if not answers:
        return "unclear"
    if any(a == "high" for a in answers):
        return "high"
    if any(a == "some" for a in answers):
        return "some_concerns" if tool == "rob2" else "moderate"
    if any(a == "unclear" for a in answers) and not any(a in ("low", "some") for a in answers):
        return "unclear"
    return "low" if tool == "rob2" else "low"


@dataclass
class GradeRow:
    outcome: str = ""
    design: str = ""
    start: str = "very_low"
    downgrades: list = field(default_factory=list)
    upgrades: list = field(default_factory=list)
    certainty: str = "very_low"
    reason: str = ""

    def to_dict(self) -> dict:
        return {
            "outcome": self.outcome, "design": self.design, "start": self.start,
            "downgrades": self.downgrades, "upgrades": self.upgrades,
            "certainty": self.certainty, "reason": self.reason,
        }


@dataclass
class GradeReport:
    ok: bool
    paper_id: str = ""
    rows: list = field(default_factory=list)
    rob: dict = field(default_factory=dict)
    summary: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "rows": self.rows,
            "rob": self.rob, "summary": self.summary, "notes": self.notes,
            "error": self.error,
            "rubric": "GRADE start-by-design with 5 downgrade / 3 upgrade factors",
        }

    def to_markdown(self) -> str:
        rows = "\n".join(
            f"| {r['outcome'] or '（未命名）'} | {r['design']} | "
            f"{r['start']} | {';'.join(r['downgrades']) or '-'} | "
            f"{';'.join(r['upgrades']) or '-'} | **{r['certainty']}** |"
            for r in self.rows
        ) or "| - | - | - | - | - | - |"
        return "\n\n".join([
            f"# 证据权重（RoB + GRADE）：{self.paper_id}",
            "## GRADE\n"
            "| 结局 | 设计 | 起始 | 降级 | 升级 | 确定性 |\n"
            "|---|---|---|---|---|---|\n" + rows,
            "## 偏倚风险\n"
            f"- 工具：{self.rob.get('tool', 'n/a')}\n"
            f"- overall：{self.rob.get('overall', 'n/a')}\n"
            f"- 领域：{self.rob.get('domains', {})}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def _clamp(rank: int) -> tuple[int, str]:
    rank = max(0, min(3, rank))
    for name, r in _RANK.items():
        if r == rank:
            return rank, name
    return rank, "very_low"


def grade(*, paper_id: str, layout: Layout, outcomes: list,
          rob: dict | None = None) -> dict:
    """GRADE 确定性分级。

    outcomes: [{outcome, design, downgrades:[...], upgrades:[...]}]
      design: rct / cohort / case-control / case series ...
      downgrades 取值: risk_of_bias / inconsistency / indirectness /
                       imprecision / publication_bias
      upgrades   取值: large_effect / dose_response / confounding_would_reduce
    rob: {"tool": "rob2"|"robins-i", "domains": {D1: "y"|"py"|"pn"|"n"|"ni", ...}}
    """
    r = GradeReport(ok=False, paper_id=paper_id)
    entries = [o for o in (outcomes or []) if isinstance(o, dict)]
    if not entries:
        r.error = "outcomes 为空（需 [{outcome, design, downgrades, upgrades}]）。"
        return r.to_dict()

    robtool = "rob2"
    roboverall = "unclear"
    robdomains: dict = {}
    if rob:
        robtool = str(rob.get("tool") or "rob2").lower()
        if robtool not in ("rob2", "robins-i"):
            robtool = "rob2"
        robdomains = {str(k): _norm_answer(v) for k, v in (rob.get("domains") or {}).items()}
        roboverall = rob_overall(robdomains, robtool)
        if robdomains and roboverall == "unclear":
            r.notes.append("偏倚领域存在未作答项（ni），overall 记为 unclear，"
                           "GRADE 不据此自动降级。")
    else:
        r.notes.append("未提供 rob 偏倚评估，GRADE 的 risk_of_bias 降级需人工判断。")

    bal_count = {"high": 0, "moderate": 0, "low": 0, "very_low": 0}

    for o in entries:
        row = GradeRow(
            outcome=str(o.get("outcome") or ""),
            design=str(o.get("design") or ""),
        )
        key = row.design.strip().lower()
        row.start = _DESIGN_START.get(key, "very_low")
        if key not in _DESIGN_START:
            r.notes.append(f"未知设计「{row.design}」，GRADE 起始按最保守的 very_low 计。")

        dg = [str(x) for x in (o.get("downgrades") or [])]
        up = [str(x) for x in (o.get("upgrades") or [])]
        row.downgrades = [f"{x}(-1)" for x in dg]
        row.upgrades = [f"{x}(+1)" for x in up]
        rank = _RANK[row.start] - len(dg) + len(up)
        rank, name = _clamp(rank)
        row.certainty = name
        bal_count[name] += 1
        row.reason = (f"起始 {row.start}（设计 {row.design or 'unknown'}）"
                      f"{'-' + str(len(dg)) + ' 降级' if dg else ''}"
                      f"{'+' + str(len(up)) + ' 升级' if up else ''}"
                      f" → {name}")
        r.rows.append(row.to_dict())

    r.rob = {"tool": robtool, "domains": robdomains, "overall": roboverall}
    r.summary = {
        "n_outcomes": len(r.rows),
        "by_certainty": bal_count,
        "lowest": min((x["certainty"] for x in r.rows),
                      key=lambda c: _RANK.get(c, 0)),
    }
    r.notes.append("确定性 = 起始档位 - 降级项 + 升级项，截断到 "
                   "very_low..high；规则可复算。")
    if r.summary["lowest"] == "very_low":
        r.notes.append("存在 very_low 结局：结论表述应使用「可能」而非确定性措辞。")

    _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: GradeReport) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "grade.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    (root / "grade.md").write_text(r.to_markdown(), encoding="utf-8")
