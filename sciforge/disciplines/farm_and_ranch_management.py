"""农场与牧场管理学科论文支持：农业管理、畜牧经营与农场经济研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="farm_and_ranch_management",
    aliases=(
        "farm_and_ranch_management", "农场与牧场管理",
        "farm and ranch management", "农场与牧场管理",
        "farm management", "农场管理",
        "ranch management", "牧场管理",
        "agricultural management", "农业管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（管理问题与背景）",
            "method（研究设计、管理干预、评估指标）",
            "results（管理效果与农场发展）",
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
        "ethics": "涉及农场数据须声明隐私保护",
    },
    conventions=(
        "面积用 ha 表示",
        "产量用 kg/ha 表示",
        "时间用 年 表示",
        "成本用 元 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Farm Management",
        "Agricultural Economics",
        "Journal of Agricultural Economics",
        "Farm Management",
        "International Journal of Agricultural Management",
        "Journal of International Farm Management",
    ),
    units_and_formulas_notes=(
        "面积用 ha 表示",
        "产量用 kg/ha 表示",
        "成本用 元 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Python (pandas, numpy)", "MATLAB", "Excel", "ArcGIS", "QGIS", "Farm Management Software", "Livestock Management Software", "Crop Management Software", "Financial Management Software", "Inventory Management Software", "Supply Chain Management Software", "Market Research Software", "SurveyMonkey", "Qualtrics", "Google Forms", "Social Media Analytics", "Customer Feedback Software", "Farmbook"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
