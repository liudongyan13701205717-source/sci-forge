"""邮政服务学科论文支持：邮政物流网络、资费定价、服务交付与行业政策研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="postal_services",
    aliases=(
        "postal services", "邮政服务", "邮政业",
        "postal logistics", "邮政物流",
        "mail delivery", "邮件投递",
        "parcel delivery", "包裹递送",
        "universal postal service", "普遍邮政服务",
        "postal operations",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（行业问题与政策背景）",
            "methodology（模型、数据与优化方法）",
            "results（性能指标与对比）",
            "discussion（运营与管理启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域或业务案例）",
            "analysis（流程、成本与服务质量）",
            "results（改善效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（邮政经济学与管理理论）",
            "evidence synthesis（国际比较证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "邮政普遍服务义务须量化描述（覆盖、时限、资费上限）",
        "k2": "运营绩效须区分包裹与信函业务口径（ITU/UN Post 口径）",
        "k3": "政策评估须给出可比国家样本与数据年份",
    },
    conventions=(
        "投递时限须注明工作日口径与统计截止点",
        "资费分析须区分普遍服务资费与市场化业务资费",
        "网络模型须说明节点数量、容量约束与数据时效",
        "跨境与海关环节须单列报关与合规成本",
        "成本分摊方法须说明分摊基准与是否含普遍服务补贴",
    ),
    key_venues=(
        "International Journal of Productivity and Performance Management",
        "Transportation Research Part E: Logistics and Transportation Review",
        "Journal of Transport Geography",
        "International Journal of Operations & Production Management",
        "Global Transport and Logistics (Emerald)",
    ),
    units_and_formulas_notes=(
        "单位成本以元/件或元/千克表示，注明重量段与计费重规则",
        "准在投率与准时率给百分比并注明统计窗口",
        "路径优化注明时间窗、车辆容量与求解算法及计算时间",
        "网络密度指标用网点数/万人口或投递员人均件量",
        "碳排强度用 gCO₂e/件并说明运输方式构成",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Oracle (TMS)", "SAP TM", "Manhattan Associates", "Google OR-Tools", "Gurobi", "Cplex", "ArcGIS", "MapInfo", "PostGIS", "QGIS", "AnyLogic", "FlexSim", "Arena", "Matlab (Optimization Toolbox)", "Python (pandas, networkx)", "R (RStudio)", "Power BI", "Tableau", "Excel", "SQL Server"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
