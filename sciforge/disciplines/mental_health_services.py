"""心理健康服务学科论文支持：精神健康护理与干预。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mental_health_services",
    aliases=("mental_health_services", "心理健康服务", "psychiatric care", "心理护理", "社区心理", "服务评估", "康复"),
    paper_types={
        "research": ("abstract", "introduction（临床背景）", "methodology（评估设计）", "results（成效数据）", "discussion（服务改进）", "references"),
        "case_study": ("abstract", "introduction", "case description（服务案例）", "analysis（需求与干预）", "results（转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（服务模式）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "量表使用须报告信度（Cronbach α）", "k2": "干预研究须报告治疗师资质与剂量", "k3": "服务评估须说明抽样与失访处理"},
    conventions=("诊断采用 DSM-5/ICD-11 编码", "量表名称与版本须注明", "患者隐私脱敏", "统计报告 95% CI 与效应量", "伦理批准与知情同意须声明"),
    key_venues=("Psychiatric Services", "World Psychiatry", "Acta Psychiatrica Scandinavica", "Lancet Psychiatry", "Psychological Medicine"),
    units_and_formulas_notes=("量表得分以总分/子量表分报告", "发病率以每万人口计", "服务利用率 = 就诊次数/登记人数", "统计以 mean±SD 或 median(IQR) 报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PHQ-9", "GAD-7", "PSC-16", "BDI-II", "PANSS", "SPSS", "R (lava)", "STATA", "OpenMx", "Mplus", "Qualtrics", "SurveyMonkey", "REDCap", "NVivo", "Atlas.ti", "GraphPad Prism", "EndNote", "Zotero", "Power BI", "Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
