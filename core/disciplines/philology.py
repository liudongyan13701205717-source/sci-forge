"""语言学研究学科论文支持：文本批评/比较/古籍整理体裁、MLA/Chicago 引用样式与文献学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philology",
    aliases=("philology", "语言学研究", "文献学", "文本批评",
             "比较语言学", "文字学", "古典文献学", "校勘学",
             "first language", "textual criticism", "古籍整理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "methodology（方法学）",
            "results（研究成果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（文本分析）",
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
    citation_style="MLA 或 Chicago 样式（人文/古典研究常用 MLA；古籍按 IUGS 规范）",
    reporting_standards={
        "textual_criticism": "文本批评遵循 Lachmann/Western Collation 规范",
        "codicology": "手稿版本遵循 Codicology 规范",
        "philological": "校勘遵循传统校勘学",
        "comparative": "比较研究遵循 Comparative Linguistics 规范",
        "corpus": "语料库研究遵循 ELRA/ELDC 规范",
        "digital_humanities": "数字人文遵循 TEI 规范",
    },
    conventions=(
        "古籍原文须给出版本与卷次",
        "术语给出原文与译文",
        "引用版本须注明版本年代与编者",
        "异文须列异文表",
        "文献学注记遵循 IUGS 规范",
    ),
    key_venues=(
        "Transactions of the Philological Society",
        "Classical Philology",
        "Harvard Studies in Classical Philology",
        "Journal of Chinese Philology",
        "中国古籍研究",
        "Language History and Change",
    ),
    units_and_formulas_notes=(
        "时间用朝代/年号/公元",
        "版本用年代与卷次",
        "引用给出页码与卷次",
        "文献学符号遵循 IUGS 规范",
        "比较语言学用国际音标（IPA）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Sketch Engine 语料库", "AntConc 语料库分析", "CLiPS 语料库工具", "CQPweb 语料库检索", "Logos Bible Software 圣经研究", "CollateX 文本比较", "TextMatch 文本比对", "TEI XML 文本编码", "LaTeX 排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "Mendeley", "EndNote", "Word（Microsoft Office）", "中国基本古籍库", "中华古籍资源库", "CTEXT 中国哲学书电子化计划", "Unicode IPA 输入", "Python 文本分析（NLTK/spaCy）", "Transkribus（手稿识别）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest", "PhilPapers 哲学数据库"),
)
