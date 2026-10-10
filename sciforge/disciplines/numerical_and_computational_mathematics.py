"""计算数学学科论文支持：数值模拟/高性能计算体裁、AMS 引用样式与 HPC 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="numerical_and_computational_mathematics",
    aliases=(
        "numerical_and_computational_mathematics",
        "计算数学",
        "Numerical and Computational Mathematics",
        "Computational Mathematics",
        "Scientific Computing",
        "High Performance Computing",
        "Numerical Simulation",
        "Mathematical Modelling",
        "数值模拟",
    ),
    paper_types={
        "research": ("abstract", "introduction（模型与贡献）", "mathematical model（数学模型）", "numerical method（数值方法）", "numerical experiments（数值实验）", "conclusions（结论）", "references"),
        "case_study": ("abstract", "introduction", "case description（应用背景）", "modelling（建模）", "simulation（模拟）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（方法综合）", "future directions", "references"),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX）",
    reporting_standards={
        "algorithm": "算法给出伪代码、复杂度与可复现实现",
        "simulation": "模拟参数、网格与统计显著性说明",
        "benchmarks": "基准对比说明硬件平台与版本",
    },
    conventions=(
        "模型假设显式列出并注明可验证性",
        "离散化记法统一（h、\\Delta t、范数 \\lVert \\cdot \\rVert）",
        "复杂度以渐近形式给出（O、Θ、\\mathcal{O}）",
        "代码可用性说明（GitHub/DOI）",
        "数值实验报告收敛阶、精度与并行效率",
    ),
    key_venues=(
        "SIAM Journal on Scientific Computing",
        "Journal of Computational Physics",
        "Journal of Computational Mathematics",
        "Computers & Fluids",
        "Journal of Parallel and Distributed Computing",
    ),
    units_and_formulas_notes=(
        "SI 单位统一并注明量纲",
        "复杂度用大 O 记号",
        "并行效率 E = T_1/(p \\cdot T_p) 给出",
        "统计显著性给 p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Julia", "Python", "C++", "Fortran", "R", "Mathematica", "Maple", "NumPy", "SciPy", "TensorFlow", "PyTorch", "PyCUDA", "Numba", "Cython", "CUDA", "Intel MKL", "OpenMPI", "PETSc", "Julia GPU"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
