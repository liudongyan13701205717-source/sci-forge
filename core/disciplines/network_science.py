"""网络科学学科论文支持：网络科学/复杂网络体裁、APA 引用样式与网络科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="network_science",
    aliases=("network_science", "网络科学", "复杂网络", "图网络分析", "network analysis"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与网络问题）",
            "methods（网络构建与指标）",
            "results（拓扑与动力学数据）",
            "discussion（结构与功能）",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "data（数据来源与网络构建）",
            "analysis（网络指标分析）",
            "discussion（与理论对比）",
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
    citation_style="APA 样式（作者-年份；Network Science 遵循 APA 规范）",
    reporting_standards={
        "empirical": "实证研究遵循数据来源报告规范",
        "network_analysis": "网络分析遵循网络研究报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "simulation": "仿真研究遵循仿真实验报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "网络构建与边定义须明确",
        "网络指标（度、介数、聚类系数等）须定义",
        "零模型与显著性检验须报告",
        "数据来源与预处理须注明",
        "节点与边数量须报告",
    ),
    key_venues=(
        "Network Science",
        "Journal of Complex Networks",
        "Physical Review E",
        "Applied Network Science",
        "Social Networks",
        "EPJ Data Science",
    ),
    units_and_formulas_notes=(
        "度与路径长度无量纲；边权用原始单位",
        "公式用 amsmath；中心性与聚类系数计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与网络规模",
        "显著性给出 p 值与零模型区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=(
        "Python 图分析（NetworkX）",
        "R 图分析（igraph）",
        "Gephi 网络可视化",
        "Cytoscape 交互分析",
    ),
    category="交叉学科",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo"),
)