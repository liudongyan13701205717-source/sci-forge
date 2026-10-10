"""经济理论学科论文支持：微观/宏观经济学与博弈论研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="economic_theory",
    aliases=(
        "economic_theory", "经济理论", "经济学理论",
        "microeconomic theory", "微观经济理论",
        "macroeconomic theory", "宏观经济理论",
        "game theory", "博弈论",
        "mechanism design", "机制设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与理论背景）",
            "model（模型设定）",
            "analysis（分析与定理证明）",
            "conclusion（结论与讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "main results（主要结果）",
            "future directions",
            "references",
        ),
        "working_paper": (
            "title",
            "abstract",
            "introduction",
            "model",
            "analysis",
            "conclusion",
            "appendix",
        ),
    },
    citation_style="AMS 样式",
    reporting_standards={
        "proof": "每个定理必须给出完整证明",
        "attribution": "定理归属必须准确",
        "assumptions": "假设须显式列出",
        "novelty": "须明确区分本工作与已有文献的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号",
        "经济变量记法全文一致",
        "证明以 QED 方块结束",
        "假设与未证明的断言必须显式标注",
    ),
    key_venues=(
        "Econometrica",
        "Journal of Political Economy",
        "American Economic Review",
        "Review of Economic Studies",
        "Journal of Economic Theory",
        "Games and Economic Behavior",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather",
        "新增算子用 \\DeclareMathOperator 声明",
        "显示公式仅在被引用时编号",
        "所有符号在首次出现处定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Stata", "EViews", "GAMS", "SCFM", "PSsolver", "Julia", "Python (Pyomo)", "Excel", "SPSS", "Origin", "Mathematica", "Maple", "SageMath", "Lean 4", "Mathlib", "Coq", "Axiom"),
    category="经济学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI"),
)
