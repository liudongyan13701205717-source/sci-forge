"""地球科学论文支持：地质学、地球化学、地球物理、古气候、矿产资源。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="earth_science",
    aliases=("earth_science", "geosciences", "地球科学", "地学"),
    paper_types={
        "research": ("abstract", "introduction", "geological setting", "methods", "results", "discussion", "conclusions", "references"),
        "survey": ("abstract", "introduction", "regional geology", "data sources", "findings", "interpretation", "conclusions", "references"),
        "modeling": ("abstract", "introduction", "model setup", "parameters", "results", "validation", "discussion", "conclusions", "references"),
    },
    citation_style="AGU style（编号），如 [1]；或 (Author Year)",
    reporting_standards={
        "geochronology": "年代学须报告分析方法（U-Pb/Ar-Ar/OSL）、矿物/岩石、误差（2σ）与标样",
        "geochemistry": "地球化学须报告分析仪器、标样、检出限与数据处理方法",
        "geophysics": "地球物理须报告仪器型号、观测参数（频率/点距）与反演方法",
        "remote_sensing": "遥感须报告卫星/传感器、波段、空间/时间分辨率与预处理步骤",
    },
    conventions=(
        "岩石名称用 IUGS 标准分类（矿物比例图解）",
        "地层用正式名称（群/组/段）+ 地理位置",
        "坐标用 WGS84；海拔用 m asl",
        "矿物缩写用 IMA 标准（如 Qtz/Pl/Kfs）",
        "图：地质图须含图例、比例尺与方位；柱状图须含地层符号",
    ),
    key_venues=(
        "Journal of Geophysical Research: Solid Earth",
        "Earth and Planetary Science Letters",
        "Geochimica et Cosmochimica Acta",
        "Geology",
        "Tectonics",
    ),
    units_and_formulas_notes=(
        "长度用 m/km；深度用 km below surface",
        "温度用 °C；压力用 GPa/kbar",
        "年龄用 Ma（百万年）/Ga（十亿年）/ka（千年）",
        "浓度用 ppm/‰/ppb；同位素比用 δ（‰ V-SMOW/V-PDB）",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("ArcGIS", "QGIS", "Python (NumPy/SciPy)", "MATLAB", "地震仪"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Zenodo", "Semantic Scholar"),
)
