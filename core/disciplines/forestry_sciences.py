"""森林科学学科论文支持：森林生态、森林保护、林产加工与森林资源调查。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forestry_sciences",
    aliases=("forestry_sciences", "forestry science", "森林科学", "森林生态", "林产加工", "森林资源", "造林学", "森林保护"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "experiment": "实验须遵循标准化实验设计方法",
        "sampling": "抽样须遵循标准化样地布设方法",
        "statistics": "统计须遵循标准化分析规范",
        "ecology": "生态评估须遵循标准化方法"
    },
    conventions=(
        "树种用拉丁学名（首次出现时附中文名）",
        "林分参数用标准术语（DBH、树高、断面积）",
        "胸径用 cm；树高用 m",
        "面积用 ha；蓄积量用 m³/ha",
        "生长率用 m³/ha/year"
    ),
    key_venues=(
        "林业科学",
        "中国林业科学",
        "Forest Ecology and Management",
        "Journal of Forestry Research",
        "Canadian Journal of Forest Research"
    ),
    units_and_formulas_notes=(
        "胸径用 cm（DBH）",
        "树高用 m",
        "面积用 ha",
        "蓄积量用 m³/ha",
        "生长率用 m³/ha/year"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "ENVI", "R", "Python", "MATLAB", "Drone", "LIDAR", "Multispectral camera", "Soil moisture sensor", "Forest inventory software", "GIS software", "Remote sensing software", "Fire risk modeling", "Wildfire simulation", "Invasive species monitoring", "Forest pathology software", "Pest detection system", "Carbon sequestration calculator", "Tree species identification"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
