"""法律与语境学科论文支持：法律的语境化、跨学科与社会语境研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="law_in_context",
    aliases=(
        "law_in_context",
        "法律与语境",
        "Law in Context",
        "Law and Society",
        "法律社会学",
        "Legal Studies in Context",
        "Interdisciplinary Legal Studies",
        "跨学科法学",
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
            "analysis（语境分析）",
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
    citation_style="OSCOLA 或 Bluebook（法教义）；APA 7（社科语境）",
    reporting_standards={
        "k1": "法教义部分给法条与案例引用规范",
        "k2": "社科数据部分给样本框、编码与统计描述",
        "k3": "跨学科论证声明理论预设与证据边界",
    },
    conventions=(
        "法条引用精确到条款；案例给案号审级",
        "社会数据给样本与时段",
        "理论使用明确学派（如法律社会学、法经济学）",
        "区分规范分析、描述分析与评价分析",
        "参考文献统一体例，勿混用",
    ),
    key_venues=(
        "Oxford Journal of Legal Studies",
        "Law & Social Inquiry",
        "International Journal of Law, Policy and the Family",
        "中国法学",
        "社会学研究",
    ),
    units_and_formulas_notes=(
        "法律效果数据以件数、时长或金额",
        "社会数据给口径、置信区间与效应量",
        "案例研究给时间线与来源",
        "文本分析给代码与信度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "元典智库", "Lexum", "Scite", "Semantic Scholar", "R", "Stata", "SPSS", "NVivo", "MAXQDA", "NVivo Transcription", "LaTeX", "Zotero", "Mendeley", "Gephi", "OSCOLA", "Bluebook", "Qualtrics", "Reflex（法律文本分析）", "Tableau"),
    category="法学",
    databases=("CNKI", "OpenAlex", "Crossref", "Westlaw", "LexisNexis", "Google Scholar"),
)
