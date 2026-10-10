"""Accounting and taxation 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="accounting_and_taxation",
    aliases=(
        "Accounting and taxation",
        "会计与税务",
        "Accounting & Taxation",
        "税务会计",
        "Taxation",
        "Tax Accounting",
        "Taxation and Accounting",
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
        "cas": "案例研究须标注适用的税法版本与年度，遵循中国会计准则（CAS）",
        "vat": "税务数据须说明口径（如增值税、企业所得税等），注明税率与扣除标准",
        "tax_treaty": "跨国税务分析须注明税收协定与避免双重征税安排",
        "planning": "税务筹划研究须区分税收法定与筹划边界，明确政策适用时点",
    },
    conventions=(
        "税务研究须区分税收法定与税收筹划，明确政策适用边界",
        "案例研究须标注适用的税法版本与年度",
        "跨国税务分析须注明税收协定与避免双重征税安排",
        "税务数据须说明口径（如增值税、企业所得税等）",
    ),
    key_venues=(
        "National Tax Journal",
        "Journal of the American Taxation Association",
        "British Tax Review",
        "Journal of International Financial Management and Taxation",
        "Tax Notes",
        "Journal of Taxation",
    ),
    units_and_formulas_notes=(
        "金额以人民币（CNY）计量并注明会计年度，跨境交易须注明汇率与折算基准",
        "有效税率以百分比（%）报告，须区分法定税率与实际税率并说明差异原因",
        "增值税率按税目分档（如 13%、9%、6%），须注明适用税目与进项抵扣口径",
        "所得税计算须报告应税所得额、税率与抵免额，递延所得税须注明暂时性差异",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("用友 U8", "金蝶 K/3", "SAP", "QuickBooks", "Oracle EBS", "NetSuite", "Xero", "SAP S/4HANA", "SPSS", "Stata", "R", "Python（pandas）", "Microsoft Excel", "EndNote", "Microsoft Power BI", "Tableau", "Eviews", "JMP", "ACL Data Explorer", "Oracle Tax Manager"),
    category="管理学",
    databases=("OpenAlex",),
)
