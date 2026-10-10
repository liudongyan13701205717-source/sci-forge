"""翻译项目学科论文支持：翻译教学、译者培养与翻译课程评估体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="translation_programmes",
    aliases=("translation_programmes", "翻译项目", "翻译教育", "翻译教学",
             "翻译培训", "translation education", "translation pedagogy"),
    paper_types={
        "research": (
            "abstract",
            "introduction（教学背景与问题）",
            "literature review（文献综述）",
            "methods（教学设计与评估方法）",
            "results（教学成效与数据）",
            "discussion（讨论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（教学分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "teaching_evaluation": "教学评估遵循同行评议与学习成效标准",
        "survey": "调查遵循 AAPOR 规范",
        "qualitative": "质性研究遵循 COREQ/SRQR",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "课程大纲与学时须注明",
        "教学目标须明确",
        "评估方法与量表须声明",
        "数据来源须说明",
        "术语遵循 ISO 17100",
    ),
    key_venues=(
        "The Translation Journal",
        "Meta",
        "Babel",
        "Target",
        "Perspectives",
    ),
    units_and_formulas_notes=(
        "学时用 学分/小时 表示",
        "翻译评估用 词/小时",
        "MT 质量用 BLEU 分数",
        "统计结果用 均值±标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Trados Studio", "memoQ", "Phrase TMS", "OmegaT", "Wordfast", "Sketch Engine", "LAWCOR", "DeepL", "Google Translate", "Microsoft Translator", "Zoom", "KUDO", "Interprefeting", "SPSS", "R", "Zotero", "WordStat", "LaTeX"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
