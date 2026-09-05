"""新增 6 工具（对比/新颖性/投稿打包/引文热度/进度记账/代码点评）的单元与集成测试。

网络一律离线：以 CLAWSGO_SELF_OFFLINE=1 环境变量模拟。模板/启发式路径为主。
"""

from __future__ import annotations

import json
import os

import pytest

from sciforge.core import Layout, get_layout


def _layout(tmp_path) -> Layout:
    os.chdir(tmp_path)
    return get_layout()


def _write_task_results(layout: Layout, task_id: str, series: dict) -> None:
    """写入 tasks/{id}/results.json，metrics 为多 tag 的伪运行序列。"""
    root = layout.task_dir(task_id)
    metrics = []
    for tag, vals in series.items():
        for v in vals:
            metrics.append({"tag": tag, "value": v, "ptype": "metric", "conf": "test"})
    (root / "results.json").write_text(
        json.dumps({"ok": True, "metrics": metrics}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def test_compare_metrics_basic_and_sig(tmp_path):
    from sciforge.research.bench import compare_metrics

    lay = _layout(tmp_path)
    _write_task_results(lay, "t_base", {"acc": [0.80, 0.81, 0.79, 0.80, 0.81, 0.80]})
    _write_task_results(lay, "t_ours",
                        {"acc": [0.90, 0.91, 0.89, 0.90, 0.91, 0.90],
                         "loss": [0.1, 0.2, 0.15, 0.12, 0.18, 0.13]})
    r = compare_metrics(paper_id="p_c", task_ids=["t_base", "t_ours"],
                        layout=lay, baseline="t_base")
    assert r.ok is True
    assert len(r.metric_rows) == 2
    ours = next(x for x in r.metric_rows if x["task"] == "t_ours")
    acc = next(i for i in ours["items"] if i["tag"] == "acc")
    assert 0.89 < acc["mean"] < 0.91
    assert acc["n"] == 6
    # baseline 自身不做检验
    base_row = next(x for x in r.metric_rows if x["task"] == "t_base")
    assert all(t["else_group"] != "t_base" for t in r.tests)
    # acc 差异显著（Welch + Mann-Whitney）
    t_acc = next(t for t in r.tests if t["tag"] == "acc")
    assert t_acc["t_test"]["different"] is True
    assert t_acc["t_test"]["p"] < 0.05
    assert t_acc["mann_whitney"]["different"] is True
    # 产物落盘
    md = (lay.project_dir("p_c") / "research" / "benchmark_compare.md")
    assert md.exists() and "对比表" in md.read_text(encoding="utf-8")


def test_compare_metrics_insufficient_samples(tmp_path):
    from sciforge.research.bench import compare_metrics

    lay = _layout(tmp_path)
    _write_task_results(lay, "t1", {"acc": [0.5]})
    _write_task_results(lay, "t2", {"acc": [0.6]})
    r = compare_metrics(paper_id="p_c2", task_ids=["t1", "t2"], layout=lay)
    assert r.ok is True
    assert r.tests == []  # 样本<2 → 不产出检验


def test_compare_metrics_invalid_task(tmp_path):
    from sciforge.research.bench import compare_metrics

    lay = _layout(tmp_path)
    lay.project_dir("p_c3")
    r = compare_metrics(paper_id="p_c3", task_ids=["ghost"], layout=lay)
    assert r.ok is False
    assert "ghost" in r.error or not r.metric_rows


def test_novelty_offline_template(tmp_path, monkeypatch):
    from sciforge.research.novelty import check_novelty

    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    lay = _layout(tmp_path)
    project = lay.project_dir("p_n")
    (project / "research").mkdir(parents=True, exist_ok=True)
    (project / "research" / "metadata.json").write_text(json.dumps({
        "title": "面向边缘设备的低延迟量化推理框架",
        "abstract": "本文提出一种新的量化方法，结合蒸馏与结构化剪枝，在端侧硬件上提升吞吐。",
    }, ensure_ascii=False), encoding="utf-8")
    r = check_novelty(paper_id="p_n", layout=lay, limit=5)
    assert r.ok is True
    assert r.offline is True
    assert r.phrases
    assert not r.similar_papers
    assert r.differentiators
    assert (project / "research" / "novelty.json").exists()


def test_novelty_missing_content(tmp_path):
    from sciforge.research.novelty import check_novelty

    lay = _layout(tmp_path)
    lay.project_dir("p_empty")
    r = check_novelty(paper_id="p_empty", layout=lay)
    assert r.ok is False
    assert "没有可利用" in r.error


def test_package_submission_zips_assets(tmp_path):
    from sciforge.deliver.package import package_submission

    lay = _layout(tmp_path)
    project = lay.project_dir("p_pkg")
    (project / "doc.md").write_text("# 标题\n正文。", encoding="utf-8")
    (project / "fig.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    (project / "research").mkdir(exist_ok=True)
    (project / "research" / "peer_review.md").write_text("审稿意见", encoding="utf-8")
    # 任务增量
    task = lay.task_dir("t_pkg")
    (task / "code.py").write_text("x = 1", encoding="utf-8")

    r = package_submission(paper_id="p_pkg", layout=lay, task_id="t_pkg")
    assert r["ok"] is True
    assert "submission_" in r["zip_path"]
    import zipfile
    with zipfile.ZipFile(r["zip_path"]) as z:
        names = set(z.namelist())
    assert "paper/doc.md" in names
    assert "paper/fig.png" in names
    assert "paper/research/peer_review.md" in names
    assert "reproduction/code.py" in names
    assert "cover_letter.md" in names
    assert "submission_checklist.md" in names
    assert "投稿前" in r["checklist"] and "- [x]" in r["checklist"]


def test_package_submission_missing_project(tmp_path):
    from sciforge.deliver.package import package_submission

    lay = _layout(tmp_path)
    r = package_submission(paper_id="p_none", layout=lay)
    assert r["ok"] is False
    assert "不存在" in r["error"]


def test_citation_landscape_offline(tmp_path, monkeypatch):
    from sciforge.research.community import citation_landscape

    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    lay = _layout(tmp_path)
    lay.project_dir("p_cit")
    r = citation_landscape(paper_id="p_cit", layout=lay,
                           doi_or_topic="大语言模型评测")
    assert r.ok is False  # 离线无数据
    assert r.mode == "topic"
    assert "无可用引文数据" in r.error


def test_citation_landscape_doi_mode_offline(tmp_path, monkeypatch):
    from sciforge.research.community import citation_landscape

    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    lay = _layout(tmp_path)
    lay.project_dir("p_cit2")
    r = citation_landscape(paper_id="p_cit2", layout=lay, doi_or_topic="10.48550/arXiv.2201.0")
    assert r.mode == "doi"
    assert r.ok is False


def test_project_memory_read_write(tmp_path):
    from sciforge.core.memory import project_memory

    lay = _layout(tmp_path)
    r1 = project_memory(paper_id="p_mem", layout=lay, action="milestone",
                        milestone="1.0.0", note="方案敲定")
    assert r1.ok is True
    r2 = project_memory(paper_id="p_mem", layout=lay, action="status",
                        status="实验")
    assert r2.ok is True
    r3 = project_memory(paper_id="p_mem", layout=lay, action="read")
    assert len(r3.entries) == 2
    assert r3.entries[-1]["status"] == "实验"
    # 空 note 时拒绝
    r4 = project_memory(paper_id="p_mem", layout=lay, action="note")
    assert r4.ok is False
    md = (lay.project_dir("p_mem") / "memory.json")
    assert md.exists()


def test_review_code_scans_py(tmp_path):
    from sciforge.reproduce.codereview import review_code

    lay = _layout(tmp_path)
    task = lay.task_dir("t_code")
    (task / "train.py").write_text(
        "import torch\n"
        "def train():\n"
        "    print('hi')\n"
        "    acc = 0.99  # magic\n"
        "    pass\n",
        encoding="utf-8",
    )
    r = review_code(task_id="t_code", layout=lay)
    assert r.ok is True
    assert len(r.files) == 1
    f = r.files[0]
    cats = {i["category"] for i in f["issues"]}
    assert "debug" in cats and "stub" in cats
    assert f["stats"]["has_backend"] is True
    assert r.scores["total"] is not None
    assert any(c["text"].startswith("含随机种子") for c in r.checklist)
    assert (task / "code_review.md").exists()


def test_review_code_missing_task(tmp_path):
    from sciforge.reproduce.codereview import review_code

    lay = _layout(tmp_path)
    r = review_code(task_id="ghost", layout=lay)
    assert r.ok is False
    assert "不存在" in r.error