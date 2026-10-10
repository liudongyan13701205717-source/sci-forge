"""驾驶培训学科论文支持：驾驶教学、培训方法与技能评估研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="driving_instructor_training",
    aliases=(
        "driving_instructor_training", "驾驶培训",
        "driving instructor", "驾驶教练",
        "driver training", "驾驶训练",
        "traffic safety education", "交通安全教育",
        "driving school", "驾校",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（培训问题与背景）",
            "method（研究设计、培训方案、评估指标）",
            "results（培训效果与技能发展）",
            "discussion（培训优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "training program（培训方案描述）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（培训理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "培训方案须完整描述",
        "assessment": "技能评估须注明方法与标准",
        "safety": "事故数据须注明来源与时间",
    },
    conventions=(
        "年龄用 岁 表示",
        "培训时长用 小时 表示",
        "通过率用 % 表示",
        "满意度用 Likert 5 级表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Journal of Transport Safety and Security",
        "Transportation Research Part F: Traffic Psychology and Behaviour",
        "Journal of Safety Research",
        "Traffic Injury Prevention",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "时长用 小时 表示",
        "通过率用 % 表示",
        "评分用 1-5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Google Classroom", "Zoom", "Microsoft Teams", "Driving Simulator", "Traffic Safety Software", "GPS Tracking System", "Vehicle Telematics", "Dashcam", "Speed Camera", "Traffic Sign Recognition", "Driving Behaviour Analysis", "Accident Reconstruction Software"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
