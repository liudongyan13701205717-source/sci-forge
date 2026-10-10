"""职业健康与工业卫生学科论文支持：职业暴露/工业卫生体裁、AIOHA 引用样式与职业卫生记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="occupational_health_and_industrial",
    aliases=("occupational_health_and_industrial", "职业健康与工业卫生", "职业卫生", "工业卫生", "职业健康", "职业医学"),
    paper_types={
        "research": ("abstract", "introduction（背景与职业暴露）", "methodology（暴露评估设计）", "results（健康效应）", "discussion（机理与干预）", "references"),
        "case_study": ("abstract", "introduction", "case description（职业病案例）", "analysis（暴露评估）", "results（诊断与处置）", "discussion（经验教训）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述主题）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="AIOHA/American Journal of Industrial Medicine 样式",
    reporting_standards={"observational": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明", "case_report": "遵循 CARE 指南"},
    conventions=("暴露限值须注明 OEL/PC/TWA", "采样方法与仪器须报告", "统计结果给出 I² 与 95% CI", "干预研究须报告前后对比", "职业疾病命名须用 ICD 编码"),
    key_venues=("Annals of Occupational and Environmental Hygiene", "Scandinavian Journal of Work Environment & Health", "American Journal of Industrial Medicine", "International Journal of Occupational Medicine and Environmental Health", "Occupational and Environmental Medicine"),
    units_and_formulas_notes=("粉尘浓度用 mg/m³", "噪声用 dBA", "光强用 lux", "温度用 °C", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("总悬浮粉尘检测仪", "颗粒物采样器", "便携式气体分析仪", "噪声计", "照度计", "热成像仪", "人体工效学评估仪", "职业暴露采样泵", "Personal Exposure Monitor", "LRI-PRO 热应力评估仪", "SafetyCulture", "Intelex EHS", "OSHA 合规工具", "NIOSH 采样套件", "Pymaceutical 分析软件", "R", "SPSS", "JMP", "Epi Info", "OSHA 300 报告系统"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
