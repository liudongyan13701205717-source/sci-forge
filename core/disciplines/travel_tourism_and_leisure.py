"""旅行、旅游与休闲学科论文支持：休闲行为、旅游经济与目的地管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="travel_tourism_and_leisure",
    aliases=("travel_tourism_and_leisure", "旅行、旅游与休闲", "旅游与休闲",
             "leisure studies", "recreation studies", "休闲研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（休闲背景与研究问题）",
            "literature review",
            "methods",
            "results",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description",
            "analysis",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "sampling": "抽样方法、样本量与抽样框须报告",
        "scale_validation": "量表须经信效度检验",
        "leisure_behavior": "休闲行为遵循 Kaplan 模型",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "休闲行为遵循 Kaplan 模型",
        "游客量单位 人次",
        "经济数据用 元/美元 注明年份",
        "满意度用 Likert 5/7 级",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Annals of Tourism Research",
        "Tourism Management",
        "Journal of Travel Research",
        "Journal of Leisure Research",
        "Current Issues in Tourism",
    ),
    units_and_formulas_notes=(
        "游客量单位 人次/年",
        "旅游收入单位 万元/亿元",
        "满意度用 Likert 5/7 级",
        "回归分析须报告 R² 与显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Python", "AMOS", "NVivo", "Atlas.ti", "QGIS", "ArcGIS", "Google Earth Pro", "Excel", "Qualtrics", "SurveyMonkey", "Google Analytics", "Amplitude", "Mixpanel", "Tableau", "Power BI", "Stata", "Mplus", "Lisrel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
