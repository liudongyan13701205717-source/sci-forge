"""云计算学科论文支持：服务模型/部署模型体裁、ACM 引用样式与资源度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cloud_computing",
    aliases=("cloud_computing", "云计算", "云原生", "serverless"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "system design（系统设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "systems_paper": (
            "abstract",
            "introduction",
            "background（背景：服务模型与部署模型）",
            "architecture（架构）",
            "implementation（实现）",
            "evaluation（评估与对比）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；SOCC/ICDCS 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循云计算系统评估规范",
        "benchmark": "基准测试遵循标准负载报告规范",
        "cost_analysis": "成本分析遵循云计费模型报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循云实验可复现性清单",
    },
    conventions=(
        "服务模型（IaaS/PaaS/SaaS/FaaS）与部署模型须明确",
        "工作负载与流量模型须报告",
        "资源度量（CPU/内存/网络/存储）定义须一致",
        "成本与性能须同时报告",
        "对比系统须公平（同负载同配置）",
    ),
    key_venues=(
        "ACM Symposium on Cloud Computing (SoCC)",
        "IEEE International Conference on Cloud Computing (CLOUD)",
        "IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGrid)",
        "IEEE Transactions on Cloud Computing",
        "ACM Transactions on Computer Systems",
        "USENIX OSDI/NSDI（云系统方向）",
    ),
    units_and_formulas_notes=(
        "延迟用 ms；吞吐用 req/s；带宽用 Gbps",
        "成本用 $/小时或 $/百万请求，注明计费模型",
        "公式用 amsmath；SLA 与可用性公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "资源利用率用百分比（%）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Docker", "Kubernetes", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)