"""电子数据处理学科论文支持：数据处理、数据库与信息系统研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronic_data_processing",
    aliases=(
        "electronic_data_processing", "电子数据处理", "数据处理",
        "electronic data processing", "电子数据处理",
        "data processing", "数据处理",
        "database systems", "数据库系统",
        "information systems", "信息系统",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（数据处理问题与背景）",
            "methodology（处理算法、系统设计、测试）",
            "results（处理效果与性能评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "implementation（实现过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "algorithm": "算法须完整描述（输入、输出、复杂度）",
        "testing": "测试环境须注明（硬件、软件、数据）",
        "performance": "性能指标须定义（吞吐量、延迟、准确率）",
    },
    conventions=(
        "数据量用 GB 或 TB 表示",
        "处理时间用 ms 或 s 表示",
        "准确率用 % 表示",
        "召回率用 % 表示",
        "F1 值用 0-1 范围表示",
    ),
    key_venues=(
        "IEEE Transactions on Knowledge and Data Engineering",
        "ACM Transactions on Database Systems",
        "Journal of Data and Information Quality",
        "Data & Knowledge Engineering",
        "Information Systems",
        "Journal of Big Data",
    ),
    units_and_formulas_notes=(
        "数据量用 GB 或 TB 表示",
        "处理时间用 ms 或 s 表示",
        "准确率与召回率用 % 表示",
        "F1 值用 0-1 范围表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python (pandas, numpy)", "R (RStudio)", "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Elasticsearch", "Apache Spark", "Hadoop", "Kafka", "Flink", "TensorFlow", "PyTorch", "scikit-learn", "NLTK", "spaCy", "Tableau", "Power BI", "Apache Airflow"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ACM Digital Library"),
)
