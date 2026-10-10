"""老年护理健康学科论文支持：老年医学、护理与健康管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="elder_care_health",
    aliases=(
        "elder_care_health", "老年护理健康", "老年医学",
        "geriatric care", "老年护理",
        "geriatric medicine", "老年医学",
        "elderly health", "老年健康",
        "aging health", "老龄化健康",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（老年健康问题与背景）",
            "method（研究设计、护理干预、评估指标）",
            "results（护理效果与生活质量）",
            "discussion（护理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "nursing process（护理过程）",
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
    citation_style="Vancouver",
    reporting_standards={
        "intervention": "护理方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及老年患者数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "护理过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "生活质量须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of the American Geriatrics Society",
        "Age and Ageing",
        "Geriatric Nursing",
        "Journal of Gerontological Nursing",
        "International Journal of Older People Nursing",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "生活质量用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "Vital Signs Monitor", "Blood Pressure Monitor", "Pulse Oximeter", "Glucose Meter", "ECG Machine", "Ultrasound Machine", "Fall Detection System", "Medication Management Software", "Electronic Health Record", "Gait Analysis System"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
