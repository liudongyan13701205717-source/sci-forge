"""航海技术学科论文支持：导航定位/航海装备/海上通信体裁、IEEE/IMU 样式与航海技术记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="navigation_technologies",
    aliases=("navigation_technologies", "航海技术", "marine navigation", "航海工程",
             "导航技术", "海上定位", "GPS/GNSS", "船舶导航", "maritime navigation"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与航海技术问题）", "methodology（试验与测量方法）", "results（定位精度与导航数据）", "discussion（工程意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（航线/事故/装备案例背景）", "analysis（导航与通信过程分析）", "results（改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技术与标准综述）", "evidence synthesis（设备与场景证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式或 IHO 规范",
    reporting_standards={
        "positioning": "定位精度须按 IMO/IHO 精度分层（PPP/RTK/静态）报告",
        "safety": "海上航行安全报告遵循 STCW 与 IMO 声明",
        "simulation": "导航仿真遵循仿真试验报告规范并给出误差分布",
    },
    conventions=(
        "坐标系统（WGS84/CGCS2000/GDA94 等）与版本须明确",
        "时间与频率给出 UTC/TT 或 GPS 时间并说明闰秒",
        "误差用 HDOP/VDOP/TDOP 或水平/垂直精度圆给出",
        "装备与型号首次给出全称与厂商版本",
        "航海术语遵循 IHO/S 55 系列标准并首次给全称",
    ),
    key_venues=(
        "Journal of Navigation",
        "Maritime Safety and Environmental Law Review",
        "Naval Research Laboratory Journal",
        "International Journal of Navigation and Observation",
        "Applied Geomatics",
    ),
    units_and_formulas_notes=(
        "位置用经纬度（度/分/秒或十进制度）、误差用 m",
        "速度用节或 m/s、时间用 s、频率用 Hz",
        "公式用 amsmath；卡尔曼滤波/状态方程须完整给出",
        "显著性给出 p 值与置信区间并说明分布假设",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GNSS Receiver", "GPS Receiver", "Beidou", "Galileo", "ECDIS", "ARPA Radar", "AIS", "VDR", "GMDSS", "DCP (Doppler Log)", "USBL", "Depth Sounder", "Gyroscope Compass", "Magnetic Compass", "Navtex", "EPIRB", "X-42", "Inertial Navigation System", "Weather Router", "Marine Radar"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
