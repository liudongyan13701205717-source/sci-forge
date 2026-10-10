"""航空运行安全学科论文支持：事故调查、安全报告与 FRISK/CASSI 事件编码记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="air_traffic_safety",
    aliases=(
        "air traffic safety",
        "航空安全",
        "aviation safety",
        "ATM safety",
        "air transport safety",
        "flight safety",
        "飞行安全",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（事故背景、事件分类与研究目标）",
            "methods（数据源、事件编码与统计方法）",
            "results（事件特征、因果链与趋势）",
            "discussion（安全文化与改进措施）",
            "conclusion",
            "references",
        ),
        "incident_report": (
            "summary（事件与场景概述）",
            "factual information（时间线、环境、设备、机组信息）",
            "analysis（直接原因、间接原因、促成因素）",
            "findings and recommendations",
            "references",
        ),
    },
    citation_style="APA 或 ICAO 官方报告样式（技术附件按 ICAO Annex 编号引用）",
    reporting_standards={
        "incident_reporting": "按 ICAO Annex 13 或 ICAO Annex 19 报告框架披露事件分类、时间线与因果链",
        "data_source": "数据源（NASA ASRS/ATSB/NTSB/EASA/SkyEye）与时间窗口须明确",
        "frisk_encoding": "不安全事件编码遵循 FRISK 或 CASSI 分类",
        "safety_culture": "安全文化/组织行为相关结论须给出样本量、信度与局限",
    },
    conventions=(
        "事故与不安全事件须按 ICAO Annex 13/19 报告框架完整披露时间线、事件分类与因果链",
        "不安全事件编码遵循 FRISK 或 CASSI 标准分类，事件类型须标注具体编码",
        "定量指标须注明来源（ASRS/ATSB/NTSB/EASA/SkyEye）、时间窗口与样本量",
        "涉及人机工程或安全文化的方法说明须包含样本量、采样方法与信度",
        "结论须区分直接原因、间接原因与促成因素（contributing factors）",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Journal of Safety Research",
        "Reliability Engineering & System Safety",
        "Safety Science",
        "Human Factors: The Journal of Human Factors and Ergonomics Society",
        "Journal of Air Traffic Control",
        "Transportation Research Part C",
        "Aviation, Space, and Environmental Medicine",
    ),
    units_and_formulas_notes=(
        "时间单位以 UTC 为准，事件时间线用 HH:MM:SS UTC 格式",
        "距离使用海里（NM）、高度使用英尺（ft）、速度使用节（kt）",
        "事件编码遵循 FRISK 或 CASSI 分类（如 07700, 07600）",
        "涉及安全文化/组织行为学的定量分析须披露信度（Cronbach's α）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Eurocontrol SAFEnet", "NASA ASRS", "ATSB", "NTSB", "EASA Safety Reporting System", "OASIS", "OASIS-Web", "CASSI", "CATS", "FRISK", "CMCAT", "ATSS", "SkyEye", "ADS-B", "FDR", "CVR", "EASA EDDPS", "IATA ISBA", "FAA FOCAST", "ACES", "EASA EDD", "Eurocontrol TM&NP", "EASA ADS", "Eurocontrol Network Manager"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ICAO Annex 13", "ICAO Annex 19", "ATSB", "NASA ASRS"),
)
