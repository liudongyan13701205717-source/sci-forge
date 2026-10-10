"""电信技术学科论文支持：网络工程与运维实践的体裁、IEEE 引用样式与网络记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="telecommunication_technology",
    aliases=(
        "telecommunication_technology",
        "电信技术",
        "网络工程",
        "网络运维",
        "通信技术应用",
        "telecom engineering",
        "network engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程问题）",
            "network design（网络架构与设备选型）",
            "implementation（部署与配置）",
            "results（性能与可靠性实测）",
            "conclusions",
            "references",
        ),
        "technical_report": (
            "abstract",
            "introduction",
            "requirement analysis（需求与约束）",
            "solution（方案与配置清单）",
            "testing（测试与验收结果）",
            "operation plan（运维方案）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "evidence synthesis（技术路线比较）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；厂商与标准文档按版本引用）",
    reporting_standards={
        "design": "网络设计遵循 ITU-T 与 3GPP 相关规范的引用格式",
        "testing": "验收测试遵循 Telcordia GR-1089 可用性测试方法",
        "reliability": "可用性须按 Telcordia SR-332 公式计算",
        "security": "安全配置须引用 IETF RFC 编号与版本号",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "拓扑图须标注节点角色、链路带宽与 IP/VLAN 规划",
        "设备型号与固件/IOS 版本须完整列出",
        "配置片段须脱敏（隐藏真实口令与敏感地址）",
        "性能指标（时延、抖动、丢包率、可用性）须定义测量方法与窗口",
        "命令与输出须区分厂商语法（Cisco IOS、Juniper Junos、Huawei VRP）"
    ),
    key_venues=(
        "IEEE Network",
        "IEEE Communications Magazine",
        "Computer Networks",
        "IEEE/ACM Transactions on Networking",
        "Journal of Network and Computer Applications",
    ),
    units_and_formulas_notes=(
        "速率用 bps/Mbps/Gbps；时延用 ms，抖动用 ms",
        "可用性用百分比并给出计算公式与统计窗口",
        "公式用 amsmath；可用性与时延预算公式须编号并被引用",
        "实测结果给出均值 ± 置信区间与采样点数量"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cisco Packet Tracer", "GNS3", "EVE-NG", "Huawei eNSP", "Wireshark", "iPerf", "Nmap", "Zabbix", "Nagios", "SolarWinds NPM", "PRTG", "Cisco DNA Center", "Ansible", "Terraform", "PuTTY", "MobaXterm", "NetBox", "LibreNMS", "Prometheus", "Grafana"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
