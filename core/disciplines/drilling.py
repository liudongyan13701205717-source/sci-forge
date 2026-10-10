"""钻井学科论文支持：钻井工程、井下作业与油气开采研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="drilling",
    aliases=(
        "drilling", "钻井", "钻井工程",
        "oil drilling", "石油钻井",
        "gas drilling", "天然气钻井",
        "drilling technology", "钻井技术",
        "well drilling", "井下作业",
        "formation drilling", "地层钻井",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（钻井问题与背景）",
            "methodology（工程设计、实验条件、数据分析）",
            "results（钻井效果与工程评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（工艺分析）",
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
    citation_style="SPE",
    reporting_standards={
        "well_data": "井深、井径、钻压须完整记录",
        "mud_properties": "钻井液参数须注明（密度、黏度、API 滤失）",
        "formation": "地层数据须注明岩性与物性",
    },
    conventions=(
        "深度用 m 表示",
        "压力用 MPa 表示",
        "流量用 L/min 或 m³/h 表示",
        "密度用 g/cm³ 表示",
        "钻压用 kN 表示",
    ),
    key_venues=(
        "SPE Drilling and Completion",
        "SPE Production & Operations",
        "Journal of Petroleum Science and Engineering",
        "Drilling and Well Completion",
        "International Journal of Drilling and Water Well Technology",
        "Journal of Petroleum Exploration and Production Technology",
    ),
    units_and_formulas_notes=(
        "深度用 m 表示",
        "压力用 MPa 表示",
        "流量用 L/min 或 m³/h 表示",
        "密度用 g/cm³ 表示",
        "钻压用 kN 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "SPE Drilling Software", "Drilling Performance Software", "Well Planning Software", "Mud Logging Software", "Formation Evaluation Software", "Reservoir Simulation Software", "Drilling Automation Software", "Telemetry System", "Mud Density Meter", "Viscometer", "API Filtrate Test", "pH Meter", "Gas Detector", "Flow Meter", "Pressure Transmitter", "Drilling Rig", "Drill Bit", "Casing Equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "OnePetro"),
)
