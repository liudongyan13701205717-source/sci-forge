"""Accounting, Auditing And Accountability 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="accounting_auditing_and_accountability",
    aliases=(
        "Accounting, Auditing And Accountability",
        "会计、审计与问责",
        "Accounting and Auditing",
        "Auditing and Accountability",
        "审计与问责",
        "Accountability Studies",
        "Accounting and Accountability",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "isa": "审计研究须明确审计准则依据（如 ISA、CAS 或本地审计准则）",
        "care": "舞弊案例研究须遵循 CARE 或 SCARE 报告规范",
        "gaggs": "政府与非营利组织会计须遵循各自准则体系（如 GAGAS 或 GAAP 非营利准则）",
        "materiality": "审计重要性判断须报告量化标准（如收入百分比、税前利润百分比）",
    },
    conventions=(
        "审计研究须明确审计准则依据（如ISA、CAS或本地审计准则）",
        "问责机制分析须区分组织内问责与外部问责",
        "政府与非营利组织会计须遵循各自准则体系",
        "舞弊案例研究须遵循CARE或SCARE报告规范",
    ),
    key_venues=(
        "Auditing: A Journal of Practice & Theory",
        "Accounting, Accountability and Accountability",
        "Journal of Accountancy",
        "Journal of the Institute of Chartered Accountants",
        "Auditing Practice",
        "Critical Perspectives on Accounting",
    ),
    units_and_formulas_notes=(
        "审计意见类型须明确分类（无保留/保留/否定/无法表示），并报告相关意见段落",
        "重要性水平以货币单位（万元）计量，须说明量化基准（如税前利润百分比）",
        "舞弊风险指标须报告样本量（n）与异常交易笔数，占比以百分比（%）报告",
        "政府会计数据须注明预算口径（收付实现制/权责发生制）与会计年度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "SPSS", "R", "Python（pandas/statsmodels）", "SAP", "Oracle EBS", "用友 U8", "金蝶 K/3", "ACL Data Explorer", "IDEA", "Tableau", "Microsoft Power BI", "Microsoft Excel", "Endnote", "JMP", "Eviews", "MATLAB", "QuickBooks", "SAS", "RevMan"),
    category="管理学",
    databases=("OpenAlex",),
)
