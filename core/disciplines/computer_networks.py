"""计算机网络学科论文支持：网络协议/架构体裁、ACM 引用样式与网络记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_networks",
    aliases=("computer_networks", "计算机网络", "网络", "网络协议"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "design（协议/架构设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "protocol_paper": (
            "abstract",
            "introduction",
            "protocol design（协议设计）",
            "analysis（分析）",
            "simulation（仿真）",
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
    citation_style="ACM 样式（作者-年份；SIGCOMM 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循网络论文评估规范",
        "simulation": "仿真遵循网络仿真报告规范",
        "benchmark": "基准测试遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "measurement": "测量研究遵循网络测量报告规范",
    },
    conventions=(
        "拓扑与流量模型须报告",
        "协议参数与版本须明确",
        "仿真器/测试平台须说明",
        "对比基线须公平（同负载）",
        "置信区间与统计检验须报告",
    ),
    key_venues=(
        "SIGCOMM",
        "NSDI",
        "IEEE INFOCOM",
        "IEEE/ACM Transactions on Networking",
        "Computer Networks",
        "IEEE Journal on Selected Areas in Communications",
    ),
    units_and_formulas_notes=(
        "带宽用 Mbps/Gbps；延迟用 ms；丢包率用 %",
        "公式用 amsmath；协议状态机须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "专利"),
    tools=("NS-3", "Wireshark", "MATLAB", "Mininet"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "CNKI"),
)