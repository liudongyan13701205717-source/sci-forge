"""通信工程学科论文支持：通信原理/信号处理/无线网络体裁、IEEE 引用样式与通信记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications_engineering",
    aliases=("communications engineering", "通信工程", "通信原理", "信号处理",
             "无线网络", "移动通信", "wireless communications",
             "signal processing", "telecommunications engineering"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与通信问题）",
            "system model（系统模型与假设）",
            "methods（方案设计与理论分析）",
            "results（性能仿真与实测）",
            "conclusions",
            "references",
        ),
        "protocol_design": (
            "abstract",
            "introduction",
            "protocol design（协议设计）",
            "analysis（理论分析）",
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
        "standardization": "标准化研究遵循 ITU/3GPP 规范引用",
    },
    conventions=(
        "信道模型与参数（衰落、路径损耗、多普勒频移）须明确说明",
        "调制/编码方案须标注标准版本号与参数配置",
        "仿真场景须可复现：给出拓扑、流量模型与随机种子",
        "性能指标（吞吐、时延、误码率、频谱效率）须定义一致",
        "标准引用（3GPP、ITU、IEEE）须给出版本号与条款号",
    ),
    key_venues=(
        "IEEE Transactions on Communications",
        "IEEE Transactions on Wireless Communications",
        "IEEE Communications Magazine",
        "IEEE/ACM Transactions on Networking",
        "Computer Networks",
        "IEEE Journal on Selected Areas in Communications",
        "IEEE Transactions on Signal Processing",
    ),
    units_and_formulas_notes=(
        "速率用 bps/kbps/Mbps/Gbps；带宽用 Hz/kHz/MHz/GHz",
        "信噪比用 dB；增益用 dBi；功率用 mW/dBm",
        "公式用 amsmath；Shannon 容量公式须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "误码率/误帧率给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "GNU Radio", "NS-3", "OPNET Modeler", "CST Studio Suite", "ANSYS HFSS", "COMSOL Multiphysics", "Python", "Wireshark", "QEMU", "GNS3", "EVE-NG", "Cisco Packet Tracer", "GNU Octave", "Julia", "C++", "Qt", "QNX", "Scapy", "Mininet", "OMNeT++", "QualNet", "Keysight ADS", "NI LabVIEW"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)
