"""环境管理学科论文支持：环境政策、环境规划与可持续发展管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_management",
    aliases=(
        "environmental_management", "环境管理", "环境规划",
        "environmental management", "环境管理",
        "environmental planning", "环境规划",
        "sustainable management", "可持续管理",
        "environmental governance", "环境治理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与背景）",
            "method（研究设计、管理干预、评估指标）",
            "results（管理效果与环境评估）",
            "discussion（管理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "management process（管理过程）",
            "evaluation（效果评估）",
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
        "intervention": "管理方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及环境数据须声明隐私保护",
    },
    conventions=(
        "面积用 ha 表示",
        "生物量用 g/m² 表示",
        "物种丰富度用 种 表示",
        "时间用 年 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Environmental Management",
        "Environmental Management",
        "Journal of Cleaner Production",
        "Environmental Science & Policy",
        "Sustainable Development",
        "Ecological Economics",
    ),
    units_and_formulas_notes=(
        "面积用 ha 表示",
        "生物量用 g/m² 表示",
        "物种丰富度用 种 表示",
        "时间用 年 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Python (pandas, numpy)", "MATLAB", "Excel", "ArcGIS", "QGIS", "ENVI", "ERDAS", "ImageJ", "NVivo", "R language", "Python (SHAP)", "Random Forest Software", "MAXENT", "GIS Mapping Software", "Drone Survey", "Remote Sensing Software", "Environmental Monitoring Equipment", "Ecosystem Model Software"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science"),
)
