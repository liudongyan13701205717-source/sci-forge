"""体育教师教育论文支持：体育教育领域教师培养、运动训练与技能评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_physical_training",
    aliases=("teacher_training_in_physical_training", "Teacher training in physical training", "体育教师教育", "体育教育培养", "运动训练教学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "training design（训练设计）",
            "implementation（实施）",
            "evaluation（评估）",
            "conclusion",
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
    citation_style="APA 7",
    reporting_standards={
        "skill_assessment": "运动技能评估须描述测试方法、评分标准与常模参照",
        "training_program": "训练计划须描述周期化安排、强度负荷与恢复策略",
        "biomechanics": "生物力学分析须注明测试设备、采样频率与数据处理方法",
        "safety": "涉及高风险运动须声明安全预案与保险安排",
    },
    conventions=(
        "运动技能名称须使用国际体联（FISU）标准术语，中文译名须统一",
        "运动强度须同时给出绝对值（如功率、心率）与相对值（如心率储备百分比）",
        "视频分析须注明帧率、慢放倍数与标注方法，确保可重复",
        "训练计划须按周期化结构描述（准备期、竞赛期、恢复期），标注关键节点",
        "运动损伤报告须区分急性损伤与慢性损伤，标注RICE处理方案",
    ),
    key_venues=(
        "Journal of Teaching in Physical Education",
        "Research Quest in Sports and Physical Education",
        "Physical Education Review",
        "Sports Teacher Education Journal",
        "Journal of Sport and Health Science",
    ),
    units_and_formulas_notes=(
        "力量以牛顿（N）或千克（kg）标注，功率以瓦特（W）标注",
        "速度以米每秒（m/s）或千米每小时（km/h）标注，须明确单位",
        "心率以次每分钟（bpm）标注，心率储备以百分比（%HRR）标注",
        "运动负荷须同时描述外部负荷（重量、距离）与内部负荷（心率、RPE）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Fitbit", "Garmin", "WHOOP", "Polar", "Strava", "Apple Watch", "Samsung Gear", "Kinovea", "Dartfish", "Hudl", "TeamLink", "Vicon", "Qualisys", "Delsys EMG", "Polar H10", "Optitrack", "AMTI", "Spirolog", "TrainingPeaks", "Sportscode"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
