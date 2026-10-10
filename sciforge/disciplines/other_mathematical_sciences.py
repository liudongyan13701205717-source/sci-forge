"""其他数学科学学科论文支持：数学分支交叉：计算数学、数学物理、金融数学与新兴方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_mathematical_sciences",
    aliases=("Other Mathematical Sciences", "其他数学科学", "Applied Mathematics", "Pure Mathematics", "Discrete Mathematics", "Mathematical Statistics", "Computational Mathematics", "Financial Mathematics"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="按期刊（AMS/Elsevier）",
    reporting_standards={
        "k1": "数值实验遵循ICM（International Code on Numerical Analysis）", "k2": "系统综述遵循PRISMA筛选流程", "k3": "复现性声明遵循JASA复现附录规范"
    },
    conventions=("定理—引理—定义环境须使用amsthm并统一编号", "符号首次出现须给出明确定义并附上下文", "公式与图表引用遵循「图X.1/表X.1」层级标注", "结论证明须完整给出或标注文献出处", "数值实验须提供代码与数据仓库可复现性声明"),
    key_venues=("Mathematical Reviews", "American Mathematical Monthly", "Advances in Applied Mathematics", "Mathematics of Computation", "Journal of Symbolic Computation", "SIAM Journal on Applied Mathematics"),
    units_and_formulas_notes=("使用SI单位且国际单位符号遵循ISO 80000", "公式编号遵循期刊层级编号（如定理X.Y）", "数值结果须注明有效位数、误差量级与复算精度", "随机量须给出分布假设、参数估计方法与置信区间"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "MATLAB", "Python", "Mathematica", "Maple", "R", "Julia", "SageMath", "Magma", "GiNaC", "CASPER", "SymPy", "Z3", "Lean 4", "Coq", "Isabelle/HOL", "Jupyter Notebook", "Overleaf", "MathSciNet", "Macaulay2"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "arXiv"),
)
