"""国民账户学科论文支持：国民经济核算体裁、SNA 报告规范与核算记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="national_accounts",
    aliases=("national_accounts", "国民账户", "国民核算", "国民经济核算", "SNA",
             "SNA 2008", "GDP核算", "国民经济统计"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与核算问题）",
            "methodology（核算方法与数据源）",
            "results（核算结果与加总）",
            "discussion（口径与政策含义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（核算单位/国家范围）",
            "analysis（核算平衡表编制）",
            "results（关键指标结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（核算理论综述）",
            "evidence synthesis（跨国比较与证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="SNA 样式（作者-年份；SNA 2008 遵循其规范）",
    reporting_standards={
        "experimental": "数据采集遵循 SNA 2008 附录 A",
        "accounting": "核算遵循 SNA 2008 各章规范",
        "balance": "平衡表编制遵循 SNA 2008 附录 D",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "statistical": "统计口径遵循 OECD/IMF 统计指南",
    },
    conventions=(
        "采用 SNA 2008 版本并标注数据年份",
        "名义/实际值与货币单位须注明",
        "时点/时段数据须区分",
        "数据来源与修订版本须报告",
        "平衡表加总与闭合误差须说明",
    ),
    key_venues=(
        "Journal of Economic Statistics",
        "IMF Staff Papers",
        "Bulletin of International Statistics",
        "JEL",
        "经济学（季刊）",
    ),
    units_and_formulas_notes=(
        "金额用本币或美元（当年价/不变价）",
        "公式用 amsmath；核算方程须编号",
        "百分比变化须定义基期",
        "名义/实际值须注明",
        "平衡表须闭合并报告残差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("IMF IFS", "World Bank WDI", "Eurostat DB", "OECD Data Explorer", "IMF DOTS", "Stata", "R", "Python（Pandas/NumPy）", "Microsoft Excel", "EViews", "Tableau", "LaTeX", "Jupyter Notebook", "Vega-Lite", "Bloomberg Terminal", "Refinitiv Eikon", "SDMX", "MEF2（SNA 账户软件）", "SDMX Editor（SDMX XML Editor）", "World Bank Data Viewer（在线数据查询工具）"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "IMF IFS", "World Bank WDI", "国家统计局数据库"),
)
