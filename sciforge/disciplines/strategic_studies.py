"""战略研究学科论文支持：战略研究/安全研究体裁、Chicago 引用样式与战略研究记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="strategic_studies",
    aliases=("strategic_studies", "战略研究", "安全研究", "战略学", "strategic analysis"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与战略问题）",
            "methods（研究设计与分析框架）",
            "results（战略态势与决策数据）",
            "discussion（战略意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（战略案例背景）",
            "analysis（战略决策过程分析）",
            "conclusions（战略启示）",
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
    citation_style="Chicago 样式（作者-年份；J Strategic Stud 遵循 Chicago 规范）",
    reporting_standards={
        "case_study": "战略案例研究遵循案例研究报告规范",
        "historical": "战略史研究遵循史料来源报告规范",
        "analytical": "战略分析遵循模型设定报告规范",
        "discourse": "战略话语分析遵循话语分析报告规范",
        "comparative": "比较战略研究遵循比较研究报告规范",
    },
    conventions=(
        "战略概念与理论框架（威慑、联盟等）须定义",
        "地缘与安全环境背景须交代",
        "决策者与机构角色须明确",
        "资料来源（档案、公开文献）须注明",
        "分析层次（体系/国家/单元）须明确",
    ),
    key_venues=(
        "Journal of Strategic Studies",
        "Survival",
        "International Security",
        "Security Studies",
        "Strategic Studies Quarterly",
        "The Washington Quarterly",
    ),
    units_and_formulas_notes=(
        "军力对比用数量与比例；时间用年份",
        "公式用 amsmath；威慑与博弈模型计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "定性判断须给出证据来源与置信度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "报告"),
    tools=(
        "情景模拟软件（MATLAB/Python）",
        "GIS 空间分析（ArcGIS）",
        "兵棋推演平台",
        "SPSS 统计分析",
    ),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)