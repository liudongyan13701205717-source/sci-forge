"""气象学学科论文支持：观测、模式、预报与评估体裁，WMO/CIMSS 引用与气象度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="meteorology",
    aliases=("meteorology", "气象学", "气象科学", "atmospheric_science", "climatology", "weather_studies", "forecasting", "mesoscale", "synoptic", "aerospace_weather", "severe_weather", "meteorological"),
    paper_types={
        "research": ("abstract", "introduction（背景、问题与意义）", "methodology（观测/数据/模式设置）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（个例背景与环境场）", "analysis（诊断与分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论与方法综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AMS 样式（作者-年份；JAS/Weather & Forecasting 遵循 AMS 规范）",
    reporting_standards={
        "observation": "观测研究遵循 WMO / CIMSS 数据报告规范",
        "modeling": "模式研究遵循模式验证与不确定度报告规范",
        "forecast": "预报研究遵循预报技巧评分规范（Brier / RMSE / POD）",
        "systematic_review": "综述遵循 PRISMA 声明",
    },
    conventions=("时空分辨率与数据源须注明", "个例须给出起止时间与区域", "偏差用偏差（观测−模式）符号约定", "统计显著性须注明检验与置信水平", "坐标与基准面须注明"),
    key_venues=(
        "Journal of the Atmospheric Sciences",
        "Quarterly Journal of the Royal Meteorological Society",
        "Monthly Weather Review",
        "Weather and Forecasting",
        "Geophysical Research Letters",
        "Atmospheric Research",
    ),
    units_and_formulas_notes=(
        "温度用 K 或 °C；气压用 hPa（标准 1000 hPa）",
        "风用 m/s；降水用 mm/h 或 mm/d；高度用 m 或 geopotential m",
        "能量通量用 W/m²；公式用 amsmath 并编号",
        "预报技巧须报 Brier score / POD / misses 等",
        "时间序列须注明时间基准（UTC）与内插方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("WRF", "ECMWF (IFS)", "GFS / NAM", "HYSPLIT", "GrADS / NCL", "Python (xarray, NetCDF)", "MATLAB", "IDW / kriging", "CMA / 雷达 (CINRAD)", "卫星数据 (FY / GOES / MODIS)", "reanalysis (ERA5 / MERRA)", "R (ggplot2, dplyr)", "QGIS", "ArcGIS", "ObsPy（邻近）", "GRIDS", "HawkEye", "MeteoPy", "DWD / NCEP 数据平台", "数值天气预报评估系统（MOGREPS）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "WMO 规范数据库"),
)
