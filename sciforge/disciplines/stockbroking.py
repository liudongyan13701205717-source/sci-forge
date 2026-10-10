"""证券经纪学科论文支持：证券经纪业务、交易行为与监管合规研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stockbroking",
    aliases=("stockbroking", "证券经纪", "股票经纪", "证券交易", "证券经纪业务",
             "stockbroker", "securities brokerage", "证券交易", "经纪商",
             "brokerage services", "经纪研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与市场环境）",
            "methodology（交易分析与实证方法）",
            "results（交易行为与市场发现）",
            "discussion（监管与实务含义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（经纪案例或市场事件）",
            "analysis（交易行为与风险分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（经纪理论与市场结构综述）",
            "evidence synthesis（市场证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 17（脚注）或 Journal of Finance 惯例",
    reporting_standards={
        "sample": "样本须给出市场、频率与期间",
        "model": "交易模型须给出估计方法与显著性水平",
        "regulation": "监管合规影响须单独讨论",
        "conflicts": "利益冲突（佣金激励、自营交易）须披露",
    },
    conventions=(
        "收益率与 beta 标注频率（日/周/月）",
        "估值指标（P/E、P/B、EV/EBITDA）注明计算方法与期间",
        "市场事件研究给事件窗口与异常收益",
        "交易成本（佣金、价差）须注明",
        "组合业绩以基准（S&P 500 或 CSI 300）比较",
    ),
    key_venues=(
        "Journal of Financial Economics",
        "Journal of Financial Markets",
        "Journal of Banking and Finance",
        "Review of Finance",
        "Financial Analysts Journal",
    ),
    units_and_formulas_notes=(
        "收益率以 % 每日或每月报告",
        "波动率以 % 报告",
        "价差以 % 或 bp（基点）报告",
        "交易成本以 % 名义报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "FactSet", "Refinitiv Eikon", "S&P Capital IQ", "Morningstar", "Wind 万得", "iFind 同花顺", "Choice 东方财富", "Interactive Brokers API", "QuantConnect", "Backtrader", "Zipline", "Python (pandas, backtrader)", "R (quantmod)", "STATA", "Excel", "Tableau", "Yahoo Finance API", "Tushare", "Jupyter Notebook"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
