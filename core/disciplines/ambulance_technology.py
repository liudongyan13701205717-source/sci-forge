"""救护车辆技术学科论文支持：整车动力学/碰撞安全/车内环境与电气集成体裁、ISO/Euro NCAP 与车辆注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ambulance_technology",
    aliases=("ambulance technology", "救护车辆技术", "救护车设计",
             "ambulance design", "整车工程", "vehicle engineering",
             "emergency vehicle", "emergency vehicle engineering",
             "救护车辆动力学", "emergency vehicle dynamics", "NVH",
             "整车安全", "vehicle safety", "碰撞安全", "crashworthiness",
             "车内热环境", "thermal comfort", "电磁兼容", "electromagnetic compatibility",
             "急救设备集成", "EMS equipment integration"),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计目标与工程约束）",
            "design and methodology（构型、材料、结构与仿真链）",
            "simulation and validation（数值与试验交叉验证）",
            "results（多目标权衡与敏感性）",
            "discussion（量产性与成本影响）",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（台架、整车与人因试验）",
            "results",
            "discussion",
            "references",
        ),
        "crashworthiness": (
            "abstract",
            "introduction",
            "methods（工况、约束与人偶/HMM 布置）",
            "results（乘员载荷、HIC 与结构侵入）",
            "discussion（法规与减重权衡）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（平台与关键子系统）",
            "outlook",
            "references",
        ),
    },
    citation_style="Elsevier 样式（作者-年份；Accident Anal. Prev. 遵循 Elsevier 规范）",
    reporting_standards={
        "simulation": "有限元/多体动力学须报告网格独立性、材料模型与收敛指标（GCI）",
        "crash_test": "碰撞试验须报告工况（速度、角度、约束）、传感器布置与误差",
        "environment": "车内热湿与污染物（CO2、NH3、VOC）测试须给出工况与采样点",
        "human_factors": "人机工程与驾驶负荷须报告测量方法与样本",
        "uncertainty": "参数不确定度按 GUM 报告；试验重复次数须说明",
    },
    conventions=(
        "坐标系统一（车身坐标系 BCS 与地面坐标系 GCS）并在首次出现处声明",
        "载荷与工况（ISO 11086、EN 1789 等）须标明标准号与版本",
        "仿真与试验对比给出误差百分比与偏差方向",
        "NVH 与热环境数据给出采样率、频段与统计口径（峰值/RMS）",
        "缩写首次出现给出全称（如 HMM = Human Machine Model）",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Vehicle System Dynamics",
        "IEEE Transactions on Intelligent Transportation Systems",
        "Traffic Injury Prevention",
        "International Journal of Vehicle Design",
        "Journal of Advanced Transportation",
        "IEEE Transactions on Vehicular Technology",
    ),
    units_and_formulas_notes=(
        "速度用 km/h 或 m/s；加速度用 m/s^2；时间用 s",
        "力用 N、扭矩用 Nm；压力用 kPa 或 Pa",
        "温度用 °C、湿度用 %RH；声压级用 dBA",
        "仿真结果须给出求解器与版本、网格规模与计算时间",
        "试验重复次数与置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ADAMS", "Simpack", "CarSim", "GT-Suite", "AVL Cruise", "AVL EXCITE", "Simcenter Amesim", "CATIA V5", "Siemens NX", "PTC Creo", "SolidWorks", "ANSYS Mechanical", "Abaqus", "Hypermesh", "LS-DYNA", "Radioss", "OptiStruct", "MADYMO", "Crashworks", "LMS Test.Lab", "Brüel & Kjær Pulse", "MATLAB/Simulink"),
    category="工学",
    databases=("Crossref", "OpenAlex", "SAE", "CNKI"),
)
