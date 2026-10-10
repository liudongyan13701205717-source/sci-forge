"""草坪培育学科论文支持：草坪建植与养护体裁、ASA/CSSA 引用样式与草坪农艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="turf_cultivation",
    aliases=("turf cultivation", "草坪培育", "草坪建植", "草坪草栽培", "草坪学",
             "turfgrass science", "turf establishment", "turfgrass cultivation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与草坪问题）",
            "materials and methods（草种、设计与测定）",
            "results（建植率、密度与质量数据）",
            "discussion（农艺机理与养护意义）",
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
    citation_style="ASA/CSSA 样式（作者-年份；Crop Science 遵循 ASA 规范）",
    reporting_standards={
        "field_trial": "田间试验遵循 ASA/CSSA 农艺试验报告规范",
        "cultivar_evaluation": "品种评价须报告 NTEP 式质量评分与试验点信息",
        "statistical": "须报告试验设计、重复数与统计检验方法",
        "turf_quality": "草坪质量评分（1-9 分制）须说明评分标准与评估人",
    },
    conventions=(
        "草坪质量评分采用 NTEP 1-9 分制并说明评估维度",
        "草种/品种须给出拉丁学名与栽培品种名",
        "修剪高度、频次与施肥量须以 SI 单位报告",
        "建植方式（播种/铺草皮/插条）须明确",
        "土壤类型与 pH 须交代",
    ),
    key_venues=(
        "Crop Science",
        "Agronomy Journal",
        "HortScience",
        "Journal of Environmental Horticulture",
        "International Turfgrass Society Research Journal",
        "Weed Technology",
    ),
    units_and_formulas_notes=(
        "面积用 m²/ha；施肥量用 kg N/ha",
        "修剪高度用 mm；密度用 株/m²",
        "土壤含水量用 g/kg 或体积含水率 %",
        "统计量给出均值与标准误；显著性用 P 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Turfgrass Management Software (TMS)", "FieldScout TDR 350 土壤水分仪", "Trimble RTK GPS", "NDVI 植被指数仪", "叶面积指数仪 (LAI-2200)", "便携式光合仪 (LI-6800)", "SPAD-502 叶绿素仪", "pH 计", "无人机多光谱相机", "Pix4Dmapper", "QGIS", "GreenSeeker 光谱仪", "Stimpmeter", "Clegg Impact Soil Tester", "土壤紧实度仪 (penetrometer)", "土壤养分速测仪", "R (agricolae)", "SAS", "SPSS", "气象站 (Davis Vantage Pro2)"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "CNKI"),
)
