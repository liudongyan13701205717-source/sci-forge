"""管理科学学科论文支持：运筹学、决策模型与优化仿真研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management_science",
    aliases=(
        "management_science",
        "管理科学",
        "运筹学",
        "决策科学",
        "Management Science",
        "Operations Research",
        "Decision Sciences",
        "决策模型",
        "优化",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
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
    citation_style="APA 7 样式（运筹学与管理科学通用）",
    reporting_standards={
        "optimization": "优化模型遵循运筹学报告规范",
        "simulation": "仿真研究遵循 M&S 报告规范",
        "survey": "决策模型遵循 DM 报告规范",
    },
    conventions=(
        "优化模型须明确决策变量、目标函数与约束",
        "算法须报告实例规模与运行时间",
        "对比方法须包含基线（精确法或启发式）",
        "随机种子与运行次数须报告",
        "收敛性/最优性须以 gap 或 bound 报告",
    ),
    key_venues=(
        "Management Science",
        "Operations Research",
        "INFORMS Journal on Computing",
        "Naval Research Logistics",
        "Mathematical Programming",
        "Journal of Operations Management",
    ),
    units_and_formulas_notes=(
        "目标函数值须以标准货币或时间单位报告",
        "计算时间以秒报告并附硬件配置",
        "gap% 报告最优性差距",
        "样本规模与参数数量须报告",
        "单位须遵循 SI 并明确量纲",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python（pandas 与 numpy）", "Python（scipy 与 scipy.optimize）", "Python（scikit-learn）", "Python（PyTorch）", "R", "Julia", "Octave", "GAMS", "AMPL", "LINGO", "CPLEX", "Gurobi", "FICO Xpress", "BARON", "SCIP", "MOSEK", "AnyLogic", "Arena", "SimPy"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
