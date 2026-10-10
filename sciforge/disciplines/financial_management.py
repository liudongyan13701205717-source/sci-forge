"""财务管理学科论文支持：企业理财、资本预算与财务决策体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="financial_management",
    aliases=(
        "financial_management", "财务管理", "企业财务管理",
        "corporate finance", "financial management",
        "公司理财", "资本预算", "财务决策", "企业理财",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（财务问题与理论背景）",
            "methodology（数据、模型与实证设计）",
            "results（财务绩效与决策分析）",
            "discussion（管理含义与政策启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业案例描述）",
            "analysis（财务分析与决策）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（财务管理研究综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式；公司金融论文亦常见 Chicago Author-Date",
    reporting_standards={
        "accounting": "财务数据遵循 IFRS/CAS/US GAAP 会计准则",
        "valuation": "估值报告须注明 DCF/EVA 模型参数与假设",
        "capital_structure": "资本结构须报告杠杆率与债务期限",
        "risk": "财务风险须报告 Beta/VaR/ES 指标",
        "empirical": "实证研究遵循 CRANES 报告规范",
    },
    conventions=(
        "财务比率须注明计算口径与期间",
        "货币单位与通胀调整注明",
        "资本预算须报告 NPV/IRR 与贴现率",
        "实证结果须报告系数、标准误与 t 值",
        "面板数据须说明固定效应与聚类稳健标准误",
    ),
    key_venues=(
        "Journal of Financial Economics",
        "Journal of Financial Economics",
        "Journal of Corporate Finance",
        "Journal of Financial and Quantitative Analysis",
        "Review of Finance",
        "Financial Management",
        "Journal of Accounting and Economics",
    ),
    units_and_formulas_notes=(
        "金额用元或亿元；比率用 % 或倍",
        "收益率 %；风险用 Beta 或标准差",
        "资本成本用 WACC %；NPV 用元",
        "杠杆率用 % 或倍（D/E）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "Wind（万得）", "S&P Capital IQ", "FactSet", "Refinitiv Eikon", "Python", "R", "Stata", "MATLAB", "Eviews", "Excel", "Tableau", "Power BI", "SPSS", "SAS", "Endnote", "JMP", "Gretl", "JAX", "DAX"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Bloomberg", "Wind"),
)
