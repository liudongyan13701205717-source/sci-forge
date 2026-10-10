"""Astronomical Sciences 学科论文支持：天体物理学、宇宙学、星系形成与大规模结构、数值模拟与理论天体物理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="astronomical_sciences",
    aliases=(
        "astronomical_sciences",
        "Astronomical Sciences",
        "天体物理科学",
        "天体物理学",
        "astrophysics",
        "宇宙学",
        "cosmology",
        "星系形成与演化",
        "galaxy formation and evolution",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "observations / simulation（数据源、参数、分辨率、初始条件）",
            "methods",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "theoretical": (
            "abstract",
            "introduction",
            "model and formalism",
            "analysis",
            "predictions",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical context",
            "main developments",
            "open questions",
            "references",
        ),
    },
    citation_style="AAS 样式（apj 2021 修订版；作者-年份或编号，视期刊）",
    reporting_standards={
        "data": "数据源、观测时间、曝光时间、望远镜/仪器、数据处理软件与版本须报告",
        "uncertainty": "不确定度须报告（Poisson 噪声、系统误差、蒙特卡洛抽样误差）",
        "simulation": "模拟分辨率、初始条件、物理开关、时间步、粒子/网格数须报告",
        "reproducibility": "代码、数据与脚本链接须给出（GitHub 或 Zenodo）；随机种子须报告",
        "comparisons": "与观测/其它工作的比较须使用统一统计口径",
    },
    conventions=(
        "天体名与缩写用 IAU 标准（如 NGC、M、M87, M31）；恒星名用 B/HDR/HD",
        "红移 z 与距离模数 μ 用 amsmath 数学环境；光年/秒差距/角秒/毫角秒用 pc, Mpc, ′, ″, mas",
        "光谱图横轴波长 nm 或 Å，纵轴 flux density（Jy、erg·s⁻¹·cm⁻²·Å⁻¹ 或 W·m⁻²·Hz⁻¹）",
        "光度用 L⊙；质量用 M⊙；角尺度用 arcmin / arcsec",
        "误差用上下标 ±；上下界用 \u27e8x\u27e9 与下/上箭头；中位数用 \tilde{x}",
        "图表首次出现处编号；数据点标注误差棒；散点密度高时用二维直方图或核密度",
    ),
    key_venues=(
        "The Astrophysical Journal (ApJ)",
        "The Astrophysical Journal Letters (ApJL)",
        "Monthly Notices of the Royal Astronomical Society (MNRAS)",
        "The Astronomical Journal (AJ)",
        "The Journal of Physics: Conferences Series",
        "Annual Review of Astronomy and Astrophysics",
        "Space Telescope Science Institute (STScI) Proceedings",
    ),
    units_and_formulas_notes=(
        "距离用 pc / kpc / Mpc；角尺度用 arcmin / arcsec / mas",
        "光度 L⊙；质量 M⊙；温度 K；红移 z 无量纲",
        "公式用 amsmath；H₀ 报告 h₇₀ = H₀ / 100 km·s⁻¹·Mpc⁻¹",
        "误差用上下标 ±；显著性用 σ（3σ、5σ）",
        "数值结果给出均值 ± SD 或中位数[IQR]",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Astropy", "PyVista", "Pyvo", "Astroquery", "Matplotlib", "NumPy", "SciPy", "pandas", "R", "Jupyter", "CAMB", "CLASS", "CosmoMC", "GetDist", "emcee", "Planck", "Gadget", "AREPO", "GIZMO", "RAMSES", "FLASH", "Enzo", "ART", "Athena++", "PLUTO", "Cholla", "VisIt", "ParaView", "YASA", "Spheral", "Zotero", "EndNote"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "NASA ADS", "SDSS", "Planck Legacy", "Gaia Archive", "DES", "DESI"),
)
