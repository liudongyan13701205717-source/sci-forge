"""计算机系统设计学科论文支持：系统设计、架构与集成体裁、IEEE 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_systems_design",
    aliases=(
        "computer systems design", "计算机系统设计", "系统设计",
        "system design", "软件架构", "software architecture",
        "分布式系统设计", "distributed systems design",
        "system architecture", "系统架构",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "design（架构与关键设计决策）",
            "implementation（关键实现细节）",
            "evaluation（性能/正确性/可扩展性）",
            "conclusion",
            "references",
        ),
        "system": (
            "abstract",
            "overview",
            "design principles",
            "architecture",
            "implementation",
            "evaluation",
            "references",
        ),
        "workshop": (
            "abstract",
            "design challenges",
            "our design",
            "experiments",
            "lessons learned",
            "references",
        ),
    },
    citation_style="IEEE 样式（ACM SIGOPS / USENIX / EuroSys 惯例）",
    reporting_standards={
        "performance": "性能评估遵循操作系统社区报告规范",
        "correctness": "正确性论证须包含形式化或实证证据",
        "scalability": "可扩展性评估须包含并发规模与容量测试",
    },
    conventions=(
        "架构图须显式区分信任边界、数据面与控制面",
        "关键设计决策须给出备选方案与取舍分析",
        "性能报告须给出硬件/软件环境、并发规模、样本量与置信区间",
        "术语表首次出现即给出缩写；避免同一术语多写法",
    ),
    key_venues=(
        "SOSP",
        "OSDI",
        "EuroSys",
        "FAST",
        "USENIX ATC",
        "ACM SIGMOD",
        "ACM Transactions on Computer Systems (TOCS)",
        "IEEE Transactions on Computers",
    ),
    units_and_formulas_notes=(
        "延迟用 ms/μs/ns 并给出 p50/p99 双分位",
        "吞吐用 ops/s 或 MB/s 并给出饱和点",
        "公式用 amsmath；复杂度须给出 Big-O 分析",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Google Sketch", "draw.io / diagrams.net", "Microsoft Visio", "Lucidchart", "Miro", "PlantUML", "Mermaid", "Rust", "Go", "C++", "Apache Kafka", "Apache Pulsar", "Redis", "etcd", "TiDB", "PostgreSQL", "Kubernetes", "Grafana", "Prometheus", "Consul"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore", "ACM DL"),
)
