"""运输服务学科论文支持：公交/出租/客运服务运营、服务质量与乘客行为研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="transport_services",
    aliases=("transport_services", "运输服务", "公交服务", "客运服务",
             "出租车服务", "ferry", "transit services"),
    paper_types={
        "research": (
            "abstract",
            "introduction（服务背景与研究问题）",
            "literature review",
            "methods（调查设计与数据采集）",
            "results（服务绩效与乘客行为分析）",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
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
        "survey": "调查遵循 AAPOR 规范",
        "service_quality": "服务质量遵循 SERVQUAL",
        "qualitative": "质性研究遵循 COREQ",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "乘客量用 人次/日 报告",
        "准点率用 % 报告",
        "满意度用 SERVQUAL 5 级量表",
        "数据来源与采集时段须说明",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Transport Policy",
        "Transportation Research Part A",
        "Research in Transportation Economics",
        "Journal of Transport Geography",
        "Transportation",
    ),
    units_and_formulas_notes=(
        "乘客量单位 人次/日",
        "准点率用 % 表示",
        "满意度用 Likert 5 级",
        "统计结果用均值±标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("AutoMOD", "VISSIM", "AnyLogic", "NetLogo", "TransCAD", "ArcGIS", "QGIS", "SPSS", "Stata", "R", "Python", "Excel", "AMOS", "NVivo", "Tableau", "Power BI", "GTFS", "Google Transit API", "Uber Hail API", "OpenStreetMap"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
