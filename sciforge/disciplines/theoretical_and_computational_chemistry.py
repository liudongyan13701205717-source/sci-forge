"""理论与计算化学学科论文支持：量子化学、分子动力学与反应机理计算研究体裁、ACS 引用样式与计算条件注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="theoretical_and_computational_chemistry",
    aliases=(
        "theoretical_and_computational_chemistry",
        "Theoretical and computational chemistry",
        "理论与计算化学",
        "计算化学",
        "量子化学",
        "分子模拟",
        "Computational chemistry",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与研究动机）",
            "computational methods（方法、体系与设置）",
            "results（能量、性质与结构数据）",
            "discussion（机理与误差分析）",
            "conclusions",
            "references",
        ),
        "methodology": (
            "abstract",
            "introduction",
            "method development（方法推导）",
            "validation study（基准验证）",
            "application examples",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（编号引用）",
    reporting_standards={
        "methods": "计算方法须完整列出（DFT 泛函、基组、离散化精度、SCF 收敛阈值）",
        "validation": "方法验证须给出基准数据对比（实验或高级方法）与偏差统计",
        "solvation": "溶剂模型须注明（显式水分子数或隐式模型参数）",
        "sampling": "采样方法须说明（温度、步数、步长、系综与块平均）",
    },
    conventions=(
        "基组与泛函用标准缩写（如 B3LYP-D3、def2-TZVP、aug-cc-pVTZ）",
        "能量用电子伏特（eV）或千焦/摩尔（kJ/mol），换算须注明",
        "几何优化须报告收敛判据与最终能量",
        "反应能垒须给出过渡态虚频与频率校正",
        "误差须报告绝对/相对偏差，避免隐藏系统性偏差",
    ),
    key_venues=(
        "Journal of Chemical Theory and Computation",
        "Journal of Computational Chemistry",
        "Chemical Science",
        "Physical Chemistry Chemical Physics",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "能量默认 eV 或 kJ/mol，1 eV = 96.485 kJ/mol",
        "频率用波数（cm⁻¹），虚频须标注",
        "温度用 K；压力用 atm 或 bar，1 atm = 1.01325 bar",
        "积分网格与平面截断须注明精度等级（loose/medium/tight）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Gaussian", "GaussView", "GAMER", "MOLCAS", "OpenMolcas", "ORCA", "Q-Chem", "CFOUR", "CP2K", "VASP", "Quantum ESPRESSO", "NWChem", "Psi4", "Tight-Binding 分析工具", "Avogadro（分子可视化）", "Gromacs（分子动力学）", "LAMMPS", "ASE（原子模拟环境）", "PyMOL", "VESTA 晶体可视化"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
