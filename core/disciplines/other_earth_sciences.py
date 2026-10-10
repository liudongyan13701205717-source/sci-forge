"""其他地球科学学科论文支持：未被细类归入的地质、地球物理与地球化学交叉研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_earth_sciences",
    aliases=(
        "other_earth_sciences", "其他地球科学",
        "other earth sciences", "其他地球科学",
        "geology", "地质学",
        "geophysics", "地球物理学",
        "geochemistry", "地球化学",
        "earth science not elsewhere classified", "地球科学未另分类",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（科学问题与背景）",
            "methodology（采样、分析与建模方法）",
            "results（数据与解释）",
            "discussion（地球科学意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（露头/矿区/剖面描述）",
            "analysis（测井、物化分析与年代学）",
            "results（物理解释）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Geochemistry, Geophysics, Geosystems 格式",
    reporting_standards={
        "k1": "采样位置、深度与采集时间须完整记录",
        "k2": "分析方法须注明仪器型号、精度与不确定度",
        "k3": "数值模型须注明参数、边界与初始条件",
    },
    conventions=(
        "地名使用标准地质名称与 ICS 地层年表名称",
        "年代用 Ma 或 ka 表示并附不确定度",
        "深度与海拔用 m 或 km 表示并说明基准面",
        "成分用 % 或 wt% 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Earth and Planetary Science Letters",
        "Geology",
        "Geophysical Research Letters",
        "Journal of Geophysical Research",
        "Geochimica et Cosmochimica Acta",
        "《地质学报》",
    ),
    units_and_formulas_notes=(
        "年代用 Ma 或 ka 表示",
        "深度用 m 或 km 表示",
        "成分用 % 或 wt% 表示",
        "温度用 °C 或 K 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "ArcGIS", "QGIS", "GRASS GIS", "GMT (Generic Mapping Tools)", "Golden Software Surfer", "Petrel", "IsoplotR", "Geochemist's Workbench", "Move", "GOCAD", "Oasis montaj", "SeisImager", "PyGimli", "GeoMesh", "GPlates", "Surfer", "EndNote"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
