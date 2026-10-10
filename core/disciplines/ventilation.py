"""通风（建筑）学科论文支持：室内空气品质、气流组织与 HVAC 能耗优化的体裁、ASHRAE 样式与暖通记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ventilation",
    aliases=(
        "ventilation",
        "通风",
        "建筑通风",
        "室内空气品质",
        "HVAC",
        "indoor air quality",
        "空气调节",
        "气流组织"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与需求背景）",
            "methods（建模、模拟或实测方法）",
            "results（IAQ、舒适度与能耗结果）",
            "discussion（机理、权衡与适用性）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（建筑类型、系统与运行工况）",
            "methods（测试点布置与参数方案）",
            "results（实测/模拟对比结果）",
            "discussion（改造建议与能效讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（通风策略与技术路线综述）",
            "evidence synthesis（标准与实证证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASHRAE 样式（作者-年份，配 ISO/ASHRAE 标准引用）",
    reporting_standards={
        "设计参数": "须给出室外气象参数来源（ASHRAE Climate Files/中国气象站）、室内设计条件与新风量计算口径",
        "CFD 模拟": "报告网格数、湍流模型、边界条件与网格无关性验证，结果与实测或关联式对比",
        "实测方案": "测点布置、仪器精度、采样时间与样本量须说明，风速与浓度报告平均值与波动范围",
        "能耗核算": "按同一边界与同一时间窗比较，报告分项能耗与运行参数，避免口径混用"
    },
    conventions=(
        "全文采用 SI 单位：风速 m/s、风量 m³/h 或 m³/s（须注明）、压力 Pa、温湿度 ℃ 与 RH%",
        "污染与浓度单位统一：CO₂ ppm、PM2.5 μg/m³、VOC mg/m³，须注明标准状态条件",
        "换气次数以次/h（ACH）标注，注明计算体积口径（净体积/含设备体积）",
        "图表标注测点位置与时间序列，时间轴注明是否跨季节或多工况",
        "标准引用写明标准号、年份与版本（如 GB 50736、ASHRAE 62.1-2019）"
    ),
    key_venues=(
        "Building and Environment",
        "Energy and Buildings",
        "HVAC&R Research",
        "ASHRAE Journal",
        "暖通空调"
    ),
    units_and_formulas_notes=(
        "新风量按 G = Q/(ρ·C) 估算去除率口径，污染物去除按一阶反应 C_out = C_in·exp(-Gt/V) 报告",
        "换气次数 ACH = Q/V，Q 取 m³/h，V 取净房间体积 m³，结果保留一位小数",
        "热平衡与散热负荷以 W 或 kW 报告，分区负荷需说明围护结构与人员设备来源",
        "能耗按 kWh 报告并注明边界（风机/冷源/末端），能效用 SCOP/EER 并标注工况"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Swag3D", "ANSYS Fluent", "OpenFOAM", "COMSOL Multiphysics", "EnergyPlus", "DesignBuilder", "OpenStudio", "MagiCAD", "Autodesk Revit MEP", "Carrier HAP", "Trane TRACE 3D+", "Daikin VRV Selector", "FDS", "FLIR 红外热像仪", "Testo 风速仪", "室内空气质量检测仪 (CO2/VOC)", "激光颗粒物计数仪", "焓差测试仪", "Minitab", "Python"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
