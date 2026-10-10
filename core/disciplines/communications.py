"""Communications (air, railway, road etc.) 学科论文支持：综合通信/交通通信体裁、IEEE 引用样式与通信记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications",
    aliases=("Communications (air, railway, road etc.)", "综合通信", "交通通信",
             "transport communications", "transportation communications",
             "综合通信系统", "交通通信系统", "communications infrastructure",
             "通信基础设施"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "proposed approach（方法）",
            "experiments/evaluation（实验与评估）",
            "discussion（讨论）",
            "conclusion（结论）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "background（背景）",
            "taxonomy（分类）",
            "challenges and open problems（挑战与开放问题）",
            "conclusion",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者-数字编号，如 [1]）",
    reporting_standards={
        "simulation": "仿真研究须说明模型参数、随机种子与验证方法",
        "measurement": "测量研究须报告实验环境与设备型号",
        "theoretical": "理论结果须给出严格证明或引用出处",
    },
    conventions=(
        "实验结果须报告置信区间与显著性",
        "仿真模型须说明参数设置与验证方法",
        "通信协议与架构须遵循国际标准（ITU/3GPP/IETF）",
        "图表须标注坐标轴、单位与图例",
    ),
    key_venues=(
        "IEEE Transactions on Intelligent Transportation Systems",
        "IEEE Transactions on Vehicular Technology",
        "Transportation Research Part C: Emerging Technologies",
        "Journal of Transportation Engineering",
        "IEEE Transactions on Wireless Communications",
        "IEEE Transactions on Communications",
        "IEEE Communications Magazine",
        "Computer Networks",
    ),
    units_and_formulas_notes=(
        "功率与信号强度用 dBm/dBW 表示",
        "带宽用 Hz/kHz/MHz/GHz 表示",
        "误码率用 BER 表示，给出 SNR 条件",
        "仿真参数须给出初始值、步长与收敛条件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "AnyLogic", "OpenTripPlanner", "TransCAD", "Aimsun", "VISSIM", "SUMO", "QGIS", "ArcGIS", "R", "Python", "NS-3", "Mininet", "Wireshark", "OMNeT++", "JADE", "ExaWiN", "NetSim", "OPNET"),
    category="工学",
    databases=("IEEE Xplore", "arXiv", "Scopus", "WoS", "OpenAlex"),
)
