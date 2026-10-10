"""文学研究学科论文支持：文本细读、批评理论与文学体裁、MLA 引用与文本分析记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="literary_studies",
    aliases=("literary_studies", "文学研究", "文学批评", "批评理论",
             "literary criticism", "literary theory", "文本细读",
             "文学分析", "文学理论", "比较文学"),
    paper_types={
        "research": ("abstract", "introduction（问题与理论框架）",
                     "methodology（分析方法）", "analysis（文本分析）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（作品/文本描述）",
                       "analysis（细读分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="MLA 9（文学与人文学科标准）",
    reporting_standards={
        "text_analysis": "文本分析须给出版本依据（版次、编校）",
        "close_reading": "细读须注明引文页码与版本",
        "comparative": "比较研究须说明比较方法论",
        "systematic_review": "PRISMA 系统综述声明",
        "theory": "理论阐释须交代概念谱系",
        "digital_humanities": "数字人文遵循 DH 报告规范",
    },
    conventions=(
        "引用遵循 MLA 9 格式（作者+页码）",
        "文本引用须标明版次与页码",
        "术语首现给英文原词与定义",
        "理论框架须交代核心概念",
        "比较研究须说明比较方法论",
        "参考文献遵循 MLA 9 格式",
    ),
    key_venues=(
        "PMLA",
        "ELH",
        "New Literary History",
        "Comparative Literature",
        "Representations",
        "Critical Inquiry",
    ),
    units_and_formulas_notes=(
        "文本引用以页码/行号标记",
        "版本差异须说明",
        "引文长度超过 40 词须用缩进块引用",
        "注释遵循脚注/尾注规范",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX", "Overleaf", "Zotero", "EndNote", "Mendeley", "RefWorks", "Google Docs", "Microsoft Word", "Python（NLTK/spacy）", "R（tidytext）", "AntConc", "Voyant Tools", "Jupyter Notebook", "JupyterLab", "Scrivener", "Adobe Acrobat", "Archive.org", "Project Gutenberg", "Collate（数字校勘）", "Dawson（Digital Philology）"),
    category="文学",
    databases=("JSTOR", "Project Gutenberg", "CNKI", "万方", "OpenAlex", "Google Scholar"),
)
