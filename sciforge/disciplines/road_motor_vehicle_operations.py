"""道路机动车辆运营学科论文支持：车辆技术、维修与运营管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="road_motor_vehicle_operations",
    aliases=(
        "road_motor_vehicle_operations",
        "道路机动车辆运营",
        "车辆工程",
        "vehicle engineering",
        "auto operations",
        "汽车运营",
        "汽车技术",
        "vehicle maintenance",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（行业问题）",
            "methodology（试验/仿真方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车队/线路/车辆）",
            "analysis（运营/技术分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与技术综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或 GB/T 7714",
    reporting_standards={
        "vehicle_test": "ECE、ISO 14085 或 GB/T 12544 试验规程须注明",
        "operational_study": "样本量、时段、车辆数须完整",
        "simulation": "多体动力学/能耗模型须给出参数与验证",
    },
    conventions=(
        "车速 km/h；能耗 L/100 km 或 kWh/100 km",
        "故障率以每千公里/千小时给出",
        "试验工况采用 NEDC/WLTC/CN85",
        "车辆参数（质量、轴距、功率）须列表",
        "维修记录给出 MTBF 与备件消耗",
    ),
    key_venues=(
        "Transportation Research Part C",
        "Vehicular System Dynamics",
        "Journal of Transportation Engineering",
        "汽车工程",
        "Journal of Applied Engineering Science",
    ),
    units_and_formulas_notes=(
        "动力性能以 0-100 km/h 加速、最高车速报告",
        "制动距离 m；噪声 dB(A)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Vehicle Chassis Dynamometer", "Wind Tunnel", "CAN-Bus Analyzer", "Multibody Dynamics Adams", "MATLAB/Simulink", "GT-SUITE", "AVL Cruise", "OBD-II Scanner", "Laser Radar Speed Detector", "GPS/Telematics Platform", "Fuel Economy Analyzer", "Battery Pack Analyzer", "Hydraulic Test Bench", "Suspension Test Rig", "Brake Tester", "Noise & Vibration Analyzer", "Thermal Imager", "Vehicle Diagnostic ODX", "Fleet Management Software", "SAP Vehicle Master"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
