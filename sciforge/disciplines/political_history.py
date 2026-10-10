"""政治史论文支持：政治制度演变、政治思想史、政治变迁与历史政治分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="political_history",
    aliases=("political_history", "政治史", "政治历史", "Political History", "历史政治学", "Historical Political Science", "政治思想史", "近代史", "政治变迁", "Political Development"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式",
    reporting_standards={"AHA": "美国历史协会报告规范", "JSTOR": "历史文献引用规范", "RGS": "皇家地理学会地图规范"},
    conventions=("史料引用须标注馆藏号与页码", "首次出现用全称", "地图须含比例尺与数据来源", "时间线须注明时区", "引文须注明版本与页码"),
    key_venues=("American Historical Review", "Past & Present", "Journal of Modern History", "History Workshop Journal", "历史研究"),
    units_and_formulas_notes=("年代用公元或年号", "地图须含比例尺", "文献引用须注明页码", "时间线须注明时区"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "LaTeX", "Python (Text Analysis)", "NVivo", "ATLAS.ti", "MAXQDA", "QGIS", "ArcGIS Pro", "MapSource", "MapTiler", "Google Books Ngram", "AntConc", "Voyant Tools", "Tableau", "Microsoft Excel", "Adobe Photoshop", "Adobe InDesign", "CamScanner"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "WorldCat"),
)