"""软件与应用开发及分析学科论文支持：需求建模/实证分析体裁、ACM 引用样式与度量口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_and_applications_development_and_analysis",
    aliases=("software_and_applications_development_and_analysis", "软件与应用开发分析", "应用开发分析", "软件需求工程", "软件开发度量", "软件分析"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="ACM 样式（作者-年份或数字制；按目标会议/期刊规范）",
    reporting_standards={
        "empirical_study": "实证研究遵循 ACM SIGSOFT 实证标准（Empirical Standards）",
        "metrics": "度量须给出计算定义、口径与数据源版本",
        "systematic_review": "系统综述遵循 PRISMA 声明（软件工程适配版）",
    },
    conventions=(
        "研究问题（RQ）须显式列出并可验证",
        "需求追溯矩阵须覆盖需求-设计-测试全链",
        "统计检验与效应量须报告",
        "有效性威胁（内部/外部/构造/结论）须讨论",
        "代码仓库与样本筛选规则须可复现",
    ),
    key_venues=(
        "Requirements Engineering",
        "Journal of Software: Evolution and Process",
        "Journal of Software: Engineering and Research",
        "IEEE Transactions on Services Computing",
        "Software Metrics Journal",
    ),
    units_and_formulas_notes=(
        "性能指标用 ms/s；吞吐用 ops/s",
        "圈复杂度、认知复杂度等度量注明工具版本与阈值",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Git", "Bitbucket", "Cursor", "Code::Blocks", "PyCharm", "Eclipse", "Codacy", "Cloc", "Understand", "Doxygen", "JupyterLab", "R", "Python", "Plotly", "Bokeh", "Lizard", "radon", "GitLab", "Apache Airflow", "DBeaver"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
