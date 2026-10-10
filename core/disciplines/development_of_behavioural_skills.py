"""行为技能发展学科论文支持：技能习得、行为改变与运动技能学习体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_of_behavioural_skills",
    aliases=(
        "development_of_behavioural_skills", "行为技能发展",
        "behavioural skill development", "技能习得",
        "motor skill learning", "运动技能学习",
        "skill acquisition", "技能获取",
        "behavioural change", "行为改变",
        "procedural learning", "程序性学习",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技能学习问题与理论背景）",
            "method（参与者、任务设计、练习条件、测量）",
            "results（学习曲线与迁移效果）",
            "discussion（学习机制与实践启示）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "intervention design（干预方案设计）",
            "results（技能发展效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework（理论框架综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experimental": "实验条件（练习量、反馈类型）须完整报告",
        "transfer": "迁移测试须定义新任务与评分标准",
        "learning_curve": "学习曲线报告须提供逐次练习数据",
        "ethics": "涉及人体验证须声明 IRB 批准",
    },
    conventions=(
        "技能定义须明确（任务、标准、评分方式）",
        "练习条件（组内/组间/组间）须区分",
        "反馈类型（结果反馈/知识反馈）须注明",
        "测量指标（准确率、反应时间、运动学参数）须定义",
        "迁移测试须在前测与后测中保持一致",
    ),
    key_venues=(
        "Journal of Motor Behavior",
        "Research Quarterly for Exercise and Sports",
        "Journal of Applied Research in Memory and Cognition",
        "Human Movement Science",
        "Psychology of Learning and Motivation",
    ),
    units_and_formulas_notes=(
        "反应时间用 ms 表示",
        "准确率用 % 表示",
        "运动学参数（速度、加速度）用标准单位",
        "学习曲线报告须提供练习次数与表现指标",
        "统计检验注明效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PsychoPy", "OpenSesame", "E-Prime", "MATLAB", "SPSS", "R (RStudio)", "JASP", "Excel", "Movenet", "KineCT", "OptiTrack", "Vicon", "Delsys EMG", "Wii Balance Board", "Gyro sensor", "Kinect Azure", "GameMaker", "Unity", "Unreal Engine", "Python (pandas, scipy)"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "PsycINFO"),
)
