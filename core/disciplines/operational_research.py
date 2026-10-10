"""运筹学学科论文支持：数学规划/排队论体裁、INFORMS 引用样式与 OR 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="operational_research",
    aliases=("operational_research", "运筹学", "OR", "Operations Research", "管理科学", "数学规划", "排队论", "Mathematical Programming"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="INFORMS 样式",
    reporting_standards={"k1": "数学模型完整定义规范", "k2": "算法可复现性要求", "k3": "计算实验报告标准"},
    conventions=("模型用标准形式书写", "复杂度分析用O记号", "算法给出伪代码", "计算实验报告实例规模与gap"),
    key_venues=("Operations Research", "Management Science", "Mathematical Programming", "INFORMS Journal on Computing", "European Journal of Operational Research"),
    units_and_formulas_notes=("目标函数与约束显式声明", "变量域（非负/整数/二元）标注", "复杂度注明最坏/平均情形", "公式用amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python", "MATLAB", "Gurobi", "CPLEX", "OR-Tools", "SCIP", "LPSolve", "AMPL", "GNU Linear Programming (GLPK)", "MOSEK", "Xpress", "KNITRO", "Julia (JuMP)", "Python (SciPy)", "R (lpSolve)", "Excel Solver", "SAP IB (IBM ILOG CPLEX)", "Java (JGraphT)", "Origin", "LaTeX"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
