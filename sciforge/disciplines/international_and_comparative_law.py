"""国际法与比较法学科论文支持：条约、判例与跨国比较研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="international_and_comparative_law",
    aliases=("international and comparative law", "国际法与比较法", "国际比较法", "国际法", "比较法", "国际私法", "国际公法", "国际公约"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题提出）", "methodology（比较框架与研究方法）", "results（条约、判例与比较发现）", "discussion（规则展望与政策建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（案件事实与程序）", "analysis（裁判要旨与法律论证）", "results（规则效果评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（学说史与关键流派）", "evidence synthesis（跨国判例与立法证据）", "future directions", "references"),
    },
    citation_style="Bluebook 第 21 版或《法学引注手册》（中文稿），国际条约引用按 UNTS 体例",
    reporting_standards={
        "k1": "条约引注须给出 UNTS 卷号与页码",
        "k2": "国际法院判例引注须给出案号、审级与判决日期",
        "k3": "比较对象选择须说明功能等价性",
    },
    conventions=(
        "法条引用精确到条、款、项、目",
        "条约文本引用优先官方版本，附译者与译注",
        "学说引注给页码并区分作者与评注者",
        "比较框架在引言交代，避免简单罗列",
        "立法建议区分立法论与解释论"
    ),
    key_venues=(
        "American Journal of International Law",
        "International Law",
        "European Journal of International Law",
        "Journal of International Dispute Settlement",
        "International and Comparative Law Quarterly"
    ),
    units_and_formulas_notes=(
        "条约引用按 UNTS 卷-页-条",
        "国际法院判决引用按 ICJ Reports 卷-页",
        "比较样本给样本框、国家数与期间",
        "无实证数据时以规范文本与判例为主"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Juris Collection International", "CURIA", "World Bank Lexeme", "VLex", "OneLaw", "WorldLex", "Bloomberg Law", "Oxford International Law Compendium", "UNCITRAL", "Kluwer", "Casetext", "Jus Mundi", "Lexum", "Hein Foreign Law and Current Affairs", "Wolters Kluwer", "ResearchGate", "Reflex（法律文本分析）", "Bluebook 引注插件", "Practical Law", "LexMachine（合同智能审查）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "Google Scholar"),
)
