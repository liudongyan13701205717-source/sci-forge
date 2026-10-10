"""机动车船舶和航空器学科论文支持：车辆/船舶/航空器工程体裁、ASME 引用样式与交通工程参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="motor_vehicles_ships_and_aircraft",
    aliases=(
        "motor_vehicles_ships_and_aircraft", "机动车船舶和航空器", "机动车", "船舶工程",
        "航空工程", "车辆工程", "marine engineering", "automotive engineering", "航空器工程"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工程问题）",
            "methodology（工程方法与实验）",
            "results（试验与仿真数据）",
            "discussion（性能分析与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程应用案例）",
            "analysis（设计/结构/性能分析）",
            "results（性能测试结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工程理论）",
            "evidence synthesis（技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASME 样式（作者-年份；机械期刊遵循 ASME 规范）",
    reporting_standards={
        "experimental": "工程实验遵循 ISO/ASTM 报告规范",
        "simulation": "仿真遵循工程仿真报告规范",
        "safety": "交通安全遵循 ISO/GB 报告规范",
    },
    conventions=(
        "工程参数须完整（尺寸/材料/工况）",
        "仿真软件与网格信息须报告",
        "单位与量纲须统一（SI 制）",
        "试验条件（温度/湿度/载荷）须明确",
        "术语（车辆/船舶/航空器）须界定",
    ),
    key_venues=(
        "Vehicle System Dynamics",
        "Ocean Engineering",
        "Aerospace Science and Technology",
        "Journal of Ship Research",
        "SAE International Journal of Transportation",
    ),
    units_and_formulas_notes=(
        "力用 N；速度用 m/s 或 km/h；功率用 kW",
        "应力用 MPa；力矩用 N·m",
        "公式用 amsmath；运动方程与强度方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB/Simulink", "ANSYS", "CATIA", "SolidWorks", "NX", "三维激光扫描仪", "风洞试验装置", "台架试验系统", "车辆行驶模拟器", "船舶模型试验水池", "飞行动力学试验装置", "NVH 噪声测试系统", "车辆性能测试系统", "Abaqus (疲劳分析)", "车辆排放测试系统", "NI 数据采集系统", "CarSim", "Simulink", "MAXsurf", "CAD/CAM (UG NX)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
