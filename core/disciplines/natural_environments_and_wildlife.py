"""自然环境与野生动物学科论文支持：环境研究/物种监测体裁、野外调查规范与生态学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="natural_environments_and_wildlife",
    aliases=("natural_environments_and_wildlife", "自然环境", "野生动物",
             "生态环境", "生态监测", "环境生态", "野生动物监测"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与生态问题）",
            "methodology（调查/采样方法与样地）",
            "results（群落/种群/生境结果）",
            "discussion（生态机理与环境意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（研究区域与环境概况）",
            "analysis（物种与栖息地分析）",
            "results（监测结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（生态学理论综述）",
            "evidence synthesis（多生境证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Ecology 遵循 Elsevier 规范）",
    reporting_standards={
        "field_survey": "野外调查遵循生态调查规范",
        "species_distribution": "物种分布建模遵循 MaxEnt 规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "remote_sensing": "遥感遵循 ESA/USGS 处理规程",
        "biodiversity": "生物多样性评估遵循 IUCN 标准",
    },
    conventions=(
        "样地设置与调查方法须完整报告",
        "物种鉴定须注明鉴定人",
        "数据来源与时间须明确",
        "环境因子须完整",
        "样方/样线/样点须说明",
    ),
    key_venues=(
        "Ecology",
        "Journal of Ecology",
        "Ecological Monographs",
        "Biological Conservation",
        "Landscape Ecology",
    ),
    units_and_formulas_notes=(
        "面积用 km²；密度用 ind./km²",
        "公式用 amsmath；种群模型方程须编号",
        "百分比变化须定义基期",
        "样方面积/数量须报告",
        "多样性指数须定义（Shannon、Simpson 等）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "GPS 追踪设备", "红外相机", "无人机（UAV）", "声学监测设备", "MaxEnt", "Google Earth Engine", "Python（R/NumPy）", "R（生态分析）", "eDNA 测序设备", "Distance（距离取样软件）", "Excel", "LaTeX", "SPSS", "iNaturalist", "ENVI（遥感影像分析）", "Sentinel/Landsat 卫星数据", "PCR/基因测序设备", "样方调查工具"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "GBIF", "IUCN Red List"),
)
