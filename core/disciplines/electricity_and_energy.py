"""电力与能源学科论文支持：能源系统、电力市场与可持续能源研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electricity_and_energy",
    aliases=(
        "electricity_and_energy", "电力与能源", "能源系统",
        "electricity and energy", "电力与能源",
        "energy systems", "能源系统",
        "power market", "电力市场",
        "sustainable energy", "可持续能源",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（能源问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（能源效果与性能评估）",
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
        "design": "设计参数须完整（容量、电压、效率等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "功率用 kW 或 MW 表示",
        "电压用 V 或 kV 表示",
        "频率用 Hz 表示",
        "效率用 % 表示",
        "燃料消耗用 kg/h 表示",
    ),
    key_venues=(
        "IEEE Transactions on Power Systems",
        "IEEE Transactions on Energy Conversion",
        "Electric Power Systems Research",
        "International Journal of Electrical Power & Energy Systems",
        "Renewable Energy",
        "Energy",
    ),
    units_and_formulas_notes=(
        "功率用 kW 或 MW、电压用 V 或 kV 表示",
        "频率用 Hz 表示",
        "效率用 % 表示",
        "燃料消耗用 kg/h 表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "PSCAD", "ETAP", "DIgSILENT", "PSSE", "EMTP", "PSpice", "LTspice", "Multisim", "Proteus", "Altium Designer", "Eagle", "KiCad", "AutoCAD Electrical", "EPLAN", "LabVIEW", "Python (numpy, scipy)", "PyPSA", "PySAM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
