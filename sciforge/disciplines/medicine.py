"""医学学科论文支持：临床医学与基础医学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medicine",
    aliases=("medicine", "医学", "clinical medicine", "内科", "外科", "基础医学", "病理学"),
    paper_types={
        "research": ("abstract", "introduction（临床问题）", "methodology（研究设计）", "results（数据与统计）", "discussion（临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例摘要）", "analysis（诊断与治疗）", "results（转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（机制概览）", "evidence synthesis（系统综述）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "randomized_trial": "临床试验须注册并声明主要结局，报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "case_report": "病例报告按 CARE 指南撰写",
        "systematic_review": "系统综述遵循 PRISMA 流程",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=("诊断须注明 ICD-10 编码", "统计结果报告 95% CI", "伦理批准与知情同意须声明", "利益冲突须注明", "患者信息脱敏"),
    key_venues=("The Lancet", "New England Journal of Medicine", "JAMA", "BMJ", "Annals of Internal Medicine"),
    units_and_formulas_notes=("血压 mmHg", "血糖 mmol/L", "体温 ℃", "统计以 mean±SD 报告", "p 值须注明检验方法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (survival)", "STATA", "Epi Info 7", "EpiData", "RedCap", "OpenClinica", "GraphPad Prism", "ImageJ", "Mass Spectrometer", "Flow Cytometer", "PCR System", "ELISA Reader", "EndNote", "Zotero", "MetaVine", "Bioanalyzer", "Ultracentrifuge", "Centrifuge", "Microsoft Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Reviews"),
)
