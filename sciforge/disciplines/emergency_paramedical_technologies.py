"""紧急医疗技术学科论文支持：急救技术、院前急救与灾难医学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="emergency_paramedical_technologies",
    aliases=(
        "emergency_paramedical_technologies", "紧急医疗技术", "急救技术",
        "emergency medical technology", "紧急医疗技术",
        "paramedic technology", "急救技术",
        "pre-hospital care", "院前急救",
        "disaster medicine", "灾难医学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（急救问题与背景）",
            "method（研究设计、急救干预、评估指标）",
            "results（急救效果与患者预后）",
            "discussion（急救优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "emergency process（急救过程）",
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
        "intervention": "急救方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及患者数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "急救时间用 min 表示",
        "生命体征须注明测量时机与方法",
        "急救效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Prehospital Emergency Care",
        "Emergency Medicine Journal",
        "Resuscitation",
        "American Journal of Emergency Medicine",
        "European Journal of Emergency Medicine",
        "Journal of Trauma and Acute Care Surgery",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "急救时间用 min 表示",
        "生命体征须注明测量时机与方法",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "Defibrillator", "Ventilator", "ECG Machine", "Pulse Oximeter", "Blood Pressure Monitor", "Glucose Meter", "Ultrasound Machine", "Patient Monitor", "Infusion Pump", "CPR Manikin", "AED Trainer"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
