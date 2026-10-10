"""卡车驾驶学科论文支持：驾驶员培训、模拟器评估、安全与重型车操作研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="truck_driving",
    aliases=("truck_driving", "卡车驾驶", "重型车驾驶", "货运驾驶",
             "驾驶员培训", "truck driving", "heavy vehicle operation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（驾驶背景与安全研究问题）",
            "materials and methods（方法与数据采集）",
            "results（驾驶绩效与安全数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（驾驶/事故案例）",
            "analysis",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "driving_training": "驾驶培训遵循 ISO 11307",
        "safety_analysis": "安全分析遵循 Highway Safety Manual",
        "simulator": "模拟器评估遵循 ISO 17615",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "速度单位 km/h",
        "制动距离单位 m",
        "疲劳指数单位 分钟/小时",
        "载荷单位 吨",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Transportation Research Part F",
        "Journal of Safety Research",
        "Traffic Injury Prevention",
        "运输",
    ),
    units_and_formulas_notes=(
        "速度单位 km/h",
        "制动距离单位 m",
        "疲劳指数单位 分钟",
        "载荷单位 吨",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("驾驶模拟器", "TruckSim", "CarSim", "CARLA", "MATLAB/Simulink", "AutoMOD", "AnyLogic", "SPSS", "R", "Python", "Excel", "Tableau", "Power BI", "GPS 追踪仪", "行驶记录仪", "行车记录仪", "ADAS 传感器", "卡车诊断仪", "重型车培训模拟软件", "NVivo"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
