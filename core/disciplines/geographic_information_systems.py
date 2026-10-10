"""地理信息系统（GIS）学科论文支持：空间数据管理、空间分析与制图。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geographic_information_systems",
    aliases=(
        "geographic_information_systems",
        "地理信息系统",
        "GIS",
        "Geographic Information Systems",
        "spatial_analysis",
        "空间分析",
        "geographic_information_technology",
        "地理信息技术",
        "spatial_data_management",
        "空间数据管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（数据与方法）",
            "results（结果与制图）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（空间分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "spatial_data": "空间数据须报告坐标系（WGS84/CGCS2000）、投影、分辨率与来源",
        "analysis": "空间分析方法须报告所用算法、参数与验证方式",
        "map_design": "地图须含比例尺、指北针、图例、数据来源与坐标系说明",
    },
    conventions=(
        "坐标用经纬度（°N/°E）或投影坐标（m），全文统一",
        "地名用正式地名（中英文），括注省/市/县",
        "地图须含比例尺、指北针、图例、数据来源与坐标系",
        "空间统计须报告 Moran's I 或 LISA 等空间自相关检验",
        "符号与图层名使用英文 snake_case；图注用中文",
    ),
    key_venues=(
        "International Journal of Geographical Information Science",
        "Transactions in GIS",
        "GeoInformatica",
        "Computers, Environment and Urban Systems",
        "Annals of GIS",
    ),
    units_and_formulas_notes=(
        "坐标用 °N/°S/°E/°W；投影坐标用 m",
        "距离用 km；面积用 km²/ha/m²",
        "海拔用 m asl；坡度用 °或 %",
        "精度报告用均方根误差（RMSE）或位置精度 m",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "PostGIS", "GeoPandas", "GDAL/OGR", "GRASS GIS", "SNAP (Sentinel Application Platform)", "Google Earth Engine", "Whitebox GEP", "GeoServer", "FME (Feature Manipulation Engine)", "SAGA GIS", "Orfeo ToolBox", "R (sf/terra)", "GeoDa", "Python", "MATLAB", "Jupyter Notebook", "TerraScan", "TerraScope"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
