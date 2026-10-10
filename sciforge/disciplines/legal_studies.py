"""法律研究学科论文支持：法理、法史、法律实证与法律社会学研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="legal_studies",
    aliases=(
        "legal_studies",
        "法律研究",
        "法学",
        "jurisprudence",
        "legal scholarship",
        "法律理论",
        "法哲学",
        "philosophy of law",
        "legal theory",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical framework（理论框架）",
            "methodology（研究方法）",
            "analysis（分析）",
            "conclusion（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例事实）",
            "analysis（分析）",
            "outcome（结果）",
            "discussion（评析）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="Bluebook 21",
    reporting_standards={
        "k1": "实证研究须报告样本量、数据源与信效度",
        "k2": "法律解释须区分文义、目的、历史与体系解释",
        "k3": "法政策分析须明确规制目标与成本收益",
    },
    conventions=(
        "法律层级：宪法 > 法律 > 行政法规 > 部门规章",
        "案例引用须标案号与法院",
        "引注样式遵循 Bluebook R. 10",
        "法条引用含章节号与生效日期",
        "外文译本须注明来源版本",
    ),
    key_venues=(
        "Harvard Law Review",
        "Yale Law Journal",
        "Stanford Law Review",
        "中国法学",
        "法学研究",
    ),
    units_and_formulas_notes=(
        "法条层级引用含条文号与生效日期",
        "实证分析置信水平以 % 表示",
        "案例抽样须报告抽样方法与偏差",
        "引注序号按出现顺序或作者字母排列",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("vLex", "Casetext", "北大法宝", "中国裁判文书网", "威科先行", "NVivo", "ATLAS.ti", "MAXQDA", "Python pandas", "R", "Stata", "SPSS", "VOSviewer", "CiteSpace", "RefWorks", "Zotero", "Bluebook 引注插件", "Reflex（法律文本分析）", "Tableau", "Practical Law 法律实务平台"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "Web of Science", "Scopus", "国家法律法规数据库"),
)
