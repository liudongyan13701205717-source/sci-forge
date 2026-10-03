"""软件工程学科论文支持：软件方法/实证/工具体裁、ACM/IEEE 引用样式与软件记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_engineering",
    aliases=("software_engineering", "软件工程", "软件", "软件方法",
             "软件测试", "软件架构"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与研究问题）",
            "related work（相关工作）",
            "approach（方法/框架设计）",
            "evaluation（实验与评估）",
            "discussion（局限与启示）",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "research questions（研究问题）",
            "study design（研究对象与流程）",
            "data collection（数据收集）",
            "results（结果与统计）",
            "threats to validity（有效性威胁）",
            "references",
        ),
        "tool_paper": (
            "abstract",
            "introduction",
            "tool design（工具设计与实现）",
            "usage scenario（使用场景）",
            "evaluation（评估）",
            "availability（可用性）",
            "references",
        ),
    },
    citation_style="ACM/IEEE 样式（作者-年份或编号制；按目标会议/期刊规范）",
    reporting_standards={
        "empirical_study": "实证研究遵循 ACM SIGSOFT 实证标准（Empirical Standards）",
        "systematic_review": "系统综述遵循 PRISMA 声明（软件工程适配版）",
        "controlled_experiment": "受控实验遵循 ACM SIGSOFT 实证标准",
        "case_study": "案例研究遵循 ACM SIGSOFT 实证标准",
        "replication": "复现研究遵循 ACM SIGSOFT 实证标准",
    },
    conventions=(
        "研究问题（RQ）须显式列出并可验证",
        "数据集/代码仓库须给出可复现链接",
        "统计检验与效应量须报告",
        "有效性威胁（内部/外部/构造/结论）须讨论",
        "工具/方法命名须与既有文献一致",
    ),
    key_venues=(
        "IEEE Transactions on Software Engineering",
        "ACM Transactions on Software Engineering and Methodology",
        "Empirical Software Engineering",
        "Journal of Systems and Software",
        "ICSE (International Conference on Software Engineering)",
        "FSE (ACM International Conference on the Foundations of Software Engineering)",
    ),
    units_and_formulas_notes=(
        "性能指标用 ms/s；吞吐用 ops/s",
        "公式用 amsmath；算法伪代码用 algorithm 环境",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "统计显著性给出 p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Git", "GitHub Actions", "Jenkins", "IDE（IntelliJ IDEA / VS Code）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "Semantic Scholar", "CNKI"),
)