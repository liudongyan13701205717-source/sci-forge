"""草坪管理学科论文支持：运动场与景观草坪养护体裁、ASA 引用样式与草坪管理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="turf_management",
    aliases=("turf management", "草坪管理", "草坪养护", "运动场草坪管理", "高尔夫球场草坪管理",
             "turfgrass management", "lawn management", "sports turf management"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与管理问题）",
            "materials and methods（场地、处理与测定）",
            "results（质量、病虫害与胁迫数据）",
            "discussion（管理机理与实践意义）",
            "references",
        ),
        "field_trial": (
            "abstract",
            "introduction",
            "materials and methods（田间设计、重复与小区）",
            "results（处理间差异与统计）",
            "discussion（适用条件与推广）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASA/CSSA 样式（作者-年份；Agronomy Journal 遵循 ASA 规范）",
    reporting_standards={
        "field_trial": "田间试验遵循 ASA/CSSA 农艺试验报告规范",
        "irrigation_trial": "灌溉试验须报告水量、频次与土壤水分状况",
        "turf_quality": "草坪质量评分（1-9 分制）须说明评分标准与评估人",
        "pest_management": "病虫害防治试验须报告药剂、剂量与施用时点",
    },
    conventions=(
        "修剪高度、频次与灌溉量须以 SI 单位报告",
        "草坪质量评分采用 NTEP 1-9 分制并说明维度",
        "土壤理化性质与 pH 须交代",
        "管理措施（施肥/灌溉/打孔/覆沙）须逐项说明",
        "胁迫（干旱/盐/热）处理条件须量化",
    ),
    key_venues=(
        "Agronomy Journal",
        "Crop Science",
        "HortTechnology",
        "Journal of Environmental Horticulture",
        "International Turfgrass Society Research Journal",
        "Weed Technology",
    ),
    units_and_formulas_notes=(
        "灌溉量用 mm；施肥量用 kg N/ha",
        "修剪高度用 mm；密度用 株/m²",
        "土壤水分用体积含水率 % 或 mm",
        "统计量给出均值与标准误；显著性用 P 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Turf Management Software", "ArcGIS Pro", "QGIS", "无人机遥感平台", "FieldScout TDR 350", "土壤水分传感器网络", "智能灌溉控制器", "Stimpmeter", "Clegg Impact Soil Tester", "土壤紧实度仪 (penetrometer)", "SPAD-502 叶绿素仪", "Trimble RTK GPS", "Canopeo 冠层覆盖软件", "草坪病害诊断 App", "气象站 (Davis Vantage Pro2)", "土壤养分速测仪", "R", "Python (pandas)", "SAS", "SPSS"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "CNKI"),
)
