"""环境伦理学科论文支持：环境伦理/生态伦理体裁、Chicago 引用样式与环境伦理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_ethics",
    aliases=("environmental_ethics", "环境伦理", "生态伦理", "环境哲学", "environmental ethics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与环境伦理问题）",
            "methods（研究设计与分析）",
            "results（伦理分析数据）",
            "discussion（伦理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（环境案例）",
            "analysis（伦理问题分析）",
            "conclusions（伦理启示）",
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
    citation_style="Chicago 样式（作者-年份；Environ Ethics 遵循 Chicago 规范）",
    reporting_standards={
        "case_study": "案例研究遵循案例研究报告规范",
        "theoretical": "理论论证遵循哲学论证报告规范",
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "discourse": "话语分析遵循话语分析报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "伦理框架（内在价值、代际正义等）须定义",
        "生态与科学背景须交代",
        "价值判断与事实陈述须区分",
        "文化与传统视角须考虑",
        "政策建议与伦理论证须衔接",
    ),
    key_venues=(
        "Environmental Ethics",
        "Environmental Values",
        "Ethics & the Environment",
        "Journal of Agricultural and Environmental Ethics",
        "Environmental Philosophy",
        "Ethics, Policy & Environment",
    ),
    units_and_formulas_notes=(
        "比例用 %；指标无量纲",
        "公式用 amsmath；评估指标计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "定性判断须给出证据来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("GIS 空间分析软件（QGIS）", "政策文本分析（NVivo）", "生命周期评价（LCA）工具"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "arXiv", "Zenodo", "CNKI"),
)