"""裁判与其他体育官员学科论文支持：竞赛执裁与判罚体裁、APA 引用样式与体育测量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="umpires_and_other_sports_officials",
    aliases=("umpires and other sports officials", "裁判与其他体育官员", "裁判学", "体育官员",
             "umpiring", "refereeing", "sports officiating", "裁判员研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与执裁问题）",
            "methods（被试、任务与测量）",
            "results（判罚准确率、决策与负荷数据）",
            "discussion（执裁机理与实践意义）",
            "references",
        ),
        "observational": (
            "abstract",
            "introduction",
            "methods（比赛样本、编码方案与信度）",
            "results（判罚分布与一致性）",
            "discussion（规则与训练启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；体育科学期刊多用 APA）",
    reporting_standards={
        "observational": "观察性研究须报告编码方案、评分者信度与样本量",
        "decision_accuracy": "判罚准确性研究须报告真值来源与判定标准",
        "physiological": "生理负荷研究须报告测量设备、采样率与指标",
        "experimental": "实验研究须报告随机化、盲法与统计方法",
    },
    conventions=(
        "判罚准确率用 %，并说明真值判定依据",
        "评分者信度用 Kappa 或 ICC 报告",
        "比赛级别、规则版本与样本量须交代",
        "生理负荷指标（心率、距离）须注明测量方式",
        "决策时间用 ms/s 并说明测量起点",
    ),
    key_venues=(
        "Journal of Sports Sciences",
        "European Journal of Sport Science",
        "Psychology of Sport and Exercise",
        "Journal of Sport Management",
        "Sports Medicine",
        "International Journal of Sports Science & Coaching",
    ),
    units_and_formulas_notes=(
        "判罚准确率用 %；信度用 Cohen's Kappa 或 ICC",
        "决策时间用 ms；心率用 bpm；距离用 m/km",
        "速度用 m/s 或 km/h；负荷用 AU（任意单位）须说明",
        "统计量给出均值 ± SD；显著性用 P 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("视频助理裁判 (VAR) 系统", "Hawk-Eye 鹰眼系统", "Seiko 电子秒表", "电子记分系统", "Instant Replay 回放系统", "Scoreboard Controller", "TeamSnap 赛事管理", "裁判通讯系统", "Catapult GPS 追踪背心", "Sportscode", "Dartfish", "Kinovea", "慢动作回放系统", "Shot Clock 系统", "电子哨 (electronic whistle)", "Polar Team Pro 心率系统", "裁判绩效评估软件", "Hudl 视频分析平台", "计时与计分系统 (Timing & Scoring)", "体育规则管理平台"),
    category="教育学",
    databases=("SPORTDiscus", "OpenAlex", "Crossref", "CNKI"),
)
