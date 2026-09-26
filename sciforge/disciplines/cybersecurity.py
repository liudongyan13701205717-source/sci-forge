"""网络安全学科论文支持：安全攻防/隐私体裁、ACM 引用样式与安全记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cybersecurity",
    aliases=("cybersecurity", "网络安全", "信息安全", "安全", "密码学应用"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "threat model（威胁模型）",
            "method（方法）",
            "evaluation（评估）",
            "references",
        ),
        "attack_paper": (
            "abstract",
            "introduction",
            "threat model（威胁模型）",
            "attack design（攻击设计）",
            "experiments（实验）",
            "countermeasures（防御对策）",
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
    citation_style="ACM 样式（作者-年份；IEEE S&P/USENIX Security 遵循其规范）",
    reporting_standards={
        "experimental": "实验遵循安全论文评估规范",
        "responsible_disclosure": "漏洞披露遵循负责任披露规范",
        "human_subjects": "人类受试者研究遵循 IRB 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "benchmark": "基准测试遵循标准基准报告规范",
    },
    conventions=(
        "威胁模型与攻击者能力须明确",
        "漏洞影响与 CVSS 评分须报告",
        "实验环境与数据集须说明",
        "防御评估须公平（同威胁模型）",
        "伦理与披露流程须说明",
    ),
    key_venues=(
        "IEEE Symposium on Security and Privacy",
        "USENIX Security Symposium",
        "ACM CCS",
        "Network and Distributed System Security Symposium",
        "IEEE Transactions on Information Forensics and Security",
        "Journal of Cryptology",
    ),
    units_and_formulas_notes=(
        "时间用 s/min；成功率用 %；密钥长度用 bit",
        "公式用 amsmath；协议与算法须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Metasploit", "Wireshark", "Scapy", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)