"""应用伦理学科论文支持：医学伦理、生命伦理、科技伦理、商业伦理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_ethics",
    aliases=(
        "applied ethics",
        "Applied Ethics",
        "应用伦理",
        "医学伦理",
        "生命伦理学",
        "bioethics",
        "科技伦理",
        "工程伦理",
        "business ethics",
        "商业伦理",
        "AI 伦理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "conceptual analysis（关键概念界定）",
            "case or scenario（案例呈现）",
            "ethical argumentation（论证与反驳）",
            "conclusions and recommendations",
            "references",
        ),
        "case_analysis": (
            "abstract",
            "case description",
            "ethical issues identified",
            "analysis with theories",
            "resolution and reflection",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical landscape",
            "controversies and debates",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes-Bibliography 或 APA 7（哲学主流用 Chicago）",
    reporting_standards={
        "concepts": "核心概念（如 autonomy、consent、fairness）须给出权威界定并说明选择理由",
        "case": "案例须真实或注明虚构；涉及真人须匿名化并获知情同意",
        "argument": "论证须明确前提与结论，标注反驳（objections）与回应（replies）",
        "theories": "涉及伦理理论（义务论/功利论/德性论/关怀伦理）须给出对应原则",
        "recommendations": "政策/实践建议须可行，并讨论潜在后果",
    },
    conventions=(
        "论证采用「命题-反驳-回应-结论」结构，每段推进一步",
        "关键术语首次出现给英文原词与中文对照（如 autonomy 自主性）",
        "引用哲学家观点时准确归属（作者+著作+年份+页码）",
        "案例呈现先事实后评价，避免先入为主的预设",
        "参考文献以英文原典为主；中译本注明译者与出版年",
    ),
    key_venues=(
        "Journal of Applied Philosophy",
        "Journal of Medical Ethics",
        "Bioethics",
        "Ethics",
        "Philosophy & Technology",
        "Ethics and Information Technology",
    ),
    units_and_formulas_notes=(
        "无统计要求；论证以哲学推理为主",
        "如涉及经验证据须给出数据来源与抽样方法",
        "引用伦理守则（如《赫尔辛基宣言》《纽伦堡法典》）给出条款号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("PhilPapers", "PhilArchive", "Stanford Encyclopedia of Philosophy", "Zotero", "Mendeley", "EndNote", "LaTeX", "Overleaf", "MS Word", "Google Docs", "IRB 系统（Viva/iRecruitment）", "Coq", "Prover9", "TPTP", "LogiFact", "Ethical Decision Support（EDS）", "ResearchGate", "Semantic Scholar", "Diderot（伦理决策支持）", "Toulmin Map（论证图示）"),
    category="哲学",
    databases=("PhilPapers", "PhilArchive", "Web of Science", "OpenAlex", "Crossref", "CNKI", "Google Scholar", "JSTOR"),
)
