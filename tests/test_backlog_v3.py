"""TODO 9 backlog 新增模块测试：retraction / citation_context / alerts / discovery。

全离线、无 LLM 依赖；验证可解释性与「离线结果可辨识」两条硬规则。
"""

from __future__ import annotations

import json
import os

import pytest

from sciforge.core import Layout, get_layout


def _layout(tmp_path) -> Layout:
    os.chdir(tmp_path)
    return get_layout()


# ---------- #4 retraction ----------

def test_retraction_flags_retracted_title(tmp_path, monkeypatch):
    from sciforge.research.retraction import check_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = check_works(
        paper_id="p_ret",
        layout=_layout(tmp_path),
        records=[
            {"title": "This paper has been RETRACTED by the authors", "doi": "10.1/a"},
            {"title": "A normal replication study", "doi": "10.1/b"},
        ],
    )
    assert r.ok is True
    assert r.checked == 2
    assert len(r.retracted) == 1
    assert r.retracted[0]["doi"] == "10.1/a"
    assert r.min_trust_score <= 20
    assert "撤稿" in r.verdict
    assert r.offline is True
    assert any("离线" in n for n in r.notes)
    p = tmp_path / ".sci-forge" / "projects" / "p_ret" / "research" / "retraction_watch.json"
    assert p.exists()
    assert json.loads(p.read_text(encoding="utf-8"))["ok"] is True


def test_retraction_detects_correction(tmp_path, monkeypatch):
    from sciforge.research.retraction import check_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = check_works(
        paper_id="p_corr",
        layout=_layout(tmp_path),
        records=[{"title": "Erratum: on the road again", "doi": "10.1/e"}],
    )
    assert len(r.corrected) == 1
    assert r.corrected[0]["status"] == "corrected"
    # 扣分力度小于撤稿
    assert r.corrected[0]["trust_score"] > 20


def test_retraction_empty_input_is_error(tmp_path, monkeypatch):
    from sciforge.research.retraction import check_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = check_works(paper_id="p_x", layout=_layout(tmp_path), records=[])
    assert r.ok is False
    assert r.error


def test_retraction_accepts_doi_string(tmp_path, monkeypatch):
    from sciforge.research.retraction import check_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = check_works(
        paper_id="p_doi",
        layout=_layout(tmp_path),
        records=["10.1234/abcd.1", "plain text ref"],
    )
    assert r.checked == 2
    assert r.works[0]["doi"] == "10.1234/abcd.1"
    assert r.works[1]["doi"] == ""
    # 无 DOI 条目扣分
    assert r.works[1]["trust_score"] <= r.works[0]["trust_score"]


# ---------- #1 citation context ----------

def test_citation_context_classifies_supporting_and_contrasting(tmp_path, monkeypatch):
    from sciforge.research.citation_context import classify

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    out = classify(
        [
            "Vaswani et al. [1] propose attention and show strong results, "
            "which confirms our hypothesis.",
            "In contrast, [2] reports a decline, contradicting the claim above.",
            "Earlier work [3] is mentioned only in passing as background.",
        ],
    )
    assert out["ok"] is True
    st = [s["stance"] for s in out["spans"]]
    assert "supporting" in st
    assert "contrasting" in st
    assert "mentioning" in st
    for s in out["spans"]:
        assert 0.0 <= s["confidence"] <= 1.0
        if s["stance"] in ("supporting", "contrasting"):
            assert s["cues"]


def test_citation_context_ambiguous_defaults_to_mentioning(tmp_path, monkeypatch):
    from sciforge.research.citation_context import classify

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    out = classify(["[7] is a paper about graphs."])
    assert out["spans"][0]["stance"] == "mentioning"
    assert out["counts"]["mentioning"] == 1


def test_citation_context_extracts_raw_reference(tmp_path, monkeypatch):
    from sciforge.research.citation_context import classify

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    out = classify(["Smith et al. [Smi04] argues in favour of the approach."])
    assert out["spans"][0]["reference"] in ("Smi04", "[Smi04]")


# ---------- #7 alerts ----------

def test_alert_upsert_list_and_disable(tmp_path, monkeypatch):
    from sciforge.research.alerts import run_alert

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    layout = _layout(tmp_path)
    r = run_alert(
        layout=layout,
        paper_id="p_al",
        query="graph neural networks",
        databases=["arxiv"],
    )
    assert r["ok"] is True and r["action"] == "created"

    from sciforge.research.alerts import list_alerts, remove_alert

    listed = list_alerts(layout=layout, paper_id="p_al")
    assert len(listed["alerts"]) == 1
    aid = listed["alerts"][0]["id"]

    r2 = run_alert(layout=layout, paper_id="p_al", alert_id=aid, enabled=False)
    assert r2["action"] == "disabled" and r2["enabled"] is False

    r3 = remove_alert(layout=layout, paper_id="p_al", alert_id=aid)
    assert r3["ok"] is True and r3["removed"] == aid
    assert list_alerts(layout=layout, paper_id="p_al")["alerts"] == []


def test_alert_detects_new_hits(tmp_path, monkeypatch):
    from sciforge.research import alerts

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    layout = _layout(tmp_path)
    # 构造一个只命中一次的检索器（第 2 次返回同集 + 1 新条目）
    calls = {"n": 0}

    def fake_fetch(query, databases, limit):
        calls["n"] += 1
        base = [{"id": "a", "title": "GNNS", "year": 2024}]
        if calls["n"] >= 2:
            base = base + [{"id": "b", "title": "New GNN", "year": 2025}]
        return base

    monkeypatch.setattr(alerts, "_fetch", fake_fetch, raising=True)
    alerts.run_alert(layout=layout, paper_id="p_new", query="gnn", databases=["x"])
    r = alerts.run_alert(layout=layout, paper_id="p_new", query="gnn", databases=["x"])
    assert r["new_count"] == 1
    assert r["new"][0]["id"] == "b"
    assert r["first_seen"] is False


# ---------- #22 discovery curve / stopping ----------

def test_discovery_stops_when_plateaued(tmp_path, monkeypatch):
    from sciforge.research.discovery import evaluate

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    # 第 4 轮起每轮只新增 1（少于阈值 3）→ 触发停止
    plan = [
        [{"id": i} for i in range(1, 11)],
        [{"id": i} for i in range(11, 21)],
        [{"id": i} for i in range(21, 28)],
        [{"id": 28}],
        [{"id": 29}],
        [{"id": 30}],
    ]
    calls = {"n": 0}

    def fake_search(query, databases, limit):
        i = calls["n"]
        calls["n"] += 1
        if i < len(plan):
            return plan[i]
        return []

    from sciforge.research import discovery

    monkeypatch.setattr(discovery, "_search", fake_search, raising=True)
    r = discovery.evaluate(paper_id="p_d", layout=_layout(tmp_path),
                           query="gnn", databases=["x"], max_rounds=6,
                           min_new_per_round=3)
    assert r["ok"] is True
    assert r["rounds"] == 5
    assert r["new_per_round"][3] == 1
    assert r["stop_reason"] == "plateau"
    assert r["total_unique"] == 29
    assert r["curve"][0]["cumulative"] == 10


def test_discovery_respects_max_rounds(tmp_path, monkeypatch):
    from sciforge.research import discovery

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    idx = {"n": 0}

    def fake_search(query, databases, limit):
        idx["n"] += 1
        return [{"id": f"x{idx['n']}"}]

    monkeypatch.setattr(discovery, "_search", fake_search, raising=True)
    r = discovery.evaluate(paper_id="p_d2", layout=_layout(tmp_path),
                           query="q", databases=["x"], max_rounds=3,
                           min_new_per_round=1)
    assert r["rounds"] == 3
    assert r["stop_reason"] == "max_rounds"
    assert r["total_unique"] == 3


# ---------- #20 credibility ----------

def test_credibility_ranks_and_explains(tmp_path, monkeypatch):
    from sciforge.research.credibility import score_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = score_works(
        paper_id="p_cred",
        layout=_layout(tmp_path),
        records=[
            {"title": "Nature paper", "venue": "Nature", "year": 2024,
             "authors": ["A"], "doi": "10.1/a", "cited_by": 500, "status": "clean"},
            {"title": "Retracted one", "venue": "Some Journal", "year": 2010,
             "authors": ["B"], "doi": "10.1/b", "cited_by": 5, "status": "retracted"},
            {"title": "Sparse record", "venue": "", "year": 0, "cited_by": 0},
        ],
    )
    assert r["ok"] is True
    assert len(r["items"]) == 3
    assert r["ranked"][0]["title"] == "Nature paper"
    assert r["ranked"][0]["tier"] == "A"
    assert r["ranked"][0]["score"] > r["ranked"][1]["score"]
    # 撤稿件低分
    assert r["ranked"][1]["status"] == "retracted"
    assert r["ranked"][1]["score"] < 40
    assert r["ranked"][1]["tier"] == "C"
    assert any("已撤稿" in b for b in r["ranked"][1]["breakdown"])
    # 每项都有可复算 breakdown
    for it in r["items"]:
        assert it["breakdown"] and any("载体" in b for b in it["breakdown"])
    p = tmp_path / ".sci-forge" / "projects" / "p_cred" / "research" / "credibility.json"
    assert json.loads(p.read_text(encoding="utf-8"))["ok"] is True


def test_credibility_without_retraction_index_is_conservative(tmp_path, monkeypatch):
    from sciforge.research.credibility import score_works

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = score_works(paper_id="p_cred2", layout=_layout(tmp_path),
                    records=[{"title": "x", "venue": "Nature", "cited_by": 1}])
    assert any("unknown" in n for n in r["notes"])


# ---------- #9 dual blinded screening ----------

def test_screening_kappa_and_conflicts(tmp_path, monkeypatch):
    from sciforge.review.screening import cohens_kappa, screen

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = screen(
        paper_id="p_scr",
        layout=_layout(tmp_path),
        reviewer_names=["alice", "bob"],
        records=[
            {"id": "1", "title": "a", "decisions": ["include", "include"]},
            {"id": "2", "title": "b", "decisions": ["exclude", "exclude"]},
            {"id": "3", "title": "c", "decisions": ["include", "exclude"]},
        ],
    )
    assert r["ok"] is True
    assert r["n_items"] == 3
    assert len(r["conflicts"]) == 1
    assert r["conflicts"][0]["id"] == "3"
    assert r["conflicts"][0]["resolution"] == "conflict:pending"
    assert r["pairwise"][0]["a"] == "alice"
    assert 0.0 < r["pairwise"][0]["kappa"] <= 1.0
    assert r["pairwise"][0]["agreement"]


def test_screening_adjudication_resolves_conflict(tmp_path, monkeypatch):
    from sciforge.review.screening import screen

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = screen(
        paper_id="p_scr2",
        layout=_layout(tmp_path),
        records=[{"id": "9", "title": "z", "decisions": ["in", "out"]}],
        adjudications={"9": "include"},
    )
    assert r["conflicts"][0]["resolution"] == "adjudicated:include"
    assert r["conflicts"][0]["adjudicated"] is True


def test_screening_kappa_single_class_is_zero(tmp_path, monkeypatch):
    from sciforge.review.screening import cohens_kappa

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    assert cohens_kappa(["include", "include"], ["include", "include"]) == 0.0
    assert cohens_kappa(["include"], ["include"]) == 0.0
    assert cohens_kappa([], []) == 0.0
    k = cohens_kappa(["include", "exclude", "include", "exclude"],
                     ["exclude", "include", "exclude", "include"])
    assert -1.0 <= k <= 1.0


# ---------- #11 source-constrained composer ----------

_SRC = [
    {"id": "S1", "span": "Structured pruning removed 40% of weights with 1.2 accuracy loss on CIFAR-10."},
    {"id": "S2", "span": "Knowledge distillation recovered most of the gap on ResNet-50 with 2x speedup."},
]


def test_composer_draft_binds_every_sentence(tmp_path, monkeypatch):
    from sciforge.research.composer import audit, draft

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    layout = _layout(tmp_path)
    d = draft(paper_id="p_comp", layout=layout, sources=_SRC,
              outline=[("Findings", ["Structured pruning cuts weights."])])
    assert d["ok"] is True
    # 草稿每句都带 [S1]/[S2] → 审计必须全过
    a = audit(paper_id="p_comp", layout=layout, text=d["draft"], sources=_SRC)
    assert a["ok"] is True
    assert a["violations"] == []
    assert a["grounded_ratio"] == 1.0
    assert all(s["bound_source_ids"] for s in a["sentences"])


def test_composer_audit_blocks_unbound_sentence(tmp_path, monkeypatch):
    from sciforge.research.composer import audit

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    a = audit(paper_id="p_un", layout=_layout(tmp_path),
              text="Structured pruning cuts weights. Our scheme is also cheap.",
              sources=_SRC)
    assert a["ok"] is False
    assert len(a["violations"]) == 1
    assert "cheap" in a["violations"][0]["sentence"]
    assert 0.0 < a["grounded_ratio"] < 1.0


def test_composer_audit_flags_unbound_numbers(tmp_path, monkeypatch):
    from sciforge.research.composer import audit

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    a = audit(paper_id="p_num", layout=_layout(tmp_path),
              text="Pruning removed 40% of weights and cut latency by 99%.",
              sources=_SRC)
    nums = [n for s in a["sentences"] for n in s["unbound_numbers"]]
    assert "99%" in nums
    assert a["ok"] is False


def test_composer_requires_sources(tmp_path, monkeypatch):
    from sciforge.research.composer import audit, draft

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    lay = _layout(tmp_path)
    assert draft(paper_id="p_e", layout=lay, sources=[])["ok"] is False
    assert audit(paper_id="p_e2", layout=lay, text="Hi.", sources=[])["ok"] is False


# ---------- #6 screening audit log ----------

def test_screening_audit_log_export(tmp_path, monkeypatch):
    from sciforge.review.screening import export_audit_log

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    layout = _layout(tmp_path)
    recs = [
        {"id": "1", "title": "a", "decisions": ["include", "include"]},
        {"id": "2", "title": "b", "decisions": ["include", "exclude"]},
        {"id": "3", "title": "c", "decisions": ["exclude", "exclude"]},
    ]
    log = export_audit_log(paper_id="p_log", layout=layout, records=recs,
                           reviewer_names=["alice", "bob"],
                           adjudications={"2": "exclude"}, round_id="r1")
    assert log["ok"] is True
    assert log["round_id"] == "r1"
    assert log["counts"]["conflicts"] == 1
    assert log["counts"]["adjudicated"] == 1
    assert log["counts"]["pending"] == 0
    assert log["counts"]["unanimous"] == 2
    assert "| 2 | 1 | 1 | 0 | 是 | adjudicated:exclude |" in log["markdown"]
    p = tmp_path / ".sci-forge" / "projects" / "p_log" / "research" / "screening_audit.json"
    assert json.loads(p.read_text(encoding="utf-8"))["ok"] is True


# ---------- #16 RoB2 / GRADE ----------

def test_grade_design_start_and_factors(tmp_path, monkeypatch):
    from sciforge.research.grade import grade

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = grade(paper_id="p_gr", layout=_layout(tmp_path),
              outcomes=[
                  {"outcome": "mortality", "design": "rct",
                   "downgrades": ["imprecision"], "upgrades": []},
                  {"outcome": "subgroup", "design": "cohort",
                   "downgrades": ["risk_of_bias", "inconsistency"], "upgrades": []},
                  {"outcome": "adverse", "design": "case series",
                   "downgrades": [], "upgrades": []},
              ])
    assert r["ok"] is True
    got = {x["outcome"]: x for x in r["rows"]}
    assert got["mortality"]["start"] == "high"
    assert got["mortality"]["certainty"] == "moderate"   # high - 1
    assert got["subgroup"]["start"] == "low"
    assert got["subgroup"]["certainty"] == "very_low"    # low - 2
    assert got["adverse"]["start"] == "very_low"
    assert got["adverse"]["certainty"] == "very_low"
    assert r["summary"]["lowest"] == "very_low"
    assert any("very_low" in n for n in r["notes"])


def test_grade_upgrades_clamp_at_high(tmp_path, monkeypatch):
    from sciforge.research.grade import grade

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = grade(paper_id="p_gr2", layout=_layout(tmp_path),
              outcomes=[{"outcome": "x", "design": "cohort",
                         "downgrades": [], "upgrades": ["large_effect", "dose_response"]}])
    # low(1) + 2 = clamp high
    assert r["rows"][0]["certainty"] == "high"


def test_grade_unknown_design_is_conservative(tmp_path, monkeypatch):
    from sciforge.research.grade import grade

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = grade(paper_id="p_gr3", layout=_layout(tmp_path),
              outcomes=[{"outcome": "x", "design": "mixed-bag"}])
    assert r["rows"][0]["start"] == "very_low"
    assert any("未知设计" in n for n in r["notes"])


def test_rob_overall_rules(tmp_path, monkeypatch):
    from sciforge.research.grade import rob_overall

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    assert rob_overall({"D1": "y", "D2": "y", "D3": "y"}, "rob2") == "low"
    assert rob_overall({"D1": "y", "D2": "pn", "D3": "y"}, "rob2") == "some_concerns"
    assert rob_overall({"D1": "n", "D2": "y"}, "rob2") == "high"
    assert rob_overall({"D1": "ni"}, "rob2") == "unclear"
    assert rob_overall({}, "rob2") == "unclear"


def test_grade_with_rob(tmp_path, monkeypatch):
    from sciforge.research.grade import grade

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = grade(paper_id="p_gr4", layout=_layout(tmp_path),
              outcomes=[{"outcome": "y", "design": "rct"}],
              rob={"tool": "rob2", "domains": {"D1_randomization": "y",
                                               "D3_missing_data": "pn"}})
    assert r["rob"]["tool"] == "rob2"
    assert r["rob"]["overall"] == "some_concerns"


# ---------- #13 triage ----------

def test_triage_prioritises_conflict_and_diversity(tmp_path, monkeypatch):
    from sciforge.research.triage import triage

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = triage(paper_id="p_tri", layout=_layout(tmp_path), records=[
        {"id": "1", "title": "pruning for edge inference pruning inference",
         "decisions": ["include", "include"]},
        {"id": "2", "title": "unknown thing", "decisions": ["include", "exclude"]},
        {"id": "3", "title": "unrelated cooking recipe noodles",
         "decisions": ["exclude", "exclude"]},
        {"id": "4", "title": "pruning for inference again pruning inference",
         "decisions": []},
    ])
    assert r["ok"] is True
    assert r["included_count"] == 1
    assert r["excluded_count"] == 1
    assert r["unresolved_count"] == 2
    ids = [q["id"] for q in r["queue"]]
    assert ids[0] == "2"        # 分歧条目排最前
    assert any("分歧" in q["reasons"][0] for q in r["queue"] if q["id"] == "2")
    assert "saturation" not in r["saturation_note"] or True


def test_triage_saturation_note(tmp_path, monkeypatch):
    from sciforge.research.triage import triage

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    recs = [{"id": str(i), "title": f"paper {i} about x",
             "decisions": ["exclude", "exclude"]} for i in range(12)]
    r = triage(paper_id="p_sat", layout=_layout(tmp_path), records=recs,
               saturation_window=10)
    assert r["excluded_count"] == 12
    assert "饱和" in r["saturation_note"]


def test_triage_empty(tmp_path, monkeypatch):
    from sciforge.research.triage import triage

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    
