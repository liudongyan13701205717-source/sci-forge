"""City planning 学科论文支持：城市规划/空间治理/城市设计体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="city_planning",
    aliases=(
        "City planning", "city planning", "urban planning",
        "urban design", "spatial planning",
        "城市规划", "城市设计", "城乡规划", "国土空间规划", "空间规划",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与规划假设）",
            "methodology（规划分析框架/GIS/统计/田野）",
            "findings（空间形态、指标、政策效应）",
            "discussion（治理、公平、可持续性）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site_description",
            "analysis",
            "planning_implications",
            "references",
        ),
        "simulation": (
            "abstract",
            "introduction",
            "model_setup",
            "results",
            "validation",
            "references",
        ),
    },
    citation_style="APA 7 样式（规划政策类亦常见 Harvard 或 Chicago）",
    reporting_standards={
        "gis_analysis": "报告坐标系（WGS84 / CGCS2000 / UTM）、比例尺与数据源",
        "survey": "问卷/入户调查遵循 IRB 审查；样本量、抽样方法、拒访率须报告",
        "simulation": "城市模拟模型报告参数、随机种子、验证方法（RMSE/MAE）",
        "policy_analysis": "政策评估遵循 DID/PSM/RD 等识别策略与平行趋势检验",
        "spatial_statistics": "空间统计报告 Moran's I、Moran's Eigenvalue 与 LISA 结果",
    },
    conventions=(
        "地名首次出现用「中文原名（English name, 简称）」格式；国家/地区使用 ISO 代码",
        "空间指标（FAR、密度、绿视率、通达性）报告单位与计算方法",
        "数据年份、行政边界与统计口径须注明（如 2020 年常住人口口径）",
        "地图标注比例尺、指北针、图例；投影说明须明确（UTM/Albers/等积投影）",
        "政策/规划文本引用给出文号（如「中共中央国务院《关于...的意见》〔202X〕XX 号」）",
    ),
    key_venues=(
        "Journal of the American Planning Association",
        "Planning Perspectives",
        "Cities",
        "Urban Studies",
        "Landscape and Urban Planning",
        "Habitat International",
        "Regional Science and Urban Economics",
        "城市规划",
    ),
    units_and_formulas_notes=(
        "土地面积 km² / ha / m²；人口单位「人」或「万人」；密度 人/km²",
        "容积率 FAR 无量纲；建筑密度 %；绿地率 %",
        "距离 km；速度 km/h；通达性 min；出行时间 min",
        "货币单位 CNY 或 USD；价格给出年份与是否名义/实际",
        "统计报告均值/中位数、95% CI、p 值；空间自相关用 Moran's I",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "MapInfo", "AutoCAD Civil 3D", "SketchUp Pro", "Rhino + Grasshopper", "Ladybug Tools", "MassingToolkit", "Houdini", "Unreal Engine 5（数字孪生）", "CityEngine", "Google Earth Pro", "Google Earth Engine", "UrbSim", "MeCuP", "QuadriSim", "Cellular Automata Toolkit", "MATSim", "TransCAD", "PTV Visum", "TransModeler", "Orfeo ToolBox", "GRASS GIS", "SAGA GIS", "ENVI", "QWAT", "SWMM", "HEC-RAS", "iDRISI", "Clementines", "R 空间分析", "PostgreSQL + PostGIS", "Cesium", "Unity", "Tableau", "QGIS Processing", "OpenStreetMap", "OpenDataSoft"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Scopus", "Web of Science"),
)
