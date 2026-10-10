"""工业生物技术论文支持：发酵工程、生物反应器、代谢工程、合成生物学与酶工程。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="industrial_biotechnology",
    aliases=("industrial_biotechnology", "工业生物技术", "bioprocess_engineering", "fermentation_technology", "synthetic_biology", "metabolic_engineering", "enzyme_engineering", "biomanufacturing", "bioprocessing"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 ACS/Elsevier 期刊格式",
    reporting_standards={"cell_line": "细胞系须报告来源、代次、鉴定方法与培养条件", "fermentation": "发酵须按 MIQE 报告培养基、装料比、DO/pH/溶氧、放大策略", "metabolic_flux": "代谢通量须报告方法（13C-MFA/无标签）、模型与参数不确定度"},
    conventions=("菌株/质粒须报告 ATCC/GenBank 保藏编号", "酶活性单位以 U、kU 或 U/mg 表达", "代谢物浓度以 mM/gL 表达", "生物量以 g/L OD600 表示", "放大效应须按体积比表达"),
    key_venues=("Metabolic Engineering", "Biotechnology and Bioengineering", "Bioresource Technology", "Microbial Cell Factories", "Biotechnology Advances"),
    units_and_formulas_notes=("酶活力以 U、kU 或 U/mg 表达", "产率以 g/L 或 g/g 底物表示", "体积以 L/mL，温度以 °C 或 K 表示", "放大倍数以 L 倍数或 V 比表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Compass Biotech BioSprint", "Apex Automation", "New Brunswick 生物反应器", "BIOSTAT B 生物反应器", "BioLector", "Shake Flasks（2L/5L）", "HPLC", "GC-MS", "LC-MS/MS", "NIR", "XRD", "FTIR", "Raman", "Flow Cytometry（BD FACSCanto）", "qPCR", "Real-time PCR", "Biopython", "COBRApy", "MATLAB", "Python"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
