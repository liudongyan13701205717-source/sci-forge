"""森林巡护学科论文支持：森林资源调查、林政执法、生态保护与遥感监测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forest_ranging",
    aliases=("forest_ranging", "forest surveying", "森林巡护", "林政执法", "森林资源调查", "森林保护", "林业管理", "野外调查"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "plot": "样地调查须遵循标准化样地布设方法",
        "allometry": "林分参数须遵循标准化测量方法",
        "remote": "遥感监测须遵循标准化分类方法",
        "carbon": "碳汇估计须遵循标准化方法"
    },
    conventions=(
        "树种用拉丁学名（首次出现时附中文名）",
        "林分参数用标准术语（DBH、树高、断面积）",
        "胸径用 cm（DBH）；树高用 m",
        "生长量用 m³/ha/year",
        "样地布设方式须用统一术语"
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Canadian Journal of Forest Research",
        "Journal of Forestry",
        "New Forests",
        "Silvae Genetica"
    ),
    units_and_formulas_notes=(
        "胸径用 cm（DBH）",
        "树高用 m",
        "断面积用 m²",
        "蓄积量用 m³/ha",
        "生长率用 m³/ha/year"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "ENVI", "R", "Python", "MATLAB", "DBH caliper", "Height laser", "Hypso meter", "Drone", "LIDAR", "Multispectral camera", "Soil sampling", "Forest plot measurement", "Tree species identification", "Biomass estimation", "Carbon flux measurement", "Satellite imagery", "Mobile mapping", "Wildlife camera trap"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
