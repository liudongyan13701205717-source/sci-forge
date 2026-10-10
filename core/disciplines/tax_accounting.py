"""Tax Accounting 学科论文支持：税务会计/税会差异论文体裁、APA 引用样式与税会差异调节记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tax_accounting",
    aliases=(
        "tax_accounting",
        "Tax accounting",
        "税务会计",
        "所得税会计",
        "deferred tax",
        "tax provision",
        "book-tax difference",
        "effective tax rate",
        "effective tax rate",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与税会研究问题）",
            "theory and hypothesis（理论框架与假设）",
            "methods（样本、数据与计量模型）",
            "results（实证结果与稳健性检验）",
            "discussion（经济含义与政策启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（企业税务案例）",
            "analysis（税会差异与调整）",
            "conclusion（结论与建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review（税会研究综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Journal of Accounting Research、Tax Review 遵循期刊规范）",
    reporting_standards={
        "sample": "样本须报告：期间、行业、地区、剔除规则（异常值、缺失值、金融企业）、观测数 N",
        "variables": "变量定义须完整：EPT、BTD、ETR、DTA/DTL 的计算方式与期间口径",
        "model": "计量模型须报告：固定效应（企业/行业/年度）、聚类标准误、控制变量与Hausman 检验",
        "robustness": "稳健性检验须包括：替换指标、剔除特殊期、内生性处理（工具变量/倾向得分）、异质性检验",
        "compliance": "涉及企业数据须说明数据来源与合规声明",
    },
    conventions=(
        "会计与税务口径统一：会计利润 taxable income 用 GAAP/IFRS/CAS；应纳税所得额 tax payable 用当地税法（如 CAS 12、IRC 2008 及其实施条例）",
        "有效税率 ETR = 所得税费用/税前会计利润；现金有效税率 CASH ETR = 现金所得税/税前会计利润；统计有效税率 SEER = 所得税费用/(税前会计利润+永久性差异)",
        "永久性差异 vs 暂时性差异须区分；递延所得税资产 DTA/负债 DTL 按 IAS 12/CAS 18 报告",
        "符号约定：正 ETR 为正税负、负 BTD 表示会计利润小于应税利润；所有比率以小数或百分数统一",
        "计量公式用 amsmath；系数报告附标准误（括号内）；显著性用 *, **, *** 对应 10%/5%/1% 水平",
        "样本区间须明确；跨期研究须注明会计年度截止日与税务申报截止日的差异",
    ),
    key_venues=(
        "Journal of Accounting Research",
        "Journal of Accounting Economics",
        "Review of Accounting Studies",
        "Journal of the American Taxation Association",
        "National Tax Journal",
        "The Accounting Review",
    ),
    units_and_formulas_notes=(
        "金额单位：元/万元/百万元；税率用百分数 %；比率用小数或百分数；时间用年度",
        "ETR = 所得税费用/(税前会计利润)；CET = 现金所得税/(税前会计利润)；EPT = 所得税费用/(税前会计利润+永久性差异)",
        "BTD = 会计利润 - 应税所得；暂时性差异 = 递延所得税变动；MTD（Momentum Tax Difference）= 会计利润 + DTA 变化 - 应纳税所得额",
        "公式用 amsmath；系数报告附标准误；样本量 N 须显式标注；R²、调整 R² 与 F 值须报告",
        "所有比率结果保留 4 位小数；均值 ± SD 与观测数 N 须完整；异质性分组须说明分组依据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SAP S/4HANA (FI-TAX)", "Oracle Fusion Cloud Tax", "Microsoft Dynamics 365 Finance", "CheckPoint by Thomson Reuters", "Bloomberg Tax", "PwC Tax Alert", "Deloitte Tax Research", "PwC Worldwide Tax Summaries", "QuickBooks", "Xero", "Stata", "R", "Python (pandas)", "Power BI", "Tableau", "Excel", "EndNote", "Zotero", "金蝶 K/3（税务管理）", "ACL Data Explorer"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "WSS", "Compustat", "Westlaw Tax Center", "LexisNexis Checkpoint"),
)
