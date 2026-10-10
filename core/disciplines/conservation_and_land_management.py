"""保育与土地管理学科论文支持：土地管理/土地利用规划/农业保护体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="conservation_and_land_management",
    aliases=(
        "conservation and land management", "保育与土地管理", "土地管理",
        "land management", "土地利用规划", "land use planning",
        "水土保持", "soil and water conservation", "土地利用",
        "land use", "土地复垦", "land reclamation",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "study area（研究区域）",
            "materials and methods（数据、模型与分析）",
            "results（土地利用变化/土壤侵蚀/植被覆盖）",
            "discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case area",
            "methods",
            "results",
            "management recommendations",
            "references",
        ),
        "assessment": (
            "abstract",
            "introduction",
            "assessment framework",
            "data and methods",
            "results（评价等级与分区）",
            "recommendations",
            "references",
        ),
    },
    citation_style="APA 7 或 Elsevier 样式（土地管理/环境科学）",
    reporting_standards={
        "land_use": "土地利用分类须遵循国家或国际标准（如 FAO/GB/T）",
        "remote_sensing": "遥感影像须报告传感器、波段、分辨率与预处理",
        "soil_erosion": "土壤侵蚀量须给出模型（USLE/RUSLE/WEPP）与参数",
        "statistics": "空间统计须报告空间自相关与不确定性",
    },
    conventions=(
        "土地覆盖分类须给出分类体系与面积口径（投影坐标系）",
        "空间分辨率用 m/pixel；时间分辨率用年/月",
        "土壤类型与侵蚀等级须遵循国家或国际标准",
        "面积用 km² 或 ha；坡度用 % 或 °",
        "图件须标注投影坐标系（EPSG 编号）与数据源",
    ),
    key_venues=(
        "Land Use Policy",
        "Land Use Science",
        "Journal of Land & Land Use Study",
        "Environmental Management",
        "Agriculture, Ecosystems & Environment",
        "Science of the Total Environment",
        "Ecological Indicators",
    ),
    units_and_formulas_notes=(
        "面积用 km²/ha；坡度用 % 或 °",
        "土壤侵蚀量用 t/km²/yr（USLE 单位）",
        "遥感波段用 nm（如 NDVI 用 865/665 nm）",
        "公式用 amsmath；统计量给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "Google Earth Engine", "GRASS GIS", "SAGA GIS", "ENVI", "ERDAS Imagine", "GDAL", "PostGIS", "R (terra/sf/raster)", "Python (GeoPandas/Fiona/Rasterio)", "Sentinel-2", "Landsat", "MODIS", "USLE/RUSLE", "WEPP (Water Erosion Prediction Project)", "HYPE", "SWAT", "InVEST", "R (landcover)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "PubMed", "Zenodo"),
)
