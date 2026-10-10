"""历史学学科论文支持：史学/档案/比较体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history",
    aliases=("history", "历史学", "史学", "历史研究", "史学史", "史料学", "历史学理论"),
    paper_types={
        "research": ("abstract", "introduction（问题与背景）", "methodology（史料与方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案史述）", "analysis（史料分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（史学史回顾）", "evidence synthesis（史料综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目或作者-年份）",
    reporting_standards={"archival": "档案研究史料考证规范", "comparative": "比较历史研究方法规范", "qualitative": "质性研究 SRQR 报告规范"},
    conventions=("史料来源与版本须注明", "一手与二手史料须区分", "时间与纪年须统一", "史学史脉络须交代", "解释框架须明确"),
    key_venues=("American Historical Review", "Past & Present", "Journal of Modern History", "The Historical Journal", "History Workshop Journal"),
    units_and_formulas_notes=("引文给出页码", "古籍用卷/篇/页标注", "版本与版次须注明", "货币用统一币种并注明年份"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Tropy", "Zotero", "Transkribus", "Omeka S", "Nodegoat", "Recogito", "Gephi", "Palladio", "QGIS", "ArcGIS", "Voyant Tools", "AntConc", "R", "Python", "Juxta", "CollateX", "FairCopy", "OxGarage", "eScriptorium", "LaTeX"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest Historical Newspapers"),
)
