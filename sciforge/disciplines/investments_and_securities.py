"""投资与证券学科论文支持：证券投资、市场结构与监管研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="investments_and_securities",
    aliases=("investments and securities", "证券投资", "投资", "股票与债券", "金融市场", "证券分析", "资产管理", "资本市场"),
    paper_types={
        "research": ("abstract", "introduction（背景与理论定位）", "methodology（因子、模型与市场检验）", "results（收益与风险发现）", "discussion（政策与实务含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（产品、公司或市场事件）", "analysis（估值与市场行为）", "results（发现与对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（有效市场、行为金融、因子模型）", "evidence synthesis（市场证据）", "future directions", "references"),
    },
    citation_style="Chicago 17（脚注）或 Journal of Finance 惯例",
    reporting_standards={
        "k1": "样本给市场、频率与期间",
        "k2": "因子与模型给估计方法与显著性",
        "k3": "监管与市场结构影响单独讨论",
    },
    conventions=(
        "收益率与 beta 标注频率",
        "估值指标（P/E、P/B、DCF）注明方法与期间",
        "市场事件研究给事件窗口与异常收益",
        "组合业绩以基准（S&P 500 或 CSI 300）比较",
        "交易成本与流动性注明"
    ),
    key_venues=(
        "Journal of Finance",
        "Journal of Financial Economics",
        "Journal of Banking and Finance",
        "Journal of Financial Markets",
        "Financial Review"
    ),
    units_and_formulas_notes=(
        "收益率以 % 每日或每月",
        "波动率以 %",
        "比率（P/E、P/B、EV/EBITDA）给年度和前瞻",
        "beta 用市场基准并注明"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "FactSet", "Refinitiv Eikon", "S&P Capital IQ", "Morningstar", "Wind 万得", "iFind 同花顺", "Choice 东方财富", "Interactive Brokers API", "QuantConnect", "Backtrader", "Zipline", "R", "Python", "Excel", "STATA", "Tableau", "Yahoo Finance API", "CME Group", "Tushare"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
