"""数据库与网络设计与管理学科论文支持：DB/网络设计与运维体裁、ACM 样式与工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="database_and_network_design_and_administration",
    aliases=(
        "database_and_network_design_and_administration", "数据库与网络设计与管理",
        "database and network administration", "数据库网络管理",
        "IT 系统管理", "IT systems administration", "系统运维",
        "IT operations", "DevOps", "DBA 与网络工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与管理问题）",
            "design（架构/DB 模式/网络设计）",
            "implementation（实现与部署）",
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
        "experimental": "实验遵循系统论文评估规范",
        "benchmark": "基准测试遵循 TPC 报告规范",
        "reproducibility": "可复现性遵循系统论文可复现性清单",
        "case_study": "案例研究遵循系统案例报告规范",
    },
    conventions=(
        "需求（功能/非功能/约束）须完整列出",
        "架构图、网络拓扑、数据模型须编号并在正文引用",
        "性能指标（吞吐、延迟、可用性、可扩展性）须报告",
        "对比基线须公平（同硬件、同参数）",
        "所有管理决策须说明理由与替代方案",
    ),
    key_venues=(
        "IEEE Transactions on Network and Service Management",
        "IEEE Transactions on Knowledge and Data Engineering",
        "ACM Transactions on Database Systems",
        "The VLDB Journal",
        "IEEE Network",
        "Journal of Network and Computer Applications",
        "IEEE Transactions on Services Computing",
    ),
    units_and_formulas_notes=(
        "带宽用 Gbps；延迟用 ms；吞吐量用 tps 或 pps",
        "数据量用 GB/TB；内存用 GB",
        "公式用 amsmath；架构与算法须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PostgreSQL", "MySQL", "MariaDB", "Oracle Database", "Microsoft SQL Server", "MongoDB", "Redis", "DuckDB", "DBeaver", "pgAdmin", "MySQL Workbench", "Cisco Packet Tracer", "GNS3", "EVE-NG", "Wireshark", "Nmap", "Zenmap", "SolarWinds NPM", "Cisco DNA Center", "Juniper Mist", "Terraform", "Ansible", "Kubernetes", "Docker", "Prometheus", "Grafana", "Datadog", "Lucidchart", "draw.io (diagrams.net)", "Visio", "Fiddler", "MTR"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
