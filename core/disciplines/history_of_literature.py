"""文学史学科论文支持：文本细读、文体学与文学批评史体裁、MLA 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_literature",
    aliases=("history_of_literature", "文学史", "文学批评史", "文学研究", "文体学", "文本学"),
    paper_types={
        "research": ("abstract", "introduction（作品与问题）", "methodology（文本与批评方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品个案）", "analysis（文本细读）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（文学理论综述）", "evidence synthesis（作品综合）", "future directions", "references"),
    },
    citation_style="MLA 9（文学规范）",
    reporting_standards={"close_reading": "文本引证须给出卷页或行号", "edition": "文本版本须给出校勘信息", "translation": "译文须注明译者与版次"},
    conventions=("文本版本须给出校勘记", "首次引用给出行号，后续简称作者-行号", "引文超过 40 词须块引", "译名须与原语对照", "诗歌须保留分行"),
    key_venues=("PMLA", "Modern Language Notes", "Comparative Literature Studies", "Literature and Theory", "中国现代文学研究丛刊"),
    units_and_formulas_notes=("文本引证给出卷页或行号", "版本须给出刊印年与版次", "译名与原语并列", "标点须与原文一致并注明是否改排"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "R", "Python", "Juxta", "CollateX", "FairCopy", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "Dia", "Cytoscape", "Stylo", "Notepad++"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
