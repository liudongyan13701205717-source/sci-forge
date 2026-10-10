"""光学与光子学学科论文支持：光-物质相互作用、集成光子学与光子器件。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optics_photonics",
    aliases=("optics_photonics", "光学与光子学", "光子学", "Optics & Photonics", "Photonics", "Integrated Photonics", "集成光子学", "Quantum Photonics", "量子光子学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE",
    reporting_standards={"PREPRINT": "arXiv 预印本声明", "DATA_AVAIL": "器件结构/版图/代码可复现", "SUPPLEMENT": "补充材料（S 参数、光斑图）完整"},
    conventions=("SI 单位制与符号体系严格一致", "波导模式用 TE/TM 与模式号标识", "损耗单位统一为 dB/cm 或 dB/m", "器件 S 参数与透射谱按标准格式给出", "实验平台图完整标注元件与波长"),
    key_venues=("Nature Photonics", "Optica", "Optics Express", "Light: Science & Applications", "Photonics Research"),
    units_and_formulas_notes=("长度 μm、波长 nm、波长周期 Λ、群速度 vg = c/n_g", "群折射率 n_g = n + λ dn/dλ", "波导损耗 α = (10/L) log₁₀(P₀/P)", "耦合损耗 η = P_out / P_in"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Synopsys Zemax OpticStudio", "Synopsys Code V", "MATLAB", "Python", "NumPy/SciPy", "Photon Engineering FRED", "Ansys Lumerical", "VPIphotonics", "RSoft BeamPROP", "MEEP", "Synopsys OptiLayer", "LaserSoft", "COMSOL Multiphysics", "Ansys OptiSystem", "LITE MODELS", "LaTeX", "Microsoft Excel", "OriginLab", "ImageJ/Fiji", "SageMath"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "IEEE Xplore"),
)
