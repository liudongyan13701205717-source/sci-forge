"""网络安全学科论文支持：网络攻防、安全架构与威胁分析研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cybersecurity",
    aliases=(
        "cybersecurity", "网络安全", "信息安全",
        "information security", "信息安全",
        "network security", "网络安全",
        "cyber defense", "网络防御",
        "threat analysis", "威胁分析",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（安全问题与背景）",
            "methodology（攻击模型、防御方案、测试）",
            "results（安全效果与性能评估）",
            "discussion（安全改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "attack analysis（攻击分析）",
            "defense strategy（防御策略）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "threat landscape（威胁态势）",
            "defense comparison（防御对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "vulnerability": "漏洞须注明 CVE 编号与 CVSS 评分",
        "attack": "攻击方法须完整描述",
        "testing": "测试环境须注明（硬件、软件、网络）",
    },
    conventions=(
        "IP 地址用 IPv4/IPv6 格式表示",
        "端口用 数字 表示",
        "加密算法须注明密钥长度",
        "攻击成功率用 % 表示",
        "检测率用 % 表示",
    ),
    key_venues=(
        "IEEE Transactions on Information Forensics and Security",
        "ACM Transactions on Information and System Security",
        "Journal of Cybersecurity",
        "Computers & Security",
        "IEEE Security & Privacy",
        "USENIX Security Symposium",
    ),
    units_and_formulas_notes=(
        "IP 地址用 IPv4/IPv6 格式表示",
        "端口用 数字 表示",
        "加密算法须注明密钥长度",
        "攻击成功率用 % 表示",
        "检测率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Wireshark", "Nmap", "Metasploit", "Burp Suite", "OWASP ZAP", "Kali Linux", "Snort", "Suricata", "Bro/Zeek", "Splunk", "ELK Stack", "OSSEC", "Nessus", "OpenVAS", "John the Ripper", "Hashcat", "Ghidra", "IDA Pro", "Volatility", "Cobalt Strike"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ACM Digital Library"),
)
