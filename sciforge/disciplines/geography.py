"""地理学论文支持：自然地理、人文地理、GIS与遥感、城市地理、区域分析。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geography",
    aliases=("geography", "geosciences", "地理学", "地理科学"),
    paper_types={
        "research": ("abstract", "introduction", "study area", "data and methods", "results", "discussion", "conclusions", "references"),
        "gis": ("abstract", "introduction", "spatial data", "analysis methods", "results", "cartographic representation", "discussion", "conclusions", "references"),
        "human": ("abstract", "introduction", "theoretical framework", "case study", "analysis", "findings", "discussion", "conclusions", "references"),
    },
    citation_style="APA 7（括号），如 (Author, Year)",
    reporting_standards={
        "spatial_analysis": "空间分析须报告坐标系（WGS84/CGCS2000）、投影方式、空间分辨率",
        "remote_sensing": "遥感须报告传感器、波段组合、预处理（大气/几何校正）与分类精度",
        "survey": "调查须报告抽样框、样本量、问卷设计与响应率",
        "fieldwork": "田野调查须报告调查时间、路线、观测点与测量方法",
    },
    conventions=(
        "地名用正式地名（中英文），括注省/市/县",
        "坐标用经纬度（°N/°E）或投影坐标（m）",
        "地图须含比例尺、指北针、图例、数据来源与坐标系",
        "距离用 km；面积用 km² 或 ha",
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
        "海拔用 m asl（above sea level）",
        "人口密度用 人/km²",
        "坡度用 °或 %",
    ),
)
