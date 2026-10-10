"""通信系统学科论文支持：系统架构/协议设计/QoS管理体裁、IEEE 引用样式与系统记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications_systems",
    aliases=("communications systems", "通信系统", "通信网络",
             "网络架构", "协议设计", "communication networks",
             "network architecture", "protocol design",
             "telecommunication systems"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与系统问题）",
            "system architecture（系统架构与接口）",
            "methods（方案设计与分析）",
            "results（性能仿真与验证）",
            "conclusions",
            "references",
        ),
        "protocol_design": (
            "abstract",
            "introduction",
            "protocol design（协议设计）",
            "analysis（理论分析与复杂度）",
            "simulation/implementation（仿真/实现）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；IEEE 期刊遵循 IEEE 规范）",
    reporting_standards={
        "experimental": "实验研究遵循 IEEE 实验报告规范",
        "simulation": "仿真研究遵循 IEEE 仿真报告规范",
        "field_trial": "外场试验遵循 ITU 试验报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "standardization": "标准化研究遵循 ITU/3GPP/IEEE 规范引用",
    },
    conventions=(
        "系统架构须给出完整框图与接口定义",
        "协议栈须标注各层功能与标准版本号",
        "QoS 参数须定义服务质量指标与测量方法",
        "安全机制须说明威胁模型与防护策略",
        "性能指标须定义一致（吞吐、时延、丢包率、可靠性）",
    ),
    key_venues=(
        "IEEE Transactions on Communications",
        "IEEE Communications Magazine",
        "IEEE/ACM Transactions on Networking",
        "Computer Networks",
        "IEEE Network",
        "IEEE Journal on Selected Areas in Communications",
        "IEEE Transactions on Network and Service Management",
    ),
    units_and_formulas_notes=(
        "速率用 bps/kbps/Mbps/Gbps；带宽用 Hz/MHz/GHz",
        "时延用 ms/s；丢包率用 % 或 ppm",
        "吞吐量用 Gbps/Tbps；频谱效率用 bits/s/Hz",
        "公式用 amsmath；容量公式与链路预算须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "GNU Radio", "NS-3", "OPNET Modeler", "Wireshark", "GNS3", "EVE-NG", "Cisco Packet Tracer", "QEMU", "Python", "Scapy", "Mininet", "OMNeT++", "NS-2", "QualNet", "iFOS", "J-SIM", "CastNet", "VMware NSX", "Network Simulator", "CockroachDB", "Prometheus", "Grafana", "Kubernetes", "Docker"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)
