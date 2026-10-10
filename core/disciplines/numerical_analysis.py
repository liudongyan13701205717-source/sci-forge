"""数值分析学科论文支持：数值方法/误差分析体裁、AMS 引用样式与数值记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="numerical_analysis",
    aliases=(
        "numerical_analysis",
        "数值分析",
        "Numerical Analysis",
        "Numerical Methods",
        "Scientific Computing",
        "Computational Mathematics",
        "Algorithmic Analysis",
        "Numerical Linear Algebra",
        "误差分析",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与贡献）", "problem setting（问题定义与离散化）", "numerical method（算法设计）", "error analysis（收敛性与稳定性）", "numerical experiments（数值实验）", "references"),
        "expository": ("abstract", "introduction", "background（背景）", "algorithm exposition（算法讲解）", "analysis（分析）", "exercises（练习）", "references"),
        "survey": ("abstract", "introduction", "historical overview（历史综述）", "main developments（主要进展）", "open problems（开放问题）", "references"),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX）",
    reporting_standards={
        "algorithm": "算法给出完整描述、复杂度与可复现实现",
        "error_analysis": "收敛阶、误差界与稳定性分析须给出严格证明",
        "computational_evidence": "数值实验说明硬件、软件、精度与统计显著性",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号",
        "离散化记法统一：网格步长 h、时间步长 \\Delta t",
        "误差记法 \\lVert e_h \\rVert 注明范数类型",
        "证明以 QED 方块结束",
        "数值实验报告收敛阶与 CPU 时间",
    ),
    key_venues=(
        "SIAM Journal on Numerical Analysis",
        "SIAM Journal on Scientific Computing",
        "Numerische Mathematik",
        "Mathematics of Computation",
        "Journal of Computational Physics",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb",
        "浮点运算用 \\operatorname{fl}(\\cdot)",
        "渐近式与估计式链用 \\ll 或显式常数",
        "括号尺寸用 \\bigl \\bigr 系列",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Julia", "Python", "C++", "Fortran", "Mathematica", "R", "GNU Octave", "SageMath", "PETSc", "Trilinos", "ARPACK", "SLEPc", "MUMPS", "SuperLU", "Gmsh", "VTK", "ParaView", "SciPy", "NumPy"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
