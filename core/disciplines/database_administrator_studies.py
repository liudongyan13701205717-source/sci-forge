"""数据库管理员研究学科论文支持：DBA/运维/性能调优体裁、ACM 样式与 DBA 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="database_administrator_studies",
    aliases=(
        "database_administrator_studies", "数据库管理员研究",
        "database administration", "数据库管理", "DBA", "数据库运维",
        "database operations", "DBOps", "数据库工程",
        "database engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与 DBA 问题）",
            "design（管理方案/自动化设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "architecture（架构）",
            "operations（运维流程）",
            "deployment（部署）",
            "evaluation（评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份）",
    reporting_standards={
        "experimental": "实验遵循数据库论文评估规范",
        "benchmark": "基准测试遵循 TPC 报告规范",
        "reproducibility": "可复现性遵循系统论文可复现性清单",
        "case_study": "案例研究遵循系统案例报告规范",
    },
    conventions=(
        "数据集与工作负载须报告（数据规模、访问模式）",
        "性能指标（QPS/TPS、延迟、可用性 SLA）须报告",
        "配置参数（连接数、缓存大小、执行引擎）须明确",
        "对比基线须公平（同硬件、同参数）",
        "扩展性实验须报告节点数与数据规模关系",
    ),
    key_venues=(
        "SIGMOD",
        "VLDB",
        "ICDE",
        "ACM Transactions on Database Systems",
        "The VLDB Journal",
        "IEEE Transactions on Knowledge and Data Engineering",
        "IEEE Transactions on Services Computing",
    ),
    units_and_formulas_notes=(
        "吞吐量用 tps；延迟用 ms；数据量用 GB/TB",
        "公式用 amsmath；算法须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PostgreSQL", "MySQL", "MariaDB", "Oracle Database", "Microsoft SQL Server", "SQLite", "MongoDB", "Redis", "Cassandra", "CockroachDB", "TimescaleDB", "DuckDB", "Neo4j", "InfluxDB", "ClickHouse", "Apache HBase", "Amazon RDS", "Amazon Aurora", "Google Cloud SQL", "Microsoft Azure SQL", "MongoDB Atlas", "Elasticsearch", "Apache Kafka (KRaft)", "pgAdmin", "DBeaver", "MySQL Workbench", "SQLyog", "Toad", "pgTAP", "pg_stat_statements", "Prometheus", "Grafana", "Ansible"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
