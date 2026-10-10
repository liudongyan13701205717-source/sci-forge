"""足球运动学科论文支持：运动表现分析、技战术研究、运动损伤与训练科学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="football_playing",
    aliases=("football_playing", "football", "足球", "足球运动", "运动表现分析", "技战术分析", "运动训练", "体育科学"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "performance": "运动表现须报告样本量、测试条件与统计显著性",
        "injury": "运动损伤须报告损伤机制、分类与恢复时间",
        "training": "训练负荷须报告周期化方案与生理指标变化"
    },
    conventions=(
        "样本量与运动员水平须明确报告",
        "测试条件须标准化（场地、气候、时间）",
        "运动损伤须用标准化分类（如 DCF、OSCS）",
        "比赛录像须注明分析软件版本",
        "统计方法须报告效应量与置信区间"
    ),
    key_venues=(
        "Journal of Sports Sciences",
        "Journal of Sports Medicine and Physical Fitness",
        "Sports Medicine",
        "British Journal of Sports Medicine",
        "Journal of Football Science"
    ),
    units_and_formulas_notes=(
        "速度用 m/s 或 km/h",
        "加速度用 m/s²",
        "心率用 bpm",
        "VO₂ 用 mL/(kg·min)",
        "肌力用 N 或 kg"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Catapult", "SportsTracks", "TrackMan", "Hawk-Eye", "Kinovea", "Veo", "Wearer", "StadiumVision", "InStat", "SmartStats", "KineSports", "GPS Sports", "Motion Capture System", "SportsVision", "TeamVision", "AthleteGPS", "Performance Metrics", "DataSport", "SportsEngine", "MatchViz"),
    category="教育学",
    databases=("OpenAlex", "Crossref"),
)
