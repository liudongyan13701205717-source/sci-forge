"""电子与自动化学科论文支持：工业自动化、控制系统与机器人技术研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronics_and_automation",
    aliases=(
        "electronics_and_automation", "电子与自动化", "工业自动化",
        "electronics and automation", "电子与自动化",
        "industrial automation", "工业自动化",
        "control systems", "控制系统",
        "robotics", "机器人技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（自动化问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（自动化效果与性能评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "implementation（实现过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "design": "设计参数须完整（电压、电流、功率等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "电压用 V 表示",
        "电流用 A 表示",
        "功率用 W 或 kW 表示",
        "频率用 Hz 表示",
        "效率用 % 表示",
    ),
    key_venues=(
        "IEEE Transactions on Industrial Electronics",
        "IEEE Transactions on Control Systems Technology",
        "IEEE Transactions on Robotics",
        "Automatica",
        "Journal of Intelligent & Robotic Systems",
        "Robotics and Computer-Integrated Manufacturing",
    ),
    units_and_formulas_notes=(
        "电压用 V 表示",
        "电流用 A 表示",
        "功率用 W 或 kW 表示",
        "频率用 Hz 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "LabVIEW", "PLC Programming Software", "SCADA Software", "HMI Software", "Robot Operating System (ROS)", "Gazebo", "V-REP", "SolidWorks", "AutoCAD", "EPLAN", "TIA Portal", "STEP 7", "RSLogix", "Codesys", "Python (numpy, scipy)", "OpenCV", "ROS 2", "MoveIt"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
