"""驾驶安全教育学科论文支持：交通安全教育、驾驶培训与事故预防研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="driver_and_safety_teacher_education",
    aliases=(
        "driver_and_safety_teacher_education", "驾驶安全教育",
        "driver education", "驾驶教育",
        "safety education", "安全教育",
        "traffic safety", "交通安全",
        "driving instructor training", "驾驶培训",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教育问题与背景）",
            "method（研究设计、教学干预、评估指标）",
            "results（教学效果与安全改善）",
            "discussion（教育优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "teaching process（教学过程）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教育理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "教学方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "safety": "事故数据须注明来源与时间",
    },
    conventions=(
        "年龄用 岁 表示",
        "驾驶时长用 小时 表示",
        "事故率用 次/万公里 表示",
        "满意度用 Likert 5 级表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Journal of Transport Safety and Security",
        "Traffic Injury Prevention",
        "Journal of Safety Research",
        "Transportation Research Part F: Traffic Psychology and Behaviour",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "时长用 小时 表示",
        "事故率用 次/万公里 表示",
        "评分用 1-5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Google Classroom", "Zoom", "Microsoft Teams", "Driving Simulator", "Traffic Safety Software", "GPS Tracking System", "Vehicle Telematics", "Dashcam", "Speed Camera", "Traffic Sign Recognition", "Driving Behaviour Analysis", "Accident Reconstruction Software"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
