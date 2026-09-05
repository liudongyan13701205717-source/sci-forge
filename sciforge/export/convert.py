"""导出线：轻量 markdown → LaTeX / HTML 转换器（无外部依赖）。

支持结构元素：
  ## 标题 -> \\section{}/<h2>
  ### 标题 -> \\subsection{}/<h3>
  行内 `code`、*em*、**bold**
  代码块 ```...``` -> verbatim/<pre>
  无序列表 - / * -> itemize/<ul>
  有序列表 1. -> enumerate/<ol>
  数学 $...$ -> 原样透传（latex）/ <span class=math>
"""

from __future__ import annotations

import re

_BLOCK_FENCE = re.compile(r"^```(\w*)\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_UL_ITEM = re.compile(r"^[-*]\s+(.*)$")
_OL_ITEM = re.compile(r"^\d+\.\s+(.*)$")


def _inline_latex(text: str) -> str:
    # 顺序处理行内：code 优先，避免公式/强调被误改
    def _code(m):
        return "\\texttt{" + m.group(1) + "}"

    def _bold(m):
        return "\\textbf{" + m.group(1) + "}"

    def _em(m):
        return "\\textit{" + m.group(1) + "}"

    # latex 环境里 $..$ 原样，不做强调替换
    t = re.sub(r"`([^`]+)`", _code, text)
    t = re.sub(r"\*\*([^*]+)\*\*", _bold, t)
    t = re.sub(r"\*([^*]+)\*", _em, t)
    # 转义 & % # _ 等（避免破坏 latex；math 已原样含 $）
    t = re.sub(r"([&%#])", r"\\\1", t)
    return t


def md_to_latex(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        fence = _BLOCK_FENCE.match(line.strip())
        if fence:
            buf = []
            i += 1
            while i < n and not _BLOCK_FENCE.match(lines[i].strip()):
                buf.append(lines[i])
                i += 1
            out.append("\\begin{verbatim}\n" + "\n".join(buf) + "\n\\end{verbatim}")
            i += 1
            continue
        h = _HEADING.match(line)
        if h:
            lvl = len(h.group(1))
            # markdown 的 ## (H2) 在论文中作顶层 section，整体降一级映射
            tex_lvl = lvl if lvl <= 1 else lvl - 1
            title = _inline_latex(h.group(2).strip())
            cmd = {1: "section", 2: "subsection", 3: "subsubsection"}.get(tex_lvl, "section")
            out.append(f"\\{cmd}{{{title}}}")
            i += 1
            continue
        ul = _UL_ITEM.match(line)
        ol = _OL_ITEM.match(line)
        if ul or ol:
            env = "itemize" if ul else "enumerate"
            buf = [rf"\begin{{{env}}}"]
            while i < n:
                it = _UL_ITEM.match(lines[i]) or _OL_ITEM.match(lines[i])
                if it:
                    buf.append(r"\item " + _inline_latex(it.group(1).strip()))
                    i += 1
                elif lines[i].strip() == "":
                    i += 1
                else:
                    break
            buf.append(rf"\end{{{env}}}")
            out.append("\n".join(buf))
            continue
        if line.strip() == "":
            i += 1
            continue
        out.append(_inline_latex(line.strip()))
        i += 1
    return "\n\n".join(out)


def _inline_html(text: str) -> str:
    def _code(m):
        return "<code>" + m.group(1) + "</code>"

    def _bold(m):
        return "<strong>" + m.group(1) + "</strong>"

    def _em(m):
        return "<em>" + m.group(1) + "</em>"

    t = re.sub(r"`([^`]+)`", _code, text)
    t = re.sub(r"\*\*([^*]+)\*\*", _bold, t)
    t = re.sub(r"\*([^*]+)\*", _em, t)
    return t


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        fence = _BLOCK_FENCE.match(line.strip())
        if fence:
            buf = []
            i += 1
            while i < n and not _BLOCK_FENCE.match(lines[i].strip()):
                buf.append(lines[i])
                i += 1
            out.append("<pre><code>" + "\n".join(buf) + "\n</code></pre>")
            i += 1
            continue
        h = _HEADING.match(line)
        if h:
            lvl = min(len(h.group(1)), 6)
            out.append(f"<h{lvl}>{_inline_html(h.group(2).strip())}</h{lvl}>")
            i += 1
            continue
        ul = _UL_ITEM.match(line)
        ol = _OL_ITEM.match(line)
        if ul or ol:
            tag = "ul" if ul else "ol"
            buf = [f"<{tag}>"]
            while i < n:
                it = _UL_ITEM.match(lines[i]) or _OL_ITEM.match(lines[i])
                if it:
                    buf.append("<li>" + _inline_html(it.group(1).strip()) + "</li>")
                    i += 1
                elif lines[i].strip() == "":
                    i += 1
                else:
                    break
            buf.append(f"</{tag}>")
            out.append("\n".join(buf))
            continue
        if line.strip() == "":
            i += 1
            continue
        out.append("<p>" + _inline_html(line.strip()) + "</p>")
        i += 1
    return "\n".join(out)


def wrap_html(body: str, title: str = "Document") -> str:
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
body{{font-family:sans-serif;max-width:820px;margin:2em auto;line-height:1.7;padding:0 1em}}
h1,h2,h3{{margin-top:1.4em}}
code{{background:#f5f5f5;padding:.1em .3em;border-radius:3px}}
pre{{background:#f5f5f5;padding:1em;overflow:auto;border-radius:4px}}
</style>
</head>
<body>
{body}
</body>
</html>"""
