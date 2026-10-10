"""湖沼学学科论文支持：淡水生态/湖泊学体裁、Wiley 引用样式与湖沼学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="limnology",
    aliases=("limnology", "湖沼学", "淡水生态学", "freshwater ecology",
             "湖泊学", "lake science", "河流生态学", "river ecology",
             "浮游生物", "plankton", "水生态学", "水生生物学"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与水体系统）",
                     "materials and methods（采样与分析方法）",
                     "results（理化与生物数据）",
                     "discussion（生态过程与意义）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（站点/水体描述）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="Wiley 样式（作者-年份；Limnol. Oceanogr. 遵循 Wiley/ASLO 规范）",
    reporting_standards={
        "sampling_design": "采样点、频率与深度分层须报告",
        "water_chemistry": "水质参数（DO、pH、营养盐）测定方法须完整",
        "biological_methods": "浮游/底栖生物采样与鉴定方法须报告",
        "data_analysis": "统计与多元分析方法须给出",
        "site_context": "湖泊/河流地理与水文背景须说明",
        "ecological_assessment": "水质分类与营养状态指数须明确",
    },
    conventions=(
        "水体分层术语（epilimnion、metalimnion、hypolimnion）定义须给出",
        "营养盐符号（TN、TP、NO3-N）规范",
        "富营养化指标（Chl-a、Secchi 深度）统一",
        "浮游生物分类与计数单位（cells/L、ind./L）规范",
        "采样深度与日期完整记录",
        "参考文献遵循期刊风格（Wiley 作者-年份）",
    ),
    key_venues=(
        "Limnology and Oceanography",
        "Freshwater Biology",
        "Journal of Limnology",
        "Hydrobiologia",
        "Inland Waters",
        "Water Research",
    ),
    units_and_formulas_notes=(
        "营养盐浓度用 μg/L、mg/L；透明度用 m",
        "叶绿素 a 用 μg/L",
        "公式用 amsmath；营养状态指数（TSI）公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R (vegan)", "Python (pandas)", "RStudio", "Jupyter Notebook", "多参数水质在线传感器", "CTD 温盐深剖面仪", "浮游生物网具与显微镜", "EndNote", "Zotero", "Mendeley", "LaTeX", "Overleaf", "GraphPad Prism", "SPSS", "QGIS", "ArcGIS", "Excel", "Matplotlib", "Ocean Data View (ODV)", "R (phyloseq)"),
    category="理学",
    databases=("OpenAlex", "PubMed", "Zenodo", "Crossref", "DOAJ"),
)
