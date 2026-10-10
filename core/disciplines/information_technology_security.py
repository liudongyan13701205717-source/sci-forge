"""信息技术安全学科论文支持：网络安全/密码分析体裁、IEEE 引用样式与安全评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_technology_security",
    aliases=("information_technology_security", "信息技术安全", "信息安全", "网络与系统安全", "IT security", "cybersecurity", "渗透测试", "漏洞研究", "密码学工程", "zero trust", "security engineering"),
    paper_types={
        "research": ("abstract", "introduction（威胁背景与贡献）", "methodology（系统/实验设计）", "results（威胁发现与度量）", "discussion（缓解措施与权衡）", "references"),
        "case_study": ("abstract", "introduction", "case description（事故/系统背景）", "analysis（攻击面与根因）", "results（修复效果与残余风险）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（威胁模型与防御体系）", "evidence synthesis（漏洞与攻防证据）", "future directions", "references"),
    },
    citation_style="IEEE 样式（编号引用，如 [1]）",
    reporting_standards={"threat_model": "攻击者能力、目标与假设须明确", "reproducibility": "实验环境（OS、版本、配置）完整列出", "mitigation": "缓解措施与残余风险须量化评估"},
    conventions=("威胁建模显式声明攻击者能力与目标", "攻击复现须提供可运行 PoC 与数据集", "安全指标用可量化定义（准确率/召回率/误报率）", "敏感信息脱敏后方可引用", "版本与补丁状态随实验注明"),
    key_venues=("IEEE Transactions on Information Forensics and Security", "Journal of Computer and Communications Networks", "ACM Transactions on Privacy and Security", "USENIX Security", "NDSS Symposium"),
    units_and_formulas_notes=("时延/吞吐用 ms 与 Gbps，注明测试条件", "误报/漏报率定义与置信区间须明确", "熵/信息量以 bit 为单位并声明计算窗口", "公式用 amsmath；概率度量统一 p(x) 记法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Metasploit", "Wireshark", "Kali Linux", "Burp Suite", "Nmap", "Zeek", "Suricata", "Cuckoo Sandbox", "Hashcat", "Ghidra", "Radare2", "Scapy", "OWASP ZAP", "ClamAV", "osquery", "Snort", "Jenkins", "Ansible", "Python (Scapy/Scikit-learn)", "Nessus"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
