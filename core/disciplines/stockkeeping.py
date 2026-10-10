"""库存管理学科论文支持：库存优化、供应链与仓储管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stockkeeping",
    aliases=("stockkeeping", "库存管理", "仓储管理", "库存控制",
             "inventory management", "stock control", "warehouse management",
             "物料管理", "仓储运营", "供应链库存"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与优化目标）",
            "methods（模型与优化方法）",
            "results（库存绩效与成本结果）",
            "discussion（管理含义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（仓储或供应链实例）",
            "analysis（库存策略与效能分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（库存理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "model_assumptions": "模型假设须明确列出并说明可放宽条件",
        "parameter": "需求率、补货提前期、持有成本等参数须给出取值依据",
        "simulation": "模拟须报告运行次数、随机种子与收敛性检验",
        "comparison": "不同策略比较须使用相同基准与评价指标",
    },
    conventions=(
        "库存策略名称须使用标准术语（EOQ、(s, S)、(R, Q) 等）",
        "需求率以件/时间单位报告",
        "成本以货币单位报告并标注持有成本、订货成本、缺货成本",
        "服务水平以周期服务水平（CSL）或单周期服务水平（Type I）报告",
        "图表须标注置信区间",
    ),
    key_venues=(
        "European Journal of Operational Research",
        "Manufacturing & Service Operations Management",
        "Journal of Operations Management",
        "International Journal of Production Economics",
        "Journal of Supply Chain Management",
    ),
    units_and_formulas_notes=(
        "需求率：件/时间单位（如件/周）",
        "持有成本：货币/件/年",
        "服务水平：CSL（%）或 Type I（%）",
        "总成本：货币单位，附持有成本与缺货成本分项",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SAP ERP", "Oracle WMS", "JDA / Blue Yonder WMS", "Manhattan Associates WMS", "Microsoft Dynamics 365 Supply Chain", "SAS Enterprise Miner", "JMP", "SPSS", "STATA", "MATLAB", "Simulink", "AnyLogic", "FlexSim", "ARENA Simulation", "Microsoft Excel (Solver)", "Python (pandas, scipy)", "R", "Jupyter Notebook", "Tableau", "Power BI"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
