"""应用计算学科论文支持：软件工程、数据工程、企业信息系统、工业应用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_computing",
    aliases=(
        "applied computing",
        "Applied Computing",
        "应用计算",
        "应用型计算机科学",
        "software engineering",
        "software engineering",
        "软件工程",
        "data engineering",
        "企业应用",
        "enterprise computing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "background and related work",
            "method (system architecture / algorithm / workflow)",
            "implementation details",
            "experiments and results",
            "discussion",
            "conclusions",
            "references",
        ),
        "systems_paper": (
            "abstract",
            "introduction",
            "motivation and challenges",
            "design and implementation",
            "evaluation",
            "deployments and case studies",
            "conclusions",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "research questions",
            "data collection",
            "analysis",
            "findings",
            "threats to validity",
            "conclusions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号）或 ACM Reference Format",
    reporting_standards={
        "reproducibility": "源代码、配置与数据集须公开（GitHub/Zenodo）并附 DOI",
        "environment": "硬件（CPU/GPU/内存）、操作系统、依赖库版本须声明",
        "metrics": "评估指标定义、基线模型、实验设置（随机种子、折数）须说明",
        "limitations": "局限性（数据偏差、模型规模、场景约束）须明确讨论",
        "license": "开源许可证（MIT/Apache/GPL）须明确",
    },
    conventions=(
        "算法伪代码按 IEEEtran 风格（Algorithm 1、Input/Output）",
        "变量名 snake_case；类/结构 PascalCase；常量 UPPER_SNAKE",
        "数据集引用带来源、年份、行数与许可；训练/验证/测试划分比说明",
        "模型参数量、训练时间、FLOPs、内存占用须报告",
        "所有结果用表格对比；改进用相对提升百分比",
    ),
    key_venues=(
        "IEEE Transactions on Software Engineering",
        "ACM Transactions on Software Engineering and Methodology",
        "Proceedings of the ACM on Programming Languages",
        "IEEE Transactions on Services Computing",
        "Journal of Systems and Software",
        "Software Engineering Notes",
    ),
    units_and_formulas_notes=(
        "时间 ms/s；内存 GB；吞吐 requests/s；准确率 % / F1 / AUC",
        "模型参数量 M/B；FLOPs TFLOPs",
        "版本控制：Git；包管理：pip/conda/npm/maven",
        "容器：Docker（基础镜像 tag 须固定）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python", "Java", "C++", "C#", "TypeScript", "Go", "Rust", "Kubernetes", "Docker", "Git", "GitHub Actions", "Jenkins", "VS Code", "IntelliJ IDEA", "PyCharm", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Apache Kafka", "Apache Spark", "TensorFlow", "PyTorch", "Jupyter", "LaTeX", "Overleaf"),
    category="工学",
    databases=("IEEE Xplore", "ACM Digital Library", "arXiv", "DBLP", "OpenAlex", "Crossref"),
)
