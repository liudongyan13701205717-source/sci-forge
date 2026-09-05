"""导出线：自研最小 DOCX 生成器（纯标准库，零外部依赖）。

DOCX 本质是 zip 包 + OOXML。逐段写入 word/document.xml：
标题用 Heading1/2 样式，正文用 Normal，代码块用等宽可忽略（统一正文）。
"""

from __future__ import annotations

import re
import zipfile

_BLOCK_FENCE = re.compile(r"^```(\w*)\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_STRIP = re.compile(r"[`*$]")
_ESCAPE = {"&": "&amp;", "<": "&lt;", ">": "&gt;"}


def _esc(t: str) -> str:
    return "".join(_ESCAPE.get(c, c) for c in t)


_CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml"
 ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1"
 Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
 Target="word/document.xml"/>
</Relationships>"""

_DOC = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>{body}
<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440"
w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>
</w:body></w:document>"""


def _para(text: str, style: str | None = None) -> str:
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f"<w:p>{style_xml}<w:r><w:t xml:space=\"preserve\">{_esc(text)}</w:t></w:r></w:p>"


def markdown_to_docx(md: str, out_path: str) -> str:
    body_parts: list[str] = []
    lines = md.splitlines()
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        fence = _BLOCK_FENCE.match(line.strip())
        if fence:
            buf = []
            i += 1
            while i < n and not _BLOCK_FENCE.match(lines[i].strip()):
                # 等宽：加空格占位（保持换行）
                buf.append(_STRIP.sub("", lines[i]))
                i += 1
            body_parts.append(_para("\n".join(buf)))
            i += 1
            continue
        h = _HEADING.match(line)
        if h:
            lvl = len(h.group(1))
            style = "Heading1" if lvl <= 2 else "Heading2"
            body_parts.append(_para(_STRIP.sub("", h.group(2).strip()), style))
            i += 1
            continue
        if re.match(r"^[-*]\s+", line):
            body_parts.append(_para(_STRIP.sub("", re.sub(r"^[-*]\s+", "- ", line))))
            i += 1
            continue
        if line.strip() == "":
            i += 1
            continue
        body_parts.append(_para(_STRIP.sub("", line.strip())))
        i += 1

    xml = _DOC.format(body="".join(body_parts))
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", _CONTENT_TYPES)
        z.writestr("_rels/.rels", _RELS)
        z.writestr("word/document.xml", xml)
    return out_path
