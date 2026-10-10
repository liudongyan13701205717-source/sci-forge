"""空间科学学科论文支持：航天器设计/空间环境与轨道力学体裁、AIAA 样式与轨道元素注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="space_sciences",
    aliases=("space_sciences", "空间科学", "Space Sciences", "航天器工程", "轨道动力学", "空间环境", "aerospace science", "空间物理", "航天飞行"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="AIAA 样式（编号引用，如 [1]）",
    reporting_standards={
        "mission_design": "任务需求、载荷质量预算、指向/通信/热控指标须完整给出",
        "orbit_analysis": "轨道元素六要素、历元、摄动模型与传播器须报告",
        "thermal_vacuum": "热真空试验须报告热流、真空度、样品编号与不确定度",
    },
    conventions=(
        "轨道元素按 J2000 历元 + ECI 坐标系报告（a、e、i、Ω、ω、M）",
        "推力单位统一 N 或 lbf，比冲 Isp 单位 s，均注明换算",
        "时间标 UTC / TT / TDB 明确区分，星历时间基准随文件标注",
        "载荷质量用 dry/wet/total 三态标注，单位 kg 或 lbm 统一",
        "误差用 ± 上下标，显著性用 σ 或 3σ 阈值",
    ),
    key_venues=(
        "Journal of Spacecraft and Rockets",
        "Acta Astronautica",
        "Advances in the Astronautical Sciences",
        "Journal of Geophysical Research: Space Physics",
        "Planetary and Space Science",
    ),
    units_and_formulas_notes=(
        "比冲 Isp = v_e / g₀（g₀ = 9.80665 m/s²），单位 s",
        "Δv = Isp·g₀·ln(m₀/mf)（齐奥尔科夫斯基公式）",
        "引力常数 μ = GM（地球 μ = 3.986004418 × 10¹⁴ m³/s²，NASA SP-8027）",
        "温度标 K；真空度 Pa 或 torr，均注明换算因子",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GMAT (NASA)", "STK (AGI)", "OrbitKit", "AstroPy", "SPICE Toolkit (NASA)", "Radioss (MSC)", "ANSYS Mechanical", "Matlab (MathWorks)", "Simulink", "MATLAB Aerospace Toolbox", "NASA CEA 推进分析", "GT-Prop", "KORD (AIAA)", "OpenVSP 参数化设计", "Cesium 地球可视化", "AFT 气动热工具", "PySPICE 电路仿真", "OpenMDAO 多学科优化", "Zemax OpticStudio", "ANSYS Fluent"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
