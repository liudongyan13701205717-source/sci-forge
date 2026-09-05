"""导出线对外 API：export_document。

策略：
- 始终生成 LaTeX 源 (doc.tex) 与 HTML 预览 (doc.html)。
- target=pdf：优先 TeX 引擎编译；无引擎则用 PyMuPDF 渲染 md→pdf。
- target=docx：自研最小 docx 生成器（纯标准库）。
"""

from __future__ import annotations

import shutil

from sciforge.core import Layout, get_layout
from sciforge.export import convert, docx as _docx, render
from sciforge.write.doc import DocStore

VALID_TARGETS = {"pdf", "docx"}


def _find_tex() -> str | None:
    for exe in ("xelatex", "pdflatex", "lualatex"):
        p = shutil.which(exe)
        if p:
            return exe
    return None


def _compile_tex(tex_path: str, workdir: str) -> bool:
    import os
    import subprocess

    tex = _find_tex()
    if not tex:
        return False
    try:
        env = dict(os.environ)
        # 非交互
        r = subprocess.run(
            [tex, "-interaction=nonstopmode", "-halt-on-error", "-output-directory", workdir,
             os.path.basename(tex_path)],
            cwd=workdir, capture_output=True, timeout=120, env=env,
        )
        return r.returncode == 0 and os.path.exists(
            os.path.join(workdir, os.path.splitext(os.path.basename(tex_path))[0] + ".pdf")
        )
    except (subprocess.TimeoutExpired, OSError):
        return False


def export_document(
    paper_id: str,
    target: str = "pdf",
    *,
    layout: Layout | None = None,
) -> dict:
    """将已写 doc.md 导出为 LaTeX/PDF/docx。"""
    layout = layout or get_layout()
    if target not in VALID_TARGETS:
        return {"ok": False, "paper_id": paper_id, "target": target,
                "error": f"未知导出目标 {target!r}；合法：{sorted(VALID_TARGETS)}"}

    doc = DocStore(layout, paper_id)
    sections = doc.list_sections()
    if not sections or not doc.doc_md.exists():
        return {"ok": False, "paper_id": paper_id, "target": target,
                "error": f"项目 {paper_id} 尚无章节内容，请先用 write_section 写作。"}

    md = doc.doc_md.read_text(encoding="utf-8")

    # 1) 始终生成 LaTeX 源
    tex = convert.md_to_latex(md)
    tex_path = doc.root / "doc.tex"
    tex_path.write_text(tex, encoding="utf-8")

    # 2) 始终生成 HTML 预览
    html = convert.wrap_html(convert.md_to_html(md), title=paper_id)
    html_path = doc.root / "doc.html"
    html_path.write_text(html, encoding="utf-8")

    artefacts = [str(tex_path), str(html_path)]
    engine = "builtin"
    ok = True
    error = ""

    if target == "pdf":
        pdf_path = doc.root / "doc.pdf"
        if _find_tex() and _compile_tex(str(tex_path), str(doc.root)):
            engine = _find_tex()
        else:
            engine = "pymupdf"
            try:
                render.markdown_to_pdf(md, str(pdf_path))
            except Exception as e:  # noqa: BLE001
                ok = False
                error = f"PDF 渲染失败：{e}"
        artefacts.append(str(pdf_path))
    elif target == "docx":
        docx_path = doc.root / "doc.docx"
        try:
            _docx.markdown_to_docx(md, str(docx_path))
        except Exception as e:  # noqa: BLE001
            ok = False
            error = f"DOCX 生成失败：{e}"
        artefacts.append(str(docx_path))

    return {
        "ok": ok,
        "paper_id": paper_id,
        "target": target,
        "engine": engine,
        "sections": len(sections),
        "artefacts": artefacts,
        "note": error or f"已生成 {target}（引擎：{engine}）。",
    }
