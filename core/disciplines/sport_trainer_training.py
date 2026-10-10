"""体育训练员培养学科论文支持：教练培养/训练学体裁、APA 引用样式与训练学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sport_trainer_training",
    aliases=("sport_trainer_training", "体育训练员培养", "教练员培训",
             "体育训练员培训", "sport trainer training", "trainer education"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（教练学与体育教育主流）",
    reporting_standards={
        "trainer_development": "教练培养项目报告遵循 CEST 教练发展框架",
        "pedagogical_intervention": "培训教学干预研究遵循 CONSORT 与 STROBE",
        "curriculum_evaluation": "课程体系评估遵循 Kirkpatrick 四级评价模型",
    },
    conventions=(
        "教练能力模型须显式引用（DCIM、CEST、NCLD 之一并注明版本）",
        "受训教练的运动员年龄与训练年限须报告",
        "培训项目须区分短期工作坊与长期文凭课程",
        "教练-运动员互动分析须报告样本量与编码信度（Kappa）",
        "培训效果评估须给出前测-后测设计与效应量",
    ),
    key_venues=(
        "International Journal of Sports Science & Coaching",
        "Coaching & Science",
        "Journal of Sports Sciences",
        "The Sport Psychologist",
        "Coaching and Elite Athlete Development",
    ),
    units_and_formulas_notes=(
        "训练负荷用 AU；相对强度报告为 %1RM 或 %VO2max",
        "教练能力分级用 Likert 5 或 7 级量表并报告 Cronbach's α",
        "培训时长用学时（contact hours），实践学时须单列",
        "公式用 amsmath；负荷/强度-时间关系须给出显式定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Catapult 惯性传感器", "Polar Vantage 运动手表", "Garmin Connect", "Wahoo TICKTALK 功率计", "Hudl 视频分析", "Wysopal 战术软件", "FinalBall 数据分析", "TeamBuilr 训练计划", "CoachDraw 战术绘制", "InBody 体成分分析仪", "Kistler 测力台", "Whoop 恢复监测", "Oura Ring 睡眠监测", "R", "SPSS", "NVivo 质性分析", "Tableau 数据可视化", "Moodle 学习管理", "USAC 在线学习", "NSCA 认证系统"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
