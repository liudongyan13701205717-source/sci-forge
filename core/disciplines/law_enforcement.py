"""执法学科论文支持：警务学、执法实践与犯罪预防研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="law_enforcement",
    aliases=(
        "law_enforcement",
        "执法",
        "Law Enforcement",
        "Police Science",
        "警务学",
        "Criminal Justice",
        "刑事司法",
        "Public Safety",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（执法分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或《中国刑事警察杂志》引注规范",
    reporting_standards={
        "k1": "数据来源（警情/司法统计）与时段口径须披露",
        "k2": "执法行动研究声明伦理审查与匿名化",
        "k3": "因果性/相关性明确区分，勿越界推断",
    },
    conventions=(
        "术语区分刑事犯罪/治安违法/行政违法",
        "统计数据给出采样框与年份",
        "案例研究须匿名化并标注来源",
        "理论使用区分预防、侦查、审判层次",
        "参考文献按字母序或引用序统一",
    ),
    key_venues=(
        "Criminology",
        "Journal of Criminal Justice",
        "Police Practice and Research",
        "中国刑事警察杂志",
        "公安研究",
    ),
    units_and_formulas_notes=(
        "犯罪率以每 10 万人为口径",
        "响应时间以分钟，出警次数以件",
        "预算以本币与年度",
        "比例给置信区间与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Crime Stat Analyst (CSA)", "CompStat", "NIBRS", "UCR Database", "FBI National Crime Index", "Europol PILOT", "Interpol I-24/7", "ArcGIS", "QGIS", "R", "Stata", "SPSS", "NVivo", "MAXQDA", "Bodycam Analytics", "Knox 911 Software", "Verizon Fusion", "LaTeX", "Zotero", "SAS"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
