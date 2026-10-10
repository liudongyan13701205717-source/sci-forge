"""考古学论文支持：田野发掘、年代测定、物质文化分析、聚落形态研究、科技考古。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="archaeology",
    aliases=(
        "archaeology",
        "archeology",
        "Archaeology",
        "考古学",
        "考古",
        "历史考古",
        "考古材料学",
        "prehistory",
        "古代史",
        "考古类型学",
        "考古地貌",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "site description",
            "methods",
            "analysis",
            "discussion",
            "conclusions",
            "references",
        ),
        "excavation_report": (
            "abstract",
            "introduction（遗址概况与发掘背景）",
            "stratigraphy（地层与遗迹单位）",
            "finds（出土遗物分析）",
            "interpretation（年代与功能）",
            "conclusions",
            "references",
        ),
        "theoretical": (
            "abstract",
            "introduction",
            "theory",
            "case studies",
            "discussion",
            "conclusions",
            "references",
        ),
    },
    citation_style="Chicago/Turabian（编号），如 [1] 或 (Author Year)",
    reporting_standards={
        "stratigraphy": "地层学须报告发掘单位（探方/层位）、土壤描述（Munsell色卡）与层序关系",
        "dating": "测年结果须报告校正曲线（Calib/INTCAL20）、误差范围（1σ/2σ）与实验室编号",
        "artifact": "器物分析须报告采样位置、数量、类型学分期与制作工艺",
        "survey": "调查须报告调查方法（系统/采样）、区域面积与采集密度",
        "material_analysis": "XRF/同位素/DNA 分析须给实验室、设备型号、精度与不确定性",
    },
    conventions=(
        "地层编号用大写罗马数字（Ⅰ/Ⅱ/Ⅲ）；遗迹编号用 F+数字（F1/F2）",
        "探方编号用 T+坐标（T12N-E5）；方向用 N/E/S/W",
        "器物描述用标准术语（口沿/腹/底/耳/足）；测量单位用 cm",
        "图版编号用 Pl. + 数字；地图比例尺和指北针必须标注",
        "遗址名称用正式地名（中英文），括注省县",
    ),
    key_venues=(
        "Journal of Archaeological Science",
        "American Antiquity",
        "Journal of Field Archaeology",
        "Antiquity",
        "World Archaeology",
        "考古",
        "文物",
    ),
    units_and_formulas_notes=(
        "长度用 cm/m；重量用 g/kg；容积用 mL/L",
        "碳14年代用 BP（Before Present, 1950）或 cal BP/cal BC",
        "地层深度用 m below surface (mbs)；海拔用 m asl",
        "XRF 元素含量 wt% 或 ppm；同位素 δ¹³C、δ¹⁸O、εNd",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("QGIS", "ArcGIS", "MetaShape", "Sketchfab", "MeshLab", "Cloud Compare", "Agisoft Metashape", "3D 激光扫描仪（Leica BLK360）", "Faro Focus 三维扫描", "无人机 DJI Mavic 3 / Phantom 4", "便携 XRF 分析仪（Oxford X-MET8000）", "碳十四 AMS 测年（Beta/AMS Labs）", "OxCal（贝叶斯年代建模）", "BCAL（贝叶斯校准）", "R", "RStudio", "Python", "TAS", "Past", "GIS 考古扩展 (GIA)", "GIMP（图版处理）", "AutoCAD（剖面图/平面图）", "LaTeX", "Zotero"),
    category="历史学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Web of Science", "JSTOR", "Europeana 遗址数据库", "中国考古遗址数据库"),
)
