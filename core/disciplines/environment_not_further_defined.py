"""环境（未进一步定义）学科论文支持：环境综合研究与可持续发展体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environment_not_further_defined",
    aliases=(
        "environment_not_further_defined", "环境（未进一步定义）",
        "environment not further defined", "环境（未定义）",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与背景）",
            "method（研究设计、实验条件、评估指标）",
            "results（环境效果与评估）",
            "discussion（环境优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "environmental process（环境过程）",
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
        "experiment": "实验条件须完整",
        "assessment": "评估指标须注明方法与时机",
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
        "Environmental Science & Technology",
        "Journal of Environmental Management",
        "Environmental Pollution",
        "Science of the Total Environment",
        "Environmental Monitoring and Assessment",
        "Journal of Cleaner Production",
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
