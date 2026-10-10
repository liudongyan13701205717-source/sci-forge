"""光学透镜制造学科论文支持：透镜几何设计、面型加工与镀膜工艺。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optical_lens_making",
    aliases=("optical_lens_making", "光学透镜制造", "透镜制造", "Optical Lens Making", "lens making", "Lens Making", "optical element fabrication", "透镜加工", "光学元件制造"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE",
    reporting_standards={"PREPRINT": "arXiv/SPIE 预印本声明", "DATA_AVAIL": "数据可用性与原始文件归档", "SUPPLEMENT": "补充材料（Zernike/干涉图）完整"},
    conventions=("SI 单位制（长度 mm、波长 nm、焦度 D）", "折射率 n 与阿贝数 ν_d 必须声明并给出温度", "表面曲率半径与厚度的正负号规则统一", "光学设计图遵循 ANSI Z14 惯例", "图表编号连续、图例齐全、色差与波像差标注"),
    key_venues=("Optics Express", "Applied Optics", "Optical Engineering", "Journal of Vacuum Science & Technology B", "Optics and Lasers in Engineering"),
    units_and_formulas_notes=("长度单位统一为 mm、波长用 nm、折射率无量纲", "薄透镜焦距公式 1/f = (n-1)(1/R₁ - 1/R₂)", "斯涅尔定律 n₁ sin θ₁ = n₂ sin θ₂", "阿贝数 ν = (n_d - 1)/(n_F - n_C)"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Synopsys Zemax OpticStudio", "Synopsys Code V", "Synopsys LightTools", "Photon Engineering FRED", "Photon Engineering RayTrace", "Synopsys SWFA/SWFD", "SolidWorks", "AutoCAD", "Mathcad", "MATLAB", "Python (NumPy/SciPy)", "LaTeX", "Microsoft Excel", "OriginLab", "Zygo 激光干涉仪", "Autocollimator 自准直仪", "Phase Shift Interferometer", "Spectrophotometer 分光光度计", "磁控溅射镀膜机", "CNC 高精度透镜磨床"),
    category="工学",
    databases=("OpenAlex", "Crossref", "SPIE Digital Library", "arXiv"),
)
