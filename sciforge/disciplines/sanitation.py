"""环卫学科论文支持：环境卫生/废物管理/公共卫生工程体裁与环卫规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sanitation",
    aliases=("sanitation", "环卫", "环境卫生", "废物管理", "公共卫生工程", "waste management", "hygiene", "城市环卫"),
    paper_types={
        "research": ("abstract", "introduction（环卫问题）", "methodology（采样与分析方法）", "results（污染物浓度结果）", "discussion（污染控制讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（环卫案例背景）", "analysis（污染分析与治理）", "results（治理效果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（环卫综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"monitoring": "环境监测遵循 ISO 5667 规范", "waste": "废物分类遵循 GB/T 19490 规范", "field_study": "现场研究遵循 COREQ 规范"},
    conventions=("污染物浓度须给出单位（mg/L 或 µg/m³）", "采样方法须给出频次与时段", "统计方法须给出置信区间", "职业暴露须讨论防护措施", "样本量须足够并说明"),
    key_venues=("Journal of Environmental Management", "Waste Management", "Environmental Science & Technology", "Water Research", "Environmental Engineering Science", "Journal of Environmental Engineering"),
    units_and_formulas_notes=("浓度以 mg/L 或 µg/m³ 记", "温度以 °C 记", "质量流量以 kg/s 记", "pH 值以无量纲记"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Air Quality Monitor (Thermo Fisher)", "Water Sampler (ISCO)", "GC-MS (Agilent)", "LC-MS/MS (Waters)", "ICP-MS (Thermo)", "Total Organic Carbon Analyzer", "pH Meter (Mettler-Toledo)", "Conductivity Meter", "Turbidity Meter", "Dissolved Oxygen Meter", "MATLAB", "GIS (ArcGIS)", "QGIS", "Tableau", "Power BI", "SPSS", "R", "Stata", "OriginLab", "COMSOL Multiphysics"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
