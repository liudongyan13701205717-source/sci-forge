"""工商管理法学学科论文支持：商法/经济法/公司法/证券法体裁与规范引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_administration_and_law",
    aliases=(
        "business_administration_and_law",
        "工商管理法学",
        "商法",
        "经济法",
        "商业法",
        "企业法律",
        "Business Law",
        "Corporate Law",
        "Commercial Law",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、意义与研究定位）",
            "literature review（文献综述）",
            "methodology（研究方法：规范分析/实证分析/案例比较）",
            "analysis（分析论证）",
            "conclusion（结论与建议）",
            "references",
        ),
        "case_commentary": (
            "abstract",
            "case summary（案例概要）",
            "legal issues（争点分析）",
            "discussion（评析）",
            "conclusion",
            "references",
        ),
        "legislative_commentary": (
            "abstract",
            "introduction（立法背景）",
            "analysis（条文逐句评析）",
            "comparison（中外比较）",
            "suggestions（立法/修法建议）",
            "references",
        ),
    },
    citation_style="蓝皮书（Bluebook）或 GB/T 7714；中国法学论文多采用《法学》体例",
    reporting_standards={
        "case_citation": "案例引用须注明案号、法院、判决年份与裁判要旨",
        "statute_citation": "法条引用须注明法律名称、届次、条文号与发布年份",
        "doctrinal_analysis": "法理分析须区分实然与应然",
        "empirical_legal_study": "实证法学须报告数据来源、样本期与因果识别",
    },
    conventions=(
        "法条引用须给出届次、条文号与年份",
        "案例引用须给出案号、法院与裁判要旨",
        "术语中英对照须使用领域通行译法",
        "论证结构遵循「规范-事实-涵摄」三段论",
    ),
    key_venues=(
        "Harvard Law Review",
        "Columbia Law Review",
        "Stanford Law Review",
        "Virginia Law Review",
        "Michigan Law Review",
        "Business Lawyer (ABA)",
        "The Journal of Corporate Law",
        "中国法学",
        "法学研究",
        "中外法学",
        "法律与社会",
    ),
    units_and_formulas_notes=(
        "金额以人民币元或统一币种报告",
        "条文号引用须给出届次与年份",
        "案例编号须给出标准案号格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "元典智库", "威科先行", "无讼", "律商联讯 Lexis", "Wolters Kluwer CCH", "Bloomberg Law", "Lexis+", "Lexology", "vLex", "I-Connect", "LegalOne", "Lexis Mega", "Reflex（法律文本分析）", "法宝资讯", "中国司法大数据研究院", "Practical Law", "LexMachine（合同智能审查）", "Bluebook 引注插件", "ROSS Intelligence（AI 法律检索）"),
    category="法学",
    databases=("北大法宝", "CNKI", "OpenAlex", "HeinOnline", "LexisNexis", "Westlaw", "JSTOR"),
)
