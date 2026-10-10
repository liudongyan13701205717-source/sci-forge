"""肿瘤学学科论文支持：肿瘤发生、诊断、治疗与研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oncology",
    aliases=("oncology", "肿瘤学", "癌症学", "Cancer", "Oncology Research", "肿瘤研究", "肿瘤治疗", "Neoplasms"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "CONSORT（随机试验）", "k2": "STROBE（观察性研究）", "k3": "PRISMA（系统综述）"},
    conventions=("肿瘤分期采用TNM系统", "生存分析用Kaplan-Meier曲线", "疗效指标ORR/PFS/OS", "统计学报告含95%CI"),
    key_venues=("The Lancet Oncology", "Journal of Clinical Oncology", "NEJM", "Cancer Research", "中华肿瘤杂志"),
    units_and_formulas_notes=("肿瘤大小以mm/cm", "分级采用WHO分级", "疗效以百分比报告", "生存期以月为单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (survival)", "GraphPad Prism", "STATA", "Python (scikit-learn)", "ImageJ", "Cytometry (BD FACS)", "Flow Cytometer", "Sequencing (Illumina NovaSeq)", "Bioinformatics (Galaxy)", "Pathology Scanner (Leica)", "Microarray Scanner", "TMA Analysis", "Cox Regression", "Kaplan-Meier (R)", "EndNote", "Zotero", "Proteomics (LC-MS/MS)", "RT-qPCR (ABI 7500)", "Western Blot (Bio-Rad)"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
