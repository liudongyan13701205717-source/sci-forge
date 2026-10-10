"""网络科学学科论文支持：复杂网络/图分析体裁、APA 引用样式与网络科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="network_science",
    aliases=("network_science", "网络科学", "复杂网络", "图网络分析", "network analysis",
             "complex networks", "graph theory", "网络分析", "复杂系统"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与网络问题）", "methodology（网络构建与指标）", "results（拓扑与动力学数据）", "discussion（结构与功能）", "references"),
        "empirical_study": ("abstract", "introduction", "case description（数据来源与网络构建）", "analysis（网络指标分析）", "results（与理论对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（模型与理论综述）", "evidence synthesis（实证与仿真证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Network Science 遵循 APA 规范）",
    reporting_standards={
        "empirical": "实证研究须遵循数据来源与网络构建报告规范",
        "computational": "计算模型须遵循模型设定与零模型报告规范",
        "systematic_review": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "网络构建与边定义须明确（有向/无权/加权/时间）",
        "网络指标（度、介数、聚类系数、路径长度）须给出定义",
        "零模型与显著性检验须报告（配置模型、重接模型）",
        "数据来源与预处理须注明并说明节点/边数量",
        "社区划分与聚类比须给出算法、迭代数与稳定性",
    ),
    key_venues=(
        "Network Science",
        "Journal of Complex Networks",
        "Physical Review E",
        "Applied Network Science",
        "Social Networks",
    ),
    units_and_formulas_notes=(
        "度、聚类系数、路径长度无量纲；边权用原始单位",
        "公式用 amsmath；中心性、聚类系数与路径计算式须完整",
        "显著性给出 p 值与零模型区间并说明分布假设",
        "仿真给出网络规模、迭代数与随机种子",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("NetworkX", "igraph", "Gephi", "Cytoscape", "Neo4j", "NetworkD3", "networkit", "GraphX", "NetworkAnalyst", "JGraphT", "Graph-tool", "SNAP", "Networkx-SDG", "Networkx-ML", "Netplot", "sna (R)", "igraph (R)", "igraph (Python)", "igraph (C)", "Networkx Community Detection"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
