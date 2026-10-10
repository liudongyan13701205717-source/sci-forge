"""艺术史学科论文支持：图像学、风格分析与跨文化比较体裁、Chicago 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_art",
    aliases=("history_of_art", "艺术史", "视觉艺术史", "图像学", "风格史", "美术史"),
    paper_types={
        "research": ("abstract", "introduction（作品与背景）", "methodology（图像学与风格方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品个案）", "analysis（图像与风格分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（艺术史理论综述）", "evidence synthesis（作品综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"imagery": "作品引证须给出馆藏与图版", "style": "风格判定须给出参照", "exhibition": "展览史须给出时间与地点"},
    conventions=("作品名称用斜体或引号一致", "图版须给出比例与来源", "藏品编号须给出馆藏", "画家/艺术家名用通用译名", "作品日期须给出区间"),
    key_venues=("Art Bulletin", "Journal of the History of Ideas", "Oxford Art Journal", "Art History", "美术研究"),
    units_and_formulas_notes=("尺寸用 cm × cm 记录", "媒介质与画幅须给出", "作品日期注明创作与首次公开展出", "馆藏编号须与图版一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Cytoscape", "Voyant Tools", "AntConc", "ImageJ", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "Inkscape", "GIMP", "Nodegoat", "Recogito", "Transkribus"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
