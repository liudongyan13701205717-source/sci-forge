"""网络技术学科论文支持：计算机网络/协议/基础设施体裁、IEEE/CCS 样式与网络技术记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="network_technology",
    aliases=("network_technology", "网络技术", "computer networks", "计算机网络",
             "网络通信", "IT infrastructure", "通信网络", "网络工程", "网络协议"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与网络技术问题）", "methodology（协议与实现方法）", "results（性能与协议数据）", "discussion（工程启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（网络事故/协议案例背景）", "analysis（协议与实现分析）", "results（改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（协议与技术综述）", "evidence synthesis（协议与实现证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式或 ACM CCS 样式",
    reporting_standards={
        "protocol": "协议研究须遵循 RFC 报告规范与互操作性测试",
        "simulation": "仿真须遵循 ns-3/Mininet 报告规范并给出参数与置信区间",
        "measurement": "网络测量须遵循采集口径、时间对齐与样本说明",
    },
    conventions=(
        "协议栈与协议版本（如 TCP/IP、IPv6、BGP）须明确",
        "链路带宽、时延、丢包率给出测量口径与测量点",
        "网络设备型号与固件版本首次给出全称与厂商",
        "实验结果给出流量模型、拓扑与运行次数",
        "术语（NAT、QoS、SDN、NFV）首次给出全称",
    ),
    key_venues=(
        "IEEE Transactions on Network and Service Management",
        "IEEE Communications Magazine",
        "ACM SIGCOMM Computer Communication Review",
        "Computer Networks",
        "IEEE Journal on Selected Areas in Communications",
    ),
    units_and_formulas_notes=(
        "带宽用 Gbps/Mbps、时延用 ms、丢包率用 %",
        "公式用 amsmath；吞吐、时延与拥塞控制计算式须完整",
        "结果给出均值 ± SD 或 P50/P95/P99 分位",
        "仿真给出拓扑规模、流量模型与随机种子",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cisco IOS", "Juniper Junos", "Fortinet FortiOS", "Palo Alto PAN-OS", "Cisco ACI", "Cisco ISE", "Cisco DNA Center", "Cisco Meraki", "VMware NSX", "VMware vSphere", "VMware vCenter", "VMware ESXi", "Wireshark", "GNS3", "Nmap", "F5 BIG-IP", "Cisco SD-Access", "Arista EOS", "Arista CloudVision", "Fortinet FortiManager"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
