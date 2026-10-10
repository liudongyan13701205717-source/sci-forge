"""Climate Engineering 学科论文支持：气候工程/地球工程/碳移除。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="climate_engineering",
    aliases=(
        "Climate Engineering", "气候工程", "Geoengineering", "地球工程",
        "Climate Intervention", "气候干预", "Solar Radiation Management",
        "太阳辐射管理", "CDR", "Carbon Dioxide Removal",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier Journal Style",
    reporting_standards={
        "ipcc_ar6": "气候干预评估须遵循 IPCC AR6 术语框架",
        "cdr_measurement": "CDR 须报告吨 CO₂/年、置信区间与方法学",
        "srm_assessment": "SRM 干预须说明尺度、剂量与模式敏感性",
    },
    conventions=(
        "使用 SRM/CDR 术语区分太阳辐射管理与碳移除",
        "报告 CDR 时给出吨 CO2/年 与置信区间",
        "引用气候模式时说明 SRM 干预尺度",
        "评估气候干预风险应遵循 IPCC AR6 术语",
        "使用 SI 单位与 IPCC 情景术语",
    ),
    key_venues=(
        "Nature Climate Change",
        "Nature Sustainability",
        "Environmental Research Letters",
        "Atmospheric Chemistry and Physics",
        "Journal of Geophysical Research",
        "Climate of the Past",
        "Nature Geoscience",
        "Environmental Science & Technology",
    ),
    units_and_formulas_notes=(
        "温度使用 SI 单位 K 或 °C；气压用 hPa；辐射用 W/m²",
        "CDR 量值以吨 CO₂/年报告，须附置信区间与方法学说明",
        "SRM 辐射强迫变化以 W/m² 计，须给出全球与区域分量",
        "公式变量须标注物理量纲；能量与热量以 J 或 GJ 计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("WRF", "CESM", "UKCP", "CMIP6", "Python", "RStudio", "MATLAB", "QGIS", "ANSYS Fluent", "COMSOL Multiphysics", "SolidWorks", "AutoCAD", "R", "Octave", "Matplotlib", "Google Earth Engine", "NetCDF", "xarray", "ParaView", "OpenFOAM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Copernicus"),
)
