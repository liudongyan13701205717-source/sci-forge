"""中世纪与文艺复兴研究学科论文支持：历史文献与艺术史。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medieval_and_renaissance_studies",
    aliases=("medieval_and_renaissance_studies", "中世纪文艺复兴研究", "medieval studies", "renaissance", "早期现代史", "艺术史", "人文主义"),
    paper_types={
        "research": ("abstract", "introduction（历史背景）", "methodology（史料方法）", "results（发现与论证）", "discussion（史学意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（史料/作品）", "analysis（文本/图像分析）", "results（结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（史学传统）", "evidence synthesis（史料综合）", "future directions", "references"),
    },
    citation_style="Chicago 17",
    reporting_standards={"k1": "史料引用须注明馆藏编号与抄本", "k2": "年代测定须说明方法（碳-14、树轮等）", "k3": "翻译文献须注明译者与版本"},
    conventions=("史料引用用脚注（Chicago）", "人名/地名保留原文拼写", "作品引用须注明馆藏与编号", "日期须说明历法（儒略/格里高利）", "术语须附原文（拉丁/古法语等）"),
    key_venues=("Speculum", "Journal of Medieval History", "Renaissance Quarterly", "Mediaeval Studies", "Persuasions"),
    units_and_formulas_notes=("日期标注历法与世纪", "度量须注明中世纪单位（foot、rod 等）", "抄本引用用 folio/recto/verso", "文献引用注明出版年"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("PaleoGraph", "LAC (Linked Art Collaboration)", "Medievalists.net", "Bibliothèque nationale de France Digital", "Vatican Library", "British Library DigiPal", "Terra", "Socratica", "Zotero", "EndNote", "LaTeX", "Mapbox", "QGIS", "Tableau", "Python (NLTK)", "Cyrus Korista", "Luminance", "ImageJ", "HathiTrust", "OpenEdition"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
