"""历史与考古学科论文支持：史前考古与文献互证、田野报告规范与年代学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_and_archaeology",
    aliases=("history_and_archaeology", "历史与考古", "考古学", "史前考古", "田野考古", "文物考古"),
    paper_types={
        "research": ("abstract", "introduction（遗址背景）", "methodology（田野与实验室方法）", "results（出土与测年结果）", "discussion（史学解释）", "references"),
        "case_study": ("abstract", "introduction", "case description（遗址描述）", "analysis（遗物分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（考古学史回顾）", "evidence synthesis（遗存综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"excavation": "田野发掘报告规范（Stratigraphic Monograph）", "dating": "测年数据须给出误差区间", "curation": "馆藏编号须可追溯"},
    conventions=("遗址坐标须用标准坐标系", "出土物须附编号与出土层位", "年代用统一纪年并注明误差", "地层关系须用 Harris Matrix 表述", "遗物绘图比例须注明"),
    key_venues=("Antiquity", "Journal of Archaeological Science", "American Antiquity", "Archaeological Investigations", "文物"),
    units_and_formulas_notes=("C14 用 BP（1950 基准）并注明 1σ", "地层号与探方号须统一", "出土物绘图比例为 1:n", "年代换算须注明校准曲线"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("QGIS", "ArcGIS", "Photoscan", "CloudCompare", "Rapidform", "MeshLab", "Pix4D", "FindsRegister", "Harris Matrix Studio", "TAS", "Zotero", "EndNote", "Python", "R", "LaTeX", "Microsoft Office", "Adobe Illustrator", "AutoCAD", "Omnivore", "Sediment Analyzer"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
