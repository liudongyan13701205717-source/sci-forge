"""电磁学学科论文支持：电动力学/电磁场理论体裁、AIP 引用样式与电磁记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electromagnetism",
    aliases=("electromagnetism", "电磁学", "电动力学", "electrodynamics",
             "电磁场理论", "electromagnetic field theory", "麦克斯韦方程", "Maxwell equations"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题陈述）",
            "formulation（Maxwell 方程、本构关系与边界条件）",
            "analysis（解析/数值求解）",
            "results（场分布、传播特性或散射结果）",
            "discussion（物理解释与实验对比）",
            "conclusion",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "model（几何、材料参数与方程离散化）",
            "numerical method（FEM/FDTD/MoM 等与收敛性）",
            "results（场图、S 参数或远场方向图）",
            "validation（与解析解/测量对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework",
            "main developments（按主题综述）",
            "open problems",
            "references",
        ),
    },
    citation_style="AIP 样式（作者-年份；期刊缩写遵循 AIP 规范）",
    reporting_standards={
        "maxwell_equations": "Maxwell 方程须以微分或积分形式完整写出，注明所用单位制",
        "boundary_conditions": "界面边界条件与辐射条件须显式陈述",
        "units_system": "SI 或高斯单位制须声明；介电常数/磁导率符号须定义",
        "numerical_methods": "数值方法须说明网格/基函数、边界处理与收敛性验证",
        "material_parameters": "材料参数（\\varepsilon_r、\\mu_r、\\sigma）须给出来源与频率依赖",
    },
    conventions=(
        "电场用 \\mathbf{E}，磁场用 \\mathbf{B}（或 \\mathbf{H}，须声明约定）",
        "时谐场约定 e^{-i\\omega t} 或 e^{+i\\omega t} 须在开头声明并全文一致",
        "矢量微分算子（\\nabla\\times、\\nabla\\cdot）排版统一",
        "Poynting 矢量 \\mathbf{S} 与能量密度定义须与单位制一致",
        "坐标系统（直角/柱/球）在建模处声明",
    ),
    key_venues=(
        "Physical Review Letters",
        "Physical Review E",
        "IEEE Transactions on Antennas and Propagation",
        "Journal of Applied Physics",
        "Optics Express",
        "Journal of Electromagnetic Waves and Applications",
    ),
    units_and_formulas_notes=(
        "默认 SI 单位：E 用 V/m，B 用 T，H 用 A/m",
        "高斯单位制使用时须给出与 SI 的换算（如 1 G = 10^-4 T）",
        "公式用 amsmath；矢量场用 \\mathbf 统一，避免手写粗体",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出频率范围、网格密度与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("COMSOL", "MATLAB", "Python (NumPy)"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)