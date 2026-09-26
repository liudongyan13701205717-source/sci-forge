"""地球生物学学科论文支持：地球生物学/生物地球化学体裁、APA 引用样式与地球生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geobiology",
    aliases=("geobiology", "地球生物学", "生物地球化学", "地质微生物学", "geobiology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与地球生物学问题）",
            "methods（采样与分析）",
            "results（地球化学与生物数据）",
            "discussion（生物-地质耦合）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "methods（野外采样与测年）",
            "results（剖面与同位素数据）",
            "discussion（环境重建）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Geobiology 遵循 Wiley 规范）",
    reporting_standards={
        "field": "野外研究遵循采样与测年报告规范",
        "geochemical": "地球化学分析遵循数据质量报告规范",
        "isotopic": "同位素分析遵循标准物质报告规范",
        "laboratory": "实验室研究遵循实验报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "采样位置与地层背景须报告",
        "测年方法与误差须注明",
        "同位素标准物质与归一化须明确",
        "地球化学数据质量（空白、重复）须报告",
        "地质时间尺度与分期须规范",
    ),
    key_venues=(
        "Geobiology",
        "Geochimica et Cosmochimica Acta",
        "Chemical Geology",
        "Palaeogeography, Palaeoclimatology, Palaeoecology",
        "Earth and Planetary Science Letters",
        "Frontiers in Earth Science",
    ),
    units_and_formulas_notes=(
        "同位素用 δ 记法（‰）；浓度用 ppm/ppb",
        "公式用 amsmath；分馏与年龄计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "测年结果给出 2σ 误差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "GIS 空间分析（ArcGIS/QGIS）",
        "质谱分析仪器",
        "显微成像系统",
        "Python 统计建模",
    ),
    category="交叉学科",
    databases=("PubMed", "OpenAlex", "Crossref", "GEO"),
)