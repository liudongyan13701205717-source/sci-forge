"""国家公园与野生动物管理学科论文支持：保护区管理/物种保护体裁、生态调查规范与野外记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="national_parks_and_wildlife_management",
    aliases=("national_parks_and_wildlife_management", "国家公园管理",
             "野生动物管理", "保护区管理", "保护区规划",
             "野生动物保护", "公园管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与保护问题）",
            "methodology（调查/建模方法与样地）",
            "results（物种/种群结果）",
            "discussion（机理与管理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（保护区概况与物种）",
            "analysis（威胁评估与管理方案）",
            "results（管理成效）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（保护生物学综述）",
            "evidence synthesis（多公园证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Conservation Biology 遵循 Elsevier 规范）",
    reporting_standards={
        "field_survey": "野外调查遵循生态调查规范",
        "species_distribution": "物种分布建模遵循 MaxEnt 规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "conservation": "保护措施遵循 IUCN 红色名录标准",
        "remote_sensing": "遥感遵循 ESA/USGS 处理规程",
    },
    conventions=(
        "调查方法与样地须完整报告",
        "物种鉴定与 voucher 须注明",
        "数据来源与时间须明确",
        "保护地管理级别须引用",
        "模型参数与不确定度须报告",
    ),
    key_venues=(
        "Ecological Applications",
        "Conservation Biology",
        "Journal of Applied Ecology",
        "Biological Conservation",
        "Oryx",
    ),
    units_and_formulas_notes=(
        "面积用 km²；密度用 ind./km²",
        "公式用 amsmath；种群模型方程须编号",
        "百分比变化须定义基期",
        "样方面积/数量须报告",
        "物种数用 S；Jaccard 相似指数须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "GPS 追踪设备", "红外相机", "无人机（UAV）", "声学监测设备", "MaxEnt", "Google Earth Engine", "Python（R/NumPy）", "R（生态分析）", "eDNA 测序设备", "Vortex（种群模型）", "Distance（距离取样软件）", "Excel", "LaTeX", "SPSS", "iNaturalist", "ENVI（遥感影像分析）", "Sentinel/Landsat 卫星数据", "PCR/基因测序设备"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "GBIF", "IUCN Red List"),
)
