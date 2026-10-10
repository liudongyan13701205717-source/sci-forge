"""数理统计（理论统计）学科论文支持：统计推断、假设检验、分布理论体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mathematical_statistics",
    aliases=("mathematical statistics", "数理统计", "理论统计", "统计推断",
             "theoretical statistics", "统计理论", "概率统计", "随机分析"),
    paper_types={
        "research": ("abstract", "introduction（问题背景与统计模型）", "model and assumptions（模型假设与记号）", "main results（定理/引理，按编号陈述）", "proofs（证明与关键技术引理）", "numerical experiments（数值模拟验证）", "conclusion（结论与开放问题）", "references"),
        "expository": ("abstract", "introduction", "background and motivation", "main exposition（以例子驱动的方法-证明链）", "exercises（练习，可选）", "references"),
        "survey": ("abstract", "introduction", "historical overview", "main developments（按主题组织的方法-结果链）", "open problems", "references"),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX）",
    reporting_standards={
        "proof": "每个定理必须给出完整证明，或明确引用出处",
        "assumptions": "统计模型假设（独立同分布、正态性、正则条件）须显式列出",
        "simulation": "数值实验给随机种子、样本量、重复次数与置信区间",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号",
        "随机变量用大写粗体（如 \\mathbf{X}、\\mathbf{Y}）；参数用希腊字母",
        "假设编号（H1、H2...）并在证明中引用",
        "proof 环境以 QED 方块（\\qedsymbol）结束",
        "数值结果以表格给出，含样本量、SE、CI、p 值",
    ),
    key_venues=(
        "The Annals of Statistics",
        "The Annals of Probability",
        "Journal of Statistical Planning and Inference",
        "Statistical Science",
        "Bernoulli",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb；对齐用 align/gather",
        "符号：E[·] 期望、Var[·] 方差、P(·) 概率密度",
        "随机种子在数值实验部分给出；p 值保留四位有效数字",
        "渐近记法：o(·)、O(·) 须说明极限变量与方向",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python (NumPy/SciPy)", "MATLAB", "Mathematica", "Stata", "SAS", "SPSS", "Julia", "Gambit", "Gretl", "GNU Octave", "SymPy", "Jupyter Notebook", "LaTeX", "Origin Pro", "Tableau", "GraphPad Prism", "MCMCpack (R)", "Tidyverse (R)", "BibTeX/Zotero"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI"),
)
