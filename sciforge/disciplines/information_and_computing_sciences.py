"""信息与计算科学学科论文支持：信息科学、计算理论、数值计算与数据驱动方法交叉研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_and_computing_sciences",
    aliases=(
        "information_and_computing_sciences",
        "信息与计算科学",
        "信息计算科学",
        "计算科学",
        "信息科学",
        "information and computing science",
        "computational science",
        "信息计算",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（工程/计算）或 APA 7 样式（跨学科）",
    reporting_standards={
        "algorithms": "算法须报告时间/空间复杂度与实测基准",
        "simulation": "仿真须注明工具版本、参数与随机种子",
        "numerical_analysis": "数值方法须报告误差阶与收敛性",
        "experimental": "实验须注明硬件平台与可复现性配置",
    },
    conventions=(
        "算法须给出伪代码并标注复杂度",
        "数值误差须注明精度等级（双精度/单精度）",
        "基准对比须注明计算时间（CPU/GPU）与版本",
        "定理证明须用 LaTeX 环境（amsmath）",
        "统计量须给 95% CI，仿真须给样本数",
    ),
    key_venues=(
        "Journal of Computing Science",
        "Theoretical Computer Science",
        "SIAM Journal on Computing and Science",
        "Journal of Computational Physics",
        "计算机学报",
    ),
    units_and_formulas_notes=(
        "复杂度用大 O 表示法，须注明 worst/best/average",
        "数值误差用相对/绝对误差，须注明精度",
        "GPU 基准须注明型号与 CUDA 版本",
        "统计量须给 M/SD/95% CI",
        "公式用 amsmath，行内避免复杂分式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python（numpy/scipy/pandas）", "MATLAB", "Julia（科学计算）", "GNU R", "C/C++（OpenMP）", "Fortran（数值计算）", "CUDA（GPU 并行）", "MPI（分布式计算）", "SciPy", "NumPy", "scikit-learn", "TensorFlow", "PyTorch", "SymPy（符号计算）", "Maple（符号推导）", "Mathematica", "COMSOL Multiphysics", "ANSYS", "Jupyter Notebook", "LaTeX（amsmath）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
