"""食品加工学科论文支持：食品加工工艺、食品工程与加工技术研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_processing",
    aliases=("food_processing", "食品加工", "食品工程", "食品工艺", "食品制造", "食品工厂", "食品生产线", "食品工业"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 22000 食品安全管理", "k2": "GB 14881 食品生产卫生标准", "k3": "Codex 食品工厂标准"},
    conventions=("工艺参数须注明温度、压力、时间与功率", "设备参数须注明型号与厂商", "食品组分须注明质量分数", "能源消耗须注明 kWh/单位产量", "试验须注明平行组数与变异系数"),
    key_venues=("Food and Bioproducts Processing", "Journal of Food Engineering", "LWT - Food Science and Technology", "Innovative Food Science and Emerging Technologies", "Food Control"),
    units_and_formulas_notes=("热功率单位：kW", "能耗：kWh/t", "产能：kg/h 或 t/d", "温度单位：℃"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Fluent（CFD 仿真）", "COMSOL Multiphysics", "MATLAB / Simulink", "Siemens TIA Portal（PLC 编程）", "WinCC（SCADA 系统）", "Minitab（六西格玛分析）", "质构仪 (Texture Analyzer)", "色差仪 (Colorimeter)", "近红外光谱仪 (NIR)", "流变仪 (Rheometer)", "水分活度仪", "气相色谱仪 (GC)", "液相色谱仪 (HPLC)", "质构剖面仪 (TPA)", "高速摄像机（过程成像）", "Python（数据处理）", "RStudio", "Origin（数据绘图）", "LaTeX（排版）", "EndNote（文献管理）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
