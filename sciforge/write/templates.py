"""写作线本地模板：无 LLM 时按章节给出结构引导骨架，并把用户 prompt 织入。"""

from __future__ import annotations

# 各章节 -> 引导句模板（会拼接用户 prompt 作为正文要点）
_SKELETON = {
    "abstract": "本章为论文摘要，需凝练研究问题、方法、关键结果与结论。",
    "introduction": "本章为引言，需交代研究背景、动机、现状与本工作贡献。",
    "problem": "本章定义研究问题，明确输入、输出与优化目标。",
    "assumptions": "本章列出模型与推导所依赖的假设，并说明其合理性。",
    "notation": "本章统一符号说明，约定变量、集合与算子的记法。",
    "modeling": "本章建立数学模型，给出形式化定义与推导。",
    "solution": "本章给出求解算法与实现要点，包括初始化、迭代与收敛讨论。",
    "results": "本章报告实验结果与分析，含指标、对比与讨论。",
    "references": "本章列出参考文献，采用规范引用格式。",
    "appendix": "本章为附录，补充推导细节、参数表与杂项。",
}


def build_template(section: str, prompt: str, *, fmt: str) -> str:
    """返回本地引导骨架，正文要点取自用户 prompt。"""
    lead = _SKELETON.get(section, "本章写作指引。")
    body = "\n- ".join(
        line.strip("- ").strip() for line in prompt.splitlines() if line.strip()
    ) or prompt.strip()
    if fmt == "latex":
        return f"""% {lead}
% 写作要点：{body}

待补充 —— 请基于要点扩写（或在配置 LLM 后自动生成）。"""
    return f""">{lead}

写作要点：
- {body or "（待补充）"}

_待补充 —— 可在配置 LLM 后自动生成完整段落。_"""
