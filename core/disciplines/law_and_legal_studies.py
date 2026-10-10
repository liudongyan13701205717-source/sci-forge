"""法律与法律研究学科论文支持：教义学与法理学并重的综合法律研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="law_and_legal_studies",
    aliases=(
        "law_and_legal_studies",
        "法律与法律研究",
        "Legal Studies",
        "Legal Research",
        "法学研究",
        "Legal Theory",
        "法理学",
        "Interdisciplinary Law",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
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
    citation_style="《法学引注手册》或 Bluebook/OSCOLA",
    reporting_standards={
        "k1": "法条引用精确到条/款/项，注明版本与修订日期",
        "k2": "案例研究给样本框、编码方案与统计描述",
        "k3": "跨学科论证须说明证据边界与预设",
    },
    conventions=(
        "规范用语（应当/可以/不得）区分",
        "学说与裁判区分引用；引注给页码",
        "比较法给功能性框架，避免罗列",
        "立法建议区分立法论与解释论",
        "实证数据给口径与置信区间",
    ),
    key_venues=(
        "法学研究",
        "中国法学",
        "Legal Studies",
        "Yale Journal of Law & Technology",
        "Journal of Legal Analysis",
    ),
    units_and_formulas_notes=(
        "裁判数据以件数/百分比，标注审级与法院",
        "金额以本币并注年份与是否含税",
        "时间跨度以年月明确",
        "比例给分母与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "元典智库", "iCourt Alpha", "CourtListener", "OpenJur", "Scite", "Semantic Scholar", "R", "Stata", "SPSS", "Nvivo", "MAXQDA", "LaTeX", "Zotero", "Bluebook", "GPO Statute", "Qualtrics", "Reflex（法律文本分析）", "Practical Law", "Tableau"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Westlaw", "LexisNexis", "HeinOnline", "Google Scholar"),
)
