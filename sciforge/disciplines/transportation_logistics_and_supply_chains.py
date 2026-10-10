"""运输物流与供应链学科论文支持：供应链管理、运输优化、仓储运营研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="transportation_logistics_and_supply_chains",
    aliases=("transportation_logistics_and_supply_chains", "运输物流", "供应链管理",
             "运输优化", "logistics", "supply chain management", "物流"),
    paper_types={
        "research": (
            "abstract",
            "introduction（供应链背景与优化问题）",
            "literature review",
            "methods（建模与求解）",
            "results（优化结果与仿真）",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description",
            "analysis",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "optimization_model": "优化模型给出约束与目标函数",
        "simulation": "仿真实验报告种子数与置信区间",
        "supply_chain_kpi": "供应链绩效使用 SCOR 模型指标",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "距离单位 km",
        "货值单位 元/美元",
        "订单周期单位 小时",
        "利用率单位 %",
        "变量声明统一使用符号表",
    ),
    key_venues=(
        "European Journal of Operational Research",
        "Transportation Science",
        "Manufacturing & Service Operations Management",
        "Journal of Supply Chain Management",
        "物流技术",
    ),
    units_and_formulas_notes=(
        "距离以 km 报告",
        "货值以 元 报告",
        "订单周期以 小时 报告",
        "利用率以 % 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP EWM", "SAP S/4HANA", "Oracle WMS", "Blue Yonder", "AnyLogic", "FlexSim", "Arena", "MATLAB", "Python", "R", "GAMS", "CPLEX", "Gurobi", "OR-Tools", "TransCAD", "Logistix", "Vega", "Tableau", "Power BI", "Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
