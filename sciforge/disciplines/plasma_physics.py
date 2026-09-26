"""等离子体物理学科论文支持：等离子体科学/聚变体裁、AIP 引用样式与等离子体记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plasma_physics",
    aliases=("plasma physics", "等离子体物理", "等离子体科学", "plasma science",
             "磁约束聚变", "magnetic confinement fusion", "等离子体诊断", "plasma diagnostics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与等离子体体系）",
            "model（动力学/流体方程与无量纲参数）",
            "methods（解析/数值/实验方法）",
            "results（不稳定性、输运或波传播）",
            "discussion（与实验/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（装置与诊断）",
            "measurements（诊断方法与数据）",
            "results（剖面、涨落或波动谱）",
            "discussion（物理解释）",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "model（方程与无量纲化）",
            "numerical method（PIC/流体/MHD 求解器）",
            "results（模拟结果与收敛性）",
            "validation（与理论/实验对比）",
            "references",
        ),
    },
    citation_style="AIP 样式（作者-年份；Physics of Plasmas 等期刊遵循 AIP 规范）",
    reporting_standards={
        "plasma_parameters": "电子/离子温度、密度、磁场等基本参数须给出",
        "dimensionless_params": "Debye 长度、等离子体频率、\\beta 等无量纲参数须定义",
        "diagnostics": "诊断方法须说明测量原理、空间/时间分辨率与误差",
        "simulation_details": "模拟须报告网格、时间步长、粒子数与收敛判据",
        "stability_analysis": "不稳定性分析须给出色散关系与增长率",
    },
    conventions=(
        "电子温度常用 eV（1 eV ≈ 11600 K）表示，须声明",
        "密度单位 cm^-3 或 m^-3 须统一并声明",
        "等离子体频率 \\omega_{pe}、回旋频率 \\Omega_{ce} 定义须给出",
        "MHD 与动理学描述的使用范围须说明",
        "磁场方向与坐标约定（如 B 沿 z）须声明",
    ),
    key_venues=(
        "Physics of Plasmas",
        "Plasma Physics and Controlled Fusion",
        "Nuclear Fusion",
        "Journal of Plasma Physics",
        "Plasma Sources Science and Technology",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "温度用 eV 或 K 须声明并给出换算；密度用 cm^-3 或 m^-3",
        "磁场用 T（1 T = 10^4 G）",
        "公式用 amsmath；矢量与张量记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出参数范围与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("MATLAB", "Python (NumPy/SciPy)", "COMSOL", "Origin", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "Zenodo"),
)