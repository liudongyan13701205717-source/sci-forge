"""复现五步闭环集成测试：懒加载脚本（无 LLM），模板代码生成跑通全部步骤。"""

from __future__ import annotations

import json

import pymupdf

from sciforge.core import Layout
from sciforge.reproduce import pipeline
from sciforge.reproduce.tasks import Task


def _make_pdf(tmp_path) -> str:
    doc = pymupdf.open()
    page = doc.new_page()
    txt = (
        "Linear Regression Reproduction\n"
        "Abstract\n"
        "We reproduce a small regression model.\n"
        "1 Introduction\n"
        "We set learning rate 0.01, 50 epochs, batch size 32.\n"
        "2 Method\n"
        "Standard gradient descent.\n"
        "3 Results\n"
        "Figure 1: Convergence.\n"
    )
    page.insert_text((72, 72), txt, fontsize=11)
    p = tmp_path / "repro.pdf"
    doc.save(str(p))
    doc.close()
    return str(p)


def test_full_pipeline_template(tmp_path):
    """模板代码生成（无 LLM）应跑通：解析→方案→代码→执行→交付。"""
    pdf = _make_pdf(tmp_path)
    layout = Layout(tmp_path)
    layout.ensure()
    task = Task(task_id="t1", pdf_path=pdf, framework="pytorch")
    res = pipeline.run_pipeline(task, layout, llm_fn=None)

    assert res["status"] == "done", res
    # 五步都在
    steps = {s["step"]: s for s in res["steps"]}
    assert set(steps) == {1, 2, 3, 4, 5}
    assert all(s["ok"] for s in steps.values()), res["steps"]

    # 执行得到了真实指标（train_loss/test_loss/r2）与图
    run_step = steps[4]
    tags = {m["tag"] for m in run_step["detail"]["metrics"]}
    assert "train_loss" in tags and "r2" in tags, run_step["detail"]
    assert run_step["detail"]["plots"], "应有图产出"

    # deliverables 目录
    deliv_step = steps[5]
    assert deliv_step["detail"]["count"] >= 3  # source + results + report (+figure)

    # 检查 results.json 落盘
    rp = layout.task_dir("t1") / "results.json"
    assert rp.exists()
    rj = json.loads(rp.read_text(encoding="utf-8"))
    assert rj["ok"] is True
    assert any(m["tag"] == "r2" for m in rj["metrics"])
