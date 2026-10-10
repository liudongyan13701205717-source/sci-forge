"""车辆与动力工程学科论文支持：动力总成与整车 NVH、台架-仿真耦合试验的体裁、IEEE 引用样式与工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_and_motor_engineering",
    aliases=(
        "vehicle_and_motor_engineering",
        "车辆与动力工程",
        "汽车与动力工程",
        "动力总成工程",
        "vehicle engineering",
        "powertrain engineering",
        "vehicle dynamics"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与待解问题）",
            "methods（建模/试验设计）",
            "results（结果）",
            "discussion（讨论与验证）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（对象与工况背景）",
            "methods（分析与试验方案）",
            "results（量化指标）",
            "discussion（改进与推广）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（技术路线综述）",
            "evidence synthesis（证据与数据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号 [1]，IEEEtran 模板与 BibTeX 缩写）",
    reporting_standards={
        "试验工况": "台架与整车试验须声明循环工况（WLTC/C-WLTC/NEDC）与测功机标定条件，功率、油耗与排放结果附测量不确定度",
        "效率与油耗口径": "热效率、油耗率与综合油耗须注明燃料低位热值基准，按 GB/T 或 ISO 15148 定义换算，禁止不同基准混算",
        "仿真验证": "数值模型须在物理台架数据上标定并报告相对误差与适用参数域，不得仅凭仿真结论下工程判断",
        "NVH 评价": "NVH 结果须说明声压测点、带宽与 A 计权；振动按加速度 PSD 与 1/3 倍频程报告"
    },
    conventions=(
        "全文采用 SI 单位与 GB 国标记法：压力 MPa、力 kN、扭矩 N·m、频率 Hz、声压级 dB(A)",
        "工况、油耗与排放结果必须标注循环类型与基准，禁止跨基准直接对比",
        "图表按 IEEEtran 期刊风格绘制，横纵轴标注物理量与量纲，图注可独立阅读",
        "仿真模型须列出关键参数、边界条件与网格/时间步长假设，关键假设显式声明",
        "术语中英对照在首次出现处标注，同一概念全文使用同一译名"
    ),
    key_venues=(
        "Vehicle System Dynamics",
        "International Journal of Automotive Technology",
        "SAE International Journal of Transportation",
        "Journal of Powertrain System Research",
        "车辆工程"
    ),
    units_and_formulas_notes=(
        "功率按 P = T·ω 换算（T 取 N·m，ω 取 rad/s），报告中转速统一标注 r/min",
        "热效率 η = W/(m_f·LHV_f)，LHV_f 为燃料低位热值；汽油与柴油对比须统一基准",
        "油耗率 bsfc 单位 g/(kW·h)，等速油耗 L/100 km，工况油耗按循环里程折算",
        "噪声与振动按 ISO 5127、GB/T 37400 报告；声压级取 A 计权，振动取加速度 PSD"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB/Simulink", "Simcenter Amesim", "MSC Adams", "GT-SUITE", "AVL CRUISE", "AVL BOOST", "Siemens NX", "CATIA V5", "Teamcenter", "ANSYS Motion", "Rational Rose", "KISSsys", "Simscape Mechanical", "GT-Aero", "发动机试验台架", "四辊整车测功机", "瞬态排气分析仪", "LMS Test.Lab 振动分析系统", "AVL ACQUIS 发动机分析仪", "红外热像仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
