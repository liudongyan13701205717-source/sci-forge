"""粒子物理学科论文支持：高能物理/标准模型体裁、APS 引用样式与粒子物理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="particle_physics",
    aliases=("particle physics", "粒子物理", "高能物理", "high energy physics",
             "标准模型", "Standard Model", "HEP", "量子场论", "quantum field theory"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与物理目标）",
            "theoretical framework（模型或有效场论）",
            "methods（计算/实验方法）",
            "results（截面、分支比或排除限）",
            "discussion（与标准模型/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "detector and dataset（探测器、亮度与数据样本）",
            "analysis（事例选择、背景估计与系统误差）",
            "results（观测/排除限与显著性）",
            "discussion（物理解释）",
            "references",
        ),
        "phenomenological": (
            "abstract",
            "introduction",
            "framework（模型设定与参数）",
            "calculations（截面/衰变率计算）",
            "phenomenology（数值预言与实验约束）",
            "discussion",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review D/Letters，REVTeX；实验合作组用合作组名引用）",
    reporting_standards={
        "significance": "观测/排除须报告统计显著性（σ）与置信水平（CL）",
        "systematics": "系统不确定度须逐项列出并说明来源与关联",
        "cross_sections": "截面与分支比须注明能标、运动学区间与单位",
        "pdg_conventions": "粒子命名、量子数与 PDG 约定须遵循",
        "monte_carlo": "MC 模拟须报告生成器、样本量与调谐参数",
    },
    conventions=(
        "自然单位 \\hbar=c=1 默认；能量动量用 GeV",
        "粒子符号遵循 PDG（如 W^\\pm、Z^0、H、\\nu_e）",
        "四动量 p^\\mu 与 Lorentz 指标约定（度规符号）须声明",
        "费曼图用 TikZ-Feynman 或等效工具，标注动量与耦合",
        "实验论文按合作组署名并引用合作组论文",
    ),
    key_venues=(
        "Physical Review D",
        "Physical Review Letters",
        "Journal of High Energy Physics (JHEP)",
        "European Physical Journal C",
        "Nuclear Physics B",
        "Physics Letters B",
    ),
    units_and_formulas_notes=(
        "自然单位 \\hbar=c=1；能量用 GeV，截面用 pb/fb",
        "精细结构常数 \\alpha 与弱混合角 \\theta_W 定义须给出",
        "公式用 amsmath；Lorentz 指标与旋量记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出中心值、统计误差与系统误差（如 1.23 ± 0.05 ± 0.08）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ROOT", "Geant4", "Python (NumPy, SciPy)", "MadGraph"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo", "HuggingFace"),
)