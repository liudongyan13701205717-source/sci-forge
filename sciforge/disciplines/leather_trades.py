"""皮革贸易学科论文支持：皮革进出口、市场规模、供应链与贸易政策研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="leather_trades",
    aliases=(
        "leather_trades",
        "皮革贸易",
        "皮革进出口",
        "leather trade",
        "leather exports",
        "leather imports",
        "皮革市场",
        "leather market",
        "皮革供应链",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "贸易数据须注明来源、HS 编码与统计口径",
        "k2": "价格与汇率须标注时点与币种",
        "k3": "供应链分析须声明覆盖范围与时间窗口",
    },
    conventions=(
        "HS 编码采用 2022 版 6-10 位",
        "贸易额单位 USD，注明口径 FOB/CIF",
        "年份用日历年，时间序列用季度或月度",
        "同比与环比数据须分别报告",
        "市场份额以百分比 % 或小数标注",
    ),
    key_venues=(
        "Journal of Leather Science",
        "Leather and Rubber Week",
        "Textile Research Journal",
        "中国皮革",
        "皮革化工",
    ),
    units_and_formulas_notes=(
        "出口额 USD/万，进口额 USD/万",
        "关税税率以 % 表示",
        "增长率 = (本期 - 上期) / 上期 × 100%",
        "贸易平衡 = 出口 - 进口",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "Wind 万得", "Refinitiv Eikon", "FactSet", "UN Comtrade", "Trade Map ITC", "IHS Markit", "S&P Capital IQ", "Global Trade Atlas", "海关总署数据平台", "Excel", "Python pandas", "R", "Stata", "SPSS", "Tableau", "Power BI", "Jupyter Notebook", "KNIME", "Qlik Sense"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
