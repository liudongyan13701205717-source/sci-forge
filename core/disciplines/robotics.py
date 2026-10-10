"""机器人学学科论文支持：系统设计与实机实验。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="robotics",
    aliases=(
        "robotics",
        "机器人学",
        "robot",
        "机械臂",
        "自主系统",
        "SLAM",
        "manipulation",
        "swarm robotics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与相关工作）",
            "methods（系统设计与算法）",
            "experiments（仿真与实机）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "system": (
            "abstract",
            "introduction",
            "hardware architecture（硬件架构）",
            "software stack（软件栈）",
            "integration（集成）",
            "field tests（现场测试）",
            "failure analysis",
            "references",
        ),
        "benchmark": (
            "abstract",
            "introduction",
            "benchmark design（基准设计）",
            "metrics（指标）",
            "baseline comparison",
            "results（结果）",
            "discussion",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "experiments": "实机试验次数与环境描述；失败案例须报告",
        "baseline": "与 SOTA 方法在同一数据集/环境对比；代码链接须给出",
        "metrics": "成功率/精度/延迟定义与测量方法须可复现",
        "safety": "安全边界与失效模式（FMEA）须讨论",
    },
    conventions=(
        "坐标系约定（ENU/FLU）与 TF 树说明；时间戳同步方式写明",
        "视频/补充材料链接；ROS 版本与开源仓库链接",
        "仿真实参数给物理引擎与步长；sim-to-real 差距讨论",
        "延迟给 p50/p95/p99 而非只给均值",
        "算力资源（GPU/CPU 型号与频率）须列出",
    ),
    key_venues=(
        "IEEE Transactions on Robotics",
        "International Journal of Robotics Research",
        "IEEE International Conference on Robotics and Automation (ICRA)",
        "Robotics: Science and Systems (RSS)",
        "Conference on Robot Learning (CoRL)",
    ),
    units_and_formulas_notes=(
        "定位误差给 RMSE（m）；姿态给四元数或欧拉角约定",
        "控制频率 Hz；算力给 FLOPS 或型号对照",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ROS 2", "Gazebo", "MuJoCo", "MATLAB Robotics System Toolbox", "SolidWorks", "FreeCAD", "NVIDIA Isaac Sim", "PyTorch", "TensorFlow", "CMake", "MoveIt 2", "Navigation 2", "MoveIt Planner", "PX4 SITL", "JAZZ SLAM", "SLAM Toolbox", "GStreamer", "ROSbag", "ROS RViz2", "Kuka KRL"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
