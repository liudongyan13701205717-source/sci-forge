"""claims.gates 测试：完整性门 + bypass + Material Passport。"""
from __future__ import annotations

import pytest

from sciforge.claims.gates import (
    gate_2_5,
    gate_4_5,
    run_gates,
    request_bypass,
    build_passport,
    BLOCK_PATTERNS,
)


# ---------- BLOCK_PATTERNS ----------
def test_block_patterns_constant():
    assert BLOCK_PATTERNS == (
        "implementation_bugs",
        "hallucinated_results",
        "shortcut_reliance",
        "bug_as_insight",
        "methodology_fabrication",
        "frame_lock",
        "citation_hallucinations",
    )


# ---------- gate_2_5 ----------
def test_gate_2_5_pass():
    ctx = {
        "code": "def train():\n    return model.fit()",
        "plan": {"method": "pruning", "dataset": "ImageNet"},
    }
    r = gate_2_5(ctx)
    assert r["stage"] == "2.5"
    assert r["passed"] is True
    assert r["blocked_patterns"] == []


def test_gate_2_5_empty_code():
    r = gate_2_5({"code": "", "plan": "plan"})
    assert r["passed"] is False
    assert "implementation_bugs" in r["blocked_patterns"]


def test_gate_2_5_placeholder():
    r = gate_2_5({"code": "def f():\n    pass  # TODO", "plan": "plan"})
    assert r["passed"] is False
    assert "implementation_bugs" in r["blocked_patterns"]


def test_gate_2_5_hardcoded():
    r = gate_2_5({"code": "accuracy = 0.99", "plan": "plan"})
    assert r["passed"] is False
    assert "shortcut_reliance" in r["blocked_patterns"]


def test_gate_2_5_no_plan():
    r = gate_2_5({"code": "def f(): pass", "plan": None})
    assert r["passed"] is False
    assert "methodology_fabrication" in r["blocked_patterns"]


def test_gate_2_5_empty_plan():
    r = gate_2_5({"code": "def f(): pass", "plan": ""})
    assert r["passed"] is False
    assert "methodology_fabrication" in r["blocked_patterns"]


def test_gate_2_5_empty_plan_dict():
    r = gate_2_5({"code": "def f(): pass", "plan": {}})
    assert r["passed"] is False
    assert "methodology_fabrication" in r["blocked_patterns"]


# ---------- gate_4_5 ----------
def test_gate_4_5_pass():
    ctx = {
        "results": {"metrics": {"accuracy": 0.95}},
        "runs": [{"metrics": {"accuracy": 0.95}}],
        "claims": [],
        "doc_text": "我们的方法达到 SOTA [1]。参考文献 [1] doi:10.1000/abc。",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["stage"] == "4.5"
    assert r["passed"] is True
    assert r["blocked_patterns"] == []


def test_gate_4_5_no_runs():
    ctx = {
        "results": {"metrics": {"accuracy": 0.95}},
        "runs": [],
        "claims": [],
        "doc_text": "",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "hallucinated_results" in r["blocked_patterns"]


def test_gate_4_5_no_results():
    ctx = {
        "results": {},
        "runs": [{"metrics": {"accuracy": 0.9}}],
        "claims": [],
        "doc_text": "",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "hallucinated_results" in r["blocked_patterns"]


def test_gate_4_5_metric_mismatch():
    ctx = {
        "results": {"metrics": {"accuracy": 0.99}},
        "runs": [{"metrics": {"accuracy": 0.90}}],
        "claims": [],
        "doc_text": "",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "shortcut_reliance" in r["blocked_patterns"]


def test_gate_4_5_bug_as_insight():
    ctx = {
        "results": {"metrics": {"accuracy": 0.9}, "note": "这个 bug 其实是个洞见"},
        "runs": [{"metrics": {"accuracy": 0.9}}],
        "claims": [],
        "doc_text": "",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "bug_as_insight" in r["blocked_patterns"]


def test_gate_4_5_frame_lock():
    ctx = {
        "results": {"metrics": {"accuracy": 0.9}},
        "runs": [{"metrics": {"accuracy": 0.9}}],
        "claims": [{"text": "我们的方法在所有指标上都优于基线"}],
        "doc_text": "",
        "negative_results": [{"metrics": {"accuracy": 0.5}}],  # 反面证据
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "frame_lock" in r["blocked_patterns"]


def test_gate_4_5_citation_hallucination():
    ctx = {
        "results": {"metrics": {"accuracy": 0.9}},
        "runs": [{"metrics": {"accuracy": 0.9}}],
        "claims": [],
        "doc_text": "我们的方法达到 SOTA [待补充]。",
        "negative_results": [],
    }
    r = gate_4_5(ctx)
    assert r["passed"] is False
    assert "citation_hallucinations" in r["blocked_patterns"]


# ---------- run_gates ----------
def test_run_gates_both_pass():
    ctx = {
        "code": "def f(): pass",
        "plan": {"method": "pruning"},
        "results": {"metrics": {"accuracy": 0.9}},
        "runs": [{"metrics": {"accuracy": 0.9}}],
        "claims": [],
        "doc_text": "正常文本。",
    }
    r = run_gates(ctx)
    assert r["2.5"]["passed"] is True
    assert r["4.5"]["passed"] is True


# ---------- request_bypass ----------
def test_request_bypass_already_passed():
    gate = {"passed": True, "stage": "2.5"}
    r = request_bypass(gate, "")
    assert r["allowed"] is True
    assert r["bypassed"] is False


def test_request_bypass_no_reason():
    gate = {"passed": False, "stage": "2.5", "blocked_patterns": ["implementation_bugs"]}
    r = request_bypass(gate, "")
    assert r["allowed"] is False
    assert r["bypassed"] is False
    assert "fail-closed" in r["error"]


def test_request_bypass_with_reason():
    gate = {"passed": False, "stage": "4.5", "blocked_patterns": ["hallucinated_results"]}
    r = request_bypass(gate, "人工确认结果真实")
    assert r["allowed"] is True
    assert r["bypassed"] is True
    assert r["bypass_reason"] == "人工确认结果真实"


# ---------- build_passport ----------
def test_build_passport_basic():
    ctx = {
        "results": {"metrics": {"accuracy": 0.9}},
        "runs": [{"run_id": "run-1", "metrics": {"accuracy": 0.9}}],
        "claims": ["我们的方法提升精度"],
    }
    gates = {"2.5": {"passed": True, "blocked_patterns": []}, "4.5": {"passed": True, "blocked_patterns": []}}
    p = build_passport(
        task_id="task-1",
        results={"metrics": {"accuracy": 0.9}},
        runs=[{"run_id": "run-1", "metrics": {"accuracy": 0.9}}],
        claims=["我们的方法提升精度"],
        gate_results=gates,
    )
    assert p["artifact"] == "material_passport"
    assert p["task_id"] == "task-1"
    assert p["stage_gates"]["2.5"]["passed"] is True
    assert p["stage_gates"]["4.5"]["passed"] is True
    assert p["experiment_provenance"]["n_runs"] == 1
    assert "claim_audit" in p
    assert "verdicts_summary" in p


def test_build_passport_claim_audit():
    p = build_passport(
        task_id="t1",
        results={"metrics": {"accuracy": 0.95}},
        runs=[{"run_id": "r1", "metrics": {"accuracy": 0.95}}],
        claims=["我们的准确率达到 95%"],
        gate_results={"2.5": {"passed": True, "blocked_patterns": []},
                      "4.5": {"passed": True, "blocked_patterns": []}},
    )
    audit = p["claim_audit"]
    assert len(audit) == 1
    assert audit[0]["verdict"] in {"ALIGNED", "OVERSTATED", "NOT_SUPPORTED_BY_PROVENANCE", "PROVENANCE_INSUFFICIENT"}
    assert "verdicts_summary" in p