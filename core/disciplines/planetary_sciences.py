"""行星科学（复数）学科论文支持：多行星比较/系外行星/行星系统动力学体裁、AAS 引用样式与行星科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="planetary_sciences",
    aliases=("planetary sciences", "行星科学", "行星学", "planetology", "行星系统", "planetary systems", "系外行星系统", "exoplanetary systems", "太阳系", "solar system", "行星物理", "planetary physics", "行星地质", "planetary geology", "行星气候", "planetary climates"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与行星系统）", "data and methods（多星比较/系外行星方法）", "results（多行星尺度发现）", "discussion（演化与形成解释）", "references"),
        "observational": ("abstract", "introduction", "observations（望远镜/探测器与观测几何）", "data reduction（定标与处理）", "results（光谱、光度或成像）", "discussion（物理解释）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（多行星比较综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AAS 样式（ApJ/ApJL 作者-年份；Icarus 等亦可遵循 Elsevier 样式）",
    reporting_standards={"body_identification": "天体名称与 IAU 命名须准确", "coordinate_system": "经纬度坐标系与参考面（IAU 约定）须声明", "data_provenance": "任务数据须注明仪器、版本与处理管线", "remote_sensing": "遥感反演须报告波段、分辨率与辐射定标", "multi_planet": "多行星比较须统一观测基线与误差模型"},
    conventions=("行星名称遵循 IAU 命名法；系外行星用 TYCHO/NASA 编号", "坐标用行星经纬度（IAU 约定）并注明本初子午线定义", "距离用 AU，质量用 M_⊕ 或 M_J", "轨道要素（P、a、e、i、ω、Ω）须完整给出", "多行星比较须报告统一口径（口径、时域、仪器）"),
    key_venues=("Icarus", "Journal of Geophysical Research: Planets", "Planetary and Space Science", "The Planetary Science Journal", "The Astrophysical Journal (exoplanets)"),
    units_and_formulas_notes=("距离用 AU；质量用 M_⊕/M_J；周期用 d 或 yr", "温度用 K；大气压用 Pa 或 bar", "公式用 amsmath；开普勒轨道方程须给出", "多行星样本量与选择偏差须讨论"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python (Astropy/NumPy/SciPy)", "R", "ArcGIS/QGIS", "MATLAB", "LaTeX", "Jupyter Notebook", "CASA (Common Astronomy Software Applications)", "Hubble Space Telescope", "James Webb Space Telescope", "Spitzer Space Telescope", "WISE/NEOWISE", "Kepler Space Telescope", "TESS (Transiting Exoplanet Survey Satellite)", "JPL Horizons", "JPL Small-Body Database", "Planetary Data System (PDS)", "NASA Exoplanet Archive", "MAST (Mikulski Archive)", "STScI Hubble Archive", "ESO VLT (Very Large Telescope)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
