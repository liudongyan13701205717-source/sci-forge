"""体育指导员培训学科论文支持：体育教学/指导员培养/教练认证体裁、APA 引用样式与体育教育学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_instructor_training",
    aliases=("sports_instructor_training", "体育指导员培训", "运动指导员培训",
             "体育教师培训", "sports instructor training", "instructor education"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（体育教育学主流）",
    reporting_standards={
        "teacher_education": "体育教师教育研究遵循 NRP 与 IAUPE 教师能力框架",
        "certification_study": "认证项目评估遵循 BSCG 教练认证评估标准",
        "pedagogical_intervention": "教学干预研究遵循 CONSORT/STROBE",
    },
    conventions=(
        "体育教师能力模型须显式引用（TASQ、IAUPE、T-PAES）",
        "课程评估须给出前测-后测设计，含技能动作、认知测试、观察量表",
        "动作教学干预须报告动作学习阶段（认知/联结/自动化）",
        "培训方案须报告学时分配（理论学时 vs 实践学时）",
        "教学观察量表须报告评分者信度（ICC 或 kappa）",
    ),
    key_venues=(
        "Journal of Teaching in Physical Education",
        "Physical Education and Sport Pedagogy",
        "Sport Teacher Education Quarterly",
        "European Physical Education Review",
        "International Journal of Physical Education",
    ),
    units_and_formulas_notes=(
        "动作评分用 Likert 5 或 7 级量表并报告 Cronbach's α",
        "培训效果给出效应量（Cohen's d 或 η²）与 95% CI",
        "课程学时以 contact hours 与 practice hours 分列",
        "公式用 amsmath；量表信度系数须随结果一同报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Hudl 视频分析", "Coach's Eye 视频分析", "MotionDraw 动作识别", "Sportsmotion 动作识别", "OpenPose 动作识别", "Vicon Motion Capture", "OptiTrack 动作捕捉", "Kinect 动作捕捉", "Google Slides 教学演示", "Obsidian 知识库", "Zoom 远程授课", "Moodle 学习管理", "NSCA 认证系统", "USAC 在线学习", "BSCG 教练认证平台", "YouTube Studio", "R", "SPSS", "NVivo 质性分析", "Tableau 数据可视化"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
