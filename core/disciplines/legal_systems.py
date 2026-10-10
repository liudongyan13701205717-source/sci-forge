"""法律制度学科论文支持：法律体系、司法制度、立法机制与法治评价研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="legal_systems",
    aliases=(
        "legal_systems",
        "法律制度",
        "法律体系",
        "legal systems",
        "legal system",
        "司法制度",
        "judicial system",
        "立法制度",
        "legal institutions",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical framework（理论框架）",
            "methodology（研究方法）",
            "findings（发现）",
            "conclusion（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例描述）",
            "analysis（制度分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "comparative analysis（比较分析）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="Bluebook 21",
    reporting_standards={
        "k1": "比较研究须声明国家、地区与语言版本",
        "k2": "制度分析须区分规范文本与实证运行",
        "k3": "法治指数须注明来源机构与年份",
    },
    conventions=(
        "法系分类：大陆法系、英美法系、宗教法系",
        "法律层级引用含章节号与生效日期",
        "案例引用遵循 Bluebook R. 10",
        "国际法条约引用含批准与生效日期",
        "外国法引用须标注译本与出处",
    ),
    key_venues=(
        "American Journal of Comparative Law",
        "Cambridge Law Journal",
        "Journal of Legal Studies",
        "法学研究",
        "比较法研究",
    ),
    units_and_formulas_notes=(
        "法治指数（WRR/WJP）以 1-5 分报告",
        "诉讼率以每 1000 人件数报告",
        "立法周期以年或月为单位",
        "判例引用标法院层级与年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("vLex", "Casetext", "北大法宝", "中国裁判文书网", "威科先行", "法信", "人民法院案例库", "NVivo", "ATLAS.ti", "MAXQDA", "Python pandas", "R", "Stata", "SPSS", "WJP Rule of Law Index", "Reflex（法律文本分析）", "Bluebook 引注插件", "Practical Law", "Tableau", "Wolters Kluwer CCH（法律研究与合规）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "Web of Science", "Scopus", "国家法律法规数据库"),
)
