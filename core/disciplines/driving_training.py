"""驾驶训练学科论文支持：驾驶技能习得、人机工程与驾驶行为研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="driving_training",
    aliases=(
        "driving_training", "驾驶训练",
        "driver training", "驾驶训练",
        "driving skills", "驾驶技能",
        "motor vehicle training", "机动车训练",
        "professional driving", "职业驾驶",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（训练问题与背景）",
            "method（训练设计、技能测试、效果评估）",
            "results（技能习得与训练效果）",
            "discussion（训练优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "training program（训练方案描述）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（训练理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "training": "训练方案须完整描述",
        "assessment": "技能评估须注明方法与标准",
        "safety": "事故数据须注明来源与时间",
    },
    conventions=(
        "年龄用 岁 表示",
        "训练时长用 小时 表示",
        "通过率用 % 表示",
        "反应时间用 ms 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Human Factors",
        "Transportation Research Part F: Traffic Psychology and Behaviour",
        "Journal of Safety Research",
        "Traffic Injury Prevention",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "时长用 小时 表示",
        "通过率用 % 表示",
        "反应时间用 ms 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Driving Simulator", "Traffic Safety Software", "GPS Tracking System", "Vehicle Telematics", "Dashcam", "Speed Camera", "Traffic Sign Recognition", "Driving Behaviour Analysis", "Accident Reconstruction Software", "Eye Tracker", "Steering Wheel Angle Sensor", "Vehicle Dynamics Simulator"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
