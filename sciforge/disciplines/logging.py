"""林业采伐（Logging）学科论文支持：木材采运、可持续采伐与林业机械。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="logging",
    aliases=(
        "logging",
        "林业采伐",
        "森林采运",
        "forestry",
        "木材采运",
        "sustainable forestry",
        "logging operations",
        "森林经营",
        "wood harvesting",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（采运分析）",
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
    citation_style="APA 7",
    reporting_standards={
        "k1": "采伐效率按立方米每公顷每小时报告",
        "k2": "环境影响按 ISO 14064 碳核算",
        "k3": "林业调查遵循 FSC 或 PEFC 认证框架",
    },
    conventions=(
        "林地类型使用 ICP/FRA 分类",
        "株数密度以株/公顷计",
        "采伐强度以百分比或公顷/年报告",
        "碳储量按吨碳每公顷报告",
        "树种名称使用拉丁学名",
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Canadian Journal of Forest Research",
        "Silvae Fennicae",
        "Canadian Journal of Forest Research",
        "林业科学",
    ),
    units_and_formulas_notes=(
        "生长量以 m³/ha·a 报告",
        "碳储量采用 IPCC 系数",
        "采伐成本按美元/立方米计",
        "遥感精度以像素或米为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "Fusion (Forestry Software)", "WinPeaks", "FieldMapper", "DendroStat", "TreeSAR", "Sapflow (Dynamic Instruments)", "Laser Scanner (Leica BLK360)", "UAV (DJI Matrice 300)", "LiDAR (RIEGL VQ-880)", "Aerial Photogrammetry", "ENVI", "R", "RStudio", "Python", "Stata", "SPSS", "Excel", "Fieldbook (Silvatics)"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
