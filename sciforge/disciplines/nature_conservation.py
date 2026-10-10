"""自然保护学科论文支持：自然保护研究体裁、生态保护规范与保护区记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nature_conservation",
    aliases=("nature_conservation", "自然保护", "生态保护",
             "生物多样性保护", "环境管理", "自然保护生物学",
             "保护生物学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与保护问题）",
            "methodology（调查/建模方法与样地）",
            "results（物种/种群/生境结果）",
            "discussion（机理与管理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（保护区/物种概况）",
            "analysis（威胁评估与保护方案）",
            "results（管理成效）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（保护理论综述）",
            "evidence synthesis（多区域证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Conservation Biology 遵循 Elsevier 规范）",
    reporting_standards={
        "field_survey": "野外调查遵循生态调查规范",
        "species_distribution": "物种分布建模遵循 MaxEnt 规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "conservation": "保护措施遵循 IUCN 标准",
        "policy": "政策研究遵循政策分析规范",
    },
    conventions=(
        "物种鉴定与 voucher 须注明",
        "数据来源与时间须明确",
        "保护区级别须引用",
        "保护措施与成效须报告",
        "不确定性与模型参数须说明",
    ),
    key_venues=(
        "Conservation Biology",
        "Biological Conservation",
        "Oryx",
        "Ecology Letters",
        "Journal of Applied Ecology",
    ),
    units_and_formulas_notes=(
        "面积用 km²；密度用 ind./km²",
        "公式用 amsmath；种群模型方程须编号",
        "百分比变化须定义基期",
        "样方面积/数量须报告",
        "多样性指数须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "GPS 追踪设备", "红外相机", "无人机（UAV）", "声学监测设备", "MaxEnt", "Google Earth Engine", "Python（R/NumPy）", "R（生态分析）", "eDNA 测序设备", "Vortex（种群模型）", "Distance（距离取样软件）", "Excel", "LaTeX", "SPSS", "iNaturalist", "ENVI（遥感影像分析）", "Sentinel/Landsat 卫星数据", "PCR/基因测序设备"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "GBIF", "IUCN Red List"),
)
