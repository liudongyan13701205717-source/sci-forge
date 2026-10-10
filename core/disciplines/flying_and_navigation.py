"""飞行与导航学科论文支持：航空飞行、导航系统与飞行控制研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="flying_and_navigation",
    aliases=("flying_and_navigation", "飞行与导航", "飞行科学", "航空导航", "无人机飞行", "惯性导航", "飞行控制", "航空"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago Author-Date",
    reporting_standards={"k1": "SAE 飞行报告规范", "k2": "FAA 无人机试验报告标准", "k3": "EASA 适航评估准则"},
    conventions=("飞行参数须注明坐标系（NED/ECEF/机体）", "航迹数据须注明 WGS-84 参考椭球", "惯性导航误差须给出 3σ 统计", "飞行控制试验须注明风速与高度", "GPS 定位须注明 PDOP 与卫星数"),
    key_venues=("AIAA Journal", "Journal of Guidance, Control, and Dynamics", "Navigation", "IEEE Transactions on Aerospace and Electronic Systems", "Flight"),
    units_and_formulas_notes=("速度单位：m/s 或 knots", "高度单位：m（MSL）或 ft", "航向：°T（真北）或 °M（磁北）", "加速度：g（1g = 9.81 m/s²）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB / Simulink", "Cesium（航迹可视化）", "QGroundControl（无人机地面站）", "ArduPilot 飞控源码", "PX4 飞控源码", "惯性测量单元 (IMU)", "u-blox GNSS 接收机", "飞行模拟器", "低速风洞", "光电跟踪系统", "LaTeX（排版）", "Python（数据处理）", "R（统计检验）", "Origin（数据绘图）", "Satellite Task Planner (STK)", "OpenVSC", "Dolphin MCMC", "RStudio", "Copter 地面站", "QGC（地面控制站）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
