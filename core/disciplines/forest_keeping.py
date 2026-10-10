"""森林管护学科论文支持：森林资源保护、森林防火、森林病虫害防治与森林经营。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forest_keeping",
    aliases=("forest_keeping", "forest management", "森林管护", "森林防火", "森林保护", "森林经营", "森林资源管理", "林业管理"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "fire": "森林防火须遵循标准化风险评估方法",
        "invasion": "生物入侵须遵循检疫与监测规范",
        "harvest": "采伐须遵循可持续经营标准",
        "rehabilitation": "生态修复须遵循标准化评估方法"
    },
    conventions=(
        "树种用拉丁学名（首次出现时附中文名）",
        "林分参数用标准术语（郁闭度、蓄积量、断面积）",
        "面积用公顷（ha）或亩",
        "蓄积量用 m³/ha",
        "生物量用 Mg/ha"
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Journal of Forestry Research",
        "Canadian Journal of Forest Research",
        "Forest Science",
        "Journal of Forestry"
    ),
    units_and_formulas_notes=(
        "面积用 ha（公顷）",
        "蓄积量用 m³/ha",
        "生物量用 Mg/ha",
        "林龄用年",
        "郁闭度用 %（百分比）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "ENVI", "QGIS", "R", "Python", "MATLAB", "Drone", "LIDAR", "Hyperspectral camera", "Multispectral camera", "Soil moisture sensor", "Forest inventory software", "GIS software", "Remote sensing software", "Fire risk modeling", "Wildfire simulation", "Invasive species monitoring", "Forest pathology software", "Pest detection system", "Carbon sequestration calculator"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
