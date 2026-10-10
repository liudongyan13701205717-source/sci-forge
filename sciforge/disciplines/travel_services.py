"""旅行服务学科论文支持：旅行服务运营、客户体验与服务质量研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="travel_services",
    aliases=("travel_services", "旅行服务", "旅行运营",
             "旅行科技", "travel service providers", "travel operations"),
    paper_types={
        "research": (
            "abstract",
            "introduction（旅行服务背景与研究问题）",
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
        "service_quality": "服务质量遵循 SERVQUAL",
        "customer_behavior": "客户行为遵循 4A 模型",
        "survey": "调查遵循 AAPOR 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "服务量单位 人次",
        "客单价单位 元/美元",
        "满意度用 Likert 5 级",
        "OTA/GDS 遵循 NDC/IATA 标准",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Journal of Travel Research",
        "Annals of Tourism Research",
        "Tourism Management",
        "Current Issues in Tourism",
        "Tourism Geographies",
    ),
    units_and_formulas_notes=(
        "服务量单位 人次",
        "客单价单位 元/美元",
        "满意度用 Likert 5 级",
        "统计结果用均值±标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Amadeus GDS", "Sabre GDS", "Travelport", "Worldspan", "Google Analytics", "Qualtrics", "SurveyMonkey", "Salesforce", "SPSS", "R", "Python", "Excel", "NVivo", "Tableau", "Power BI", "Amplitude", "Mixpanel", "Amadeus NDC", "IATA OpenTravel", "Expedia"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
