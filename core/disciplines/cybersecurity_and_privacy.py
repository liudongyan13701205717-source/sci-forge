"""网络安全与隐私学科论文支持：隐私保护、数据安全与合规研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cybersecurity_and_privacy",
    aliases=(
        "cybersecurity_and_privacy", "网络安全与隐私",
        "privacy protection", "隐私保护",
        "data security", "数据安全",
        "privacy engineering", "隐私工程",
        "data protection", "数据保护",
        "GDPR compliance", "GDPR 合规",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（隐私问题与背景）",
            "methodology（隐私模型、保护方案、评估）",
            "results（隐私保护效果与合规评估）",
            "discussion（隐私改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "privacy analysis（隐私分析）",
            "protection strategy（保护策略）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "privacy framework（隐私框架）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "privacy": "隐私模型须定义（k-匿名、差分隐私等）",
        "compliance": "合规性须注明适用法规（GDPR、CCPA 等）",
        "testing": "测试环境须注明（硬件、软件、网络）",
    },
    conventions=(
        "隐私模型须定义（k-匿名、差分隐私等）",
        "合规性须注明适用法规（GDPR、CCPA 等）",
        "数据分类须注明（个人数据、敏感数据等）",
        "隐私预算用 ε 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "IEEE Transactions on Information Forensics and Security",
        "ACM Transactions on Privacy and Security",
        "Journal of Cybersecurity",
        "Computers & Security",
        "IEEE Security & Privacy",
        "USENIX Security Symposium",
    ),
    units_and_formulas_notes=(
        "隐私预算用 ε 表示",
        "数据分类须注明（个人数据、敏感数据等）",
        "合规性须注明适用法规（GDPR、CCPA 等）",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Wireshark", "mitmproxy", "Charles Proxy", "Fiddler", "OpenDP", "PyDP", "Opacus", "TensorFlow Privacy", "Google DP Library", "Microsoft Presidio", "Amazon Macie", "Google Cloud DLP", "Azure Information Protection", "SyntheticDataViz", "Faker", "OpenRefine", "Apache Spark", "MobSF", "APKTool", "Tor"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ACM Digital Library"),
)
