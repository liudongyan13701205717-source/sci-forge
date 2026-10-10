"""分布式计算与系统软件学科论文支持：并行计算、分布式系统与软件架构体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="distributed_computing_and_systems_software",
    aliases=(
        "distributed_computing_and_systems_software", "分布式计算与系统软件",
        "distributed computing", "分布式计算",
        "parallel computing", "并行计算",
        "distributed systems", "分布式系统",
        "systems software", "系统软件",
        "concurrent programming", "并发编程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（系统问题与背景）",
            "methodology（系统设计、实现与测试）",
            "results（性能评估与可扩展性）",
            "discussion（优化方向与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "system description（系统描述）",
            "implementation（实现细节）",
            "evaluation（效果评估）",
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
        "implementation": "技术栈须明确（语言、框架、版本）",
        "testing": "测试方案须注明测试类型与环境",
        "performance": "性能指标须定义（吞吐量、延迟、可扩展性）",
    },
    conventions=(
        "代码遵循项目编码规范",
        "版本控制遵循 Git 工作流",
        "API 文档遵循 OpenAPI/Swagger 规范",
        "性能测试须注明硬件配置与网络环境",
        "可扩展性测试须报告节点数与负载",
    ),
    key_venues=(
        "ACM Computing Surveys",
        "IEEE Transactions on Parallel and Distributed Systems",
        "Journal of Parallel and Distributed Computing",
        "ACM Transactions on Computer Systems",
        "IEEE Transactions on Computers",
        "Cluster Computing",
    ),
    units_and_formulas_notes=(
        "吞吐量用 ops/s 或 requests/s 表示",
        "延迟用 ms 表示",
        "带宽用 Gbps 表示",
        "可扩展性用加速比或效率表示",
        "测试覆盖率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Git", "GitHub", "Visual Studio Code", "Eclipse", "IntelliJ IDEA", "PyCharm", "MATLAB", "Python (pandas, numpy)", "R (RStudio)", "SPSS", "Jupyter Notebook", "Anaconda", "Docker", "Kubernetes", "Mesos", "Apache Spark", "Hadoop", "MapReduce", "MPI", "OpenMPI"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ACM Digital Library"),
)
