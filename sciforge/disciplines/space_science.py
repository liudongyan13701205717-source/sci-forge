"""空间科学学科论文支持：遥感/GNSS/卫星载荷/对地观测体裁、IUGG/ISPRS 样式与坐标基准注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="space_science",
    aliases=("space_science", "空间科学", "Space Science", "卫星遥感", "空间探测", "对地观测", "space observation", "遥感科学", "地球观测"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IUGG / ISPRS 样式（作者-年份）",
    reporting_standards={
        "sensor": "载荷参数（波段、空间/光谱/辐射分辨率、辐射定标系数）须完整报告",
        "geometry": "坐标基准与投影须显式声明（WGS 84 / CGCS2000 + EPSG 代码）",
        "calibration": "定标流程与地面真值来源（站点、时段、精度）须报告",
    },
    conventions=(
        "坐标统一标 WGS 84 / CGCS2000 并给出 EPSG 代码，投影单独声明",
        "遥感影像注明卫星-载荷-过境时间-级别（L1/L2A/L3）四段式",
        "时间基准统一 UTC 或 UT1，地球自转与岁差改正须说明",
        "轨道倾角、偏心率、近地点高度三要素随卫星型号一并报告",
        "辐射度量程标数字量与物理单位换算（如 DN ↔ W·m⁻²·sr⁻¹·nm⁻¹）",
    ),
    key_venues=(
        "Remote Sensing of Environment",
        "Ispra Journal (IOP Conference Series: Earth and Environmental Science)",
        "Acta Geodaetica et Cartographica Sinica",
        "IET Radar, Sonar and Navigation",
        "Journal of Spacecraft and Rockets",
    ),
    units_and_formulas_notes=(
        "辐射定标 L = kL·DN + bL（DN 数字量，kL/bL 定标系数）",
        "反射率 ρ = π·L·d² / (E_sun·cos θ_z − L_path)（d 地日距离，θ_z 太阳天顶角）",
        "空间分辨率标 m/pixel，地面采样间隔 GSD 与分辨率区分标注",
        "GNSS 定位精度标 CEPE/CEP95 与时间基准（UTC/GNSS 时刻）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ENVI 5.4", "Erdas Imagine", "QGIS", "GDAL", "SNAP 哨兵处理工具包", "GRASS GIS", "GMT 通用地图工具", "Sentinel Hub EO Browser", "Orfeo ToolBox 遥感处理", "L2A-Tools Sentinel 处理", "PyMission 卫星仿真", "LibRadTran 辐射传输", "MODTRAN 辐射传输", "Radiance 辐射度仿真", "Python Rasterio", "USGS Earth Explorer", "Python Cartopy", "Python Geopandas", "Spectral Workbench 光谱库", "RadiPy 光谱库"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
