"""物理化学学科论文支持：化学热力学/化学动力学体裁、ACS 引用样式与物化记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_chemistry",
    aliases=("physical chemistry", "物理化学", "化学热力学", "chemical thermodynamics",
             "化学动力学", "chemical kinetics", "量子化学", "quantum chemistry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与体系）",
            "theory（理论框架与方程）",
            "methods（实验/计算方法）",
            "results（热力学量、速率常数或光谱）",
            "discussion（与理论/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（仪器与测量方法）",
            "data analysis（数据处理与拟合）",
            "results（数据与误差）",
            "discussion（物理解释）",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "methods（电子结构/分子动力学方法）",
            "computational details（基组、泛函与参数）",
            "results（能量、几何或光谱）",
            "validation（与实验对比）",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；J. Phys. Chem. 系列遵循 ACS 规范）",
    reporting_standards={
        "thermodynamic_quantities": "热力学量（\\Delta H、\\Delta G、\\Delta S）须注明温度与标准态",
        "kinetics": "速率常数须报告温度与活化参数（Arrhenius/Eyring）",
        "computational_details": "计算须报告方法、基组与收敛判据",
        "error_analysis": "实验误差与拟合优度须报告",
        "units_consistency": "能量单位（kJ/mol、kcal/mol、eV、Hartree）须统一并给出换算",
    },
    conventions=(
        "热力学量符号（\\Delta H、\\Delta G、\\Delta S）与标准态上标 ° 统一",
        "速率常数 k 与反应级数定义须给出",
        "光谱跃迁标注（\\nu、\\lambda、\\tilde{\\nu}）与单位一致",
        "Arrhenius 方程与 Eyring 方程形式须明确",
        "计算化学方法缩写（DFT、MP2、CCSD(T)）首次出现处给出全称",
    ),
    key_venues=(
        "Journal of Physical Chemistry A/B/C",
        "Journal of Chemical Physics",
        "Physical Chemistry Chemical Physics (PCCP)",
        "Journal of the American Chemical Society",
        "Chemical Reviews",
        "Journal of Chemical Theory and Computation",
    ),
    units_and_formulas_notes=(
        "能量常用 kJ/mol；换算 1 kcal/mol ≈ 4.184 kJ/mol，1 eV ≈ 96.485 kJ/mol",
        "温度用 K；压力用 bar 或 atm（1 atm = 1.01325 bar）",
        "公式用 amsmath；热力学偏导数与化学势记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出中心值与误差（如 k = 2.3(1) × 10^-3 s^-1）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("Python (NumPy/SciPy)", "MATLAB", "Origin", "Gaussian", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)