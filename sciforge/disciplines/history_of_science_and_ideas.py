"""科学思想史学科论文支持：科学史、思想史、科学哲学与科学传播研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_science_and_ideas",
    aliases=("history_of_science_and_ideas", "科学思想史", "科学史", "思想史", "科学哲学", "科学传播", "History of Science", "History of Ideas", "Science Studies"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17",
    reporting_standards={"k1": "HPS International Guidelines", "k2": "ISIMH 会议论文规范", "k3": "GB/T 7714 参考文献标准"},
    conventions=("史料须标注馆藏编号与页码", "译名须保留原语并附首次出现的英文原名", "引文须区分直接引语与转述", "概念史研究须注明术语的历史语用", "数字人文分析须公布数据集与代码"),
    key_venues=("Isis", "Studies in History and Philosophy of Science", "History of Science", "Annals of Science", "Science, Technology, & Human Values"),
    units_and_formulas_notes=("年代须区分公元纪年与干支/民国纪年", "度量衡换算须注明基准年代", "术语演变须给出双语对照", "文献考据须注明来源版本"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "Dia", "Cytoscape", "Notepad++", "FairCopy"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
