"""光学技术学科论文支持：工程光学系统设计、非成像光学与光纤工程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optical_technology",
    aliases=("optical_technology", "光学技术", "工程光学", "Optical Technology", "Engineering Optics", "Applied Optics", "非成像光学", "Non-imaging Optics", "光纤技术"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE",
    reporting_standards={"PREPRINT": "arXiv/SPIE 预印本声明", "DATA_AVAIL": "数据可用性与原始文件归档", "REPRODUCIBILITY": "仿真参数与软件版本可复现"},
    conventions=("SI 单位制与符号体系严格一致", "光学效率、通量守恒（etendue）必声明", "图表标注单位、误差棒与不确定度", "实验装置图遵循示意图惯例（等距投影）", "仿真与实验结果对照讨论"),
    key_venues=("Optics and Lasers in Engineering", "Optical Engineering", "Optics Communications", "Applied Optics", "Optics Express"),
    units_and_formulas_notes=("长度 mm/cm、波长 nm、光学效率以百分数报告", "etendue G = n² · Ω · A 光通量不变量", "光学效率 η = Φ_out / Φ_in", "光纤数值孔径 NA = n sin θ_max"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Synopsys Zemax OpticStudio", "Synopsys Code V", "Photon Engineering FRED", "Synopsys LightTools", "MATLAB", "Python (NumPy/SciPy)", "Synopsys OptiLayer", "Ansys Lumerical", "RSoft BeamPROP", "SolidWorks", "AutoCAD", "COMSOL Multiphysics", "LaTeX", "Microsoft Excel", "OriginLab", "ImageJ/Fiji", "激光干涉仪", "光学示波器", "光谱仪", "分光光度计"),
    category="工学",
    databases=("OpenAlex", "Crossref", "SPIE Digital Library", "IEEE Xplore"),
)
