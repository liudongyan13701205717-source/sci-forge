"""军事科学学科论文支持：军事科学/作战研究体裁、Chicago 引用样式与军事科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="military_science",
    aliases=("military_science", "军事科学", "军事学", "作战研究", "military studies"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与军事问题）",
            "methods（研究设计与数据来源）",
            "results（作战与组织数据）",
            "discussion（军事意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（战例/案例背景）",
            "analysis（作战过程与决策分析）",
            "conclusions（经验教训）",
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
    citation_style="Chicago 样式（作者-年份；Military Review 遵循 Chicago 规范）",
    reporting_standards={
        "case_study": "战例研究遵循案例研究报告规范",
        "historical": "军事史研究遵循史料来源报告规范",
        "analytical": "作战分析遵循模型设定报告规范",
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "simulation": "作战仿真遵循仿真实验报告规范",
    },
    conventions=(
        "作战概念与术语（条令定义）须注明",
        "兵力与装备数据来源须报告",
        "时间线与战役阶段划分须明确",
        "涉密信息处理与脱密声明须注明",
        "分析框架（作战效能、指挥控制）须明确",
    ),
    key_venues=(
        "Military Review",
        "Journal of Strategic Studies",
        "Armed Forces & Society",
        "Military Operations Research",
        "Parameters",
        "Naval War College Review",
    ),
    units_and_formulas_notes=(
        "兵力用编制单位（师/旅/营）；装备用数量",
        "公式用 amsmath；作战效能与损耗计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "仿真结果给出置信区间与运行次数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "兵棋推演软件（MCWL）",
        "GIS 态势分析（ArcGIS）",
        "蒙特卡洛作战仿真",
        "SPSS 军事数据分析",
    ),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)