"""电子工程学科论文支持：电子系统、嵌入式系统与集成电路研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronics_engineering",
    aliases=(
        "electronics_engineering", "电子工程", "电子系统工程",
        "electronics engineering", "电子工程",
        "embedded systems", "嵌入式系统",
        "integrated circuits", "集成电路",
        "VLSI design", "VLSI 设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（工程效果与性能评估）",
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
        "design": "设计参数须完整（电压、电流、功率等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "电压用 V 表示",
        "电流用 A 表示",
        "功率用 W 或 kW 表示",
        "频率用 Hz 表示",
        "效率用 % 表示",
    ),
    key_venues=(
        "IEEE Transactions on Circuits and Systems",
        "IEEE Transactions on Very Large Scale Integration (VLSI) Systems",
        "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems",
        "IEEE Journal of Solid-State Circuits",
        "IEEE Transactions on Consumer Electronics",
        "IEEE Transactions on Industrial Electronics",
    ),
    units_and_formulas_notes=(
        "电压用 V 表示",
        "电流用 A 表示",
        "功率用 W 或 kW 表示",
        "频率用 Hz 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "PSCAD", "ETAP", "DIgSILENT", "PSSE", "EMTP", "PSpice", "LTspice", "Multisim", "Proteus", "Altium Designer", "Eagle", "KiCad", "AutoCAD Electrical", "EPLAN", "LabVIEW", "Python (numpy, scipy)", "VHDL/Verilog", "ModelSim"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
