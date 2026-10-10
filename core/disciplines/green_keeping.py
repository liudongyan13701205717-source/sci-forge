"""园艺养护学科论文支持：城市绿化与室内绿植的养护技术、土壤水分监测与养护方案评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="green_keeping",
    aliases=("green_keeping", "园艺养护", "绿化养护", "greenery maintenance", "园林绿化", "landscape horticulture", "修剪", "pruning", "土壤水分管理"),
    paper_types={
        "research": ("abstract", "introduction（养护问题与研究动机）", "methodology（样地、指标与监测方法）", "results（生长量、土壤水分与病虫害）", "discussion（养护措施对景观效果的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（场所、植被组成与养护背景）", "analysis（修剪、灌溉与植保方案分析）", "results（成活率与景观效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（植物生理与养护理论）", "evidence synthesis（养护技术与管理文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"site_description": "样地位置、气候区与土壤类型须描述", "irrigation": "灌溉量、频次与水利用效率须报告", "assessment": "成活率、树势与病虫害指数须给出评分标准与观测日期"},
    conventions=("植物首次出现以拉丁学名斜体标注，中文名随附", "冠幅、胸径与株高分别用 m、cm、cm 报告", "灌溉水量以 mm 或 L/株·次 报告，并注明计量方式", "修剪类型（疏剪、短截、回缩）须区分标注", "病虫害记录须含物种、危害等级与首次发现日期"),
    key_venues=("Acta Horticulturae", "HortScience", "Journal of Environmental Horticulture", "Arboricultural Journal", "园艺学报"),
    units_and_formulas_notes=("土壤含水率用体积分数（%）报告", "光照用 μmol/(m²·s)；土壤电导率用 mS/cm", "灌溉强度用 mm/h；灌溉量用 mm 或 L/株", "公式用 LaTeX（amsmath）；成活率 = 成活株数 / 栽植株数 × 100%"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Decagon EC-5", "Decagon PR-2", "Onset HOBO PX3", "Kestrel 5700", "Trimble R12i", "SketchUp", "QGIS", "AutoCAD Civil 3D", "Husqvarna Automower S570x", "Stihl FS 120", "Bosch RTG 450", "Husqvarna K570", "Plantix", "Pl@ntNet", "iNaturalist", "CropX", "Spectrum Crop", "Rain Bird", "Netafim", "AgriEye"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
