"""审计学 (Auditing) 学科论文支持：财务审计、内部审计、政府审计、审计信息化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="auditing",
    aliases=(
        "Auditing", "审计", "审计学", "audit",
        "financial auditing", "财务审计",
        "internal auditing", "内部审计",
        "government auditing", "政府审计",
        "信息系统审计", "IT audit", "IT auditing",
        "forensic accounting", "法务会计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "research design / methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "case background",
            "audit process",
            "findings",
            "recommendations",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current state",
            "open questions",
            "references",
        ),
    },
    citation_style="APA 7（管理学惯例）",
    reporting_standards={
        "standards": "须遵循 ISA / PCAOB / CAS 审计准则编号",
        "sampling": "审计抽样方法与样本量须报告（分层随机/PPS/属性抽样）",
        "materiality": "重要性水平须声明计算依据",
        "data": "财务数据来源与凭证完整性须可追溯",
        "ethics": "注册会计师独立性须声明（无利益冲突）",
    },
    conventions=(
        "审计报告要素按 CAS 报告准则 1501 完整披露",
        "审计准则引用须注明 ISAs/PCAOB/CAS 具体编号",
        "工作底稿按 CAS 工作底稿准则归档",
        "审计风险按 CAS 风险准则 1101 定义并量化",
        "错报按 CAS 1251 汇总与评价",
        "会计科目按《企业会计准则》统一名称",
        "报告语言与计量单位须声明（人民币元/万元）",
    ),
    key_venues=(
        "The Accounting Review",
        "Auditing: A Journal of Practice & Theory",
        "Journal of Accounting Research",
        "Contemporary Accounting Research",
        "Journal of Business Ethics",
        "Journal of Financial Reporting and Accounting Regulation",
        "Managerial Auditing Journal",
        "审计研究",
        "会计研究",
        "审计与经济研究",
    ),
    units_and_formulas_notes=(
        "货币单位 CNY/USD 并注明币种与年份",
        "重要性水平用绝对值与百分比双重表述",
        "比率统一百分号，比率分析按 CAS 定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("金蝶 K/3", "金蝶 EAS", "金蝶 Star", "用友 NC", "用友 U8+", "用友 BIP", "用友畅捷通", "金蝶精斗云", "SAP S/4HANA", "SAP ECC", "SAP Business One", "Oracle EBS", "Oracle Fusion Cloud", "Oracle NetSuite", "浪潮 Inspur", "Power BI", "Tableau", "QlikView", "Galvanize ACL", "IDEA (Audit Data Analytics)", "AuditWizard", "Deloitte Wdesk", "Deloitte EAM", "Workiva", "Arisuite", "BlackLine", "Diligent", "KPMG Clara", "EY Axiom", "EY Aura", "EY Helix", "PwC Axiom", "PwC Workfront", "SAS", "Python (Pandas / NumPy / scikit-learn)", "R (dplyr / tidyr)", "Stata", "SPSS", "SQL (MySQL / PostgreSQL / Oracle)", "Snowflake", "AWS Redshift", "Excel (VBA / Power Query)", "DBeaver", "Navicat"),
    category="管理学",
    databases=("CNKI", "OpenAlex", "Crossref", "JSTOR", "CNAS", "WIKICL", "中国审计署官网"),
)
