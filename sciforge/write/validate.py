"""写作线验证：4 层引用/完整性验证。

Layer 1 validate_inputs     —— 章节合法、格式合法、prompt 有效（语法/入口层）
Layer 2 validate_structure  —— LaTeX 结构配对：\\begin/\\end、\\label/\\ref、括号配对
Layer 3 validate_references —— 引用一致性：检测孤立的 \\ref（无对应 label）
Layer 4 validate_doc        —— 整篇补全度与章节覆盖（写作推进完整性）
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

VALID_SECTIONS = {
    "abstract",
    "introduction",
    "problem",
    "assumptions",
    "notation",
    "modeling",
    "solution",
    "results",
    "references",
    "appendix",
}
VALID_FORMATS = {"latex", "markdown"}

_SCI_PROMPT_HINT = re.compile(
    r"[\u4e00-\u9fffA-Za-z0-9]{6,}", re.UNICODE
)


@dataclass
class Verdict:
    ok: bool = True
    messages: list[str] = field(default_factory=list)

    def add_error(self, msg: str) -> None:
        self.ok = False
        self.messages.append(msg)

    def to_dict(self) -> dict:
        return {"ok": self.ok, "issues": self.messages}


# ---------- Layer 1 ----------
def validate_inputs(*, section: str, format: str, prompt: str) -> Verdict:
    v = Verdict()
    if section not in VALID_SECTIONS:
        v.add_error(f"未知章节 {section!r}；合法章节：{sorted(VALID_SECTIONS)}")
    if format not in VALID_FORMATS:
        v.add_error(f"未知格式 {format!r}；合法格式：{sorted(VALID_FORMATS)}")
    if not prompt or not prompt.strip():
        v.add_error("prompt 不能为空")
    elif len(prompt) < 4:
        v.add_error("prompt 过短，缺少有效信息")
    if not _SCI_PROMPT_HINT.search(prompt or ""):
        v.add_error("prompt 未含可识别的有效内容")
    return v


# ---------- Layer 2 ----------
_BEGIN_RE = re.compile(r"\\begin\{([a-zA-Z*]+)\}")
_END_RE = re.compile(r"\\end\{([a-zA-Z*]+)\}")
_BRACKETS = {"{": "}", "(": ")"}


def _balanced(text: str) -> bool:
    if text.count("{") != text.count("}"):
        return False
    if text.count("(") != text.count(")"):
        return False
    if text.count("[") != text.count("]"):
        return False
    return True


def validate_structure(content: str, *, format: str) -> Verdict:
    v = Verdict()
    if format != "latex":
        # markdown 仅做括号配对的轻度校验
        if not _balanced(content):
            v.add_error("括号不配对")
        return v
    begins = _BEGIN_RE.findall(content)
    ends = _END_RE.findall(content)
    if len(begins) != len(ends):
        v.add_error(f"LaTeX begin/end 数量不匹配：{len(begins)} 开 vs {len(ends)} 闭")
    # 环境名集合一致性（begin 出现过则 end 也应出现同名）
    envs = set(begins)
    for e in envs:
        if begins.count(e) != ends.count(e):
            v.add_error(f"LaTeX 环境 {e} begin/end 不配对：开 {begins.count(e)} 闭 {ends.count(e)}")
    if not _balanced(content):
        v.add_error("LaTeX 括号不配对")
    return v


# ---------- Layer 3 ----------
def validate_references(labels: set[str], content: str, *, format: str) -> Verdict:
    """检测孤立 \\ref：引用了但未定义的 label。需传入全文已定义的 label 集合。"""
    v = Verdict()
    if format != "latex":
        return v
    defined = set(labels)
    refs = set(re.findall(r"\\ref\{([^}]+)\}", content))
    for r in refs - defined:
        v.add_error(f"孤立引用 \\ref{{{r}}}：无对应 \\label")
    return v


# ---------- Layer 4 ----------
def validate_doc(present_sections: list[str]) -> Verdict:
    """整篇补全度：核心章节是否都已覆盖（不要求一次写全，给出建设性提示）。"""
    v = Verdict()
    core = ["abstract", "introduction", "results"]
    missing = [s for s in core if s not in present_sections]
    if missing:
        # 未完成不算硬错误，但给出提示
        v.messages.append(f"核心章节尚未覆盖：{missing}（可继续补充）")
    return v
