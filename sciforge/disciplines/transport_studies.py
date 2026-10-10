"""运输研究学科论文支持：交通规划、政策与经济研究、4 步法模型研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="transport_studies",
    aliases=("transport_studies", "运输研究", "交通规划", "交通政策",
             "交通经济", "transport planning", "transport policy"),
    paper_types={
        "research": (
            "abstract",
            "introduction（交通问题与研究框架）",
            "literature review",
            "methods（建模与数据采集）",
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
        "model_validation": "交通模型遵循 4 步法标定验证",
        "survey": "出行调查遵循 TRB/ITE 手册",
        "economic_assessment": "经济评估遵循 DMRB/BAC 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "出行量单位 pcu/h",
        "出行距离单位 km",
        "出行时间单位 min",
        "经济指标单位 元/美元",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Transport Policy",
        "Journal of Transport Economics and Policy",
        "Transportation Research Part A",
        "Journal of Transport Geography",
        "Transportation",
    ),
    units_and_formulas_notes=(
        "出行量单位 pcu/h",
        "出行距离单位 km",
        "出行时间单位 min",
        "经济指标单位 元/美元",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("TransCAD", "VISUM", "VISSIM", "SUMO", "Calibre", "Cube", "EMME", "ArcGIS", "QGIS", "SPSS", "Stata", "R", "Python", "MATLAB", "AnyLogic", "NetLogo", "AMOS", "NVivo", "Tableau", "GTFS"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
