"""计算机网络安装与维护学科论文支持：网络设备部署/综合布线/网络运维体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_network_installation_and",
    aliases=("network installation and maintenance", "网络安装与维护",
             "网络布线", "cabling", "structured cabling", "综合布线",
             "网络部署", "network deployment", "network technician",
             "网络工程与维护"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method/design",
            "deployment and evaluation",
            "results",
            "conclusion",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "topology and design",
            "implementation",
            "evaluation",
            "operations notes",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="IEEE 编号样式",
    reporting_standards={
        "experimental": "测试须报告链路类型、速率、测试仪器与标准（TIA/EIA、ISO 11801）",
        "deployment": "部署须说明拓扑、布线、供电与标签规范",
        "benchmark": "带宽/延迟须按标准负载报告",
        "reproducibility": "配置与拓扑须公开",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "链路标准（Cat5e/Cat6/单模/多模）与距离限制须标注",
        "拓扑图须标明设备型号、端口与 VLAN",
        "测试报告须附测试仪器型号与校准信息",
        "延迟/带宽对比须在同负载下进行",
        "结论须区分设计改进与部署效果",
    ),
    key_venues=(
        "IEEE Network",
        "IEEE Communications Magazine",
        "Computer Networks",
        "IEEE International Conference on Communications (ICC)",
        "IEEE Global Communications Conference (GLOBECOM)",
        "IEEE Internet of Things Journal",
        "Journal of Network and Computer Applications",
        "Computer & Communications",
    ),
    units_and_formulas_notes=(
        "带宽用 Mbps/Gbps；延迟用 ms；丢包率用 %",
        "线缆长度用 m；信噪比用 dB",
        "吞吐量用 GB/s",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cisco Packet Tracer", "GNS3", "Pandatel", "Huawei eNSP", "Wireshark", "tcpdump", "Nmap", "SolarWinds Network Performance Monitor", "SolarWinds NCM", "Nagios", "Zabbix", "OpenNMS", "Cacti", "LibreNMS", "PRTG", "NetSpot", "inSSIDer", "Fluke DSX", "Keysight DTX", "Cisco ISE", "Ruckus Cloud", "Cisco DNA Center", "BMC Helix", "Fibre Optic Cleaning System", "RJ45 Punchdown Tool", "Fiber Optic Splicer", "SMA Connector Crimping Tool"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
