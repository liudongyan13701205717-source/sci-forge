"""经典力学学科论文支持：分析力学/刚体动力学体裁、AIP 引用样式与力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="classical_mechanics",
    aliases=("classical mechanics", "经典力学", "分析力学", "analytical mechanics",
             "刚体动力学", "rigid body dynamics", "牛顿力学", "Newtonian mechanics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题陈述）",
            "formulation（广义坐标、约束与运动方程推导）",
            "analysis（守恒量、稳定性或数值解）",
            "results（解析/数值结果与验证）",
            "discussion（物理解释与适用范围）",
            "conclusion",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background（Lagrange/Hamilton 形式体系回顾）",
            "main exposition（以例子驱动的推导链）",
            "exercises（练习，可选）",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "model（动力学方程与无量纲化）",
            "numerical method（积分器、步长与误差控制）",
            "results（轨迹、相图与收敛性）",
            "validation（与解析解/实验对比）",
            "references",
        ),
    },
    citation_style="AIP 样式（作者-年份，如 [Smith 2020]；期刊缩写遵循 AIP 规范）",
    reporting_standards={
        "equations_of_motion": "运动方程须从明确的作用量/受力分析导出，注明坐标选取与约束类型",
        "conservation_laws": "守恒量（能量、动量、角动量）须显式说明其成立条件与对称性来源",
        "initial_conditions": "初值条件须完整给出，数值解须报告积分区间与步长",
        "dimensional_analysis": "无量纲化须说明特征尺度；量纲一致性须可复核",
        "stability_claims": "稳定性结论须给出判据（线性化、Lyapunov 或数值证据）并注明适用范围",
    },
    conventions=(
        "广义坐标统一用 q_i，广义动量用 p_i；Lagrangian 用 L，Hamiltonian 用 H",
        "矢量记法全文一致：位置 r、速度 \\dot{\\mathbf{r}}、角速度 \\boldsymbol{\\omega}",
        "约束分类（完整/非完整、定常/非定常）在建模处显式声明",
        "相图与轨迹图须标注坐标轴、参数值与初值",
        "数值积分须说明积分器类型（如 RK4、辛积分）与误差控制策略",
    ),
    key_venues=(
        "Physical Review E",
        "Journal of Applied Mechanics (ASME)",
        "Archive for Rational Mechanics and Analysis",
        "SIAM Journal on Applied Dynamical Systems",
        "European Journal of Mechanics - A/Solids",
        "Nonlinear Dynamics",
    ),
    units_and_formulas_notes=(
        "默认 SI 单位；角度用弧度，角速度用 rad/s",
        "公式用 amsmath：多行推导按 = 对齐，矢量用 \\mathbf 或 \\boldsymbol 统一",
        "能量单位 J，功率 W；天体/分子尺度可注明改用 eV 或原子单位并给出换算",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出有效数字位数与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("MATLAB", "Python (NumPy, SciPy)", "Mathematica"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)