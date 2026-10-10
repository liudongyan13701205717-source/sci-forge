"""园艺学科论文支持：栽培、育种、生理、生态与观赏植物应用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gardening",
    aliases=("gardening", "园艺", "园艺学", "Horticulture", "Ornamental horticulture", "Landscape horticulture", "果树学", "蔬菜学"),
    paper_types={
        "research": ("abstract", "introduction（作物与问题）", "methodology（材料与方法、栽培/试验设计）", "results（生长、产量与品质数据）", "discussion（机理与展望）", "references"),
        "case_study": ("abstract", "introduction", "case description（园圃/生产园概况）", "analysis（栽培制度与栽培管理）", "results（产量、品质、经济效益）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（栽培理论、育种理论、生理与生态综述）", "evidence synthesis（不同品种/地区对比）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份），或中国植物学/园艺学期刊 GB/T 7714 规范",
    reporting_standards={"experimental": "栽培试验须报告地点、气候、土壤、重复数、随机化与区组设计", "variety": "品种对比须报告参试品种来源、种植密度、处理与生育期指标", "yield": "产量须报告单位（kg/667m² 或 t/ha）、统计方法与显著性检验"},
    conventions=("作物品种名用斜体加引号", "气候数据按中国气象局标准统计", "土壤分析执行 GB/T 19482-1950", "生长指标包括株高、叶面积指数（LAI）、鲜/干物质量", "产量以成熟期实际计"),
    key_venues=("Horticulture Research", "Journal of Horticultural Science & Biotechnology", "Scientia Horticulturae", "中国农业科学", "园艺学报"),
    units_and_formulas_notes=("植物生长用 cm/d 或 m·d⁻¹", "光合速率用 μmol CO₂·m⁻²·s⁻¹", "产量用 kg/667m² 或 t/ha", "含水率用 %", "叶绿素用 SPAD 值"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Photosynth3000（光合作用测定）", "LI-6400XT（光合仪）", "SPAD-501（叶绿素计）", "便携式气象站（Weather Meter）", "SoilTest Pro", "LIDAR 测高仪", "手持式叶绿素荧光仪", "GCMS（品质分析）", "HPLC（次级代谢物分析）", "植物表型组系统（PhenoCore）", "Drone（无人机测绘）", "ArcGIS", "R", "SPSS", "Origin", "Excel", "Primer 5（系统发育分析）", "GenMarker（分子标记分析）", "SolidWorks（温室模型）", "Python（数据可视化）", "AutoCAD（园圃设计）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
