"""人文地理学科论文支持：空间格局/人口流动/人地关系研究体裁、APA/AGI 引用样式与空间统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_geography",
    aliases=(
        "human_geography",
        "人文地理",
        "人口地理",
        "Human Geography",
        "Population Geography",
        "Urban Geography",
        "空间分析",
        "经济地理",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AGI/APA 样式（作者-年份；人文地理学亦常用地理学传统引用）",
    reporting_standards={"k1": "空间统计须报告 Moran's I 等自相关指标", "k2": "栅格研究须说明投影与分辨率", "k3": "人口研究须注明普查年份"},
    conventions=(
        "坐标与投影系统须注明",
        "栅格分辨率给出单位",
        "空间统计结果报告显著性",
        "数据来源与年份须注明",
        "地图图例须完整",
    ),
    key_venues=(
        "Annals of the Association of American Geographers",
        "Transactions of the Institute of British Geographers",
        "Progress in Human Geography",
        "Population, Space and Place",
        "Journal of Regional Science",
    ),
    units_and_formulas_notes=(
        "距离/面积单位统一（km/km²）",
        "人口密度以人/平方公里计",
        "栅格分辨率以米/像元计",
        "统计量给出均值/相关系数/显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "ENVI", "MapInfo", "MapWinGIS", "GRASS GIS", "Gambit", "Stata", "SPSS", "R", "Python", "MATLAB", "Excel", "Tableau", "PostgreSQL/PostGIS", "GeoPandas", "NetLogo", "Endnote", "Google Earth Engine", "Snap"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
