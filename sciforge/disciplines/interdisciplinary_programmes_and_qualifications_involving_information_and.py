"""信息与技术类跨学科项目与学位：研究、案例、综述体裁，IEEE 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_information_and",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_information_and",
        "信息与技术类跨学科项目与学位",
        "Information and Technology Interdisciplinary Programmes",
        "IT Interdisciplinary Degree",
        "ICT Degree Programme",
        "跨学科信息学位",
        "信息科学学位",
        "IT 跨学科",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="IEEE（数字编号）",
    reporting_standards={
        "k1": "DCASE（数据集与系统评价）",
        "k2": "PRISMA（系统综述）",
        "k3": "ACM 软件与工程报告规范",
    },
    conventions=(
        "实验硬件与软件版本须列出",
        "数据集与预处理流程须公开",
        "评价指标须给出基线对比",
        "训练/验证/测试划分须说明",
        "代码可复现声明须附",
    ),
    key_venues=(
        "Communications of the ACM",
        "IEEE Transactions on Knowledge and Data Engineering",
        "Information Systems Research",
        "ACM Computing Surveys",
        "Journal of the Association for Information Science and Technology",
    ),
    units_and_formulas_notes=(
        "网络带宽用 bps 而非 B/s",
        "存储容量区分 Bit 与 Byte",
        "训练数据标注规范与置信度须报告",
        "指标报告 accuracy/precision/recall/F1 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python（PyTorch）", "TensorFlow", "Jupyter Notebook", "Docker", "Kubernetes", "TensorBoard", "Weights & Biases", "MLflow", "GitLab", "GitHub Actions", "PostgreSQL", "MongoDB", "Redis", "Kafka", "Spark", "Tableau", "Power BI", "Lucidchart", "draw.io"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
