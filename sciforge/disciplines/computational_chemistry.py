"""计算化学学科论文支持：电子结构/分子模拟体裁、ACS 引用样式与计算化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computational_chemistry",
    aliases=("computational chemistry", "计算化学", "分子模拟", "molecular simulation",
             "电子结构计算", "electronic structure", "分子动力学", "molecular dynamics",
             "化学信息学", "cheminformatics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与计算目标）",
            "methods（理论方法与软件）",
            "computational details（基组、泛函、参数）",
            "results（能量、几何、光谱或动力学）",
            "discussion（与实验/文献对比）",
            "conclusion",
            "references",
        ),
        "method_development": (
            "abstract",
            "introduction",
            "theory（方法推导）",
            "benchmark（测试集与评估指标）",
            "results（精度与效率）",
            "discussion（适用范围）",
            "references",
        ),
        "simulation": (
            "abstract",
            "introduction",
            "model（力场/体系构建）",
            "simulation details（系综、温度、时长）",
            "results（轨迹分析与性质）",
            "validation（与实验对比）",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；J. Chem. Theory Comput. 遵循 ACS 规范）",
    reporting_standards={
        "method_reproducibility": "软件、版本、基组、泛函与收敛判据须完整报告",
        "basis_set": "基组与赝势须说明；BSSE 修正如适用须报告",
        "convergence": "能量/几何收敛标准与 k 点/网格密度须报告",
        "benchmark": "方法对比须给出测试集与统计指标（MAE、RMSE）",
        "data_availability": "输入文件与参数须可复现（附补充材料）",
    },
    conventions=(
        "方法缩写（DFT、HF、MP2、CCSD(T)、MD、QM/MM）首次出现处给出全称",
        "泛函命名（B3LYP、ωB97X-D、PBE0）与基组（def2-TZVP、6-31G*）规范书写",
        "能量单位（Hartree、eV、kJ/mol）须统一并给出换算",
        "几何优化与频率计算（确认驻点）须报告",
        "分子动力学须报告力场、系综与积分步长",
    ),
    key_venues=(
        "Journal of Chemical Theory and Computation",
        "Journal of Chemical Physics",
        "Journal of Physical Chemistry A/B/C",
        "Journal of Computational Chemistry",
        "Physical Chemistry Chemical Physics (PCCP)",
        "Wiley Interdisciplinary Reviews: Computational Molecular Science",
    ),
    units_and_formulas_notes=(
        "能量换算：1 Hartree ≈ 627.509 kcal/mol ≈ 2625.5 kJ/mol",
        "距离用 Å；时间用 ps/ns（MD）",
        "公式用 amsmath；Hamiltonian 与算符记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出精度（如 MAE = 0.8 kcal/mol）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("Gaussian", "ORCA", "Python (NumPy/SciPy)", "VMD", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "Zenodo"),
)