"""地球科学学科论文支持：地球系统、气候、海洋、大气、行星科学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geoscience",
    aliases=(
        "geoscience",
        "地球科学",
        "earth_science",
        "地球科学",
        "planetary_science",
        "行星科学",
        "atmospheric_science",
        "大气科学",
        "climate_science",
        "气候科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（数据、模型与验证）",
            "results（观测与模拟）",
            "discussion（机制与不确定度）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域/事件背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="AGU（作者-年份，APA 变体）",
    reporting_standards={
        "data": "数据须报告来源、时空覆盖、精度与许可",
        "model": "模型须报告版本、参数、初始/边界条件与验证",
        "uncertainty": "结果须报告不确定度、置信区间与敏感性分析",
    },
    conventions=(
        "时空覆盖、分辨率与精度须显式说明",
        "坐标系、基准与投影须显式",
        "气候变量用 WMO 命名；单位与量纲统一",
        "统计检验报告 p 值、效应量与样本量",
        "模型与观测比较须给偏差与 RMSE",
    ),
    key_venues=(
        "Journal of Geophysical Research",
        "Nature Geoscience",
        "Earth and Planetary Science Letters",
        "Environmental Research Letters",
        "Global and Planetary Change",
    ),
    units_and_formulas_notes=(
        "温度用 K 或 °C；压强用 Pa 或 hPa",
        "长度用 m/km；速度用 m/s",
        "浓度用 ppm 或 μg/m³；通量用 W/m² 或 kg/m²/s",
        "年代用 yr CE/yr BP；同位素给 δ 与标准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "GMT (Generic Mapping Tools)", "GEOMAP", "GEOPY", "Python", "MATLAB", "R", "NetCDF", "OPeNDAP", "Panoply", "Meteostat", "ERA5 (ECMWF)", "CMIP6", "CESM", "WRF", "MATLAB NetCDF", "Jupyter Notebook", "Google Earth Engine", "MeteoSwiss"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
