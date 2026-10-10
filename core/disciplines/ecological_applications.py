"""生态应用学科论文支持：生态系统管理、环境修复与生态保护研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ecological_applications",
    aliases=(
        "ecological_applications", "生态应用",
        "applied ecology", "应用生态",
        "ecosystem management", "生态系统管理",
        "environmental restoration", "环境修复",
        "conservation biology", "保护生物学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（生态问题与背景）",
            "method（研究设计、实验条件、评估指标）",
            "results（生态效果与管理评估）",
            "discussion（管理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "restoration process（修复过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experiment": "实验条件须完整",
        "assessment": "评估指标须注明方法与时机",
        "ethics": "涉及野生动物须声明伦理审批",
    },
    conventions=(
        "面积用 ha 表示",
        "生物量用 g/m² 表示",
        "物种丰富度用 种 表示",
        "时间用 年 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Restoration Ecology",
        "Ecological Applications",
        "Conservation Biology",
        "Journal of Applied Ecology",
        "Ecological Engineering",
        "Landscape Ecology",
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
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science"),
)
