"""地理学学科论文支持：自然地理、人文地理、区域地理、应用地理与地球系统。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geography",
    aliases=(
        "geography",
        "地理学",
        "human_geography",
        "人文地理",
        "physical_geography",
        "自然地理",
        "regional_geography",
        "区域地理",
        "applied_geography",
        "地理科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（数据、方法与区域）",
            "results（发现）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域/案例背景）",
            "analysis（分析）",
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
        "spatial_analysis": "空间分析须报告坐标系、投影、空间分辨率与精度",
        "survey": "调查须报告抽样框、样本量、问卷设计与响应率",
        "remote_sensing": "遥感须报告传感器、波段、预处理与分类精度",
    },
    conventions=(
        "地名用正式地名（中英文），括注省/市/县",
        "坐标用经纬度（°N/°E）或投影坐标（m）",
        "地图须含比例尺、指北针、图例、数据来源与坐标系",
        "距离用 km；面积用 km² 或 ha；人口密度用 人/km²",
        "空间统计须报告 Moran's I / LISA 等空间自相关检验",
    ),
    key_venues=(
        "Annals of the American Association of Geographers",
        "Journal of Geography",
        "Progress in Human Geography",
        "Geographical Analysis",
        "International Journal of Geographical Information Science",
    ),
    units_and_formulas_notes=(
        "坐标用 °N/°S/°E/°W；投影坐标用 m",
        "距离用 km；面积用 km²/ha/m²",
        "海拔用 m asl；温度用 °C；降水量用 mm",
        "空间分辨率用 m/pixel；时间分辨率用 s/d/yr",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "ENVI", "ERDAS IMAGINE", "Python", "R", "STATA", "SPSS", "MATLAB", "GRASS GIS", "Google Earth Pro", "SAGA GIS", "GeoDa", "PostGIS", "SNAP", "GeoPandas", "GDAL", "Matplotlib", "Surfer", "Idrisi"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
