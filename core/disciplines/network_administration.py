"""网络管理学科论文支持：运维/监控/配置管理体裁、IEEE/CCS 样式与运维记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="network_administration",
    aliases=("network_administration", "网络管理", "network operations", "network ops",
             "网络运维", "网络监控", "IT operations", "netops", "网络运维管理"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与运维问题）", "methodology（管理与监控方法）", "results（运维指标与数据）", "discussion（工程启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（运维事故/场景案例背景）", "analysis（故障与响应分析）", "results（改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（运维理论与技术综述）", "evidence synthesis（平台与场景证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式或 ACM CCS 样式",
    reporting_standards={
        "incident": "运维事故报告须遵循 ITIL/ITSM 事件管理声明",
        "monitoring": "监控数据须遵循采集口径、时间对齐与告警阈值报告规范",
        "automation": "自动化运维须报告脚本版本、回滚方案与灰度范围",
    },
    conventions=(
        "指标口径（可用性、时延、丢包率、MTTR）须定义并给出计算式",
        "告警阈值与告警抑制策略须明确",
        "配置项与资产编号须可追溯",
        "变更须遵循变更管理流程与回滚方案",
        "运维术语（CMDB、ITIL、NOC 等）首次给出全称",
    ),
    key_venues=(
        "IEEE Transactions on Network and Service Management",
        "IEEE Communications Magazine",
        "ACM SIGCOMM Computer Communication Review",
        "Journal of Network and Computer Applications",
        "IEEE Network",
    ),
    units_and_formulas_notes=(
        "时延用 ms、丢包率用 %、吞吐量用 bps、可用性用 %",
        "公式用 amsmath；可用性、时延与吞吐计算式须完整",
        "结果给出均值 ± SD 或 P50/P95/P99 分位",
        "显著性给出 p 值与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SolarWinds NPM", "Nagios", "Zabbix", "PRTG", "NetBox", "Wireshark", "Nmap", "Ansible", "Puppet", "Chef", "Grafana", "Prometheus", "ELK Stack", "Splunk", "OpenNMS", "Cisco DNA Center", "Cisco Prime", "ManageEngine", "iReason", "SolarWinds IPAM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
