"""Commercial Law 学科论文支持：商法/公司法/商事交易法体裁、法律引用样式与法律写作注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="commercial_law",
    aliases=("Commercial Law", "商法", "商业法", "商事法", "commercial law",
             "business law", "trade law", "corporate law", "公司法", "商事交易法"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出与背景）",
            "literature review（文献综述）",
            "legal framework（法律框架）",
            "analysis（分析）",
            "conclusion（结论与建议）",
            "references",
        ),
        "comparative": (
            "abstract",
            "introduction",
            "legal systems compared（比较法体系）",
            "comparison analysis（比较分析）",
            "findings（发现）",
            "recommendations（建议）",
            "references",
        ),
        "commentary": (
            "abstract",
            "introduction",
            "legislative background（立法背景）",
            "statutory analysis（条文分析）",
            "case analysis（案例评析）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Bluebook（美国法律引用）/ OSCOLA（英国）/ 中国法律引用规范",
    reporting_standards={
        "legislative": "法律法规须标注全称、条号与发布日期",
        "case": "判例须标注案号、法院与判决日期",
        "comparative": "比较法研究须说明比较法源与适用范围",
    },
    conventions=(
        "引用法律法规须标注法律全称、条号与发布日期",
        "引用判例须标注案号、法院与判决日期",
        "比较法研究须说明比较法源与适用范围",
        "法律术语使用规范，首次出现时标注原文",
    ),
    key_venues=(
        "Chinese Journal of Law",
        "Journal of International Economic Law",
        "European Business Organization Law Review",
        "China Economic Law Review",
        "Commercial Law Yearbook",
        "Journal of Corporate Law and Finance",
        "Business Law Review",
        "Chinese Law Review",
    ),
    units_and_formulas_notes=(
        "法条引用格式：法律名称（年份）条号",
        "判例引用格式：案名（案号）（法院、日期）",
        "外文法律文献须附中文译文或说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("北大法宝", "威科先行", "法信", "知产宝", "iCourt", "无讼", "Bloomberg Law", "SSRN", "Casetext", "AnyLaw", "智慧芽", "Wolters Kluwer", "法条网", "中国裁判文书网", "Lexis+", "vLex", "LegalOne", "Bluebook 引注插件", "Practical Law", "LexMachine（合同智能审查）"),
    category="法学",
    databases=("北大法宝", "威科先行", "Westlaw", "LexisNexis", "OpenAlex", "Crossref", "JSTOR", "HeinOnline", "ProQuest", "LexisNexis China"),
)
