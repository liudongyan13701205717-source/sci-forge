"""能源效率学科论文支持：节能技术、能源管理与可持续能源研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="energy_efficiency",
    aliases=(
        "energy_efficiency", "能源效率", "节能技术",
        "energy efficiency", "能源效率",
        "energy management", "能源管理",
        "sustainable energy", "可持续能源",
        "energy conservation", "节能",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（能源问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（节能效果与性能评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "implementation（实现过程）",
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
    citation_style="IEEE",
    reporting_standards={
        "design": "设计参数须完整（功率、效率、能耗等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "功率用 kW 或 MW 表示",
        "能耗用 kWh 表示",
        "效率用 % 表示",
        "节能率用 % 表示",
        "投资回收期用 年 表示",
    ),
    key_venues=(
        "Energy Efficiency",
        "Applied Energy",
        "Energy and Buildings",
        "Renewable Energy",
        "Energy",
        "Journal of Cleaner Production",
    ),
    units_and_formulas_notes=(
        "功率用 kW 或 MW 表示",
        "能耗用 kWh 表示",
        "效率用 % 表示",
        "节能率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "EnergyPlus", "eQUEST", "DOE-2", "TRNSYS", "HOMER", "RETScreen", "LEAP", "MARKAL", "TIMES", "Energy Audit Software", "Building Energy Modeling Software", "HVAC Design Software", "Lighting Design Software", "Power System Analysis Software", "Life Cycle Assessment Software", "Carbon Footprint Calculator", "COP/SPF Calculator", "Exergy Analysis Tool"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
