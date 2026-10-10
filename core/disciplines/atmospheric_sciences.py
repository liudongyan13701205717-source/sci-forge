"""大气科学 (Atmospheric Sciences) 学科论文支持：气象/气候/大气化学/环境/航空/行星大气。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="atmospheric_sciences",
    aliases=(
        "Atmospheric Sciences", "大气科学", "atmospheric science",
        "meteorology", "气象学", "climatology", "气候学",
        "atmospheric chemistry", "大气化学", "aviation meteorology",
        "severe weather", "行星大气", "planetology", "空间天气", "space weather",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "data and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "modeling": (
            "abstract",
            "introduction",
            "model description",
            "experiment design",
            "results",
            "evaluation",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current state",
            "open questions",
            "references",
        ),
    },
    citation_style="AMS 样式（编号）或 IPCC 样式",
    reporting_standards={
        "model_evaluation": "模式评估须报告技巧评分、偏差、RMSE、相关系数",
        "reanalysis": "再分析数据须声明版本与分辨率（ERA5 / MERRA-2 / JRA-55）",
        "uncertainty": "不确定性须用集合预报或 bootstrap 量化",
        "sensitivity": "敏感性试验须控制单一变量",
        "reproducibility": "模式配置、初边界条件、代码版本须完整披露",
    },
    conventions=(
        "气象变量用标准缩写（T2m/U10m/Q2m/SP）；时次用 UTC",
        "坐标：纬度 °N/°S，经度 °E/°W；气压层 hPa 或几何高度 km",
        "天气系统用 WMO 分类；热带气旋用 Saffir-Simpson 或 JTWC 分级",
        "模式分辨率用 Δx × Δy 或等效谱截断（T639、N96 等）",
        "集合预报须报告成员数、初始扰动幅度、控制运行标识",
        "气候指标须遵循 WMO/TGAI 定义（如 1.5℃ 阈值）",
    ),
    key_venues=(
        "Journal of the Atmospheric Sciences",
        "Monthly Weather Review",
        "Atmospheric Chemistry and Physics",
        "Journal of Climate",
        "Weather and Forecasting",
        "Geophysical Research Letters",
        "Nature Climate Change",
        "Climate Dynamics",
        "Atmospheric Environment",
        "Journal of Geophysical Research: Atmospheres",
    ),
    units_and_formulas_notes=(
        "温度 K 或 °C（须声明）；气压 hPa；风速 m/s",
        "降水量 mm/day 或 mm/h；混合比 g/kg 或 kg/kg",
        "辐射通量 W/m²；光学厚度无量纲",
        "预报提前量 h 或 days；模式时间步长 s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("WRF", "NCAR WPS", "WRF-chem", "GEOS-Chem", "GEFS", "MERRA-2", "ERA5", "JRA-55", "CFSv2", "CMA-GFS", "NMM-CHEM", "GrADS", "NCL", "xarray", "MetPy", "Python (NumPy/SciPy)", "MATLAB", "GMT", "Cartopy", "Panoply", "CDO", "ArcGIS", "QGIS", "ECMWF OpenData", "Copernicus CAMS", "MeteoInfo", "PyPSolar"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI", "Pangaea", "Copernicus", "NOAA", "WMO"),
)
