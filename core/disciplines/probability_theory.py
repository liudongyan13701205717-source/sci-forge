"""概率论学科论文支持：测度论/极限定理体裁、AMS 引用样式与概率记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="probability_theory",
    aliases=("probability_theory", "概率论", "概率", "probability", "probability theory", "随机过程", "极限定理", "测度论", "随机分析"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与主定理陈述）", "methodology（模型设定、假设与记号）", "results（定理、命题与证明）", "discussion（应用、例子与进一步问题）", "references"),
        "case_study": ("abstract", "introduction", "case description（具体问题与背景描述）", "analysis（模型、证明与数值分析）", "results（定理结论与数值示例）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（概率论理论综述）", "evidence synthesis（主要发展与文献综合）", "future directions", "references"),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={"k1": "每个定理必须给出完整证明，或明确引用出处；不得以“显然”替代论证", "k2": "矩条件、可积性与正则性假设须显式列出，并说明是否可放宽", "k3": "定理归属与结果边界须准确，并区分本工作与已有文献"},
    conventions=("定理环境按 theorem/lemma/proposition/corollary 分级编号", "概率记法全文一致：概率用 \\mathbb{P}，期望用 \\mathbb{E}，方差用 \\operatorname{Var}", "随机变量用大写字母，取值用小写；分布收敛用 \\xrightarrow{d}", "证明以 QED 方块 \\qedsymbol 结束", "假设与未证明的断言必须显式标注为 conjecture 或 question"),
    key_venues=("Annals of Probability", "Probability Theory and Related Fields", "Electronic Journal of Probability", "Annals of Applied Probability", "Journal of Theoretical Probability"),
    units_and_formulas_notes=("使用 amsmath/amsthm/amssymb：对齐用 align/gather", "新增算子用 \\DeclareMathOperator 声明，不手打 \\mathrm 拼算子", "显示公式仅在被正文引用时编号", "括号尺寸用 \\bigl \\bigr 系列而非手动放大"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "NumPy", "SciPy", "MATLAB", "Octave", "Julia", "Stata", "Stan", "PyMC", "JAGS", "RStan", "SageMath", "SymPy", "Wolfram Mathematica", "Maple", "Jupyter Notebook", "R Markdown", "EndNote", "Zotero"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI"),
)
