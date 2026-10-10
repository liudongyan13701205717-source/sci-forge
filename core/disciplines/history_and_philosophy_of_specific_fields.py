"""具体领域科学与哲学学科论文支持：科学哲学、科学社会学与跨学科反思。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_and_philosophy_of_specific_fields",
    aliases=("history_and_philosophy_of_specific_fields", "具体领域科学与哲学", "科学哲学", "技术哲学", "认知科学哲学", "科学社会学"),
    paper_types={
        "research": ("abstract", "introduction（问题与哲学背景）", "methodology（论证方法）", "results（结论）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（论证分析）", "results（结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"argumentation": "哲学论证须给出反例与反驳", "empirical": "经验证据须给出样本与方法", "literature": "文献综述须按时间脉络"},
    conventions=("术语须给出精确定义与出处", "论证结构须显式化", "经验与先验须区分", "哲学结论须给出适用边界", "对反例的回应须显式"),
    key_venues=("Philosophy of Science", "Synthese", "Mind", "Philosophical Studies", "科学技术与辩证法"),
    units_and_formulas_notes=("形式化论证须给出符号表", "模型与假设须分开陈述", "引用给出页码", "跨语言引文须给出原文与译文"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Juxta", "CollateX", "Gephi", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Omeka S", "Nodegoat", "Recogito", "Tropy", "Transkribus", "LaTeX", "Dia", "Cytoscape", "FairCopy", "OxGarage", "Notepad++"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "Google Scholar"),
)
