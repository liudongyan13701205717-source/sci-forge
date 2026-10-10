"""生物物理论文支持：分子动力学、单分子力学、冷冻电镜与热力学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biophysics",
    aliases=(
        "biophysics",
        "molecular_biophysics",
        "biophysical_chemistry",
        "structural_biophysics",
        "single_molecule_biophysics",
        "生物物理",
        "分子生物物理",
        "生物物理化学",
        "结构生物学",
        "单分子生物物理",
        "生物力学物理学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（样品制备、测量条件、重复性）",
            "results（数据、误差棒与统计显著性）",
            "discussion（物理解释与模型）",
            "data availability and code availability",
            "references",
        ),
        "modeling": (
            "abstract",
            "introduction",
            "model（势函数/哈密顿量与参数）",
            "simulation protocol（集成器、温度控制、时长）",
            "validation against experiment",
            "results and analysis",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "principles",
            "methods and results",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（编号）或作者-年份（Phys. Rev. Lett. / eLife 视期刊）",
    reporting_standards={
        "molecular_dynamics": "MD 模拟须报告力场、拓扑、集成器、温控/压控算法与总模拟时长",
        "cryo_em": "冷冻电镜结构须报告分辨率、FSC 标准（0.143）、粒子数与对称性",
        "xray_crystallography": "晶体学结构须报告 R-factor、R-free、完整度与空间群",
        "single_molecule": "单分子实验须报告信噪比、扫描速率与重复测量数",
        "calorimetry": "热力学须报告重复性、参比与拟合函数",
    },
    conventions=(
        "所有物理量用 SI 单位并注明温度（常标 298 K / 293 K）",
        "统计平均值须报告误差（SEM 或 bootstrap CI），非仅均值",
        "拟合函数与参数须给出，含拟合优度（χ² 或 R²）",
        "自由能报告 ΔG（kJ/mol），结合常数报告 Kd（M）",
        "蛋白质残基编号遵循 PDB/mmCIF 标准；突变用单字母缩写（如 A50V）",
    ),
    key_venues=(
        "Biophysical Journal",
        "Journal of Molecular Biology",
        "Physical Review Letters",
        "Nature Structural & Molecular Biology",
        "Proceedings of the National Academy of Sciences",
        "Structure",
        "Nucleic Acids Research",
        "PLOS Computational Biology",
    ),
    units_and_formulas_notes=(
        "能量用 kJ/mol 或 kcal/mol；力用 pN；长度用 nm/Å；时间用 ns/ps",
        "温度 T（K），压力 P（atm 或 bar），浓度用 μM/nM",
        "相关函数用 C(t)、自由能差用 ΔF = -kBT ln(⟨exp(-ΔE/kBT)⟩)",
        "扩散系数 D（m²/s 或 μm²/s），粘度用 cP 或 Pa·s",
        "统计量：kBT ≈ 2.48 kJ/mol（298 K），Boltzmann 因子显式声明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GROMACS", "AMBER", "CHARMM-GUI", "NAMD", "OpenMM", "LAMMPS", "DESMOND（Schrödinger）", "PyMOL", "UCSF ChimeraX", "VMD", "VESTA", "Coot", "CCP4", "Phenix", "CryoSPARC", "RELION", "IMOD", "ColabFold（AlphaFold）", "Thermo Scientific Polaris", "Thermo Scientific Titan Krios", "Thermo Scientific Talos F200i", "Rigaku HyPix-6000HE", "Bruker AVANCE NEO 800（NMR）", "HORIBA Fluorolog Max（荧光光谱）", "TA Instruments Nano DSC", "MicroCal PEAQ-ITC", "Biacore T200（SPR）", "Molecular Devices MOSQITO", "Bruker Dimension Icon AFM"),
    category="理学",
    databases=("PubMed", "PDB", "UniProt", "AlphaFold DB", "Zenodo", "arXiv"),
)
