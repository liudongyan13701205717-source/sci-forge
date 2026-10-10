"""化学物理学科论文支持：分子动力学、统计力学与光谱理论的写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_physics",
    aliases=(
        "chemical physics", "化学物理", "分子物理化学",
        "化学物理学", "分子动力学", "分子光谱",
        "molecular dynamics", "molecular spectroscopy",
        "量子化学", "quantum chemistry",
        "反应动力学", "reaction dynamics",
        "表面化学物理", "surface chemistry physics",
        "激光光谱", "ultrafast spectroscopy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "theoretical framework（模型与理论方法）",
            "methods（计算方法与实验方案）",
            "results and discussion（结果与理论对照）",
            "conclusion",
            "supporting information",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（领域范围）",
            "theoretical framework",
            "main developments",
            "outlook",
            "references",
        ),
        "letter": (
            "abstract",
            "introduction",
            "results and discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="ACS 样式（编号；期刊缩写按 CASSI）",
    reporting_standards={
        "theory": "哈密顿量、势能与基态/激发态给出解析表达式与数值参数",
        "computation": "DFT/CI/MRCI/CASSCF/CCSD(T) 给出方法、基组、软件版本与收敛判据",
        "experiment": "光谱实验给出波长范围、分辨率、光源、探测器与温度",
        "simulation": "MD/Monte Carlo 给出系综、时间步长、步数、初始构型",
    },
    conventions=(
        "势能面给出函数形式与拟合参数表",
        "激发态给出电子态编号（S₁、S₂、T₁…）与跃迁偶极矩",
        "MD 结果给自相关函数、扩散系数与误差棒",
        "光谱模拟用卷积函数说明（如高斯/Lorentzian，FWHM 值）",
        "能量单位统一（eV 或 cm⁻¹）；力常数用 mdyn·Å⁻¹",
        "所有基组/泛函缩写首次出现给全称",
    ),
    key_venues=(
        "The Journal of Chemical Physics",
        "Physical Chemistry Chemical Physics (PCCP)",
        "Chemical Physics Letters",
        "Chemical Physics",
        "Journal of Chemical Theory and Computation",
        "The Journal of Physical Chemistry A",
        "The Journal of Physical Chemistry B",
        "Molecular Physics",
        "ChemPhysChem",
    ),
    units_and_formulas_notes=(
        "能量 eV、cm⁻¹ 或 kJ·mol⁻¹；频率 Hz、cm⁻¹；温度 K",
        "力常数 mdyn·Å⁻¹；偶极矩 Debye（D）",
        "跃迁偶极矩 |μ|² 单位 C·m 或 D",
        "时间步长 fs；模拟时长 ns 或 μs",
        "波数 cm⁻¹；振动能级用 v、v'、Δv 标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Gaussian", "ORCA", "Q-Chem", "Turbomole", "Molpro", "NWChem", "CP2K", "VASP", "Quantum ESPRESSO", "ABINIT", "SIESTA", "Casscf/MRCI 计算（Molcas/OpenMolcas）", "R12-ORCA 高精度计算", "Multiwfn 波函数分析", "GIMIC 图形化分子界面（Molcas）", "Molcas 多参考计算", "Molvis 分子可视化", "VESTA 晶体可视化", "XCrystalToolKit 晶体工具", "ASE（原子模拟环境）", "PyMOL", "VMD", "OVITO 原子结构可视化", "Avogadro", "ChemDraw", "LAMMPS 分子动力学", "GROMACS", "NAMD", "LAMMPS-DP（Deep Potential）", "LAMMPS-ReaxFF", "GPUMD GPU 分子动力学", "DeepMD 深度势分子动力学", "CP2K 大规模第一性原理", "SIESTA-OpenMD 分子动力学", "LAMMPS-Optimize 势函数优化", "MACE 机器学习势", "SchNetPack 机器学习势", "PyTorch MD", "分子势能面拟合工具 Fit2D", "光谱模拟软件 SHG/HHHH（HyperHonestHubert）", "Spectroscopy: BoltzTraP", "Spectroscopy: Boltzmann Trajectory Path（BoltzTraP）", "分子光谱拟合软件 LIFBASE", "多光子光谱软件 MultiPhoton", "拉曼光谱软件 Winram", "荧光光谱软件 FLM3", "激光光谱仪 Spectra-Physics Tsunami", "飞秒激光器 Coherent Lightning", "同步辐射光源（上海光源 SSRF）", "X 射线吸收光谱仪（XAS）", "光电子能谱仪（XPS/UPS）", "飞行时间质谱仪（TOF-MS）", "激光诱导荧光谱仪（LIF）", "傅里叶变换红外光谱仪（FTIR）", "原子吸收/发射光谱仪", "原子级探针显微镜（APT）", "低温恒温器（Cryostat Janis）", "低温真空腔体（CryoVac）", "原子级操纵针尖扫描隧道显微镜（STM）", "AFM 原子力显微镜", "STM 扫描隧道显微镜", "TEM 透射电子显微镜", "SDD 单晶衍射仪（Bruker D8）", "X 射线晶体学 CCD 探测器（Pixium 2M）", "SHELXL 晶体精修", "OLEX2 晶体学软件", "Chemcraft 波函数可视化", "Multiwfn 波函数可视化", "Plotting: OriginLab", "Plotting: GraphPad Prism", "LaTeX 排版", "Python（numpy/scipy/scikit-learn）", "MATLAB 数据处理", "R 数据分析", "Zotero 文献管理", "EndNote 文献管理"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "CCDC", "Materials Project", "Web of Science"),
)
