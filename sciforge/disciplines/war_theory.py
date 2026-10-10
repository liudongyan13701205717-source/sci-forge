"""战争理论学科论文支持：战略思想、战例分析与军事模拟的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="war_theory",
    aliases=("war_theory", "战争理论", "军事战略", "军事理论", "战略研究",
             "war theory", "military strategy", "warfare studies",
             "strategic studies", "military theory"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "theoretical framework（理论框架）",
            "case analysis（战例分析）",
            "simulation results（模拟结果）",
            "discussion（讨论与推论）",
            "conclusions and implications（结论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "historical context（历史背景）",
            "case description（战役/战争描述）",
            "key decisions（关键决策分析）",
            "outcome analysis（结果分析）",
            "lessons learned（经验教训）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical evolution（理论演变综述）",
            "school of thought（学派观点比较）",
            "contemporary applications（当代应用）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_analysis": "战例分析须标注时间、地点、参战方与关键决策节点，使用地图辅助空间分析",
        "source_reliability": "战史数据须标注来源可靠性等级（一手档案、二手研究、民间记录）",
        "classification": "敏感信息须按密级标注，公开材料须经脱密审查后方可使用",
    },
    conventions=(
        "军事术语遵循 GJB 或国防部统一术语表，中英文对照标注",
        "战例按战略、战役、战术三级分类，明确分析层级",
        "地图使用 WGS84 坐标，标注比例尺、投影方式与数据日期",
        "时间线以 UTC 或当地时区标注，明确换算关系",
        "伤亡统计标注来源与估算方法，区分确认伤亡与估算值",
    ),
    key_venues=(
        "Parameters",
        "Defense Analysis",
        "Naval War College Review",
        "Journal of Strategic Studies",
        "Military Review",
    ),
    units_and_formulas_notes=(
        "距离单位为 km 或 nmi（海里），按语境选择",
        "时间以 UTC 为基准，作战行动标注时区换算",
        "火力密度以发/分或枚/时为单位",
        "伤亡以百分比或绝对数标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NetLogo", "AnyLogic", "STELLA", "Vensim", "Palisade @RISK", "Crystal Ball", "ArcGIS Pro", "QGIS", "MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "Gephi", "LaTeX", "OpenRefine", "Tableau Prep", "FME", "WEKA"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
