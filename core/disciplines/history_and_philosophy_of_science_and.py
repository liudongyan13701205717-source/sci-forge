"""科学与技艺史学科论文支持：科学史、技艺史、STS 交叉体裁与实验史方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_and_philosophy_of_science_and",
    aliases=("history_and_philosophy_of_science_and_technology", "科学与技艺史", "科学史", "技艺史", "STS", "科学技术史"),
    paper_types={
        "research": ("abstract", "introduction（问题与史学背景）", "methodology（文献与实验史方法）", "results（发现）", "discussion（解释与理论）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案史述）", "analysis（史料与技术分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（科学史综述）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"experimental_history": "实验史须给出可重复的复现条件", "archival": "档案史料须给出库藏编号", "philosophical": "哲学论证须给出反例讨论"},
    conventions=("科学文献须区分原始论文与后世评述", "术语须给出原语与首次使用时点", "仪器/装置须给出规格与制作者", "论证结构须区分描述与解释", "史学脉络须与哲学讨论分层"),
    key_venues=("Isis", "Studies in History and Philosophy of Science", "History of Science, Philosophy of Science and Physical Sciences", "Ambix", "科学史研究"),
    units_and_formulas_notes=("仪器数据须给出原单位与换算", "实验记录须给出日期与地点", "公式须与原文一致并注明来源", "文献日期以出版年为准"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Juxta", "CollateX", "FairCopy", "OxGarage", "Gephi", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Omeka S", "Nodegoat", "Recogito", "Tropy", "Transkribus", "LaTeX", "Dia", "Cytoscape", "Notepad++"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
