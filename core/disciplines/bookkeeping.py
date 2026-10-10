"""会计基础/簿记学科论文支持：账务处理/复式簿记体裁、CAS/IFRS 引用样式与会计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bookkeeping",
    aliases=(
        "bookkeeping",
        "Bookkeeping",
        "簿记",
        "基础会计",
        "账务处理",
        "复式簿记",
        "会计",
        "accounting",
        "double-entry bookkeeping",
        "账务会计",
        "会计与簿记",
        "financial bookkeeping",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（数据来源、样本、方法）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "case": (
            "abstract",
            "company background",
            "methodology",
            "case analysis",
            "discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7（会计学引用样式）",
    reporting_standards={
        "gaap": "会计准则（CAS/IFRS/GAAP）须明确",
        "units": "金额单位统一（人民币元、万元或 US$）",
        "accounting_policy": "会计政策须列明",
        "consistency": "可比性须保证",
    },
    conventions=(
        "会计科目名称全文一致（如'库存现金'、'应收账款'）",
        "金额单位须在首次出现处声明并全文一致",
        "借贷方向用'借/贷'或'Dr/Cr'标记",
        "报表项目按准则顺序排列",
        "报表数据四舍五入到一致精度",
    ),
    key_venues=(
        "The Accounting Review",
        "Journal of Accounting Research",
        "Journal of Accounting Economics",
        "Contemporary Accounting Research",
        "Auditing: A Journal of Practice & Theory",
        "Management Accounting Research",
        "Accounting, Organizations and Society",
    ),
    units_and_formulas_notes=(
        "金额用人民币元或万元（明确单位）",
        "比率保留两位小数",
        "会计等式：资产 = 负债 + 所有者权益",
        "利润 = 收入 - 费用",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("用友", "金蝶", "QuickBooks", "Xero", "Sage", "MYOB", "Tally", "SAP Business One", "Oracle Financials", "Microsoft Dynamics 365", "Zoho Books", "FreshBooks", "Wave", "Oracle NetSuite", "Microsoft Excel", "LibreOffice Calc", "Google Sheets", "Python (pandas)", "PostgreSQL", "MySQL"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "Google Scholar", "SSRN", "EBSCO"),
)
