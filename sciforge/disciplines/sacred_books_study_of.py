"""圣经学学科论文支持：文本考证、历史解释与比较宗教研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sacred_books_study_of",
    aliases=(
        "sacred_books_study_of",
        "圣经学",
        "biblical studies",
        "圣经典籍",
        "旧约",
        "新约",
        "textual criticism",
        "神学研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与文献综述）",
            "methodology（方法与文献基础）",
            "results（分析结果）",
            "discussion（讨论）",
            "references",
        ),
        "commentary": (
            "abstract",
            "introduction",
            "textual analysis（文本分析）",
            "historical context（历史背景）",
            "thematic discussion（主题讨论）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与批评综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="SBL 或 APA 7",
    reporting_standards={
        "textual_criticism": "抄本传统与异文须注明编号",
        "historical_grmatism": "年代学方法与假定须说明",
        "reception_history": "译本/诠释谱系须给出来源",
    },
    conventions=(
        "章节引用用 BHS、NRSV 等版本编号并注明版本",
        "抄本编号用国际编号（如 P⁴⁶、א 等）",
        "希伯来/希腊原文须附转写或注释",
        "术语表列出专业词与原文对照",
        "参考文献按语言分组（希伯来、希腊、拉丁、现代）",
    ),
    key_venues=(
        "Journal of Biblical Literature",
        "Novum Testamentum",
        "Vetus Testamentum",
        "Jewish Quarterly Review",
        "Journal of Theological Studies",
    ),
    units_and_formulas_notes=(
        "文献引用用页码/节号；抄本年份给出 BCE/CE 与世纪",
        "术语首次出现给原文、转写与释义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Bible Works Software", "Logos Bible Software", "Accordance Bible Software", "SBL Greek/Hebrew Fonts", "Logos Lexicon", "NET Bible", "Digital Scriptorium", "Trismegistos Search Platform", "Perseus Digital Library", "Papyri.info", "Dead Sea Scrolls Database", "Epigraphical Database", "Interlinear Bible Platform", "Endnote", "Zotero", "Mendeley", "LaTeX with biblatex", "MATLAB Statistical Toolkit", "R with topicmodelling", "Python TextBlob"),
    category="文学",
    databases=("OpenAlex", "Crossref", "ATLA Religion Database"),
)
