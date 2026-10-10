"""燃气分布学科论文支持：管道运输、调压、泄漏检测、燃烧与安全管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gas_distribution",
    aliases=("gas_distribution", "燃气分布", "燃气输配", "城镇燃气", "Gas distribution network", "Natural gas distribution", "管道运输", "调压站"),
    paper_types={
        "research": ("abstract", "introduction（管网与安全问题）", "methodology（管网建模、检测与仿真方法）", "results（运行数据与仿真结果）", "discussion（安全改进与经济评价）", "references"),
        "case_study": ("abstract", "introduction", "case description（城镇燃气系统现状）", "analysis（管网结构、调压与运行）", "results（能耗、泄漏与经济效益）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（管道流体力学、泄漏检测与调控综述）", "evidence synthesis（不同检测技术比较）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份），或《燃气》等工程期刊 GB/T 7714 规范",
    reporting_standards={"network": "管网建模须报告节点数、管段数、流量与压力等级", "leak_detection": "泄漏检测须报告方法（激光/热成像/嗅探）、检出限与漏率", "operation": "运行须报告日均供气量、压力波动、事故率与能耗"},
    conventions=("压力用 MPa 或 kPa", "管径用 DN（公称直径）", "流量用 Nm³/h", "燃气体积分数（甲烷、丙烷）以 % 计", "温度用 ℃"),
    key_venues=("Journal of Natural Gas Science and Engineering", "天然气工业", "Applied Energy", "Energy", "燃气与热力工程"),
    units_and_formulas_notes=("压力用 MPa（10⁶ Pa）", "流量用 Nm³/h 或 m³/s", "管径用 mm 或 DN", "温度用 ℃", "热值用 MJ/m³"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PIPEFLOW（管道水力学）", "GasSim（管网仿真）", "AFT Impulse（瞬变流分析）", "EPANET（管网分析）", "ANSYS Fluent（CFD 分析）", "COMSOL Multiphysics", "OpenFOAM（自由流体）", "激光甲烷检测仪（LidarGas）", "热成像仪（FLIR）", "管道声呐（管道检测）", "AutoCAD Civil 3D", "SolidWorks", "MATLAB", "Simulink", "SCADA 系统", "Python（pandas/网络建模）", "R", "Origin", "SPSS", "QGIS", "ArcGIS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
