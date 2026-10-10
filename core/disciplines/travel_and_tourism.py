"""旅游学科论文支持：旅游规划、游客行为与旅游经济研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="travel_and_tourism",
    aliases=("travel_and_tourism", "旅游", "旅游管理", "旅游规划",
             "游客研究", "travel management", "tourism industry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（旅游背景与研究问题）",
            "literature review",
            "methods",
            "results",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（目的地案例）",
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
        "ethical_approval": "涉及人类受试者须声明伦理审批",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "旅游术语遵循 UNWTO 定义",
        "游客量单位 人次",
        "经济数据用 元/美元 注明年份",
        "游客满意度用 Likert 5/7 级",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Annals of Tourism Research",
        "Tourism Management",
        "Journal of Travel Research",
        "Current Issues in Tourism",
        "旅游学刊",
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
