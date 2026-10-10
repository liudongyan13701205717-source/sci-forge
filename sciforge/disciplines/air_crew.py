"""航空机组（飞行与导航）学科论文支持：飞行训练、机组资源管理与导航教学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="air_crew",
    aliases=(
        "Air crew (flying and navigation)",
        "航空机组",
        "飞行与导航",
        "飞行训练",
        "机组资源管理",
        "pilot training",
        "crew resource management",
        "flight navigation",
        "aviation crew",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与培训问题）",
            "methods（训练方案/实验设计/数据来源）",
            "results（绩效与结论）",
            "discussion（训练学与航空安全讨论）",
            "conclusion（培训建议与展望）",
            "references",
        ),
    },
    citation_style="APA 7 或 IEEE 样式（航空领域常混合 ICAO/FAA 规范引用）",
    reporting_standards={
        "simulation": "模拟机训练须说明机型等级（AATD/Full Flight Simulator 级别）与运行配置",
        "training_validity": "训练有效性须以飞行品质/情境判断任务成绩等可验证指标呈现",
        "pilot_population": "受试飞行员资质等级（私照/商照/复训）须明确",
    },
    conventions=(
        "飞行高度/速度/时间统一标注单位（ft、kt、Zulu 时间）",
        "标准喊话与 SOP 术语遵循 ICAO Annex 1 与 IATA OPS 用语",
        "CRS/CRM 场景须给出情境-决策-结果三段式叙述",
        "飞行数据引用须标注来源（FDR/QAR/飞行记录表）与采集时段",
        "疲劳/差错事件报告遵循 ICAO Annex 19 与匿名化原则",
    ),
    key_venues=(
        "Journal of Aircraft",
        "Flight Safety Foundation Quarterly",
        "Aviation, Space, and Environmental Medicine",
        "Human Factors: The Journal of the Human Factors and Ergonomics Society",
        "Aviation Education and Training",
        "ATM Research Journal",
    ),
    units_and_formulas_notes=(
        "高度单位使用英尺（ft）或高度层（FL），速度用节（kt），航程用海里（NM）",
        "时间与时刻统一使用 UTC（Zulu）",
        "飞行计划数据遵循 ICAO Doc 4444 与 Doc 8085 规定格式",
        "气象信息遵循 ICAO Annex 3 METAR/TAF 规范",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("X-Plane 12", "Microsoft Flight Simulator", "Prepar3D", "JUNGLE by Just Flight", "Redbird FTU", "Caesar Simulators", "CAE ALSim Pro", "Alsim Pro", "Lockheed Martin Full Flight Simulator", "Thomson Training Systems", "Kohler Avionics Sim", "Flowmaster", "ADS-B Exchange", "ADS-B Data System", "ForeFlight", "SkyVector", "Omnigraphical", "FlightDeck", "Jeppesen Flight Guide", "Jeppesen ChartPro", "Lido", "Top Flite", "PMDG Simulator", "G1000 Simulator", "Garmin G1000 NXi", "AirRadar", "MyRadar Live", "WindNinja", "Oversight", "FAA FOCAST", "AFTN"),
    category="工学",
    databases=("OpenAlex", "Crossref", "FAA Knowledge Center", "EUROCONTROL Safety Data"),
)
