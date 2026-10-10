"""旅行社服务学科论文支持：旅行社运营、产品设计与客户关系研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="travel_agency_services",
    aliases=("travel_agency_services", "旅行社服务", "旅行社运营",
             "旅游代理", "travel agency", "travel agent services"),
    paper_types={
        "research": (
            "abstract",
            "introduction（旅行社背景与业务问题）",
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
        "customer_satisfaction": "客户满意度遵循 SERVQUAL",
        "survey": "调查遵循 AAPOR 规范",
        "qualitative": "质性研究遵循 COREQ",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "客源单位 人次",
        "客单价单位 元/美元",
        "满意度用 Likert 5 级",
        "OTA 平台遵循 NDC/IATA 标准",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Journal of Travel Research",
        "Annals of Tourism Research",
        "Tourism Management",
        "Current Issues in Tourism",
        "旅游学刊",
    ),
    units_and_formulas_notes=(
        "客源单位 人次",
        "客单价单位 元/美元",
        "满意度用 Likert 5 级",
        "统计结果用均值±标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Amadeus GDS", "Sabre GDS", "Travelport", "Worldspan", "Galileo", "Google Analytics", "Qualtrics", "SurveyMonkey", "Salesforce", "Microsoft Dynamics", "SPSS", "R", "Python", "Excel", "NVivo", "Tableau", "Power BI", "Amadeus NDC", "IATA OpenTravel", "Expedia Partner Central"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
