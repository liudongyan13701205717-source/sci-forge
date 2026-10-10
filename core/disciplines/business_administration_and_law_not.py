"""工商管理法学（未另分类）学科论文支持：企业法律实务、法规评析与法律检索。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_administration_and_law_not",
    aliases=(
        "business_administration_and_law_not",
        "工商管理法学（未另分类）",
        "商业法律（未另分类）",
        "企业法律实务",
        "法律商管",
        "Business Administration and Law (not elsewhere classified)",
        "Legal Studies in Business",
        "Law and Business",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与定位）",
            "literature review",
            "methodology",
            "analysis",
            "conclusion",
            "references",
        ),
        "practitioner_brief": (
            "abstract",
            "case background（案例背景）",
            "legal analysis",
            "risk assessment（风险评估）",
            "recommendations（合规建议）",
            "references",
        ),
        "regulatory_commentary": (
            "abstract",
            "introduction（立法/监管背景）",
            "analysis",
            "comparison（中外监管比较）",
            "recommendations",
            "references",
        ),
    },
    citation_style="蓝皮书或 GB/T 7714；实务写作采用律所体例",
    reporting_standards={
        "statute_citation": "法规引用须注明届次、条文号与年份",
        "case_citation": "案例须给出标准案号与裁判要旨",
        "compliance_recommendation": "合规建议须给出可操作路径与风险敞口",
        "empirical": "实证研究须说明数据源与因果识别",
    },
    conventions=(
        "法条与司法解释须标注届次",
        "案例须引用案号并标注裁判要旨",
        "术语中英对照须使用领域通行译法",
        "合规建议须给出具体路径与风险等级",
    ),
    key_venues=(
        "Yale Law Journal",
        "Cornell Law Review",
        "Duke Law Journal",
        "The Business Lawyer (ABA)",
        "Washington University Journal of Law & Policy",
        "法学",
        "法律科学",
        "当代法学",
        "比较法研究",
    ),
    units_and_formulas_notes=(
        "金额以人民币元报告",
        "条文号引用须给出届次与年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "元典智库", "威科先行", "无讼", "中国裁判文书网", "中国司法案例库", "Bloomberg Law", "vLex", "I-Connect", "Lexology", "LegalOne", "天同学院", "Lexis+", "法宝资讯", "Wolters Kluwer CCH", "Casetext（AI 法律检索）", "LexMachine（合同智能审查）", "Practical Law", "Bluebook 引注插件", "Clio（律所管理软件）"),
    category="法学",
    databases=("北大法宝", "CNKI", "HeinOnline", "LexisNexis", "OpenAlex", "Westlaw", "JSTOR", "国家法律法规数据库"),
)
