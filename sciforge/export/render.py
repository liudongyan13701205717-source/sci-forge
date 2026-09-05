"""导出线：用 PyMuPDF 将 markdown 渲染为不依赖外部 TeX 引擎的 PDF。

无外部二进制时交付真实可用 PDF。布局：标题分级字号、代码块用等宽字体、
自动分页。
"""

from __future__ import annotations

import re

import pymupdf

_BLOCK_FENCE = re.compile(r"^```(\w*)\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_UL_ITEM = re.compile(r"^[-*]\s+(.*)$")
_OL_ITEM = re.compile(r"^\d+\.\s+(.*)$")
_STRIP = re.compile(r"[`*$]")

_MARGIN = 60
_W = pymupdf.paper_size("a4")[0] - 2 * _MARGIN
_FONTS = {1: ("helv", 22), 2: ("helv", 17), 3: ("helv", 14), 4: ("helv", 12),
          5: ("helv", 11), 6: ("helv", 10)}
_BODY = ("helv", 11)
_MONO = ("cour", 9.5)


def _clean(text: str) -> str:
    return _STRIP.sub("", text)


class _Writer:
    def __init__(self) -> None:
        self.doc = pymupdf.open()
        self.page = None
        self.y = 0.0
        self._new_page()

    def _new_page(self) -> None:
        self.page = self.doc.new_page(width=pymupdf.paper_size("a4")[0],
                                      height=pymupdf.paper_size("a4")[1])
        self.y = _MARGIN

    def _ensure(self, need: float) -> None:
        if self.y + need > pymupdf.paper_size("a4")[1] - _MARGIN:
            self._new_page()

    def text(self, txt: str, *, font: str = "helv", size: float = 11,
             indent: float = 0.0, space_after: float = 4.0) -> None:
        self._ensure(size + space_after)
        self.page.insert_text((_MARGIN + indent, self.y), txt,
                              fontname=font, fontsize=size)
        self.y += size * 1.4 + space_after

    def code_block(self, lines: list[str]) -> None:
        need = 14 + len(lines) * (_MONO[1] * 1.4)
        self._ensure(need)
        # 浅底色
        h = len(lines) * _MONO[1] * 1.4 + 10
        r = pymupdf.Rect(_MARGIN, self.y - 8, _MARGIN + _W, self.y - 8 + h)
        self.page.draw_rect(r, color=(0.9, 0.9, 0.9), fill=(0.95, 0.95, 0.95))
        for ln in lines:
            self.text(ln, font=_MONO[0], size=_MONO[1], indent=6.0, space_after=0.0)
        self.y += 6


def markdown_to_pdf(md: str, out_path: str) -> str:
    w = _Writer()
    lines = md.splitlines()
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        fence = _BLOCK_FENCE.match(line.strip())
        if fence:
            buf = []
            i += 1
            while i < n and not _BLOCK_FENCE.match(lines[i].strip()):
                buf.append(_clean(lines[i]))
                i += 1
            w.code_block(buf)
            i += 1
            continue
        h = _HEADING.match(line)
        if h:
            lvl = min(len(h.group(1)), 6)
            font, size = _FONTS.get(lvl, _FONTS[6])
            w.text(_clean(h.group(2).strip()), font=font, size=size, space_after=6)
            i += 1
            continue
        ul, ol = _UL_ITEM.match(line), _OL_ITEM.match(line)
        if ul or ol:
            num = 1
            while i < n:
                it = _UL_ITEM.match(lines[i]) or _OL_ITEM.match(lines[i])
                if it:
                    prefix = f"{num}. " if ol else "- "
                    w.text(_clean(prefix + it.group(1).strip()),
                           indent=12.0, space_after=2)
                    num += 1
                    i += 1
                elif lines[i].strip() == "":
                    i += 1
                else:
                    break
            w.y += 3
            continue
        if line.strip() == "":
            i += 1
            continue
        w.text(_clean(line.strip()))
        i += 1
    w.doc.save(out_path)
    w.doc.close()
    return out_path
