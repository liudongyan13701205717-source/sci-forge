"""哲学论文支持：论证结构、概念分析、思想史综述。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philosophy",
    aliases=("philosophy", "ethics", "epistemology", "metaphysics", "logic",
             "哲学", "伦理学", "认识论", "形而上学", "逻辑学"),
    paper_types={
        "research": ("abstract", "introduction", "argument", "objections", "responses", "conclusion", "references"),
        "commentary": ("abstract", "original claim", "response", "conclusion", "references"),
        "review": ("abstract", "introduction", "main text", "conclusion", "references"),
    },
    citation_style="Chicago Author-Date 或 MLA",
    reporting_standards={
        "argument": "核心论点须独立于证据简述（claim 独立于反驳）",
        "objection": "反论证须对应，观点不歪曲原意（steelman）",
        "sources": "引用原始版本+标准页码；柏拉图/亚里士多德用对应页码系统",
        "definition": "术语定义须精确（不含糊谓词歧义）",
        "originality": "对现有立场说清创新点（反命题）",
    },
    conventions=(
        "用引号直引原文；观点不歪曲原作",
        "区分概念分析与经验论证",
        "论点逐点列需反驳的的前提；结论说清范围",
        "注意作者与被指观点一致不一致（分歧 uncConnext）",
    ),
    key_venues=(
        "Mind",
        "Philosophical Review",
        "Journal of Philosophy",
        "Ethics",
        "Noûs",
    ),
    units_and_formulas_notes=(
        "无需数值或实证数据",
        "论证有效性用真值表/模型可判",
        "概念分析举例（ Gettier/ trolley 顺序互证）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("LaTeX", "Zotero"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar"),
)