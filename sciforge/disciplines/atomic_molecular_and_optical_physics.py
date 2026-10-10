"""原子分子与光学物理 (Atomic, Molecular and Optical Physics) 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="atomic_molecular_and_optical_physics",
    aliases=(
        "Atomic, Molecular And Optical Physics", "原子分子与光学物理",
        "AMO physics", "atomic physics", "原子物理", "分子物理", "molecular physics",
        "光学物理", "optical physics", "量子光学", "quantum optics",
        "laser physics", "激光物理", "冷原子物理", "cold atoms",
        "原子分子光学物理", "AMO",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "experimental setup / theoretical framework",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current state",
            "open questions",
            "references",
        ),
    },
    citation_style="APS / AIP 样式（编号，物理期刊）",
    reporting_standards={
        "uncertainty": "所有测量须给出统计+系统误差（1σ，95% CI）",
        "calibration": "激光频率、时间、强度须声明校准方法与不确定度",
        "spectral_lines": "跃迁波长、频率、线强、寿命须声明数据来源（NIST / Buffer Lab）",
        "units": "SI 或 Gaussian 须全文一致",
        "reproducibility": "关键实验参数须完整披露以便重现",
    },
    conventions=(
        "原子态记法：n, l, j, F 量子数；同位旋/超精细结构用符号明确",
        "光谱用 SI：波长 nm/µm，频率 THz/cm⁻¹，线强 W·s·cm²·sr⁻¹",
        "能量 eV 或 cm⁻¹（须声明）；激光参数用 P, λ, τ, FWHM",
        "单位制必须全文统一（SI 或 Gaussian 二选一，须在方法节声明）",
        "实验图表须标误差棒，拟合须给出拟合函数与残差",
    ),
    key_venues=(
        "Physical Review Letters",
        "Physical Review A",
        "Physical Review X",
        "Optics Letters",
        "Optics Express",
        "Journal of the Optical Society of America B",
        "Journal of Physics B: Atomic, Molecular and Optical Physics",
        "Reviews of Modern Physics",
        "Nature Photonics",
        "Physical Review",
        "Laser & Photonics Reviews",
    ),
    units_and_formulas_notes=(
        "长度 nm/µm；频率 THz 或 cm⁻¹；能量 eV 或 cm⁻¹",
        "强度 W/cm²；磁矩 μB 或 nB",
        "激光相干时间 ps/ns；线宽 kHz/Hz",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gaussian", "ORCA", "Molpro", "MOLCAS", "CFOUR", "PySCF", "NWChem", "Turbomole", "ABINIT", "Quantum ESPRESSO", "VASP", "FHI-aims", "NIST Atomic Spectra Database", "NIST Boulder Labs", "Basis Set Exchange", "LabVIEW", "Lumerical", "COMSOL Multiphysics", "Zemax OpticStudio", "GaussView", "Avogadro", "VMD", "PyMOL", "JMOL", "Python (NumPy/SciPy)", "MATLAB"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "NIST", "AtomicSpec", "CDD", "Zenodo"),
)
