"""英国文学学科论文支持：英国文学、文学理论与批评研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="english_literature",
    aliases=(
        "english_literature", "英国文学", "英语文学",
        "English literature", "英国文学",
        "English literary studies", "英国文学研究",
        "British literature", "英国文学",
        "literary criticism", "文学批评",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（文学问题与理论背景）",
            "methodology（文本分析、理论框架、批评方法）",
            "results（文学分析与批评）",
            "discussion（文学理论与实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "work analysis（作品分析）",
            "critical analysis（批评分析）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "major works（重要作品分析）",
            "future trends",
            "references",
        ),
    },
    citation_style="MLA",
    reporting_standards={
        "analysis": "文本分析须注明版本与页码",
        "theory": "理论框架须明确",
        "citation": "引用须注明版本与页码",
    },
    conventions=(
        "作品首次出现给出标题、作者、年份与版本",
        "引用须注明版本与页码",
        "文学术语须使用行业标准",
        "翻译作品须注明译者与版本",
    ),
    key_venues=(
        "PMLA",
        "ELH",
        "Modern Language Quarterly",
        "Studies in English Literature",
        "Journal of English and Germanic Philology",
        "Review of English Studies",
    ),
    units_and_formulas_notes=(
        "作品首次出现给出标题、作者、年份与版本",
        "引用须注明版本与页码",
        "文学术语须使用行业标准",
        "翻译作品须注明译者与版本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "RefWorks", "NVivo", "Atlas.ti", "AntConc", "Sketch Engine", "CLAN", "LaCA (Lancaster Corpus Analyse)", "Voyant Tools", "TEI Publisher", "LaTeX", "R (RStudio)", "Python (pandas, nltk)", "MarginNote", "VOSviewer", "CiteSpace", "Wordfreq", "Sigil"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
