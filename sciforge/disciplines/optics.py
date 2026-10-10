"""光学学科论文支持：光的本质、传播、干涉、衍射与偏振等基础研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optics",
    aliases=("optics", "光学", "几何光学", "Geometrical Optics", "Wave Optics", "波动光学", "Quantum Optics", "量子光学", "非线性光学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE",
    reporting_standards={"PREPRINT": "arXiv 预印本声明", "DATA_AVAIL": "原始数据公开与代码可用性", "SUPPLEMENT": "补充材料（干涉图、光谱图）完整"},
    conventions=("SI 单位制与符号体系遵循 IEEE Std 100", "波长 λ 与频率 ν 用符号表示、颜色用 nm 标注", "折射率 n 与色散系数 ν_d 定义清晰", "衍射与干涉用统一符号（相位差 Δφ）", "图表编号连续、图例规范、误差棒齐全"),
    key_venues=("Nature Photonics", "Optica", "Optics Letters", "Physical Review Letters", "Journal of the Optical Society of America A"),
    units_and_formulas_notes=("SI 单位制（长度 m、波长 nm、频率 Hz、能量 J）", "折射率 n = c/v，介电常数 ε = μ_r μ_0 ε_0", "斯涅尔定律 n₁ sin θ₁ = n₂ sin θ₂", "瑞利判据 θ_min = 1.22 λ/D"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Synopsys Zemax OpticStudio", "Synopsys Code V", "MATLAB", "Python", "NumPy/SciPy", "Photon Engineering FRED", "COMSOL Multiphysics", "Ansys Lumerical", "RSoft BeamPROP", "MATLAB Optics Toolbox", "GNU Octave", "LaTeX", "Microsoft Excel", "OriginLab", "ImageJ/Fiji", "激光干涉仪", "光谱仪", "光电倍增管", "高灵敏度示波器", "单光子计数器"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "IEEE Xplore"),
)
