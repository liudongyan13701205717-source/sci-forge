"""研究线（构思→辩论→实验设计→注入论文）单元/集成测试。

全程不依赖 LLM（走模板回退）与真实网络（papers 注入 mock）。
"""

from __future__ import annotations

import json

import pytest

from sciforge.core import Layout, get_layout
from sciforge.write.doc import DocStore

_MOCK_PAPERS = [
    {"title": "Interpretability of Large Models", "year": 2023,
     "authors": ["A"], "cited_by": 120, "doi": "10.1/abc"},
    {"title": "Efficient Inference on Edge Devices", "year": 2022,
     "authors": ["B"], "cited_by": 80},
    {"title": "Resource-constrained Learning", "year": 2021,
     "authors": ["C"], "cited_by": 40},
]


def _layout(tmp_path) -> Layout:
    import os

    os.chdir(tmp_path)
    return get_layout()


def test_ideate_produces_gaps_rq_candidates(tmp_path):
    from sciforge.research.ideate import ideate

    r = ideate(
        "大语言模型的轻量化可解释方法",
        layout=_layout(tmp_path),
        paper_id="p_idea",
        papers=_MOCK_PAPERS,
    )
    assert r.ok is True
    assert r.llm_used is False  # 无 LLM → 模板回退
    assert r.gaps and r.questions and r.candidates


def test_ideate_rejects_empty_topic(tmp_path):
    from sciforge.research.ideate import ideate

    r = ideate("   ", layout=_layout(tmp_path), paper_id="p_bad", papers=[])
    assert r.ok is False
    assert "不能为空" in r.error or "过短" in r.error


def test_debate_ranks_and_recommends(tmp_path):
    from sciforge.research import ideate
    from sciforge.research.hypoth import debate

    ir = ideate.ideate(
        "分布式训练", layout=_layout(tmp_path), paper_id="p_d", papers=_MOCK_PAPERS
    )
    dr = debate(ir.candidates, layout=_layout(tmp_path), paper_id="p_d")
    assert dr.ok is True
    assert dr.reviews
    assert dr.reviews[0].rank == 1
    assert dr.recommendation and "推荐" in dr.recommendation


def test_design_produces_plan_markdown(tmp_path):
    from sciforge.research import ideate
    from sciforge.research.design import design

    ir = ideate.ideate(
        "图神经网络泛化", layout=_layout(tmp_path), paper_id="p_m", papers=_MOCK_PAPERS
    )
    cand = ir.candidates[0] if ir.candidates else None
    er = design(cand, layout=_layout(tmp_path), paper_id="p_m")
    assert er.ok is True
    assert er.metrics
    md = er.to_markdown()
    assert "实验设计" in md and "数据集" in md


def test_inject_writes_real_metrics_to_section(tmp_path):
    from sciforge.core import Layout
    from sciforge.research.inject import inject_results

    layout = _layout(tmp_path)
    tid = "task_x"
    task_root = layout.task_dir(tid)
    task_root.joinpath("results.json").write_text(
        json.dumps(
            {
                "ok": True,
                "paper_title": "Demo",
                "metrics": [
                    {"tag": "acc", "value": 0.912, "ptype": "real", "conf": True},
                    {"tag": "loss", "value": 0.21, "ptype": "real", "conf": True},
                ],
                "plots": ["curve.png"],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    task_root.joinpath("plan.json").write_text(
        json.dumps({"inferred_hyperparams": {"lr": 0.01}}), encoding="utf-8"
    )
    task_root.joinpath("curve.png").write_bytes(b"PNG")

    out = inject_results(layout=layout, paper_id="paperB", task_id=tid, section="results")
    assert out["ok"] is True
    assert out["metrics_count"] == 2

    store = DocStore(layout, "paperB")
    sec = store.read_section("results") or ""
    assert "0.9120" in sec
    assert "0.2100" in sec


def test_inject_missing_result_raises(tmp_path):
    from sciforge.research.inject import InjectError, inject_results

    layout = _layout(tmp_path)
    with pytest.raises(InjectError):
        inject_results(layout=layout, paper_id="paperC", task_id="ghost_task")


def test_verdict_proceed_when_metrics_and_plot(tmp_path):
    from sciforge.research.api import decision_readout

    layout = _layout(tmp_path)
    tid = "tv"
    task_root = layout.task_dir(tid)
    task_root.joinpath("results.json").write_text(
        json.dumps(
            {
                "ok": True,
                "metrics": [
                    {"tag": "m", "value": 1.0, "ptype": "real", "conf": True},
                    {"tag": "m2", "value": 2.0, "ptype": "real", "conf": True},
                ],
                "plots": ["a.png"],
            }
        ),
        encoding="utf-8",
    )
    v = decision_readout(task_id=tid, layout=layout)
    assert v["verdict"] == "PROCEED"


def test_verdict_pivot_on_failure(tmp_path):
    from sciforge.research.api import decision_readout

    layout = _layout(tmp_path)
    tid = "tf"
    task_root = layout.task_dir(tid)
    task_root.joinpath("results.json").write_text(
        json.dumps({"ok": False, "error": "自愈重试失败"}), encoding="utf-8"
    )
    v = decision_readout(task_id=tid, layout=layout)
    assert v["verdict"] == "PIVOT"


# ---- 新增科研/论文六工具 ----

def _write_doc(layout: Layout, paper_id: str, text: str) -> None:
    store = DocStore(layout, paper_id)
    store.sections_dir.mkdir(parents=True, exist_ok=True)
    store.write_section("introduction", text, fmt="markdown")


def test_research_plan_template(tmp_path):
    from sciforge.research.plan import research_plan

    layout = _layout(tmp_path)
    r = research_plan("大语言模型可解释性", paper_id="p_rp", layout=layout)
    assert r.ok is True
    assert r.llm_used is False
    assert r.hypotheses and r.objectives and r.milestones
    md = r.to_markdown()
    assert "研究计划书" in md and "里程碑" in md
    assert (layout.project_dir("p_rp") / "research" / "research_plan.json").exists()


def test_literature_review_offline_template(tmp_path, monkeypatch):
    from sciforge.research.survey import literature_review

    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    layout = _layout(tmp_path)
    r = literature_review("可解释性", paper_id="p_lr", layout=layout)
    assert r.ok is True
    assert r.keyworks
    assert r.gaps and r.outline  # 离线也能产出确定性综述框架
    assert (layout.project_dir("p_lr") / "research" / "literature_review.json").exists()


def test_venue_suggest_mapping(tmp_path):
    from sciforge.research.venue import venue_suggest

    layout = _layout(tmp_path)
    r = venue_suggest("大语言模型可解释性与概念探针", paper_id="p_v", layout=layout)
    assert r.ok is True
    assert r.matches  # 命中可解释性映射
    assert any("ICLR" in m["name"] or "NeurIPS" in m["name"] for m in r.matches)
    assert (layout.project_dir("p_v") / "research" / "venue_suggest.json").exists()


def test_auto_title_abstract_heuristic(tmp_path):
    from sciforge.research.extract import auto_title_abstract

    layout = _layout(tmp_path)
    body = (
        "# 探针辅助的注意力归因方法\n\n"
        "## 摘要\n本工作提出一种轻量可解释方法。\n\n"
        "## 关键词\n注意力归因, 概念探针, 大语言模型\n\n"
        "## 引言\n我们关注模型可解释性。"
    )
    _write_doc(layout, "p_meta", body)
    r = auto_title_abstract(paper_id="p_meta", layout=layout)
    assert r.ok is True
    assert r.title == "探针辅助的注意力归因方法"
    assert "轻量可解释" in r.abstract
    assert "注意力归因" in r.keywords


def test_auto_title_abstract_no_h1_fallback(tmp_path):
    """无一级标题时：标题回退为摘要首句；无关键词行时：中文 n-gram 回退。
    """
    from sciforge.research.extract import auto_title_abstract

    layout = _layout(tmp_path)
    body = (
        "## 摘要\n本工作提出一种面向边缘设备的大语言模型轻量化推理加速方法。"
        "该方法结合结构化剪枝与知识蒸馏，在边缘设备上显著降低推理延迟。\n\n"
        "## 引言\n边缘设备上大语言模型推理延迟较高，相关研究致力于轻量化部署。"
        "结构化剪枝与知识蒸馏是两种主流压缩策略。"
    )
    _write_doc(layout, "p_meta2", body)
    r = auto_title_abstract(paper_id="p_meta2", layout=layout)
    assert r.ok is True
    # 标题回退：从摘要首句生成候选，剔除「本工作提出一种」前缀
    assert r.title and "面向边缘设备" in r.title
    # 中文关键词回退：出现有信息量的主题词（非英文词兜底）
    joined = "".join(r.keywords)
    assert any(k in joined for k in ("大语言模型", "剪枝", "蒸馏", "边缘设备", "推理"))
    assert not r.title.startswith(("本工作", "本文", "提出"))


def test_peer_review_scores_and_recommendation(tmp_path):
    from sciforge.research.review import peer_review

    layout = _layout(tmp_path)
    body = (
        "# 标题\n\n## 摘要\n摘要内容足够长。" * 2 +
        "\n\n## 引言\n motivation 与背景介绍段落内容。" * 3 +
        "\n\n| 方法 | 精度 |\n| --- | --- |\n| 基线 | 0.9 |\n| 本文 | 0.95 |\n" +
        "\n\n![fig1](x.png)\n\n[1] arxiv:1234.5678"
    )
    _write_doc(layout, "p_pr", body)
    r = peer_review(paper_id="p_pr", layout=layout)
    assert r.ok is True
    assert {"novelty", "rigor", "clarity", "soundness"} <= set(r.scores)
    assert r.recommendation in ("Accept (with minor)", "Minor Revision", "Major Revision", "Reject")
    assert (layout.project_dir("p_pr") / "research" / "peer_review.json").exists()


def test_paper_polish_completeness_flags_missing(tmp_path):
    from sciforge.research.polish import paper_polish

    layout = _layout(tmp_path)
    # 只写引言，缺结果/结论/引用
    _write_doc(layout, "p_pol", "# 引言\n内容内容内容。")
    r = paper_polish(paper_id="p_pol", layout=layout, mode="completeness")
    assert r.ok is True
    assert r.issues and isinstance(r.score, float)
    assert any("结果" in i or "结论" in i or "参考文献" in i for i in r.issues)


def test_paper_polish_empty_error(tmp_path):
    from sciforge.research.polish import paper_polish

    layout = _layout(tmp_path)
    r = paper_polish(paper_id="ghost_pol", layout=layout)
    assert r.ok is False
    assert "尚无正文" in r.error


def test_peer_review_empty_error(tmp_path):
    from sciforge.research.review import peer_review

    layout = _layout(tmp_path)
    r = peer_review(paper_id="ghost_pr", layout=layout)
    assert r.ok is False
    assert "尚无正文" in r.error
