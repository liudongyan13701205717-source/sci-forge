"""哲学与宗教研究学科论文支持：神学/比较宗教/宗教哲学体裁、Chicago/APA 引用样式与神学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philosophy_and_religious_studies",
    aliases=("philosophy and religious studies", "哲学与宗教研究",
             "religion", "religion studies", "宗教研究", "神学",
             "比较宗教", "宗教学", "philosophy of religion", "宗教哲学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "argument（论证）",
            "analysis（分析）",
            "objections（反驳）",
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
    citation_style="Chicago 或 APA 样式（宗教研究/神学常用 Chicago 注-书目）",
    reporting_standards={
        "argument": "核心论点须独立于证据简述",
        "textual": "文本研究遵循宗教学文献学规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 COREQ/SRQR 规范",
        "comparative": "比较研究遵循 Comparative Religion 规范",
        "religious_text": "宗教文本遵循 IUGS/文本批评规范",
    },
    conventions=(
        "神名与宗教术语用中文并注译原文",
        "文本给出版本与卷次",
        "比较宗教给出传统背景",
        "区分神学与宗教学",
        "时间给出宗教历法与公历",
    ),
    key_venues=(
        "Religion",
        "Journal for the Scientific Study of Religion",
        "Journal of Religious Ethics",
        "Zenkai",
        "New Blackfriars",
        "Philosophia Christi",
    ),
    units_and_formulas_notes=(
        "时间给出宗教历法与公历",
        "文本给出版本与卷次",
        "引用给出页码",
        "术语用中文并注译原文",
        "比较宗教给出传统背景",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX 神学排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "EndNote", "Mendeley", "PhilArchive 预印本平台", "Stanford Encyclopedia of Philosophy (SEP)", "BibleWorks 圣经研究", "Logos Bible Software", "SBL Bible Software", "LogicGator 逻辑证明", "LogiQA 逻辑工具", "ProofGardener 证明", "Lean 4 逻辑证明", "Word（Microsoft Office）", "Argument mapping（Rationale）", "CSL 引用样式管理", "数字圣经/宗教典籍库", "Accordance Bible Software", "Coq（形式化证明）"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "PhilPapers", "CNKI", "ProQuest", "JSTOR 数据库", "PhilPapers 哲学数据库"),
)
