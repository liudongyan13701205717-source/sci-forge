"""写作线对外 API：write_section（LLM 优先，模板回退，落盘 + 4 层验证）。"""

from __future__ import annotations

from sciforge.core import Layout, get_layout
from sciforge.core import model as llm
from sciforge.write import templates, validate
from sciforge.write.doc import DocStore, _heading_for

_SECTION_PROMPT = {
    "abstract": "撰写论文摘要：300 词内，概述问题、方法、结果、结论。",
    "introduction": "撰写引言：背景、现状、空白、本工作贡献与结构安排。",
    "problem": "形式化定义研究问题：输入、输出、约束、目标函数。",
    "assumptions": "列出关键假设，说明合理性，避免过度理想化。",
    "notation": "汇总符号：变量、集合、算子、下标，统一记法。",
    "modeling": "建立数学模型：变量定义、目标、约束、推导。",
    "solution": "给出求解算法：初始化、迭代、收敛性、实现要点。",
    "results": "报告结果：设置、指标表、对比、分析讨论。",
    "references": "列出参考文献，规范引文格式。",
    "appendix": "补充推导细节、参数、杂项。",
}


def _collect_labels(doc: DocStore) -> set[str]:
    labels: set[str] = set()
    for sec in doc.list_sections():
        txt = doc.read_section(sec) or ""
        labels.update(sec for sec in __import__("re").findall(r"\\label\{([^}]+)\}", txt))
    return labels


def write_section(
    paper_id: str,
    section: str,
    prompt: str,
    format: str = "latex",
    *,
    layout: Layout | None = None,
) -> dict:
    """按章节引导生成内容（LLM 优先，模板回退），落盘并返回。"""
    layout = layout or get_layout()

    # Layer 1 输入验证
    v1 = validate.validate_inputs(section=section, format=format, prompt=prompt)
    if not v1.ok:
        return {
            "ok": False,
            "paper_id": paper_id,
            "section": section,
            "validations": {"l1_inputs": False, "l2_structure": False,
                            "l3_references": False, "l4_doc": False},
            "notes": v1.messages,
        }

    doc = DocStore(layout, paper_id)

    # 生成：LLM 优先，模板回退
    generator = "template"
    content = templates.build_template(section, prompt, fmt=format)
    try:
        if llm.configured():
            llm_prompt = (
                f"请撰写论文「{_heading_for(section)}」章节，格式为 {format}。\n"
                f"写作要点：{prompt}\n"
                f"{_SECTION_PROMPT.get(section, '')}\n"
                "只输出该章节正文，不要标题。"
            )
            content = llm.chat(llm_prompt, temperature=0.4, max_tokens=2500)
            generator = "llm"
    except RuntimeError:
        pass  # LLM 不可用 -> 模板回退

    # Layer 2 结构验证（\begin/\end、括号配对）
    v2 = validate.validate_structure(content, format=format)

    # Layer 3 引用验证（孤立 \ref）
    labels = _collect_labels(doc)
    v3 = validate.validate_references(labels, content, format=format)
    # 若产生孤立引用，补上定义以保持一致性（记录性修复，不阻断）
    extra_labels: list[str] = []
    if format == "latex":
        import re

        refs = set(re.findall(r"\\ref\{([^}]+)\}", content))
        for r in refs - labels:
            content += f"\n\\label{{{r}}}\n"
            extra_labels.append(r)

    doc.write_section(section, content, fmt=format)

    # Layer 4 整篇补全度
    v4 = validate.validate_doc(doc.list_sections())

    issues = v1.messages + v2.messages + v3.messages + v4.messages
    return {
        "ok": True,
        "paper_id": paper_id,
        "section": section,
        "format": format,
        "generator": generator,
        "doc_path": str(doc.doc_md),
        "content": content,
        "validations": {
            "l1_inputs": v1.ok,
            "l2_structure": v2.ok,
            "l3_references": v3.ok,
            "l4_doc": v4.ok,
        },
        "notes": issues,
        "auto_labels": extra_labels,
    }
