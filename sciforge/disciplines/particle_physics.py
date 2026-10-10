"""粒子物理学科论文支持：高能物理/标准模型体裁、APS 引用样式与粒子物理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="particle_physics",
    aliases=("particle physics", "粒子物理", "高能物理", "high energy physics", "标准模型", "Standard Model", "HEP", "量子场论", "quantum field theory"),
    paper_types={
        "research": ("abstract", "introduction（背景与物理目标）", "methodology（理论框架或实验方法）", "results（截面/分支比/排除限）", "discussion（与标准模型对比）", "references"),
        "case_study": ("abstract", "introduction", "case description（探测器与数据样本）", "analysis（事例选择与背景估计）", "results（观测显著性）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（模型与有效场论）", "evidence synthesis（实验约束综述）", "future directions", "references"),
    },
    citation_style="APS 样式（Physical Review D/Letters，REVTeX；实验合作组用合作组名引用）",
    reporting_standards={"significance": "观测/排除须报告统计显著性（σ）与置信水平（CL）", "systematics": "系统不确定度须逐项列出并说明来源与关联", "cross_sections": "截面与分支比须注明能标、运动学区间与单位", "mc_simulation": "MC 模拟须报告生成器、样本量与调谐参数"},
    conventions=("自然单位 \\hbar=c=1 默认；能量动量用 GeV", "粒子符号遵循 PDG（如 W^\\pm、Z^0、H、\\nu_e）", "四动量 p^\\mu 与 Lorentz 指标约定须声明", "费曼图用 TikZ-Feynman，标注动量与耦合", "数值结果给出中心值、统计误差与系统误差"),
    key_venues=("Physical Review D", "Physical Review Letters", "Journal of High Energy Physics (JHEP)", "European Physical Journal C", "Nuclear Physics B", "Physics Letters B"),
    units_and_formulas_notes=("自然单位 \\hbar=c=1；能量用 GeV，截面用 pb/fb", "精细结构常数 \\alpha 与弱混合角 \\theta_W 定义须给出", "公式用 amsmath；Lorentz 指标与旋量记号统一", "显示公式仅在被引用时编号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ROOT", "Geant4", "Pythia8", "MadGraph5_aMCfast", "Sherpa", "Delphes", "CMSSW", "ATLAS 分析框架", "CMS 分析框架", "Pandora 粒子流算法", "FormCalc", "Mathematica", "FeynArts", "TikZ-Feynman", "Jupyter", "MATLAB", "Python (NumPy, SciPy)", "HEPData", "Particle Data Group Review", "LHC Higgs Cross Section Working Group 工具"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
