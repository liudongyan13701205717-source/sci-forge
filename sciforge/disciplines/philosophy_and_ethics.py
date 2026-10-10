"""哲学与伦理学学科论文支持：规范伦理/应用伦理/生命伦理体裁、APA/Chicago 引用样式与伦理学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philosophy_and_ethics",
    aliases=("philosophy and ethics", "哲学与伦理学", "伦理学",
             "applied ethics", "applied philosophy", "生命伦理",
             "规范伦理", "道德哲学", "医学伦理", "商业伦理"),
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
            "analysis（伦理分析）",
            "results（结论）",
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
    citation_style="APA 或 Chicago 样式（伦理学/生命伦理学常用）",
    reporting_standards={
        "argument": "核心论点须独立于证据简述",
        "case": "伦理案例遵循 Hastings Center 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "life_ethics": "生命伦理遵循 ICH-GCP 与生命伦理原则",
        "empirical": "实证研究遵循 COREQ/SRQR 规范",
        "consensus": "共识研究遵循 Delphi 方法",
    },
    conventions=(
        "伦理原则（不伤害/行善/自主/公正）须明确",
        "案例给出时间与背景",
        "引用伦理原则给标准文献",
        "术语用中文并注译",
        "区分规范伦理与描述伦理",
    ),
    key_venues=(
        "Ethics",
        "Journal of Applied Philosophy",
        "Bioethics",
        "Journal of Medical Ethics",
        "The Hastings Center Report",
        "Philosophy, Public Policy, and Ethics",
    ),
    units_and_formulas_notes=(
        "伦理原则须明确",
        "案例须给出时间与背景",
        "引用给出页码",
        "术语用中文并注译",
        "区分规范伦理与描述伦理",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX 哲学排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "EndNote", "Mendeley", "PhilArchive 预印本平台", "Stanford Encyclopedia of Philosophy (SEP)", "Hastings Center 生命伦理案例库", "EthicDB 伦理案例库", "LogicGator 逻辑证明", "LogiQA 逻辑工具", "ProofGardener 证明", "Lean 4 逻辑证明", "Word（Microsoft Office）", "Argument mapping（Rationale）", "QCA 定性比较分析", "CSL 引用样式管理", "CTEXT 中国哲学书电子化计划", "Tweagoo 逻辑工具", "Coq（形式化证明）"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "PhilPapers", "CNKI", "JSTOR 数据库", "PhilPapers 哲学数据库"),
)
