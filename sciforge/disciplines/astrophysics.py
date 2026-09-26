"""天体物理学论文支持：观测数据、宇宙学参数、信噪比分析。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="astrophysics",
    aliases=("astrophysics", "astronomy", "cosmology", "astro", "stars", "galaxies"),
    paper_types={
        "research": ("abstract", "introduction", "observations/data", "analysis", "results", "discussion", "conclusions", "references"),
        "survey": ("abstract", "introduction", "survey design", "data release", "results", "references"),
        "letter": ("abstract", "text", "references"),
    },
    citation_style="AAS Journals style（编号），如 [1] 或 (Author et al. 2023)",
    reporting_standards={
        "photometry": "测光系统与零点须声明（AB/Vega）；误差含随机与系统",
        "spectroscopy": "光谱仪分辨率、信噪比、消光改正须报告",
        "cosmology": "宇宙学参数须引 Planck 或声明采用的 ΛCDM 值",
        "uncertainty": "置信区间用蒙特卡洛或 Fisher/桶分析传播",
        "reproducibility": "观测/模拟数据须存档（Zenodo/NASA/IPAC 链接）",
    },
    conventions=(
        "坐标用 J2000；星表名统一（SDSS/2MASS/GAIA DR3）",
        "流量用 mJy/mag；光谱分辨率 R=λ/Δλ",
        "红移 z 定义与细胞距离约定明确",
        "望远镜/仪器名与 Proposal ID 须出现",
        "图坐标轴用对数时须声明",
    ),
    key_venues=(
        "The Astrophysical Journal",
        "Astronomical Journal",
        "Monthly Notices of the Royal Astronomical Society",
        "Astronomy & Astrophysics",
        "ApJ Letters",
    ),
    units_and_formulas_notes=(
        "距离用 pc/kpc/Mpc；光度 erg/s 或 Lsun；质量 Msun",
        "宇宙年龄给 Gyr；哈勃常数 H0 单位 km/s/Mpc",
        "星等对数负数（数值越小越亮），测量须带误差棒",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("Python (NumPy/SciPy)", "LaTeX", "CASA", "DS9", "TOPCAT"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo", "HuggingFace"),
)