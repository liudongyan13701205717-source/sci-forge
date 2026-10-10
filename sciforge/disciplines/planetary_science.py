"""行星科学学科论文支持：行星地质/行星大气/系外行星级彩、AAS 引用样式与行星科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="planetary_science",
    aliases=("planetary science", "行星科学", "行星学", "planetology", "行星地质", "planetary geology", "行星大气", "planetary atmospheres", "系外行星", "exoplanets", "太阳系统", "solar system", "天体测量", "astrometry"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与天体）", "data and methods（观测/任务数据与分析方法）", "results（表面、大气或轨道性质）", "discussion（地质/气候/演化解释）", "references"),
        "observational": ("abstract", "introduction", "observations（望远镜/探测器与观测几何）", "data reduction（定标与处理）", "results（光谱、光度或成像）", "discussion（物理解释）", "references"),
        "mission_report": ("abstract", "introduction", "mission context（任务与仪器）", "measurements（数据采集与校准）", "results（科学发现）", "discussion（意义与后续）", "references"),
    },
    citation_style="AAS 样式（ApJ/ApJL 作者-年份；Icarus 等亦可遵循 Elsevier 样式）",
    reporting_standards={"body_identification": "天体名称与 IAU 命名须准确", "coordinate_system": "经纬度坐标系与参考面（IAU 约定）须声明", "data_provenance": "任务数据须注明仪器、版本与处理管线", "remote_sensing": "遥感反演须报告波段、分辨率与辐射定标", "model_parameters": "大气/地质模型参数须给出来源与不确定性"},
    conventions=("行星/卫星名称遵循 IAU 命名法；地形特征用标准术语（crater、regio 等）", "坐标用行星经纬度（IAU 2000/2015 约定）并注明本初子午线定义", "距离用 AU，质量用 M_⊕ 或 M_J", "表面年龄用撞击坑统计定年", "光谱数据标注波长单位与仪器"),
    key_venues=("Icarus", "Journal of Geophysical Research: Planets", "Planetary and Space Science", "The Planetary Science Journal", "Earth and Planetary Science Letters"),
    units_and_formulas_notes=("距离用 AU（1 AU ≈ 1.496 × 10^8 km）；质量用 M_⊕/M_J", "表面温度用 K；大气压用 Pa 或 bar", "公式用 amsmath；轨道要素（a、e、i）定义须给出", "数值结果给出中心值与误差，注明数据版本"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python (Astropy/NumPy/SciPy)", "R", "ArcGIS/QGIS", "MATLAB", "LaTeX", "Jupyter Notebook", "CASA (Common Astronomy Software Applications)", "Hubble Space Telescope", "James Webb Space Telescope", "Spitzer Space Telescope", "WISE/NEOWISE", "Kepler Space Telescope", "TESS (Transiting Exoplanet Survey Satellite)", "JPL Horizons", "JPL Small-Body Database", "Planetary Data System (PDS)", "NASA Planetary Science Data System", "MAST (Mikulski Archive)", "STScI Hubble Archive", "ESO VLT (Very Large Telescope)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
