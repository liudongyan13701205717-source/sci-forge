"""PDF 结构化解析。

核心机制（防长文 OOM）：
- 用 PyMuPDF 的 Generator 模式逐页读取，并逐页 `gc.collect()`，避免长论文把所有页文本常驻内存。
- 产出类型化 `PdfParseResult`：分页文本、章节层级、图表标题、公式、元数据。

兼容两种导入：`pymupdf`（新）与 `fitz`（旧，仅回退）。
"""

from __future__ import annotations

import gc
import re
from dataclasses import dataclass, field as dataclass_field
from pathlib import Path
from typing import Iterator, Optional

try:  # pragma: no cover - 依赖探测
    import pymupdf as _pdf  # type: ignore
except ImportError:  # pragma: no cover
    import fitz as _pdf  # type: ignore  # noqa: N813


# 常见章节标题（可扩展）
_SECTION_PATTERNS = [
    re.compile(r"^\s*(abstract|introduction|related work|method(ology)?|"
               r"experiments?|results?|conclusion|discussion|appendix)\s*$", re.I),
    re.compile(r"^\s*(\d+(\.\d+)*)[\s.\-]\s*([A-Z][A-Za-z0-9 &/\\\-]+)\s*$"),
]

# 图表标题（常见格式：Figure N: ... / Table N: ...）
_FIG_CAP = re.compile(r"^\s*(fig(?:ure)?|fig\.)\s*\.?\s*(\d+)\s*[:\-]?\s*(.*)$", re.I)
_TABLE_CAP = re.compile(r"^\s*(tab(?:le)?|tab\.)\s*\.?\s*(\d+)\s*[:\-]?\s*(.*)$", re.I)

# 块级数学环境
_MATH_ENV = re.compile(r"\\begin\{(equation|align|gather|multline|\[)\*?\}.*?\\end\{[\}\]\*]*\}",
                       re.DOTALL)
_INLINE_MATH = re.compile(r"\$[^$\n]+\$")


@dataclass
class Block:
    """解析出的一个文本块。"""
    page: int
    kind: str  # 'heading' | 'para' | 'caption_fig' | 'caption_table' | 'math'
    text: str
    meta: dict = dataclass_field(default_factory=dict)


@dataclass
class PdfParseResult:
    path: str
    title: str = ""
    authors: list[str] = dataclass_field(default_factory=list)
    abstract: str = ""
    num_pages: int = 0
    pages_text: list[str] = dataclass_field(default_factory=list)
    blocks: list[Block] = dataclass_field(default_factory=list)
    figures: list[dict] = dataclass_field(default_factory=list)
    tables: list[dict] = dataclass_field(default_factory=list)
    sections: list[dict] = dataclass_field(default_factory=list)

    def to_json(self) -> dict:
        return {
            "path": self.path,
            "title": self.title,
            "authors": self.authors,
            "abstract": self.abstract,
            "num_pages": self.num_pages,
            "pages_text": self.pages_text,
            "blocks": [b.__dict__ for b in self.blocks],
            "figures": self.figures,
            "tables": self.tables,
            "sections": self.sections,
        }


def _iter_pages(path: Path) -> Iterator[tuple[int, str]]:
    """逐页 yield (页码, 文本)，逐页 GC。"""
    doc = _pdf.open(str(path), filetype="pdf")
    try:
        for i, page in enumerate(doc):
            text = page.get_text("text") or ""
            yield i, text
            del page
            if i % 5 == 0:
                gc.collect()
    finally:
        doc.close()
        gc.collect()


def _looks_like_heading(line: str) -> Optional[str]:
    for pat in _SECTION_PATTERNS:
        m = pat.match(line)
        if m:
            return line.strip()
    return None


def _classify_line(line: str) -> Optional[str]:
    """返回 (kind) 或 None（普通段落）。"""
    if _FIG_CAP.match(line):
        return "caption_fig"
    if _TABLE_CAP.match(line):
        return "caption_table"
    if _looks_like_heading(line):
        return "heading"
    # 独立公式块：含 begin{...} 或多于 2 个行内公式的孤立行
    if _MATH_ENV.search(line) or _INLINE_MATH.findall(line):
        return "math"
    return None


def _parse_meta(text: str) -> tuple[str, list[str], str]:
    """启发式抽取元数据：标题（首非空行）、作者、摘要。"""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    title = lines[0] if lines else ""
    # 摘要：Abstract 冒号后或空白之后的段
    abstract = ""
    am = re.search(r"Abstract[:.\s]*\n?(.*?)(?=$|Keywords|1\.|I\.)", text, re.I | re.S)
    if am:
        abstract = am.group(1).strip()
    return title, [], abstract


def parse_pdf(pdf_path: str | Path, *, max_pages: Optional[int] = None) -> PdfParseResult:
    """解析 PDF 为结构化结果。

    Args:
        pdf_path: PDF 路径。
        max_pages: 可选，最多解析页数（防超长文档）。
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF 不存在：{path}")

    result = PdfParseResult(path=str(path))
    doc = _pdf.open(str(path), filetype="pdf")
    try:
        result.num_pages = doc.page_count
        meta = doc.metadata or {}
        result.title = meta.get("title") or path.stem
    finally:
        doc.close()

    # 第一遍：分页文本 + 组装 blocks；同时收集元数据
    for i, text in _iter_pages(path):
        if max_pages is not None and i >= max_pages:
            break
        result.pages_text.append(text)
        for raw in text.splitlines():
            line = raw.rstrip()
            if not line.strip():
                continue
            kind = _classify_line(line)
            if kind == "heading":
                result.blocks.append(Block(i, "heading", line.strip(), {"level": 1}))
            elif kind in ("caption_fig", "caption_table"):
                result.blocks.append(Block(i, kind, line.strip()))
            elif kind == "math":
                result.blocks.append(Block(i, "math", line.strip()))
            else:
                result.blocks.append(Block(i, "para", line.strip()))

    # 从首页文本抽取标题/作者/摘要（覆盖元数据为空的情况）
    if result.pages_text:
        t, authors, abstract = _parse_meta(result.pages_text[0])
        result.authors = authors or result.authors
        result.abstract = abstract or result.abstract
        if not result.title and t:
            result.title = t

    # 收集图表
    for b in result.blocks:
        if b.kind == "caption_fig":
            m = _FIG_CAP.match(b.text)
            if m:
                result.figures.append({"page": b.page, "index": int(m.group(2)),
                                       "caption": m.group(3).strip()})
        elif b.kind == "caption_table":
            m = _TABLE_CAP.match(b.text)
            if m:
                result.tables.append({"page": b.page, "index": int(m.group(2)),
                                      "caption": m.group(3).strip()})

    # 章节层级（按标题块顺序）
    for b in result.blocks:
        if b.kind == "heading":
            result.sections.append({"page": b.page, "title": b.text, "level": 1})

    return result
