"""解析线单元测试：先用 PyMuPDF 生成一个最小 PDF，再解析验证。"""

from __future__ import annotations

import pymupdf

from sciforge.parse.pdf import parse_pdf


def _make_sample_pdf(tmp_path):
    """生成含标题/摘要/章节/图表标题的最小 PDF。"""
    doc = pymupdf.open()
    page = doc.new_page()
    txt = (
        "A Sample Paper Title\n"
        "Author One\n"
        "Abstract\n"
        "We study a simple method.\n"
        "1 Introduction\n"
        "Some introduction text.\n"
        "2 Method\n"
        "We define the approach.\n"
        "Figure 1: Overview of pipeline.\n"
        "Table 1: Hyperparameters.\n"
        "3 Conclusion\n"
        "We conclude.\n"
    )
    page.insert_text((72, 72), txt, fontsize=11)
    pdf = tmp_path / "sample.pdf"
    doc.save(str(pdf))
    doc.close()
    return pdf


def test_parse_pdf_structure(tmp_path):
    pdf = _make_sample_pdf(tmp_path)
    res = parse_pdf(pdf)
    assert res.num_pages == 1
    # 至少有一个章节标题
    titles = [s["title"] for s in res.sections]
    assert any("Introduction" in t for t in titles)
    # 图表标题被识别
    assert len(res.figures) >= 1 or any(b.kind == "caption_fig" for b in res.blocks)
    assert len(res.tables) >= 1 or any(b.kind == "caption_table" for b in res.blocks)
    # 有正文段落
    assert any(b.kind == "para" for b in res.blocks)
    # 可序列化
    j = res.to_json()
    assert j["num_pages"] == 1
    assert "pages_text" in j


def test_parse_pdf_missing_file(tmp_path):
    import pytest

    with pytest.raises(FileNotFoundError):
        parse_pdf(tmp_path / "nope.pdf")
