"""纯数学学科论文支持：数学理论、证明、符号计算与数学软件工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pure_mathematics",
    aliases=("pure_mathematics", "纯数学", "pure mathematics", "mathematics", "数学", "abstract mathematics", "mathematical sciences", "math", "theory of math"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AMS",
    reporting_standards={"theorem": "定理表述需给出完整条件与结论", "notation": "符号须在首次出现时定义", "proving": "证明步骤需给出严格推导"},
    conventions=("定理/引理/命题分节使用定理环境", "数学公式使用 LaTeX 排版", "符号定义遵循首用即定义原则", "图形与图表使用统一样式", "参考文献按 AMS 标准著录"),
    key_venues=("Annals of Mathematics", "Acta Mathematica", "Journal of the American Mathematical Society", "Inventiones Mathematicae", "Mathematische Annalen"),
    units_and_formulas_notes=("无量纲量与抽象结构为主，不采用 SI 单位", "公式使用 LaTeX mathmode 排版", "符号定义须在首次出现处声明", "定理编号采用章节层级编号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Mathematica", "Maple", "SageMath", "Maxima", "MATLAB Symbolic Math Toolbox", "GeoGebra", "Wolfram Alpha", "LaTeX", "MathJax", "TikZ", "Matplotlib", "gnuplot", "Coq", "Lean 4", "Isabelle/HOL", "Magma", "GAP", "PARI/GP", "SymPy", "Mathpix"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
