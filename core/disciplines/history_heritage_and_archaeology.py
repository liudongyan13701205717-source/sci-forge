"""历史遗产与考古学科论文支持：文化遗产、遗址保护与档案管理体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_heritage_and_archaeology",
    aliases=("history_heritage_and_archaeology", "历史遗产与考古", "文化遗产", "遗产研究", "文物与博物馆", "遗产管理"),
    paper_types={
        "research": ("abstract", "introduction（遗产与背景）", "methodology（田野与档案方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（遗产个案）", "analysis（分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（遗产理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"conservation": "保护性报告须给出条件与建议", "excavation": "发掘报告遵循 Stratigraphic Monograph", "curatorial": "馆藏记录须可追溯"},
    conventions=("遗产编号须给出标准编号", "文物绘图须注明比例", "保护状态须用统一术语", "档案出处须可核查", "跨机构藏品须注明归属"),
    key_venues=("World Archaeology", "Archaeological Management", "Museum Management and Curatorship", "Heritage Studies", "文物"),
    units_and_formulas_notes=("遗址坐标须给出标准坐标系", "文物材质检测须给出方法与仪器", "年代须给出区间与置信度", "比例尺须注明分度"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("QGIS", "ArcGIS", "Photoscan", "CloudCompare", "MeshLab", "Pix4D", "Rapidform", "Harris Matrix Studio", "Tropy", "Omeka", "Zotero", "EndNote", "Python", "R", "LaTeX", "Adobe Illustrator", "AutoCAD", "Microsoft Office", "Sediment Analyzer", "Find Register"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
