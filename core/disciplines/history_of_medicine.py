"""医学史学科论文支持：疾病史、医疗制度史与医疗技术史体裁、Chicago 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_medicine",
    aliases=("history_of_medicine", "医学史", "疾病史", "医疗史", "医史", "健康史"),
    paper_types={
        "research": ("abstract", "introduction（疾病/制度与背景）", "methodology（史料与文献方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案史述）", "analysis（史料分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（医学史综述）", "evidence synthesis（史料综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"disease": "疾病史须给出首次记载与诊断", "institution": "制度史须给出文献与档案出处", "technique": "技术史须给出装置与操作文献"},
    conventions=("疾病名须给出原语与现代名", "医史年代须与当时医学文献对照", "医家与学派须给出谱系", "医案须给出原始出处", "术语须区分当时与今译"),
    key_venues=("Bulletin of the History of Medicine", "Isis", "Journal of the History of Medicine and Allied Sciences", "Social History of Medicine", "医史月刊"),
    units_and_formulas_notes=("疾病流行时间用流行学年份", "文献日期以原始出版年为准", "医家谱系须给出师承关系", "医案出处给出馆藏编号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "Dia", "Cytoscape", "Notepad++", "FairCopy"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed", "JSTOR", "ProQuest Historical Newspapers", "HeinOnline"),
)
