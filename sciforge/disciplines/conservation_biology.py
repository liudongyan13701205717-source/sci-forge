"""保护生物学学科论文支持：物种保护/保护规划体裁、Wiley 引用样式与保护生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="conservation_biology",
    aliases=("conservation biology", "保护生物学", "物种保护", "species conservation",
             "保护规划", "conservation planning", "生物多样性保护", "biodiversity conservation",
             "恢复生态学", "restoration ecology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与保护问题）",
            "materials and methods（数据与分析方法）",
            "results（种群/栖息地数据）",
            "discussion（保护建议）",
            "references",
        ),
        "assessment": (
            "abstract",
            "introduction",
            "methods（IUCN 评估/种群生存力分析）",
            "results（威胁等级与风险）",
            "discussion（管理对策）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题/类群综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Conserv. Biol. 遵循 Wiley 规范）",
    reporting_standards={
        "threat_assessment": "威胁因子识别与评估方法须报告",
        "population_data": "种群数据来源、时间跨度与调查方法须完整",
        "model_parameters": "种群模型（PVA）参数与不确定性须报告",
        "management_actions": "保护行动与监测方案须明确",
        "stakeholder_context": "社会经济背景与利益相关方须说明",
    },
    conventions=(
        "IUCN 红色名录等级（CR、EN、VU、NT、LC）规范引用",
        "保护术语（metapopulation、corridor、ex situ）定义须给出",
        "种群参数（N_e、λ、r）符号统一",
        "栖息地类型与土地利用分类规范",
        "保护成效指标（PA 覆盖率、种群趋势）明确",
    ),
    key_venues=(
        "Conservation Biology",
        "Biological Conservation",
        "Conservation Letters",
        "Global Ecology and Conservation",
        "Journal of Applied Ecology",
        "Frontiers in Ecology and the Environment",
    ),
    units_and_formulas_notes=(
        "面积用 km^2/ha；密度用 只/km^2",
        "种群增长率 λ 无量纲；r 用 年^-1",
        "公式用 amsmath；种群增长与灭绝风险公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出置信区间与不确定性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "GIS (QGIS/ArcGIS)",
        "R (terra/sf)",
        "遥感影像（Landsat/Sentinel）",
        "种群生存力分析软件",
        "MaxEnt 生态位建模软件",
    ),
    category="理学",
    databases=(
        "OpenAlex",
        "PubMed",
        "Zenodo",
        "Crossref",
        "DOAJ",
    ),
)