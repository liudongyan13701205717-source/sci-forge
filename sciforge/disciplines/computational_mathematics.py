"""计算数学论文支持：数值分析、科学计算、误差分析。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computational_mathematics",
    aliases=("numerical", "scientific computing", "数值分析", "偏微分方程", "pde",
             "有限元", "finite element", "迭代法", "preconditioner", "蒙特卡洛"),
    paper_types={
        "research": ("abstract", "introduction", "problem formulation", "numerical scheme", "error analysis", "numerical results", "conclusions", "references"),
        "algorithm": ("abstract", "introduction", "algorithm", "convergence analysis", "implementation", "experiments", "references"),
        "review": ("abstract", "introduction", "taxonomy", "comparisons", "open problems", "references"),
    },
    citation_style="SIAM（编号按出现顺序），如 [1]",
    reporting_standards={
        "convergence": "收敛阶须实测（网格加密）并与理论阶对比",
        "stability": "稳定性条件（CFL）与验证须给出",
        "solver": "迭代收敛容差、迭代次数、条件数须报告",
        "implementation": "代码可用性须声明（链接或附录）；硬件规格须写",
        "benchmark": "与传统方法在精度与效率上对比",
    },
    conventions=(
        "网格参数h、时间步 τ 均定义；范数（L², H¹）定义首现说明",
        "数值结果给最佳逼近误差；误差带对数坐标",
        "矩阵/算子大小写区块加粗；向量用小写粗体或箭头",
        "证明引理用完整证明；数值定理给（证明见附录）参考格式",
        "运行时间给 CPU 型号与并行化方式（OpenMP/MPI）",
    ),
    key_venues=(
        "SIAM Journal on Numerical Analysis",
        "SIAM Review",
        "Mathematics of Computation",
        "Journal of Computational Physics",
        "Numerische Mathematik",
    ),
    units_and_formulas_notes=(
        "函数空间记号须解释（H¹₀, H(div)）；范数/内积是否归一化须说明",
        "离散格式给 CFL 或约束条件（如 dt ≤ C·h²）",
        "自适应网格给标记准则与加密率",
    ),
)