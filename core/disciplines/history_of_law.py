"""法律史学科论文支持：典章沿革、判例研究与法制史体裁、Chicago 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_law",
    aliases=("history_of_law", "法律史", "法制史", "法史学", "法律沿革", "司法史"),
    paper_types={
        "research": ("abstract", "introduction（问题与法律背景）", "methodology（法源与判例方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（判例/律例个案）", "analysis（法源与判例分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（法史学综述）", "evidence synthesis（法源综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"case": "判例须给出案号与裁判机构", "statute": "法条引用须给出颁布年份与修订版本", "comparison": "比较法史须给出可比时点"},
    conventions=("法源须区分制定法、判例与习惯法", "法律名称与编号须一致", "修订版本须给出与旧版对照", "术语用原语并注明译名", "裁判日期用统一纪年"),
    key_venues=("Law and History Review", "Journal of Legal History", "Legal History", "Chinese Law Review", "中国法史研究"),
    units_and_formulas_notes=("判例给出案号与裁判机构", "法条给出颁布日期与修订版本", "引用给出条款与子款编号", "跨法域引用须注明适用地域"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "Dia", "Cytoscape", "Notepad++", "FairCopy"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "Google Scholar", "ProQuest Historical Newspapers", "JSTOR"),
)
