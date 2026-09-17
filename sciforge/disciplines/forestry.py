"""林学论文支持：森林生态、造林学、森林经理学、林木遗传育种、森林保护。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forestry",
    aliases=("forestry", "forest_science", "林学", "林业科学"),
    paper_types={
        "research": ("abstract", "introduction", "study area", "methods", "results", "discussion", "conclusions", "references"),
        "inventory": ("abstract", "introduction", "sampling design", "field methods", "results", "estimation", "conclusions", "references"),
        "management": ("abstract", "introduction", "objectives", "treatment design", "monitoring", "results", "recommendations", "conclusions", "references"),
    },
    citation_style="APA 7（括号），如 (Author, Year)",
    reporting_standards={
        "sampling": "抽样须报告样地尺寸/数量、布设方式（系统/随机/分层）与估计精度",
        "growth_model": "生长模型须报告模型形式、拟合优度（R²/RMSE）与残差分析",
        "remote_sensing": "遥感须报告影像来源、分类方法与精度评价（总体精度/Kappa）",
        "treatment": "试验处理须报告设计类型（RCT/配对/区组）、重复数与统计检验",
    },
    conventions=(
        "树种用拉丁学名（首次）+ 中文名（此后可用中文）",
        "林分参数用标准术语（郁闭度/蓄积量/断面积/株数密度）",
        "胸径 DBH 用 cm；树高用 m；材积用 m³",
        "立地指数用 SI = H（基准年龄时的优势木平均高）",
        "地图须含比例尺、指北针、图例与坐标系",
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Canadian Journal of Forest Research",
        "Forest Science",
        "Silvae Genetica",
        "New Phytologist",
    ),
    units_and_formulas_notes=(
        "胸径用 cm（DBH）；树高用 m",
        "材积用 m³/ha；蓄积量用 m³/ha",
        "生物量用 Mg/ha 或 t/ha",
        "林龄用年（age）或龄级（age class）",
        "生长率用 %/年 或 m³/ha/year",
    ),
)
