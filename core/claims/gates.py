"""完整性门：stage 2.5 / 4.5 两道门 + Material Passport + fail-closed bypass。

7 模式阻塞清单：
  implementation_bugs / hallucinated_results / shortcut_reliance
  bug_as_insight / methodology_fabrication / frame_lock / citation_hallucinations
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from typing import Any

try:
    from sciforge.claims.verify import verify as _claims_verify
except Exception:  # pragma: no cover
    _claims_verify = None  # type: ignore

# ---------- 常量 ----------
BLOCK_PATTERNS = (
    "implementation_bugs",
    "hallucinated_results",
    "shortcut_reliance",
    "bug_as_insight",
    "methodology_fabrication",
    "frame_lock",
    "citation_hallucinations",
)

_HARDCODED_METRIC_RE = re.compile(
    r"(accuracy|precision|recall|f1|auc|loss|rmse|score)\s*=\s*-?\d+\.\d+"
)
_PLACEHOLDER_RE = re.compile(r"(TODO|FIXME|NotImplementedError|pass\s*#\s*TODO|raise\s+NotImplementedError)", re.I)


# ---------- Gate 2.5 (代码生成 → 执行之间) ----------
def gate_2_5(context: dict[str, Any]) -> dict:
    """Stage 2.5：代码生成 → 执行之间的完整性门。

    context keys:
      - code: str 生成的代码文本
      - plan: dict|str|None 规划/方法论文档
    """
    code = context.get("code", "")
    plan = context.get("plan")
    checks: dict[str, bool] = {}
    blocked: list[str] = []

    # implementation_bugs
    if not code.strip():
        blocked.append("implementation_bugs")
        checks["code_nonempty"] = False
    else:
        checks["code_nonempty"] = True

    if _PLACEHOLDER_RE.search(code):
        blocked.append("implementation_bugs")
        checks["no_placeholders"] = False
    else:
        checks["no_placeholders"] = True

    # shortcut_reliance (stage 2.5)
    if _HARDCODED_METRIC_RE.search(code):
        blocked.append("shortcut_reliance")
        checks["no_hardcoded_metrics"] = False
    else:
        checks["no_hardcoded_metrics"] = True

    # methodology_fabrication
    if plan is None:
        blocked.append("methodology_fabrication")
        checks["plan_present"] = False
    elif isinstance(plan, str):
        checks["plan_present"] = bool(plan.strip())
        if not plan.strip():
            blocked.append("methodology_fabrication")
    elif isinstance(plan, dict):
        checks["plan_present"] = bool(plan)
        if not plan:
            blocked.append("methodology_fabrication")
    else:
        checks["plan_present"] = False
        blocked.append("methodology_fabrication")

    return {
        "stage": "2.5",
        "passed": len(blocked) == 0,
        "blocked_patterns": blocked,
        "checks": checks,
        "bypassed": False,
    }


# ---------- Gate 4.5 (结果 → 论文/交付之间) ----------
def gate_4_5(context: dict) -> dict:
    """Stage 4.5：结果 → 论文/交付之间的完整性门。

    context keys:
      - results: dict 实验结果
      - runs: list 运行记录（provenance）
      - claims: list 论文中的 claim 列表
      - doc_text: str 论文全文（用于引文核验）
      - negative_results: list 反面证据
    """
    results = context.get("results", {})
    runs = context.get("runs", [])
    claims = context.get("claims", [])
    doc_text = context.get("doc_text", "")
    negative_results = context.get("negative_results", [])

    checks: dict[str, bool] = {}
    blocked: list[str] = []

    # hallucinated_results：有结果但无运行 provenance
    if results and not runs:
        blocked.append("hallucinated_results")
        checks["results_have_provenance"] = False
    elif not results:
        blocked.append("hallucinated_results")
        checks["results_exist"] = False
    else:
        checks["results_have_provenance"] = True
        checks["results_exist"] = True

    # shortcut_reliance：结果指标值未在 runs 中出现
    if results and runs:
        run_values = set(str(v) for r in runs for v in (r.get("metrics", {}) or {}).values())
        result_values = set(str(v) for v in (results.get("metrics", {}) or {}).values())
        if result_values and not result_values.issubset(run_values):
            blocked.append("shortcut_reliance")
            checks["metrics_backed_by_runs"] = False
        else:
            checks["metrics_backed_by_runs"] = True
    else:
        checks["metrics_backed_by_runs"] = True

    # bug_as_insight：结果/备注同时含 bug/异常 + insight/洞见/发现
    bug_insight_text = json.dumps({"results": results, "runs": runs}, ensure_ascii=False).lower()
    if ("bug" in bug_insight_text or "error" in bug_insight_text or "异常" in bug_insight_text) \
       and ("insight" in bug_insight_text or "洞见" in bug_insight_text or "发现" in bug_insight_text or "novel" in bug_insight_text):
        blocked.append("bug_as_insight")
        checks["no_bug_as_insight"] = False
    else:
        checks["no_bug_as_insight"] = True

    # frame_lock：有反面证据但无 claim 覆盖
    if negative_results:
        neg_tokens = set()
        for nr in negative_results:
            from sciforge.review.validators import content_tokens
            neg_tokens |= set(content_tokens(str(nr)))
        claim_tokens = set()
        for c in claims:
            from sciforge.review.validators import content_tokens
            claim_tokens |= set(content_tokens(str(c)))
        if claim_tokens and not (claim_tokens & neg_tokens):
            blocked.append("frame_lock")
            checks["no_frame_lock"] = False
        else:
            checks["no_frame_lock"] = True
    else:
        checks["no_frame_lock"] = True

    # citation_hallucinations：doc_text 触发 claims.verify gate_refuse
    if _claims_verify:
        vr = _claims_verify(doc_text or "")
        if vr.get("gate_refuse"):
            blocked.append("citation_hallucinations")
            checks["citations_clean"] = False
        else:
            checks["citations_clean"] = True
    else:
        checks["citations_clean"] = True

    return {
        "stage": "4.5",
        "passed": len(blocked) == 0,
        "blocked_patterns": blocked,
        "checks": checks,
        "bypassed": False,
    }


# ---------- 双门合跑 ----------
def run_gates(context: dict) -> dict:
    return {"2.5": gate_2_5(context), "4.5": gate_4_5(context)}


# ---------- fail-closed bypass ----------
def request_bypass(gate: dict, reason: str) -> dict:
    """fail-closed：无理由拒绝放行；有理由记录放行。"""
    if gate.get("passed"):
        return {"allowed": True, "stage": gate["stage"], "bypassed": False,
                "bypass_reason": "", "error": ""}
    reason = (reason or "").strip()
    if not reason:
        return {"allowed": False, "stage": gate["stage"], "bypassed": False,
                "bypass_reason": "", "error": "bypass 必须记录理由（fail-closed）"}
    return {
        "allowed": True,
        "stage": gate["stage"],
        "bypassed": True,
        "bypass_reason": reason,
        "error": "",
    }


# ---------- Material Passport ----------
def build_passport(
    task_id: str,
    results: dict | None,
    runs: list | None,
    claims: list | None,
    gate_results: dict,
    hypothesis: str = "",
    negative_results: list | None = None,
    doc_text: str = "",
    as_of: str = "",
) -> dict:
    """构建 Material Passport（per-run artifact）。"""
    if not as_of:
        as_of = date.today().isoformat()

    # provenance
    n_runs = len(runs or [])
    run_ids = [r.get("run_id") or r.get("id") or f"run-{i}" for i, r in enumerate(runs or [])]
    results_keys = list((results or {}).keys())
    claims_list = claims or []
    negative_results_list = negative_results or []

    # claim 审计
    claim_audit = []
    from sciforge.review.validators import content_tokens
    prov_text = json.dumps({"results": results, "runs": runs}, ensure_ascii=False)
    prov_tokens = set(content_tokens(prov_text))

    for c in claims:
        ctext = str(c)
        ctokens = set(content_tokens(str(c)))
        claim_nums = re.findall(r"\d+(?:\.\d+)?%?", ctext)
        prov_nums = re.findall(r"\d+(?:\.\d+)?%?", prov_text)

        if not prov_text.strip():
            verdict = "PROVENANCE_INSUFFICIENT"
            matched = []
            reason = "无 provenance（无 runs/results）"
        elif not (set(content_tokens(str(c))) & set(content_tokens(prov_text))):
            verdict = "NOT_SUPPORTED_BY_PROVENANCE"
            matched = []
            reason = "claim 与 provenance 无 token 重叠"
        else:
            claim_nums_set = set(claim_nums)
            prov_nums_set = set(prov_nums)
            if claim_nums and not (set(claim_nums) & prov_nums_set):
                verdict = "OVERSTATED"
                reason = "claim 含 provenance 中无的数值"
            else:
                verdict = "ALIGNED"
                reason = "claim 与 provenance 对齐"
            matched = list(set(content_tokens(str(c))) & set(content_tokens(prov_text)))

        claim_audit.append({
            "claim": str(c)[:200],
            "verdict": verdict,
            "matched_tokens": matched[:10],
            "reason": reason,
        })

    verdict_summary = {}
    for ca in claim_audit:
        v = ca["verdict"]
        verdict_summary[v] = verdict_summary.get(v, 0) + 1

    return {
        "artifact": "material_passport",
        "task_id": task_id,
        "created": as_of,
        "stage_gates": {k: {"passed": v.get("passed"), "blocked": v.get("blocked_patterns")} for k, v in gate_results.items()},
        "experiment_provenance": {
            "n_runs": len(runs or []),
            "run_ids": run_ids,
            "results_keys": list((results or {}).keys()),
            "intake": "experiment provenance recorded from runs + results",
        },
        "claim_audit": claim_audit,
        "verdicts_summary": verdict_summary,
        "bypasses": [],  # 由 request_bypass 记录
    }