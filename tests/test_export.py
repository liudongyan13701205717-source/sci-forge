"""导出线测试：md → LaTeX / HTML / PDF / DOCX 全部真实产出。"""

from __future__ import annotations

import zipfile

import pymupdf

from sciforge.core import Layout
from sciforge.export import convert, docx as _docx, render
from sciforge.export.api import export_document
from sciforge.write.api import write_section

_SAMPLE = """## 摘要

本研究提出一种高效方法。

## 引言

研究背景：\n- 现状一\n- 现状二\n\n核心是 `f(x) = x^2`。
"""


def test_md_to_latex_structures():
    tex = convert.md_to_latex(_SAMPLE)
    assert "\\section{摘要}" in tex
    assert "\\section{引言}" in tex
    assert "\\begin{itemize}" in tex
    assert "\\texttt{f(x) = x\\^2}" in tex or "\\texttt{f(x) = x^2}" in tex


def test_md_to_html_wrap():
    html = convert.wrap_html(convert.md_to_html(_SAMPLE), title="t")
    assert "<h2>摘要</h2>" in html
    assert "<ul>" in html
    assert "<code>f(x) = x^2</code>" in html


def test_md_to_pdf_valid(tmp_path):
    out = tmp_path / "o.pdf"
    render.markdown_to_pdf(_SAMPLE, str(out))
    assert out.exists()
    d = pymupdf.open(str(out))
    assert d.page_count >= 1
    d.close()


def test_md_to_docx_valid(tmp_path):
    out = tmp_path / "o.docx"
    _docx.markdown_to_docx(_SAMPLE, str(out))
    assert out.exists()
    with zipfile.ZipFile(str(out)) as z:
        names = z.namelist()
        assert "word/document.xml" in names
        assert "[Content_Types].xml" in names
        xml = z.read("word/document.xml").decode("utf-8")
        assert "摘要" in xml


def test_export_document_all_targets(tmp_path):
    layout = Layout(tmp_path)
    layout.ensure()
    write_section("d1", "abstract", "研究大语言模型可解释性的高效方法", layout=layout)
    write_section("d1", "introduction", "背景与动机要点", layout=layout)

    rpdf = export_document("d1", "pdf", layout=layout)
    assert rpdf["ok"] is True, rpdf
    p = layout.project_dir("d1")
    for name in ("doc.md", "doc.tex", "doc.html", "doc.pdf"):
        assert (p / name).exists(), f"缺 {name}"

    rdocx = export_document("d1", "docx", layout=layout)
    assert rdocx["ok"] is True, rdocx
    assert (p / "doc.docx").exists()

    rbad = export_document("d1", "epub", layout=layout)
    assert rbad["ok"] is False
