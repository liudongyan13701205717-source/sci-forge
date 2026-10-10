"""航空运行学科论文支持：航线规划、机组管理与流量管理体裁及运行标准记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aircraft_operation",
    aliases=(
        "aircraft operation",
        "航空运行",
        "flight operations",
        "aviation operations",
        "aircraft operations management",
        "飞行运行",
        "航空运行管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（运行问题、任务背景与目标）",
            "methods（运行建模、仿真与数据分析方法）",
            "results（航班执行率、延误、机组利用率、经济性）",
            "discussion（与运行策略对比与改进建议）",
            "conclusion",
            "references",
        ),
        "operations_report": (
            "运行背景",
            "运行建模与仿真",
            "运行评估",
            "改进建议",
            "结论",
            "参考文献",
        ),
    },
    citation_style="IEEE 或 Elsevier 样式（技术附件按 ICAO Annex 16 或 FAA Part 121 编号引用）",
    reporting_standards={
        "operational_validation": "运行建模须披露模型假设、机组规则（Duty Rest）与仿真时长",
        "data_source": "运行数据源（如 FAA FOCAST、SkyEye、ADS-B）与时间窗口须明确",
        "crew_management": "机组管理须遵循 ICAO Annex 1 或 FAA Part 117 规则",
        "economic_evaluation": "经济性评估须注明单位成本（USD/NM 或 CNY/km）与假设",
    },
    conventions=(
        "运行建模须披露模型假设、机组规则（Duty Rest）与仿真时长，并按 ICAO Annex 16 或 FAA Part 117 报告",
        "延误分类须遵循 IATA ATNM 标准（如 ATNM Category A/B/C）",
        "经济性指标须注明单位（USD/NM 或 CNY/km）与假设（如燃油、维修、机组成本）",
        "时间单位以 UTC 为准，运行时间用 Zulu 时间（HH:MM UTC）",
        "涉及空域容量/流量管理须披露空域划分、时段与流量上限",
    ),
    key_venues=(
        "Journal of Air Traffic Control",
        "Transportation Research Part C",
        "European Journal of Operational Research",
        "Journal of Operations Research Society",
        "Journal of Air Transport Management",
        "Transportation Research Part E",
        "航空学报",
        "中国民航",
    ),
    units_and_formulas_notes=(
        "距离用海里（NM）或公里（km），时间用 UTC/Zulu",
        "速度用节（kt）或 km/h，高度用英尺（ft）或飞行高度层（FL）",
        "延误时间用分钟（min）或小时（h），按 ATNM Category A/B/C 报告",
        "经济性用 USD/NM 或 CNY/km，注明假设年份与汇率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Jeppesen Flight Planning", "ForeFlight", "Lido", "ADS-B Exchange", "FlightRadar24", "WindNinja", "FAA FOCAST", "X-Plane", "Microsoft Flight Simulator", "Python", "MATLAB", "R", "C++", "TopFlite", "Jeppesen Charts", "Jeppesen ChartPro", "Garmin G1000", "Garmin AirMap", "Garmin FlyMap", "Garmin ForeFlight Mobile"),
    category="工学",
    databases=("ICAO Annex 16", "FAA", "OpenAlex", "Crossref"),
)
