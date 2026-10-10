"""抹灰/石膏工学科论文支持：抹灰工艺/墙面工程/装饰结构体裁、ASCE 引用样式与抹灰记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plastering",
    aliases=("plastering", "抹灰", "抹灰工", "plastering trades", "石膏工", "stucco", "石灰砂浆", "lime mortar", "墙面抹灰", "wall plastering", "湿抹灰", "wet plastering", "预制石膏板", "drywall"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（工艺与方法）", "results（性能数据）", "discussion（工艺意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例与工程）", "analysis（工艺与工序）", "results（成品质量）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（抹灰材料/工艺综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASCE 样式（国内期刊遵循 GB/T 7714）",
    reporting_standards={"GB 50210": "建筑装饰装修工程质量验收规范", "JGJ 126": "抹灰工程", "EN 15824": "外墙抹灰系统", "EN 13279": "建筑用抹灰砂浆", "ASTM C842": "抹灰试验方法"},
    conventions=("抹灰厚度用 mm 表示（分层厚度）", "砂浆配合比（体积/质量比）须给出", "基层处理（清理、湿润、界面剂）须报告", "抹灰材料（石膏、石灰、水泥）须注明", "干燥时间与养护须给出"),
    key_venues=("Construction and Building Materials", "Journal of Building Engineering", "抹灰与建筑涂料", "Construction Research & Innovation", "Building and Environment"),
    units_and_formulas_notes=("抹灰厚度 mm；砂浆配合比体积比（如 1:3）", "强度 MPa；抗压/抗折", "含水率 %；干燥天数", "面积 m²；单价 元/m²"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "SketchUp Pro", "ArchiCAD", "Chief Architect", "Vectorworks", "ProEstimator", "CostX", "Cubicost", "BIM 360", "Procore", "RLM ReadyLink Manager", "Hilti PS 300", "Wagner Plaster Spray", "Hilti DM1-LR", "Bosch PLG-120", "Bosch PLG-180", "Hilti LR 300", "Trimble TBM600", "Trimble TBM615"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
