"""法学论文支持：教义分析、案例评论、比较法与实证研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="law",
    aliases=(
        "law",
        "法学",
        "法律",
        "Jurisprudence",
        "Legal Studies",
        "法律研究",
        "Legal Theory",
        "法理学",
    ),
    paper_types={
        "doctrinal": (
            "abstract（可省）",
            "introduction（问题提出）",
            "legal framework（规范梳理）",
            "analysis（教义分析）",
            "conclusion（立法/解释建议）",
            "references",
        ),
        "case_note": (
            "case background（案情）",
            "court reasoning（裁判要旨）",
            "commentary（评析）",
            "implications（规则展望）",
            "references",
        ),
        "comparative": (
            "abstract",
            "introduction",
            "jurisdiction A",
            "jurisdiction B",
            "comparison",
            "recommendations",
            "references",
        ),
    },
    citation_style="《法学引注手册》或 Bluebook/OSCOLA（英文稿）",
    reporting_standards={
        "sources": "法条引用精确到条/款/项；案例引用案号与审级",
        "currency": "法律版本（修订日期）须注明；已废止条文标注",
        "comparative": "比较对象选择理由（功能等价）须说明",
        "empirical": "裁判数据研究给样本框、编码方案与统计描述",
    },
    conventions=(
        "规范用语（应当/可以）区分；学说引注给页码",
        "案例评论区分裁判摘要与作者观点；注释体例全稿统一",
        "比较法避免简单罗列，须给功能性比较框架",
        "立法建议区分立法论与解释论",
        "英文稿遵循 Bluebook 或 OSCOLA",
    ),
    key_venues=(
        "法学研究",
        "中国法学",
        "Harvard Law Review",
        "Yale Law Journal",
        "Journal of Legal Studies",
    ),
    units_and_formulas_notes=(
        "无实证数据时以规范与案例分析为主",
        "裁判数据统计给样本量与期间；比例给分母口径",
        "实证法律研究须声明伦理审查与匿名化",
        "金额类以本币单位注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "威科先行", "元典智库", "Alpha 法宝", "判例库", "iCourt Alpha", "R", "Nvivo", "MAXQDA", "Stata", "LaTeX", "Zotero", "Mendeley", "Oscola", "Bluebook", "CourtListener", "GPO Statute Database", "SPSS", "Reflex（法律文本分析）", "Qualtrics"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Westlaw", "LexisNexis", "HeinOnline"),
)
