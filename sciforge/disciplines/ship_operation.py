"""船舶操作学科论文支持：船舶操纵/航行安全/桥楼模拟/海员培训体裁、IEEE 引用样式与航海学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ship_operation",
    aliases=("ship_operation", "船舶操作", "船舶操纵", "船舶航行",
             "ship maneuvering", "marine operations", "bridge operations", "海员操作"),
    paper_types={
        "research": (
            "abstract",
            "introduction（船舶操纵与安全问题）",
            "methods（仿真、实验与情境设计）",
            "results（操纵性能、决策与安全性结果）",
            "discussion（航安意义与培训启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（事故/情境案例）",
            "analysis（原因、人为因素与流程）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（船舶操学理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者编号；海事工程主流）",
    reporting_standards={
        "simulation": "桥楼仿真遵循 IMO STCW 与 MSC.302(87) 模拟器标准",
        "safety": "海安研究遵循 ISO 24617（STCW）与 IEC 61162（NMEA 2000）",
        "maneuvering": "操纵性试验遵循 IMO IMO Res.750(18)（三对一与 Z 形试验）",
    },
    conventions=(
        "船舶类型按 IMO 分类（散货、集装箱、油轮等）与总吨位报告",
        "操纵参数按前进距（advancement）、横移距（transfer）与旋回率报告",
        "海况按 DWT（Dover 北海海况表）与 Beaufort 风级分组报告",
        "航速用节（knots）；距离用海里（NM）；高度与吃水用 m",
        "人为因素研究须报告情境意识（SA）与决策时间（秒）",
    ),
    key_venues=(
        "Ocean Engineering",
        "Journal of Navigation",
        "Marine Policy",
        "Journal of Marine Science and Engineering",
        "Journal of Ship Production and Design",
    ),
    units_and_formulas_notes=(
        "航速用节（1 kn = 1.852 km/h）；距离用海里（1 NM = 1.852 km）",
        "操纵性试验用 Z 形试验参数（转首时间、横移距、旋回圆直径）",
        "海况用 DWT 1-6 级；风级用 Beaufort 0-12",
        "报告样本量 n ≥ 30；置信区间 95%；仿真随机种子与重复次数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ECDIS", "NavStation", "AIS Receiver", "Marine Radar", "SIMHORN Bridge Simulator", "Garmin Marine GPS", "GMDSS Terminal", "SART", "DSC", "NavPilot", "C-Globe WorldMap", "Navio Ship Monitoring", "VDR", "EPIRB", "Lifeboat Drill Trainer", "Fire Drill Trainer", "Emergency Response Simulator", "Trimble Bridge Simulator", "Kongsberg SimHorn", "Navionics"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
