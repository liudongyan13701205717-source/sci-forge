"""机器人学论文支持：系统设计、实机实验、基准评测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="robotics",
    aliases=("robotics", "robot", "slam", "manipulation", "机器人", "机械臂", "自主系统"),
    paper_types={
        "research": ("abstract", "introduction", "related work", "system design",
                     "methods", "experiments（仿真+实机）", "results", "conclusion", "references"),
        "system": ("abstract", "introduction", "hardware architecture", "software stack",
                   "integration", "field tests", "failure analysis", "references"),
        "benchmark": ("abstract", "introduction", "benchmark design", "metrics", "baseline comparison",
                      "results", "discussion", "references"),
    },
    citation_style="IEEE 编号",
    reporting_standards={
        "hardware": "传感器型号、分辨率、标定方法与计算平台（CPU/GPU 型号）须列全",
        "experiments": "实机试验次数与环境描述；失败案例必须报告（不只报成功）",
        "metrics": "成功率/精度/延迟定义与测量方法须可复现",
        "baseline": "与 SOTA 方法在同一数据集/环境对比；代码与模型链接",
        "safety": "安全边界与失效模式（FMEA）须讨论",
    },
    conventions=(
        "坐标系约定（ENU/FLU）与 TF 树说明；时间戳同步方式写明",
        "视频/补充材料链接；ROS 版本与开源仓库链接",
        "仿真实参数给物理引擎与步长；sim-to-real 差距讨论",
        "延迟给 p50/p95/p99 而非只给均值",
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
    contribution_forms=("论文", "软件与代码", "专利"),
    tools=("ROS", "MATLAB", "SolidWorks", "Gazebo"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
