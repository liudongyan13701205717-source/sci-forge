"""国际经济学学科论文支持：贸易、金融、跨国企业与增长研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="international_economics",
    aliases=("international economics", "国际经济学", "国际贸易", "国际金融", "跨国公司", "国际资本流动", "汇率经济学", "国际贸易研究"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（识别策略、数据与计量）", "results（模型估计与稳健性）", "discussion（机制与政策含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（国家或贸易协定背景）", "analysis（贸易流或汇率冲击的机制识别）", "results（实证发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（贸易与金融理论演进）", "evidence synthesis（跨国证据汇总）", "future directions", "references"),
    },
    citation_style="Chicago 17（脚注-文体）或 CAPA（Journal of International Economics 惯例）",
    reporting_standards={
        "k1": "识别策略须说明外生性假设与安慰剂检验",
        "k2": "跨国面板给出样本国家、年份与遗漏处理",
        "k3": "汇率与贸易衡单位换算口径统一",
    },
    conventions=(
        "符号在首次出现处定义，全文一致",
        "图表在正文引用并给编号与标题",
        "稳健性检验至少三组（子样本、替代指标、时点）",
        "机制讨论与政策含义分离",
        "文献评论按主题而非时间罗列"
    ),
    key_venues=(
        "Journal of International Economics",
        "Review of Economics and Statistics",
        "Journal of International Money and Finance",
        "American Economic Review",
        "Journal of Development Economics"
    ),
    units_and_formulas_notes=(
        "贸易额以 FOB 或 CIF 区分，币种注明与年度",
        "汇率用直接法或间接法注明，名义与实际区分",
        "增长率用 % 年度、ln 差分或水平值须明示",
        "跨国数据以 US$2017 PPP 或当期名义为统一基准"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Terminal", "IMF DataMapper", "IMF International Financial Statistics", "World Bank WDI", "World Bank PIN", "WTO Statistics", "CEPII Gravity Database", "OECD.Stat", "BIS Statistics", "UN COMTRADE", "FRED", "STATA", "R", "Python", "MATLAB", "EViews", "Gretl", "Julia", "Tableau", "Power BI"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
