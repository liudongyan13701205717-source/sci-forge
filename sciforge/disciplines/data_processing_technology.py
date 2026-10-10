"""Data processing technology 学科论文支持：ETL/流处理/数据管道体裁、ACM 样式与工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_processing_technology",
    aliases=(
        "data_processing_technology", "数据处理技术", "数据管道", "data pipeline",
        "ETL", "数据集成", "data integration", "批处理", "流处理",
        "big data engineering", "大数据工程", "stream processing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "design（系统/管道设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "architecture（架构）",
            "pipeline（数据处理管道）",
            "deployment（部署）",
            "evaluation（评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份）",
    reporting_standards={
        "experimental": "实验遵循数据处理系统评估规范",
        "benchmark": "基准测试遵循 TPC 报告规范",
        "reproducibility": "可复现性遵循系统论文可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "数据集与工作负载须报告（数据规模、模式、更新频率）",
        "处理延迟、吞吐量、端到端时延须报告（ms/s、tps、行/秒）",
        "管道组件与依赖版本须明确",
        "对比基线须公平（同硬件、同参数）",
        "扩展性实验须报告节点数与数据规模关系",
    ),
    key_venues=(
        "IEEE Transactions on Knowledge and Data Engineering",
        "IEEE Transactions on Big Data",
        "ACM Transactions on Database Systems",
        "The VLDB Journal",
        "Big Data and Cognitive Computing",
        "Data & Knowledge Engineering",
        "IEEE Transactions on Parallel and Distributed Systems",
    ),
    units_and_formulas_notes=(
        "吞吐量用 行/秒 或 事件/秒；延迟用 ms",
        "内存用 GB/TB；数据量用 GB/TB",
        "公式用 amsmath；管道与算法须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Apache Spark", "Apache Flink", "Apache Kafka", "Apache Storm", "Apache Hadoop (MapReduce)", "Apache NiFi", "Apache Airflow", "Apache Beam", "Apache Kafka Streams", "Apache Cassandra", "Apache Hive", "Apache Impala", "Apache Druid", "Apache Pinot", "Apache Kafka Connect", "dbt (Data Build Tool)", "Talend Data Integration", "Informatica PowerCenter", "Microsoft SSIS", "Alteryx Designer", "Oracle Data Integrator", "Fivetran", "Airbyte", "Meltano", "Dagster", "Prefect", "Ceph", "HDFS", "Glue (AWS)", "Dataproc (Google)", "Databricks"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
