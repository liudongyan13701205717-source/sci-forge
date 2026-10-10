"""物流管理学科论文支持：供应链管理、运输优化与仓储运营研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="logistic_management",
    aliases=(
        "logistic_management",
        "物流管理",
        "supply chain",
        "供应链管理",
        "logistics",
        "仓储",
        "transportation",
        "inventory",
        "operations management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（运营分析）",
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
    citation_style="APA 7",
    reporting_standards={
        "k1": "优化模型给出约束与目标函数",
        "k2": "仿真实验报告种子数与置信区间",
        "k3": "供应链绩效使用 SCOR 模型指标",
    },
    conventions=(
        "变量声明统一使用符号表",
        "仿真参数给出默认与敏感区间",
        "成本以人民币元报告并标注年份",
        "运输网络以节点和弧报告",
        "库存指标区分 SKU 与订单口径",
    ),
    key_venues=(
        "European Journal of Operational Research",
        "Transportation Science",
        "Manufacturing & Service Operations Management",
        "Journal of Supply Chain Management",
        "物流技术",
    ),
    units_and_formulas_notes=(
        "距离以公里报告",
        "货值以人民币元报告",
        "订单周期以小时或工作日报告",
        "利用率以百分比报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("AnyLogic", "FlexSim", "Arena", "Matlab", "Python", "R", "GAMS", "CPLEX", "Gurobi", "OR-Tools", "Vega", "TransCAD", "Logistix", "SAP EWM", "Oracle WMS", "Blue Yonder", "FlexLogix", "Tableau", "Power BI", "Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
