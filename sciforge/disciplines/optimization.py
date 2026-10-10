"""优化学科论文支持：数学规划、算法设计与最优化理论。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optimization",
    aliases=("optimization", "优化", "最优化", "Operations Research", "数学规划", "Mathematical Programming", "Optimization Theory", "凸优化", "Combinatorial Optimization"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE",
    reporting_standards={"OPTIMALITY": "最优化条件（KKT）与理论证明", "CONVERGENCE": "收敛性分析与速率证明", "REPRODUCIBILITY": "随机种子、机器与运行时长可复现"},
    conventions=("符号严格区分变量 x、参数 b、函数 f", "算法伪代码与复杂度分析同现", "数值实验报告硬件/求解器/许可信息", "对偶变量 y 与影子价格定义明确", "最优性、KKT 与强对偶性须论证"),
    key_venues=("Mathematical Programming", "Operations Research", "IEEE Transactions on Automatic Control", "SIAM Journal on Optimization", "Journal of Optimization Theory and Applications"),
    units_and_formulas_notes=("变量与参数按 SI 单位统一", "拉格朗日函数 L(x, λ) = f(x) - Σλᵢ gᵢ(x)", "KKT 条件 ∇f + Σλᵢ∇gᵢ = 0 且 λᵢgᵢ = 0", "计算复杂度用大 O 记号标注"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Gurobi", "IBM CPLEX", "GLPK", "Google OR-Tools", "Pyomo", "JuMP (Julia)", "CasADi", "SciPy.optimize", "MATLAB Optimization Toolbox", "fmincon", "NLopt", "GAMS", "Knitro", "Bonmin", "IPOPT", "CVXPY", "R OptimTools", "OpenOpt", "LaTeX", "Microsoft Excel Solver"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "INFORMS"),
)
