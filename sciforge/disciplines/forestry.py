"""林学学科论文支持：森林生态、造林学、森林经理学、林木遗传育种、森林保护。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forestry",
    aliases=("forestry", "forest science", "林学", "林业科学", "森林生态", "造林学", "森林经理学", "林木遗传育种"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（括号式引用）",
    reporting_standards={
        "sampling": "抽样须报告样地尺寸、数量与布设方式",
        "growth_model": "生长模型须报告模型形式与拟合优度（R²/RMSE）",
        "remote_sensing": "遥感须报告影像来源与精度评价（总体精度/Kappa）"
    },
    conventions=(
        "树种用拉丁学名（首次出现时附中文名）",
        "林分参数用标准术语（郁闭度、蓄积量、断面积、株数密度）",
        "胸径 DBH 用 cm；树高用 m；材积用 m³",
        "立地指数用 SI = H（基准年龄时优势木平均高）",
        "地图须含比例尺、指北针、图例与坐标系"
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Canadian Journal of Forest Research",
        "Forest Science",
        "Silvae Genetica",
        "New Phytologist"
    ),
    units_and_formulas_notes=(
        "胸径用 cm（DBH）；树高用 m",
        "材积用 m³/ha；蓄积量用 m³/ha",
        "生物量用 Mg/ha 或 t/ha",
        "林龄用年（age）或龄级（age class）",
        "生长率用 %/年 或 m³/ha/year"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "ENVI", "QGIS", "R", "Python", "MATLAB", "ConeLogger", "LIDAR", "Helmholtz", "Pitfall Traps", "Forest Inventory Analyzer", "i-Tree", "TimberQA", "SilvaCalc", "TreeTracker", "ForestryPro", "ForestGen", "BioSilo", "SILVA", "ForestSim"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
