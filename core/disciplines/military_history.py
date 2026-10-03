"""军事史学科论文支持：军事史/战争史体裁、Chicago 引用样式与军事史记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="military_history",
    aliases=("military_history", "军事史", "战争史", "战史", "war history"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与军事史问题）",
            "methods（史料与研究方法）",
            "results（史实考证与叙事）",
            "discussion（历史意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（战役/事件背景）",
            "analysis（过程与因果分析）",
            "conclusions（历史教训）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；J Mil Hist 遵循 Chicago 规范）",
    reporting_standards={
        "historical": "军事史研究遵循史料来源报告规范",
        "archival": "档案研究遵循史料考证报告规范",
        "case_study": "战例研究遵循案例研究报告规范",
        "comparative": "比较军事史遵循比较研究报告规范",
        "oral_history": "口述史研究遵循口述史报告规范",
    },
    conventions=(
        "史料类型与来源（档案、回忆录、战报）须注明",
        "史实考证与二手文献辨析须明确",
        "时间线与战役阶段划分须规范",
        "兵力与伤亡数字须注明出处",
        "历史解释与当代视角须区分",
    ),
    key_venues=(
        "The Journal of Military History",
        "War in History",
        "Journal of Strategic Studies",
        "Armed Forces & Society",
        "Military History Quarterly",
        "The Journal of the Society for Army Historical Research",
    ),
    units_and_formulas_notes=(
        "兵力用编制单位；伤亡用人数并注明口径",
        "公式用 amsmath；伤亡率与兵力对比计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "日期用公历并注明历法差异",
        "数字引用须与原始史料核对",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "史料数据库（军事档案）",
        "GIS 历史地图（ArcGIS）",
        "文献管理软件（EndNote）",
        "历史数据统计（Python）",
    ),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)