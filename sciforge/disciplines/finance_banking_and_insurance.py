"""金融银行与保险学科论文支持：银行管理、风险管理、保险精算与金融监管体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="finance_banking_and_insurance",
    aliases=(
        "finance_banking_and_insurance", "金融银行与保险",
        "银行与保险", "金融保险",
        "banking and insurance", "financial services",
        "银行管理", "保险学", "精算学", "金融监管",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（金融风险与监管背景）",
            "methodology（数据、模型、精算方法）",
            "results（实证结果与稳健性）",
            "discussion（经济含义与政策启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（银行/保险公司案例）",
            "analysis（风险管理与运营分析）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（金融与保险研究综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式；金融实证遵循 JBF / JFE / JF 期刊惯例",
    reporting_standards={
        "accounting": "财务数据遵循 IFRS/CAS 会计准则与审计意见",
        "risk": "风险敞口遵循 Basel III/IV 支柱 2 划分",
        "insurance": "保险数据遵循偿付能力监管规则（Solvency II / C-ROSS）",
        "actuarial": "精算报告遵循 SOA / IA 精算实务标准",
        "empirical": "实证研究遵循 CRANES / CONSORT 报告规范",
    },
    conventions=(
        "财务数据须遵循当地会计准则并标注审计意见",
        "风险敞口须按监管口径（Basel III/IV）划分",
        "利率用 % 或 bp；金额用亿元或 USD mn",
        "保险费率用 %；赔付率用 %",
        "监管数据须标注发布机构与发布日期",
    ),
    key_venues=(
        "Journal of Banking and Finance",
        "Journal of Financial Economics",
        "Journal of Financial Intermediation",
        "Journal of Risk and Insurance",
        "ASTIN Bulletin",
        "Insurance: Mathematics and Economics",
        "Financial Management",
    ),
    units_and_formulas_notes=(
        "利率 % 或 bp；金额亿元或 USD mn",
        "风险用 VaR / ES / 标准差",
        "流动性用 LCR / NSFR；资本充足率 %",
        "保险赔付率 %；费率 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "Bloomberg BQuant", "Refinitiv (Reuters)", "LSEG", "FactSet", "S&P Capital IQ", "Wind（万得）", "Choice（东方财富）", "Morningstar Direct", "Barra", "Excel", "R", "Python", "Stata", "MATLAB", "Tableau", "Power BI", "Endnote", "SPSS", "SAS"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "Bloomberg", "Refinitiv"),
)
