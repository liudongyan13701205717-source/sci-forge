"""橄榄栽培学科论文支持：橄榄种植与生产技术研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="olive_growing",
    aliases=("olive_growing", "橄榄栽培", "橄榄种植", "Olive Cultivation", "油橄榄", "Olive Production", "橄榄育种", "Olive Growing"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "农学田间试验报告规范", "k2": "植物育种数据标准", "k3": "果实品质评价方法"},
    conventions=("田间试验设计标注", "物候期划分", "果实产量测定方法", "土壤参数报告"),
    key_venues=("Scientia Horticulturae", "Acta Horticulturae", "Journal of the Science of Food and Agriculture", "果树学报", "园艺学报"),
    units_and_formulas_notes=("SI单位制", "产量kg/树或t/ha", "土壤含水量以质量分数表示", "生长速率mm/d"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R (lme4)", "SPSS", "ArcGIS", "QGIS", "Photoshop", "Adobe Illustrator", "LaTeX", "Microsoft Excel", "PlantCV", "ImageJ", "Drone (DJI)", "Soil Moisture Sensor", "Chromatography (GC-MS)", "Spectrophotometer", "Python", "Origin", "EndNote", "Zotero", "Prism (GraphPad)", "GeoStats"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
