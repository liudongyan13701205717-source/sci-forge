"""地球科学学科论文支持：地质学、地球物理与地球化学综合研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="earth_sciences",
    aliases=(
        "earth_sciences", "地球科学",
        "geological sciences", "地质科学",
        "geosciences", "地球科学",
        "earth science", "地球科学",
        "planetary science", "行星科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（科学问题与背景）",
            "materials and methods（样品、分析方法、模型）",
            "results（实验数据与解释）",
            "discussion（地球科学意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
        "methodology": (
            "title",
            "introduction",
            "methods",
            "applications",
            "limitations",
            "conclusions",
        ),
    },
    citation_style="Geochemistry, Geophysics, Geosystems 格式",
    reporting_standards={
        "sampling": "采样位置、深度与时间须完整记录",
        "analysis": "分析方法须注明仪器与精度",
        "statistics": "统计检验须注明方法与显著性水平",
        "models": "数值模型须注明参数与边界条件",
    },
    conventions=(
        "地名使用标准地质名称",
        "年代用 Ma 或 ka 表示",
        "深度用 m 或 km 表示",
        "成分用 % 或 wt% 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Earth and Planetary Science Letters",
        "Geology",
        "Geophysical Research Letters",
        "Journal of Geophysical Research",
        "Geochimica et Cosmochimica Acta",
        "Precambrian Research",
    ),
    units_and_formulas_notes=(
        "年代用 Ma 或 ka 表示",
        "深度用 m 或 km 表示",
        "成分用 % 或 wt% 表示",
        "温度用 °C 或 K 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "GEOCARB3", "Isoplot", "IsoplotR", "Geochemist's Workbench", "SISCOM", "SISCOM/3D", "PETREL", "Move", "Petrel", "Sisworx", "GeoMesh", "Surfer", "ArcGIS", "QGIS", "Golden Software Surfer", "Python (GEOPLUM)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "GSA Data Repository"),
)
