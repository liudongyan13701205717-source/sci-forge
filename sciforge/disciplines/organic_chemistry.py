"""有机化学学科论文支持：有机合成、结构表征与反应机理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="organic_chemistry",
    aliases=("organic_chemistry", "有机化学", "有机合成", "Organic Chemistry", "Organic Synthesis", "Organic Reaction Mechanism", "有机反应", "Medicinal Chemistry", "药物化学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACS",
    reporting_standards={"SYNTHESIS": "合成方法完整性与产率按 IUPAC 报告", "REPRODUCIBILITY": "重现性（±2σ）与批次一致性", "SAFETY": "化学品安全声明与 MSDS 引用"},
    conventions=("化学结构图与命名遵循 IUPAC 惯例", "产率按摩尔计，非质量，纯度以 GC/LC 报告", "表征手段完整（NMR/MS/IR/HRMS）", "反应条件与溶剂标注清楚", "化学式用下标而非斜体"),
    key_venues=("Journal of the American Chemical Society", "Angewandte Chemie International Edition", "Chemical Science", "Organic Letters", "Journal of Organic Chemistry"),
    units_and_formulas_notes=("产率按摩尔百分数报告，纯度 % w/w", "反应温度以 °C 报告，压力以 atm 或 bar", "GC-MS/LC-MS 保留时间 tR 用 min", "旋光度 [α]D 用 (°) (g·cm⁻³)·cm⁻¹"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ChemDraw", "Chem3D", "MarvinSketch", "ACD/Labs", "Avogadro", "Gaussian 16", "ORCA", "MestReNova", "Bruker TopSpin", "Agilent OpenLab LC-MS", "Thermo Xcalibur LC-MS", "Shimadzu LabSolutions", "KemOne 有机合成机器人", "Process Monitor 反应监测仪", "Bruker AVANCE NMR", "Agilent 7890/5977 GC-MS", "Agilent 6500 Q-TOF LC-MS", "FTIR 红外光谱仪", "Mettler Toledo 熔点仪", "Jasco P-2000 旋光仪"),
    category="理学",
    databases=("OpenAlex", "Crossref", "ACS Publications", "SciFinder"),
)
