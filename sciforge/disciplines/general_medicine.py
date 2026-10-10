"""临床医学学科论文支持：诊断、治疗、临床研究、循证医学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="general_medicine",
    aliases=("general_medicine", "临床医学", "内科", "General practice", "Primary care", "循证医学", "内部医学"),
    paper_types={
        "research": ("abstract", "introduction（疾病背景与研究目的）", "methodology（研究设计、对象、诊断与干预方法）", "results（疗效与安全数据）", "discussion（临床意义与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例信息）", "analysis（诊断与治疗过程）", "results（预后）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（疾病机制与诊疗综述）", "evidence synthesis（循证证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（编号引用），临床期刊普遍采用",
    reporting_standards={"randomized": "随机对照试验遵循 CONSORT 声明", "cohort": "队列研究遵循 STROBE", "diagnostic": "诊断试验遵循 STARD", "meta_analysis": "Meta 分析遵循 PRISMA", "guideline": "临床指南遵循 GRADE"},
    conventions=("疾病诊断按 ICD-11 编码", "药物用 INN（国际非专有名称）", "试验数据报告效应量（HR/OR/RR）与 95% CI", "P 值与置信区间同时报告", "不良事件按 CTCAE 分级"),
    key_venues=("The Lancet", "New England Journal of Medicine", "British Medical Journal", "Journal of General Internal Medicine", "中华医学杂志"),
    units_and_formulas_notes=("血细胞计用 10⁹/L", "生化指标 mg/dL 或 mmol/L", "血压用 mmHg", "心率用 bpm", "药物浓度用 μg/L 或 ng/mL"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ClinicalTrials.gov", "REDCap", "OpenClinica", "R（统计与绘图）", "SPSS", "Stata", "RStudio", "R 生存分析（survival 包）", "RevMan（meta 分析）", "CMA（meta 分析）", "OpenEHR（电子病历）", "DICOM（影像）", "PACS", "HIS（医院信息系统）", "SAS", "GraphPad Prism", "Origin", "Excel", "UpToDate 临床决策", "Medscape 临床决策"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI", "Cochrane Library", "Medline"),
)
