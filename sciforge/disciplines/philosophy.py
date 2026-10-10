"""哲学学科论文支持：论证结构、概念分析、思想史综述。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philosophy",
    aliases=("philosophy", "ethics", "epistemology", "metaphysics", "logic",
             "哲学", "伦理学", "认识论", "形而上学", "逻辑学",
             "metaphilosophy", "metaphysics", "epistemology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "argument（论证）",
            "objections（反驳）",
            "responses（回应）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（发现）",
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
    citation_style="Chicago Author-Date 或 MLA 样式（哲学/伦理学常用）",
    reporting_standards={
        "argument": "核心论点须独立于证据简述（claim 独立于反驳）",
        "objection": "反论证须对应，观点不歪曲原意（steelman）",
        "sources": "引用原始版本+标准页码；柏拉图/亚里士多德用对应页码系统",
        "definition": "术语定义须精确（不含糊谓词歧义）",
        "originality": "对现有立场说清创新点（反命题）",
        "logical": "形式论证遵循标准逻辑规范",
    },
    conventions=(
        "用引号直引原文；观点不歪曲原作",
        "区分概念分析与经验论证",
        "论点逐点列需反驳的前提；结论说清范围",
        "注意作者与被指观点一致不一致",
        "哲学论证用 steelman 而非 strawman",
    ),
    key_venues=(
        "Mind",
        "Philosophical Review",
        "Journal of Philosophy",
        "Ethics",
        "Noûs",
        "Analysis",
    ),
    units_and_formulas_notes=(
        "无需数值或实证数据",
        "论证有效性用真值表/模型可判",
        "概念分析举例（Gettier/trolley 顺序互证）",
        "逻辑符号遵循标准规范",
        "引用哲学传统给标准页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX 排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "EndNote", "Mendeley", "PhilArchive 预印本平台", "Stanford Encyclopedia of Philosophy (SEP)", "LogicGator 逻辑证明", "LogiQA 逻辑工具", "ProofGardener 证明", "Tweagoo 逻辑工具", "Lean 4 逻辑证明", "Word（Microsoft Office）", "Argument mapping（Rationale）", "Venn diagrams 工具", "CSL 引用样式管理", "QCA 定性比较分析", "CTEXT 中国哲学书电子化计划", "MindManager", "Coq（形式化证明）"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "PhilPapers", "CNKI", "JSTOR 数据库", "PhilPapers 哲学数据库"),
)
