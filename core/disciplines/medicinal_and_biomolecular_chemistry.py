"""药物与生物分子化学学科论文支持：药物合成与分子表征。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medicinal_and_biomolecular_chemistry",
    aliases=("medicinal_and_biomolecular_chemistry", "药物化学", "biomolecular", "药物设计", "分子合成", "药理化学", "biocatalysis"),
    paper_types={
        "research": ("abstract", "introduction（合成背景）", "methodology（合成路线）", "results（结构与活性）", "discussion（构效关系）", "references"),
        "case_study": ("abstract", "introduction", "case description（分子案例）", "analysis（机制分析）", "results（活性数据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（领域概览）", "evidence synthesis（活性总结）", "future directions", "references"),
    },
    citation_style="ACS",
    reporting_standards={"k1": "合成条件须完整报告（溶剂、温度、时间、产率）", "k2": "结构表征须附 NMR/MS 数据", "k3": "活性数据须注明 IC50/EC50 测定方法"},
    conventions=("化合物编号按合成顺序", "NMR 数据格式：δ 值, 裂分, 耦合常数", "产率以 % 报告", "纯化合物须注明纯度（HPLC）", "生物活性须注明细胞系与浓度范围"),
    key_venues=("Journal of Medicinal Chemistry", "Angewandte Chemie", "Chemical Science", "Nature Chemistry", "European Journal of Organic Chemistry"),
    units_and_formulas_notes=("NMR 以 ppm 报告", "产率 = 实际质量/理论质量 × 100%", "活性以 μM 或 nM 报告", "pKa 须注明测定条件（温度、溶剂）", "分子量以 g/mol 报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("NMR Spectrometer", "Mass Spectrometer", "HPLC", "TLC System", "Ultracentrifuge", "Rotary Evaporator", "Schlenk Line", "Glovebox", "Infrared Spectrometer", "X-ray Diffractometer", "HPLC-MS", "LC-MS/MS", "BioAssay Reader", "Thermofisher Synthesis", "Sigma-Aldrich", "ChemDraw", "Shimadzu HPLC", "Bruker NMR", "Waters LC-MS", "Agilent HPLC"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
