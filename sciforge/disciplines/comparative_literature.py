"""比较文学学科论文支持：跨文化/主题/影响体裁、MLA 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="comparative_literature",
    aliases=("comparative_literature", "比较文学", "跨文化文学研究", "影响研究",
              "comparative literature", "cross-cultural literary studies",
              "influence study", "文学接受研究", "reception studies",
              "世界文学", "world literature", "intercultural literature",
              "跨文化文学", "literary translation studies", "文学翻译研究",
              "比较诗学", "comparative poetics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "textual analysis（文本分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "comparative_study": (
            "abstract",
            "introduction",
            "corpus（比较对象）",
            "framework（框架）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "influence_study": (
            "abstract",
            "introduction",
            "source（源文本）",
            "reception（接受）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="MLA 样式（作者-页码；Comparative Literature 遵循 MLA 规范）",
    reporting_standards={
        "textual": "文本分析遵循文本分析报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "translation": "翻译分析遵循翻译分析报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "版本与校勘须注明",
        "引文给出页码",
        "译文给出原文页码",
        "跨文化语境须交代",
        "理论框架须明确",
    ),
    key_venues=(
        "Comparative Literature",
        "Comparative Literature Studies",
        "PMLA",
        "Modern Language Quarterly",
        "World Literature Today",
        "Journal of World Literature",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "译文给出原文页码",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("AntConc", "Sketch Engine", "Lexica", "eHRAF (Yale)", "EndNote", "Zotero", "Mendeley", "LaTeX", "Overleaf", "Gephi", "Voyant Tools", "DeepL", "Google Books Ngram Viewer", "Trados", "RefWorks", "JabRef", "World Literature Today", "Python (NLTK/ spaCy)", "R (quanteda)", "Microsoft Excel", "Tableau", "ConText", "WordSmith Tools", "Babel Fish", "Google Translate", "GitHub"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "JSTOR", "ProQuest", "Worldcat", "Google Scholar"),
)