"""施工机械操作学科论文支持：操作员培训、遥测、安全运维与效率优化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="construction_plant_operation",
    aliases=(
        "construction plant operation",
        "plant operation",
        "plant management",
        "施工机械操作",
        "工程机械操作",
        "施工设备管理",
        "plant maintenance",
        "施工机械运维",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程场景与运营痛点）",
            "system description（设备、遥测与调度架构）",
            "methodology（数据采集与分析方法）",
            "results（效率、油耗、故障率评估）",
            "conclusions",
            "references",
        ),
        "operational_report": (
            "abstract",
            "site overview",
            "plant fleet configuration",
            "operational metrics（工时、稼动率、油耗）",
            "maintenance schedule",
            "safety record",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current methods",
            "open challenges",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号），工程应用类",
    reporting_standards={
        "data": "遥测数据须报告采样频率、传感器型号、时间同步方式",
        "efficiency": "效率指标须给出稼动率、负载率、油耗率（L/h）与工时分布",
        "safety": "涉及安全须遵循 ISO 4301、ISO 12100 或 GB/T 15706",
        "maintenance": "维修记录须注明故障代码（ISO 14224）与备件批次",
        "training": "操作员培训须报告培训时长、模拟器机时与考核结果",
    },
    conventions=(
        "设备编号遵循 ISO 3691 或 GB/T 9999 起重机械分类",
        "故障代码遵循 ISO 14224 或 IEC 62541 (OPC UA)",
        "安全标准按 GB/T 15706 / ISO 12100 定级",
        "遥测数据时间戳统一 UTC 或本地 ISO 8601",
        "操作记录须标注操作员 ID、机时与工况",
    ),
    key_venues=(
        "Automation in Construction",
        "Journal of Construction Engineering and Management",
        "International Journal of Project Management",
        "Construction Innovation",
        "Engineering Management Journal",
        "施工机械",
        "建筑机械",
        "工程机械",
        "建筑经济",
    ),
    units_and_formulas_notes=(
        "工时 h；稼动率 %；负载率 %",
        "油耗 L/h 或 L/100km；功率 kW",
        "扭矩 N·m；质量 t；里程 km",
        "振动 mm/s；噪声 dB(A)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Caterpillar CAT SIM Training & Assessment", "Caterpillar CAT Link", "Caterpillar CAT Product Link", "Doosan DX Training Simulator", "Komatsu Smart Construction", "Komatsu GPS", "Komatsu Simulator", "Liebherr LIEBHERR SIM", "Volvo CE Operator Simulator", "Hitachi HI-VISION", "Kobelco SK Simulator", "Zoomlion Cloud", "XCMG XCMG Cloud", "SANY SAT", "Trimble Command", "Trimble Trimble GPS", "Trimble Earthworks", "Trimble TSC", "Trimble Business Center", "Trimble Access", "Trimble GeoVision", "Trimble Field Level", "Trimble RealWorks", "Hexagon SmartWorx", "Trimble Trimble TBC", "Oracle Primavera P6", "Microsoft Project", "Autodesk Construction Cloud", "Procore", "PlanGrid", "Bentley AECOsim", "Siemens Tecnomatix Plant Simulation", "AnyLogic", "FlexSim", "Plexos"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "ScienceDirect", "IEEE Xplore", "CNKI"),
)
