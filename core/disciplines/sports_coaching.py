"""运动教练学学科论文支持：教练学/战术学/训练学体裁、APA 引用样式与教练学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_coaching",
    aliases=("sports_coaching", "运动教练学", "教练学", "运动训练学",
             "sports coaching", "coaching education"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（教练学与运动表现分析主流）",
    reporting_standards={
        "tactical_analysis": "比赛战术分析遵循 TTA（Tactical Time-series Analysis）编码方案",
        "coach_athlete_interaction": "教练-运动员互动分析遵循 NISSE 或 NISSE-2 编码系统",
        "coaching_model": "教练模型报告遵循 DCF（Developing Coaching Framework）或 ACT 框架",
    },
    conventions=(
        "教练学理论框架（如 ACT、DCF、NCLD）须显式引用",
        "比赛录像分析须报告编码信度（Cohen's kappa ≥ 0.75）",
        "训练周期（周期化）须区分宏观/中观/微观周期",
        "教练反馈与指令类型须分类统计（指令性/信息性/激励性）",
        "术语首次出现给出中文全称与英文对照",
    ),
    key_venues=(
        "International Journal of Sports Science & Coaching",
        "Coaching & Science",
        "Journal of Sports Sciences",
        "Sport, Exercise and Performance Psychology",
        "Psychology of Sport and Exercise",
    ),
    units_and_formulas_notes=(
        "教练-运动员互动编码用 NISSE 类别并报告百分比与频次",
        "训练周期以周为单位报告（WIMBA 时间块）",
        "球员表现指标用事件次数或每 90 分钟次数",
        "公式用 amsmath；编码类别与统计口径须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Wysopal 战术软件", "FinalBall 数据分析", "Statoscope 战术分析", "InStat 比赛数据", "TrackSports 田径分析", "CoachDraw 战术绘制", "Polysports Coach", "Coach's Eye 视频分析", "Hudl 视频分析", "Catapult 惯性传感器", "Polar 心率监测", "Wahoo 功率计", "InBody 体成分分析仪", "Kistler 测力台", "Trackman 雷达追踪", "TeamBuilr 训练计划", "R", "SPSS", "NVivo 质性分析", "Tableau 数据可视化"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "SportDiscus"),
)
