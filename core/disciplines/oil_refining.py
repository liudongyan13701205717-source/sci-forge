"""石油炼制学科论文支持：石油加工与精炼工艺研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oil_refining",
    aliases=("oil_refining", "石油炼制", "炼油", "Petroleum Refining", "炼油工艺", "原油加工", "石油加工", "Refining"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "化工工艺报告规范", "k2": "能源行业数据标准", "k3": "环境评估报告要求"},
    conventions=("反应条件标注", "收率与转化率定义", "产物组成分析方法", "能量平衡核算"),
    key_venues=("Fuel", "Energy & Fuels", "Applied Catalysis A", "石油学报", "化工进展"),
    units_and_formulas_notes=("SI单位制", "热值单位MJ/kg", "收率以质量分数表示", "反应动力学用Arrhenius方程"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "HYSYS", "GAUSS (GC-MS)", "NMR Spectrometer", "XRD", "DSC", "GC-FID", "FTIR", "Molecular Dynamics (LAMMPS)", "HPLC", "TGA", "CFD (ANSYS Fluent)", "MATLAB", "COMSOL", "ProSim", "Sylvan SimSci", "Python", "OriginPro", "EndNote", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
