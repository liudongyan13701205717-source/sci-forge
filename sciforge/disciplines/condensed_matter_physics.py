"""凝聚态物理学科论文支持：固体物理/材料物理体裁、APS 引用样式与凝聚态记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="condensed_matter_physics",
    aliases=("condensed matter physics", "凝聚态物理", "固体物理", "solid state physics",
             "材料物理", "materials physics", "强关联电子", "strongly correlated electrons"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与体系）",
            "methods（实验/计算方法）",
            "results（结构、电子或输运性质）",
            "discussion（机理分析与对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "sample preparation（样品生长与表征）",
            "measurement（测量方法与仪器）",
            "results（数据与图）",
            "discussion（物理解释）",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "method（DFT/紧束缚/量子蒙特卡洛等）",
            "computational details（赝势、基组、k 点采样）",
            "results（能带、态密度、磁性等）",
            "validation（与实验对比）",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review 系列，作者-年份，REVTeX 模板）",
    reporting_standards={
        "crystal_structure": "晶体结构、空间群与晶格参数须给出（含 ICSD/COD 编号或来源）",
        "computational_details": "DFT 计算须报告交换关联泛函、赝势、截断能与 k 点网格",
        "symmetry": "对称性分析与不可约表示须与结构一致",
        "experimental_conditions": "测量温度、磁场、压力等条件须完整报告",
        "reproducibility": "样品制备与测量参数须足以复现",
    },
    conventions=(
        "倒格子矢量与 Brillouin 区高对称点（Γ、X、M 等）记号统一",
        "能带图标注费米能级 E_F 与高对称路径",
        "晶格常数用 Å，能量用 eV，磁矩用 \\mu_B",
        "态密度、能带与输运量的定义须给出",
        "相图与相变温度标注误差棒",
    ),
    key_venues=(
        "Physical Review B",
        "Physical Review Letters",
        "Physical Review X",
        "Nature Materials",
        "Advanced Materials",
        "Nano Letters",
    ),
    units_and_formulas_notes=(
        "常用单位：长度 Å（1 Å = 10^-10 m），能量 eV，磁矩 \\mu_B",
        "k 点采样与截断能收敛性须给出收敛曲线或数值",
        "公式用 amsmath；Bloch 函数与能带记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出计算参数与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("VASP", "Quantum ESPRESSO", "MATLAB", "Python (NumPy, SciPy)"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo"),
)