"""火山学学科论文支持：火山喷发机制、监测与灾害评估的体裁与监测数据规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vulcanology",
    aliases=("vulcanology", "火山学", "火山研究", "火山监测", "volcano", "volcanoes",
             "volcano research", "volcano monitoring", "volcano hazard"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与科学问题）",
            "site description（研究区概况）",
            "methods（监测与采样方法）",
            "results（结果与数据分析）",
            "discussion（讨论与机理解释）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "volcanic setting（火山构造背景）",
            "case description（喷发事件记录）",
            "analysis（观测数据分析）",
            "hazard assessment（灾害评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "volcanic types and eruption styles（火山类型与喷发样式综述）",
            "monitoring techniques（监测技术综述）",
            "hazard prediction and risk（灾害预测与风险评估）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "eruption_chronology": "喷发事件须给出明确时间线、分类（VEI 等级）与产物描述（火山碎屑、熔岩流、火山灰柱）",
        "hazard_assessment": "灾害评估须结合地震、气体排放、地表形变等多源监测数据，并标注各数据源的不确定性范围",
        "field_observation": "野外观测须包含采样位置（WGS84 GPS 坐标）、采样时间、样品编号与环境条件记录",
    },
    conventions=(
        "火山命名使用全称加别名体系（如 Mount St. Helens / 圣海伦斯火山），首次出现时标注",
        "喷发分类采用 VEI（火山爆发指数）或 GVP（全球火山潜力）分级，全文一致",
        "坐标以 WGS84 为基准；高程以基准面（MSL）为参照，单位 m",
        "气体成分以 mol% 表示；地壳变形以 μstr（微应变）或 mm 为单位",
        "术语遵循 IAVCEI（国际火山学与地球深部研究协会）与 IUGG（国际大地测量与地球物理联合会）统一命名",
    ),
    key_venues=(
        "Bulletin of Volcanology",
        "Journal of Volcanology and Geothermal Research",
        "Geology",
        "Journal of Geophysical Research: Solid Earth",
        "Geophysical Research Letters",
    ),
    units_and_formulas_notes=(
        "温度以 K（开尔文）标注；野外数据同时报告 °C 便于对照",
        "气压单位为 bar 或 hPa；高度差以 m 表示",
        "地震波速度单位为 km/s；震级为无单位量纲数值",
        "CO₂ / SO₂ 通量以 t/d（吨/日）或 kg/s 为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SAC", "SeisComP", "MATLAB", "Python", "ArcGIS Pro", "QGIS", "ENVI", "SODATE", "Cassiopeia", "DJI Enterprise", "Agisoft Metashape", "Trimble GPS", "Leica RTK", "ObsPy", "GMT", "Surfer", "Petrel", "R", "WebGis", "PyTremor"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
