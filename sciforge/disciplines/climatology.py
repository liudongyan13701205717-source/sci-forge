"""气候学与气象学论文支持：气候系统、大气环流、极端天气。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="climatology",
    aliases=("climate", "meteorology", "oceanography", "气候", "大气科学",
             "海洋", "weather", "气候模拟", "extreme weather"),
    paper_types={
        "research": ("abstract", "introduction", "data and methods", "results", "discussion", "conclusions", "references"),
        "simulation": ("abstract", "introduction", "model setup", "experiments", "results", "analysis", "references"),
        "review": ("abstract", "introduction", "scope", "findings", "outlook", "references"),
    },
    citation_style="AGU（American Geophysical Union）",
    reporting_standards={
        "data": "观测数据来源与不完整合规须声明；再分析资料给版本",
        "model": "模式版本与分辨率须声明；SPM/IPCC 对比需要尺度参考",
        "stats": "显著性检验须考虑空间相关（AR(1) 或 MC 模拟）",
        "scenarios": "排放情景须使用（SSP/RCP）一致",
        "impact": "影响评估须含置信区间",
    },
    conventions=(
        "全球/区域平均须给面积权重；年份平均用365.25日",
        "图给自定义色标；偏差图与格点图注显著性hatch区域",
        "台风路径用最佳路径数据集（IBTrACS/JTWC）",
        "异常数据距平基准期使用气候学参考期（如 1991–2020）",
        "报告多指标（平均值、百分位）不仅阈值变量",
    ),
    key_venues=(
        "Journal of Climate",
        "Journal of the Atmospheric Sciences",
        "Geophysical Research Letters",
        "Climate Dynamics",
        "Bulletin of the American Meteorological Society",
    ),
    units_and_formulas_notes=(
        "温度 K 或 °C；降水 mm/day；气压 hPa",
        "辐射 W/m²；热含量 J；海平面 mm",
        "时间尺度却给年年标准差或趋势斜率/显著性",
    ),
)