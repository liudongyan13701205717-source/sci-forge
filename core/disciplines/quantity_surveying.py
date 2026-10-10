"""工料测量学科论文支持：工程造价、数量测与建设项目成本管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantity_surveying",
    aliases=("quantity_surveying", "工料测量", "quantity surveying", "QS", "cost estimation", "造价", "工程算量", "cost planning", "construction cost"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RICS 工料测量服务规范", "k2": "RICS 新工料测量测量标准（NRM）", "k3": "ISO 21500 项目成本管理框架"},
    conventions=("工程量清单遵循 NRM 编码", "货币使用项目所在国法定货币", "成本估算须列出单价来源与置信区间", "图表使用统一的成本分类", "变更管理须记录变更单与责任归属"),
    key_venues=("Construction Management and Economics", "Journal of Financial Management in Property and Construction", "Engineering Economics", "Quantity Surveying International", "International Journal of Construction Management"),
    units_and_formulas_notes=("长度使用米（m），面积使用平方米（m²）", "体积使用立方米（m³），重量使用吨（t）", "货币按项目国法定单位，含税与不含税分列", "工料测量单价以 RICS 或当地费率手册为基准"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CostX", "PlanSwift", "Bluebeam Revu", "RIB Software", "CostOS 2", "Costbook (Spon)", "Procore Cost Control", "Aconex Contract Management", "Primavera P6", "Microsoft Project", "Autodesk Revit", "AutoCAD Civil 3D", "ArchiCAD", "SketchUp Pro", "Vectorworks", "BIM 360", "Excel Advanced Modeling", "RICS New Rules of Measurement", "Xero Construction", "QuickBooks Contractor"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
