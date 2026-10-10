"""医学科学学科论文支持：基础与临床医学研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_science",
    aliases=("medical_science", "医学科学", "clinical research", "基础研究", "转化医学", "证据医学", "临床试验"),
    paper_types={
        "research": ("abstract", "introduction（临床问题）", "methodology（研究设计）", "results（数据与统计）", "discussion（临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例摘要）", "analysis（诊断与治疗）", "results（转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（机制概览）", "evidence synthesis（系统综述）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "临床试验注册与结局指标须声明", "k2": "系统综述须遵循 PRISMA 流程", "k3": "病例报告须按 CARE 指南撰写"},
    conventions=("首次出现标注全名与缩写", "样本量须声明依据（power analysis）", "统计结果报告 95% CI", "伦理批准与知情同意须注明", "利益冲突须声明"),
    key_venues=("The Lancet", "New England Journal of Medicine", "JAMA", "Annals of Internal Medicine", "BMJ"),
    units_and_formulas_notes=("SI 单位：mmHg（血压）、mmol/L（生化）", "统计以 mean±SD 或 median(IQR) 报告", "临床指标须注明检测方法", "p 值与效应量须同时报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epi Info 7", "SPSS", "R (survival)", "STATA", "EpiData", "OpenClinica", "REDCap", "MetaVine", "EndNote", "Zotero", "GraphPad Prism", "ImageJ", "Mass Spectrometer", "Flow Cytometer", "PCR System", "ELISA Reader", "Centrifuge", "Ultracentrifuge", "Bioanalyzer", "Microsoft Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Reviews"),
)
