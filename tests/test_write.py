"""写作线测试：4 层引用验证 + 模板生成 + 落盘。"""

from __future__ import annotations

import pytest

from sciforge.core import Layout
from sciforge.write import validate
from sciforge.write.api import write_section


@pytest.fixture
def layout(tmp_path):
    l = Layout(tmp_path)
    l.ensure()
    return l


def test_l1_inputs_rejects_bad_section(layout):
    r = write_section("p1", "badsection", "有效要点内容", layout=layout)
    assert r["ok"] is False
    assert any("未知章节" in m for m in r["notes"] or [])


def test_l1_inputs_rejects_bad_format(layout):
    r = write_section("p1", "abstract", "有效要点内容", format="docx", layout=layout)
    assert r["ok"] is False
    assert any("未知格式" in m for m in r["notes"] or [])


def test_l1_inputs_rejects_empty_prompt(layout):
    r = write_section("p1", "abstract", "  ", layout=layout)
    assert r["ok"] is False


def test_template_fallback_persists(layout):
    r = write_section("p1", "abstract", "研究大语言模型的可解释性方法", layout=layout)
    assert r["ok"] is True
    assert r["generator"] == "template"  # 无 LLM 环境
    assert r["section"] == "abstract"
    assert r["validations"]["l1_inputs"] is True
    # 落盘 + doc.md 拼接
    p = layout.project_dir("p1") / "doc.md"
    assert p.exists()
    assert "## 摘要" in p.read_text(encoding="utf-8")


def test_latex_structure_validation():
    v = validate.validate_structure(r"\begin{align} x=1 \end{align}", format="latex")
    assert v.ok is True
    v2 = validate.validate_structure(r"\begin{align} x=1", format="latex")
    assert v2.ok is False
    assert any("begin/end" in m for m in v2.messages)


def test_l3_reference_orphan_detection():
    v = validate.validate_references({"fig1"}, r"见 \ref{fig9}", format="latex")
    assert v.ok is False
    assert any("孤立引用" in m for m in v.messages)
    v2 = validate.validate_references({"fig1"}, r"见 \ref{fig1}", format="latex")
    assert v2.ok is True


def test_full_doc_build(layout):
    # 写多个章节后 doc.md 按序拼接
    for sec in ["introduction", "notation", "results", "abstract"]:
        write_section("p2", sec, f"正文要点 {sec}", layout=layout)
    md = (layout.project_dir("p2") / "doc.md").read_text(encoding="utf-8")
    # 按 SECTION_ORDER，abstract 应在 introduction 前
    assert md.index("## 摘要") < md.index("## 引言")
