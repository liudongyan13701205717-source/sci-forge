"""法律辅助学科论文支持：法律辅助实践、法律研究与法律信息管理研究体裁、判例与法规引用规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="paralegal_studies",
    aliases=(
        "paralegal_studies",
        "法律辅助",
        "Para-legal Studies",
        "Paralegal Studies",
        "法律文秘",
        "法律助理研究",
        "Legal Support Services",
        "法律信息管理",
        "legal research methodology"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Bluebook（美国法学引用规范）",
    reporting_standards={
        "k1": "法律案例研究须遵循法律注释与判例引用规范",
        "k2": "法律检索研究须报告检索式、数据源与检索时间点",
        "k3": "实证法律研究须报告数据来源、编码与信度"
    },
    conventions=(
        "判例引用须遵循 Bluebook 格式并注明法院、年份与卷期",
        "法律条文须注明版本、生效日期与修订历史",
        "检索式与筛选过程须完整报告以保证可复现",
        "案例描述须脱敏并说明信息来源",
        "结论须区分法定解释与学理解释"
    ),
    key_venues=(
        "Journal of Legal Studies",
        "Law and Contemporary Problems",
        "Virginia Law Review",
        "Stanford Law Review",
        "American Bar Association Journal"
    ),
    units_and_formulas_notes=(
        "判例引用须遵循法院层级与年份格式",
        "法律条文须给出条文号、生效日与修订版本",
        "检索式须给出布尔操作符与检索时间",
        "数据集须报告案例数量与筛选率"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bloomberg Law", "vLex", "Casetext", "Justia", "FindLaw", "iManage", "Relativity", "Everlaw", "Clio", "MyCase", "HotDocs", "NetDocuments", "Bluebook（在线版）", "Shepard's Citations", "KeyCite", "Zotero", "Microsoft Office", "DocuSign", "LegalOne", "Kira Systems"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline"),
)
