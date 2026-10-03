"""大气科学论文支持：气象学、气候学、大气化学、数值天气预报。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="atmospheric_science",
    aliases=("atmospheric_science", "meteorology", "climatology", "大气科学", "气象学", "气候学"),
    paper_types={
        "research": ("abstract", "introduction", "data and methods", "results", "discussion", "conclusions", "references"),
        "modeling": ("abstract", "introduction", "model description", "experiment design", "results", "evaluation", "discussion", "conclusions", "references"),
        "observation": ("abstract", "introduction", "instruments", "data processing", "results", "discussion", "conclusions", "references"),
    },
    citation_style="AMS style（编号），如 [1] 或 (Author and Author Year)",
    reporting_standards={
        "model_evaluation": "模式评估须报告技巧评分（skill score）、偏差、RMSE、相关系数",
        "reanalysis": "再分析数据须声明版本（ERA5/MERRA-2/JRA-55）与时空分辨率",
        "uncertainty": "不确定性须用集合预报或 bootstrap 量化",
        "sensitivity": "敏感性试验须控制单一变量，其余保持基线",
    },
    conventions=(
        "气象变量用标准缩写（T2m/U10m/Q2m/SP）；时次用 UTC",
        "天气系统用 WMO 标准分类；热带气旋用 Saffir-Simpson 或 T-分级",
        "图：天气图用等压线/等温线；时间序列用折线图+阴影（集合散布）",
        "坐标：纬度用 °N/°S，经度用 °E/°W；高度用 hPa 或 km",
        "模式分辨率用 Δx × Δy 或等效谱截断（如 T639）",
    ),
    key_venues=(
        "Journal of the Atmospheric Sciences",
        "Monthly Weather Review",
        "Atmospheric Chemistry and Physics",
        "Journal of Climate",
        "Weather and Forecasting",
    ),
    units_and_formulas_notes=(
        "温度用 K 或 °C（须声明）；气压用 hPa；风速用 m/s",
        "降水量用 mm/day 或 mm/hour；混合比用 g/kg 或 kg/kg",
        "辐射通量用 W/m²；光学厚度无量纲",
        "模式时间步长用 s；预报提前量用 h 或 days",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("WRF", "GrADS", "Python (NumPy/SciPy)", "NCL", "MATLAB"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI", "arXiv"),
)
