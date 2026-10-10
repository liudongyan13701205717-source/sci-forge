"""技术史学科论文支持：技术演化、工程史与产业技术史研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_technology",
    aliases=("history_of_technology", "技术史", "工程史", "工业史", "产业技术史", "Technology History", "Engineering History", "Industrial History", "Technological Change"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17",
    reporting_standards={"k1": "IEEE History Society Guidelines", "k2": "ISIF 技术史写作规范", "k3": "GB/T 7714 参考文献标准"},
    conventions=("专利号须标注国家与年代", "机器参数须注明单位与年代", "口述史须标注录音编号与访谈者", "档案引用须附馆藏与档号", "技术图须注明原始出处与修改"),
    key_venues=("Technology and Culture", "IEEE Annals of the History of Computing", "History of Technology Journal", "Technical Vision", "Annals of Science"),
    units_and_formulas_notes=("功率单位须标注 kW/hp 与年代", "效率换算须注明口径", "档案时间须统一为公制", "技术图须保留比例尺"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "Dia", "Cytoscape", "FreeCAD", "KiCad"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus Engineering History"),
)
