"""气象学学科论文支持：天气/气候/数值预报体裁、AMS 引用样式与气象度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="meteorology",
    aliases=("meteorology", "气象学", "天气学", "大气科学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "synoptic overview（天气形势概述）",
            "data（观测与再分析数据）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "forecast_verification": (
            "abstract",
            "introduction",
            "model and data（模式与数据）",
            "verification methods（检验方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-年份；JAS/JCLI 遵循 AMS 规范）",
    reporting_standards={
        "observational": "观测研究遵循气象观测数据报告规范",
        "modeling": "数值模式研究遵循模式评估报告规范",
        "forecast_verification": "预报检验遵循标准检验评分规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "个例研究遵循天气个例报告规范",
    },
    conventions=(
        "数据来源（观测/再分析/模式）须报告",
        "时间与空间分辨率须说明",
        "检验评分（RMSE/ACC/CRPS 等）定义须一致",
        "模式版本与参数化方案须说明",
        "统计显著性须报告",
    ),
    key_venues=(
        "Journal of the Atmospheric Sciences",
        "Journal of Climate",
        "Monthly Weather Review",
        "Bulletin of the American Meteorological Society",
        "Geophysical Research Letters",
        "Weather and Forecasting",
    ),
    units_and_formulas_notes=(
        "温度用 °C 或 K；气压用 hPa；风速用 m/s",
        "降水用 mm；辐射用 W/m²",
        "公式用 amsmath；动力方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "时间用 UTC 并注明时区",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("MATLAB", "GrADS", "WRF", "R"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)