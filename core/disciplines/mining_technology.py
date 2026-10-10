"""采矿技术学科论文支持：采矿技术/装备/自动化体裁、SME 引用样式与矿山技术注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mining_technology",
    aliases=(
        "mining_technology", "采矿技术", "采矿", "mining technology", "矿山技术",
        "矿山机械", "矿山自动化", "智能采矿", "采矿装备"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与技术问题）",
            "methodology（技术方法与实验）",
            "results（技术与装备数据）",
            "discussion（机理与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿山技术案例）",
            "analysis（技术装备与设计）",
            "results（技术性能与效益）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（采矿技术理论）",
            "evidence synthesis（技术装备综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="SME 样式（作者-年份；SME 期刊遵循 SME 规范）",
    reporting_standards={
        "experimental": "矿山技术实验遵循 ISRM/IEEE 建议方法",
        "automation": "矿山自动化遵循 IEC 规范",
        "safety": "矿山安全遵循 MSHA 报告规范",
    },
    conventions=(
        "矿山技术术语须统一",
        "自动化设备参数须完整",
        "传感器数据须报告采样频率与精度",
        "算法与仿真须给出参数与边界",
        "单位与量纲须规范",
    ),
    key_venues=(
        "Mining Technology",
        "International Journal of Mining Science and Technology",
        "Automated Technology",
        "Underground Mining Systems",
        "Journal of Mining Science",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；速度用 m/s；功率用 kW",
        "算法性能用准确率/F1/收敛速度",
        "公式用 amsmath；技术公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS", "FLAC3D", "3D MineDesign", "Python", "MATLAB", "岩石力学试验系统", "采掘设备状态监测系统", "矿山压力监测系统", "矿井通风模拟软件 Ventsim", "智能矿山调度系统", "三维激光扫描仪", "地质雷达", "无人机探测系统", "地下定位系统 UWB", "采空区充填系统", "液压支架", "掘进机", "GIS (ArcGIS/QGIS)", "矿山生态监测系统", "BIM (建筑信息模型)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
