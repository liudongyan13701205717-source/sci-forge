"""投资分析学科论文支持：资产定价、组合优化与估值。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="investment_analysis",
    aliases=("investment analysis", "投资分析", "资产管理", "资产定价", "股票分析", "组合优化", "估值", "量化投资"),
    paper_types={
        "research": ("abstract", "introduction（背景与文献定位）", "methodology（模型、因子与识别）", "results（收益与风险估计）", "discussion（机制与实务含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（标的、组合或事件）", "analysis（估值与因子归因）", "results（发现与对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（CAPM、Fama-French 与因子模型演进）", "evidence synthesis（因子与策略证据）", "future directions", "references"),
    },
    citation_style="Chicago 17（脚注）或 Journal of Finance 惯例",
    reporting_standards={
        "k1": "样本给范围、频率与幸存者偏差处理",
        "k2": "收益率与风险用日或月频率并注明",
        "k3": "因子与模型给估计方法、显著性与稳健性",
    },
    conventions=(
        "收益率按几何或算术注明",
        "风险以标准差、VaR 或 beta 表示并给置信水平",
        "组合优化给约束与权重",
        "估值方法（DCF、可比、相对）明确",
        "交易成本与滑点在回测中处理"
    ),
    key_venues=(
        "Journal of Finance",
        "Journal of Financial Economics",
        "Review of Financial Studies",
        "Journal of Financial and Quantitative Analysis",
        "Financial Analysts Journal"
    ),
    units_and_formulas_notes=(
        "收益率以 % 每期，年化用平方根法",
        "波动率以 % 或标准差",
        "比率（P/E、P/B）给年度和前瞻",
        "beta 与 alpha 注明估计方法与样本期"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "Refinitiv Eikon", "FactSet", "S&P Capital IQ", "Morningstar", "Wind 万得", "iFind 同花顺", "Choice 东方财富", "STATA", "R", "Python", "MATLAB", "EViews", "MSCI Barra", "Axioma Portfolio Analytics", "RiskMetrics", "Excel", "Tableau", "Interactive Brokers API", "QuantConnect"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
