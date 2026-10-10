"""其他建筑环境与设艺术学论文支持：跨方向设计评价与实证方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_built_environment_and_design",
    aliases=(
        "other_built_environment_and_design",
        "其他建筑环境与设计",
        "Other Built Environment and Design",
        "建筑环境交叉",
        "Interior Design",
        "Environmental Psychology",
        "城市设计交叉",
        "Habitat Studies",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（调研与评价方法）",
            "results（数据与分析）",
            "discussion（讨论与设计启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与场地描述）",
            "analysis（设计分析）",
            "results（评价结果）",
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
    citation_style="APA 7（社会科学向）/ GB/T 7714（中文）",
    reporting_standards={
        "survey": "APAS 调查规范",
        "systematic_review": "PRISMA 声明",
        "design_evaluation": "Post-Occupancy Evaluation POE 规范",
        "environmental_studies": "ISO 16738 环境测量",
    },
    conventions=(
        "场地描述含规模/位置/建成年代",
        "问卷与量表须给出信度 Cronbach α",
        "图表须遵循学术配色与无障碍",
        "设计案例须含平面图/剖面图/照片",
        "伦理审批编号（IRB）须列出",
    ),
    key_venues=(
        "Building and Environment",
        "Journal of Environmental Psychology",
        "Building Research & Information",
        "Architectural Science Review",
        "建筑学报",
    ),
    units_and_formulas_notes=(
        "面积/体积用 m² / m³",
        "光环境用 lx 或 μmol/m²/s",
        "声环境用 dB(A)，温度用 ℃",
        "统计量给出 M/SD/95% CI 或量表均值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD（制图）", "Revit（BIM）", "Rhino + Grasshopper", "SketchUp", "Enscape / Lumion（渲染）", "Photoshop（图像）", "InDesign（排版）", "SPSS（问卷统计）", "R / RStudio", "Excel", "Origin（绘图）", "EndNote", "LaTeX", "NVivo（质性分析）", "QGIS / ArcGIS（地理）", "EnergyPlus（能耗模拟）", "Radiance（光环境模拟）", "ECOTECT（环境分析）", "SurveyMonkey / Qualtrics（问卷）", "Dekra-Scan 环境传感"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
