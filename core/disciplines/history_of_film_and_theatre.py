"""电影与戏剧史学科论文支持：影像档案、剧本文本与影视批评体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_film_and_theatre",
    aliases=("history_of_film_and_theatre", "电影与戏剧史", "电影史", "戏剧史", "影视史", "表演艺术史"),
    paper_types={
        "research": ("abstract", "introduction（作品与背景）", "methodology（文本与影像方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品个案）", "analysis（影像与文本分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（电影/戏剧理论综述）", "evidence synthesis（作品综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"film": "影片引用须给出片长与时间点", "theatre": "演出史须给出日期与剧团", "script": "剧本引用须给出场次与时点"},
    conventions=("影片名用斜体", "导演/演员姓名须给出国际通用译名", "时间点用 mm:ss 或 hh:mm:ss 记录", "馆藏版本须注明", "首次放映与首次公映须区分"),
    key_venues=("Cinema Journal", "Journal of Film and Video", "Film History", "Twentieth Century Theatre", "当代电影"),
    units_and_formulas_notes=("影片时间用 mm:ss 记录", "胶片格式与画幅比例须给出", "剧本版本用印刷与演出版本区分", "首映日期用当地历法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Cytoscape", "Voyant Tools", "AntConc", "ELAN", "R", "Python", "QGIS", "Juxta", "CollateX", "LaTeX", "ImageJ", "Nodegoat", "Recogito", "Transkribus", "Final Cut Pro"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
