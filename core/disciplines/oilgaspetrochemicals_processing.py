"""油气化工处理学科论文支持：石油天然气与化工处理工艺。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oilgaspetrochemicals_processing",
    aliases=("oilgaspetrochemicals_processing", "油气化工处理", "石油天然气化工", "Petrochemical Processing", "油气加工", "化工处理", "炼化", "Petrochemicals"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "化工安全报告规范", "k2": "工艺流程数据标准", "k3": "环保排放报告要求"},
    conventions=("工艺流程图规范", "物料与能量衡算", "催化剂表征方法", "反应器设计参数"),
    key_venues=("Industrial & Engineering Chemistry Research", "Chemical Engineering Science", "AIChE Journal", "化工科技", "精细化工"),
    units_and_formulas_notes=("SI单位制", "摩尔流量kmol/h", "转化率与选择性定义", "热力学用K、bar"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "HYSYS", "GAUSS (GC-MS)", "NMR Spectrometer", "XRD", "DSC", "FTIR", "CFD (ANSYS Fluent)", "COMSOL", "ProSim", "MATLAB", "Python", "HPLC", "TGA", "SEM-EDS", "OriginPro", "EndNote", "Zotero", "Gaussian 16", "ChefMAP"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
