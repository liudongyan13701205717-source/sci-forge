"""环境工程论文支持：污染控制、生命周期评估、环境模型。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_engineering",
    aliases=("environmental", "environmental engineering", "水处理", "给水排水",
             "污染控制", "air pollution", "水污染", "LCA"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results", "discussion", "conclusions", "references"),
        "case_study": ("abstract", "introduction", "site description", "methods", "results", "lessons", "references"),
        "review": ("abstract", "introduction", "review methodology", "topics", "gaps", "references"),
    },
    citation_style="ACS（American Chemical Society）",
    reporting_standards={
        "monitoring": "采样点位、频次、保存条件须符合标准方法（EPA/SM/GB）",
        "analysis": "仪器型号+检出限+加标回收率须报告；空白与平行样须设",
        "modeling": "模型验证指标（RMSE、R²、NSE）与不确定性须给出",
        "health": "暴露评估须含人群特征+摄入量参数",
        "lca": "边界、功能单位、分配方法须声明（ISO 14040/44）",
    },
    conventions=(
        "化学式规范书写；浓度单位统一（mg/L、ppb、mol/m³）",
        "排放标准引用具体标准号（GB-8978、EPA 40 CFR）",
        "图表标注采样季/年份；地图给比例尺与坐标系",
        "不确定度传播用 Monte Carlo 或 Taylor 展开，报告至显著位",
        "新材料表征含 SEM/TEM/XRD 与孔径分析（BET）",
    ),
    key_venues=(
        "Environmental Science & Technology",
        "Water Research",
        "Environmental Science & Technology Letters",
        "Journal of Environmental Engineering",
        "Separation and Purification Technology",
    ),
    units_and_formulas_notes=(
        "流量 m³/d 或 L/s；负荷 kgCOD/m³/d；去除率 %",
        "能耗 kWh/m³ 或 MJ/kg；碳足迹 kgCO2-eq",
        "亨利常数、分配系数给温度并注明单位",
    ),
)