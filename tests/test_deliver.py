"""交付线测试：复现任务与写作项目的交付物清单。"""

from __future__ import annotations

from sciforge.core import Layout
from sciforge.deliver.api import get_deliverables
from sciforge.write.api import write_section


def _make_task_dir(layout, tid):
    d = layout.task_dir(tid)
    (d / "generated.py").write_text("print(1)", encoding="utf-8")
    (d / "results.json").write_text('{"ok": true}', encoding="utf-8")
    (d / "convergence.png").write_bytes(b"fake-png")
    (d / "runs").mkdir(exist_ok=True)
    (d / "runs" / "out.log").write_text("log", encoding="utf-8")
    return d


def test_deliverables_task_classified(tmp_path):
    layout = Layout(tmp_path)
    layout.ensure()
    _make_task_dir(layout, "t9")
    r = get_deliverables(task_id="t9", layout=layout)
    assert r["ok"] is True
    assert r["kind"] == "task"
    assert r["count"] >= 3
    kinds = set(r["by_kind"])
    # generated.py -> source, results.json -> data, png -> image
    assert "source" in kinds and "data" in kinds and "image" in kinds
    paths = {i["path"] for i in r["deliverables"]}
    assert "generated.py" in paths
    assert "convergence.png" in paths


def test_deliverables_missing_task_empty_not_error(tmp_path):
    layout = Layout(tmp_path)
    layout.ensure()
    r = get_deliverables(task_id="ghost", layout=layout)
    assert r["ok"] is True
    assert r["count"] == 0


def test_deliverables_project(tmp_path):
    layout = Layout(tmp_path)
    layout.ensure()
    write_section("doc9", "abstract", "测试论文要点", layout=layout)
    from sciforge.export.api import export_document

    export_document("doc9", "pdf", layout=layout)
    r = get_deliverables(paper_id="doc9", layout=layout)
    assert r["ok"] is True
    assert r["kind"] == "project"
    by = r["by_kind"]
    assert "report" in by
    assert any(p.endswith("doc.pdf") for p in by.get("report", []))
    assert any(p.endswith("doc.md") for p in by.get("report", []))


def test_deliverables_requires_key(tmp_path):
    layout = Layout(tmp_path)
    layout.ensure()
    r = get_deliverables(layout=layout)
    assert r["ok"] is False
