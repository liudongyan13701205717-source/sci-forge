"""核、水力与热能学科论文支持：水力学/热工/能源系统体裁、IEEE 引用样式与工程热物性记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nuclear_hydraulic_and_thermal_energy",
    aliases=("nuclear_hydraulic_and_thermal_energy", "核、水力与热能",
             "Nuclear Hydraulic And Thermal Energy", "hydraulic engineering",
             "水力学", "热工", "thermal energy", "能源系统",
             "能源工程", "energy systems"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与能源问题）",
            "methodology（实验与仿真方法）",
            "results（水力学/热工数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与电厂背景）",
            "analysis（水力/热工分析）",
            "results（性能与优化）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（水力学/热工理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号，工程期刊规范）",
    reporting_standards={
        "experimental": "实验遵循 ASME/ANS 实验报告规范",
        "simulation": "仿真遵循 CFX/RELAP5 报告规范",
        "safety": "安全分析遵循 IAEA SSR-2",
        "data": "数据集遵循 Open Energy Data 共享规范",
        "uncertainty": "统计与系统不确定度须分别报告",
    },
    conventions=(
        "流量用 m³/s 或 kg/s",
        "压力用 MPa 或 Pa",
        "温度用 K 或 ℃",
        "功率用 MW",
        "公式用 amsmath；显示公式编号",
    ),
    key_venues=(
        "Nuclear Engineering and Design",
        "Annals of Nuclear Energy",
        "International Journal of Heat and Mass Transfer",
        "Energy",
        "Applied Thermal Engineering",
        "Journal of Hydraulic Engineering",
    ),
    units_and_formulas_notes=(
        "流量 m³/s；压力 MPa；温度 K",
        "功率 MW；热流密度 kW/m²",
        "公式用 amsmath；显示公式编号",
        "数值结果给出均值 ± 不确定度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("RELAP5", "CFX", "FLUENT", "STAR-CCM+", "SAM", "TRACE", "COCOS", "APEX", "THETIS", "NEK", "OpenFOAM", "MATLAB", "Python (NumPy, SciPy)", "HYSYS", "Aspen Plus", "GT FieldView", "OpenFAST", "WAsP", "BladeGen", "ANSYS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
