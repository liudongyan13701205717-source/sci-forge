"""乘务培训学科论文支持：客舱安全、乘务训练、航空人因与仿真训练体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cabin_crew_training",
    aliases=(
        "cabin_crew_training",
        "乘务培训",
        "客舱乘务",
        "空乘培训",
        "客舱安全",
        "客舱服务",
        "Cabin Crew Training",
        "Airline Cabin Crew",
        "Cabin Safety",
        "Aircraft Cabin Training",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review",
            "methodology（培训设计/仿真评估/人因分析）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "training_evaluation": (
            "abstract",
            "introduction",
            "training program description（项目介绍）",
            "evaluation design（Kirkpatrick 四层评估）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "safety_study": (
            "abstract",
            "introduction",
            "human factors framework（人因框架）",
            "methodology",
            "findings",
            "recommendations（改进建议）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 或 IEEE；航空安全期刊遵循 Aviation, Space, and Environment Medicine 体例",
    reporting_standards={
        "simulator": "模拟器训练须说明设备型号、认证等级与训练场景",
        "evaluation": "培训评估须遵循 Kirkpatrick 四层模型（反应/学习/行为/结果）",
        "safety": "安全研究须报告事故数据源（如 Aviation Safety Network）、样本期",
        "human_factors": "人因研究须报告任务、被试数与任务绩效指标",
    },
    conventions=(
        "机型须使用 ICAO 三字母代码（如 A320、B737）与注册号规范",
        "训练项目须标注法规依据（EASA Part-141、FAA ASEL、CCAR-121）",
        "模拟器须标注仿真等级（FSTD Level D、CSTD Level C 等）",
        "评估须给出评分量规与合格标准",
    ),
    key_venues=(
        "Journal of Air Transport Management",
        "Safety Science",
        "Aviation, Space, and Environment Medicine",
        "International Journal of Aviation & Aeronautical Sciences",
        "Journal of Aerospace Human Performance",
        "Airline Transport World",
        "Transportation Research Part F",
        "交通运输工程学报",
        "中国民航管理干部学院学报",
        "航空学报",
    ),
    units_and_formulas_notes=(
        "训练时长以小时（h）或分钟（min）报告",
        "温度以 °C 报告，湿度以 %RH 报告",
        "飞行参数以航空标准单位报告（ft、kts、°C）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("A320 全飞行模拟机（Full Flight Simulator）", "Boeing 737NG 全飞行模拟机", "C919 飞行模拟机", "ARJ21 飞行模拟机", "Cabin Crew Training Device（CSTD）", "GEnx 训练机", "Cockpit Voice Recorder (CVR) 训练设备", "Microsoft Flight Simulator", "X-Plane 12", "Aerosoft 航空插件", "FSUIPC", "应急撤离模拟器", "EASA Part-141 训练体系", "FAA ASEL 训练体系", "ATO 认证训练系统", "EASA CS-25 训练模块", "JAR-FCL 训练教材", "CRM 课程平台", "Cabin Safety Training 系统", "航空安全培训 e-learning 平台", "Kirkpatrick 培训评估模板", "Microsoft Excel", "SPSS", "LaTeX", "EndNote"),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "IEEE Xplore"),
)
