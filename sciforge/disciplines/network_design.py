"""网络设计学科论文支持：网络架构/拓扑/规划体裁、IEEE/CCS 样式与网络设计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="network_design",
    aliases=("network_design", "网络设计", "network architecture", "network planning",
             "网络工程", "IT architecture", "组网设计", "网络拓扑", "network topology"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与网络设计问题）", "methodology（拓扑与仿真方法）", "results（性能与容量数据）", "discussion（设计启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（场景/园区/骨干案例背景）", "analysis（拓扑与选型分析）", "results（实施与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（架构与标准综述）", "evidence synthesis（拓扑与实现证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式或 ACM CCS 样式",
    reporting_standards={
        "design": "网络设计须遵循 RFC/IANA 与拓扑报告规范",
        "simulation": "仿真须遵循 ns-3/Mininet 报告规范并给出参数与置信区间",
        "implementation": "实施须遵循变更管理与回滚方案规范",
    },
    conventions=(
        "拓扑与分层（接入/汇聚/核心）须图示并给出设备型号",
        "地址与 VLAN 规划须给出与来源",
        "链路带宽与延迟按口径给出并说明测量点",
        "QoS/冗余/HA 策略须完整说明",
        "网络设备型号与版本首次给出全称与厂商",
    ),
    key_venues=(
        "IEEE Transactions on Network and Service Management",
        "IEEE Communications Magazine",
        "ACM SIGCOMM Computer Communication Review",
        "Journal of Network and Computer Applications",
        "Computer Networks",
    ),
    units_and_formulas_notes=(
        "带宽用 Gbps/Mbps、时延用 ms、距离用 km",
        "公式用 amsmath；容量、时延与吞吐计算式须完整",
        "仿真给出拓扑规模、流量模型与运行次数",
        "结果给出均值 ± SD 或 P50/P95/P99 分位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Visio", "AutoCAD", "Cisco Packet Tracer", "GNS3", "EVE-NG", "Draw.io", "Lucidchart", "NetBox", "Cisco IOS", "Juniper Junos", "VMware vSphere", "Cisco Meraki", "F5 BIG-IP", "Palo Alto Networks", "Fortinet FortiOS", "Cisco DCNM", "Cisco UCS Director", "SolarWinds IPAM", "NetView", "Network Diagram Creator"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
