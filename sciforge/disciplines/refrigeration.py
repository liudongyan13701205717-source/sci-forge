"""制冷学科论文支持：制冷循环、热泵与低温工程建模、COP/焓熵图注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="refrigeration",
    aliases=(
        "refrigeration",
        "制冷",
        "制冷工程",
        "低温工程",
        "Refrigeration and Cryogenics",
        "Cryogenics",
        "Heat Pump",
        "热泵"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与制冷问题）",
            "methodology（实验/建模方法）",
            "results（性能与工况数据）",
            "discussion（机理与工程意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（系统与工况）",
            "analysis（性能分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（热力学基础）",
            "evidence synthesis（技术趋势）",
            "future directions",
            "references"
        ),
    },
    citation_style="IJR/Elsevier 样式（编号制；IJ Refrigeration 遵循 Elsevier 规范）",
    reporting_standards={
        "thermodynamic_cycle": "须给出完整压焓图并注明等熵/等压过程",
        "coefficient_of_performance": "COP 定义须与测试工况匹配（EN14511/ASHRAE 标准）",
        "experimental": "实验报告须注明制冷剂、质量流量与测点标定"
    },
    conventions=(
        "SI 单位：制冷量 W/kW；压力 kPa/MPa；温度 K 或 °C",
        "COP、COP_h、SCOP 与 EER 首次出现须给出定义与量纲",
        "压焓图（p-h）坐标须标注制冷剂与参考态",
        "实验装置图须标注测点位置与仪器型号",
        "对比研究须在同一工况点比较"
    ),
    key_venues=(
        "International Journal of Refrigeration",
        "Applied Thermal Engineering",
        "Energy Conversion and Management",
        "Energy",
        "International Journal of Thermal Sciences"
    ),
    units_and_formulas_notes=(
        "制冷量 Q (kW)；功率 W (kW)；COP = Q/W 无量纲",
        "焓 h (kJ/kg)；熵 s (kJ/(kg·K))",
        "压力单位 kPa/MPa；温度 K 或 °C",
        "制冷系数、性能系数与能效比（EER）须区分"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("REFPROP", "CoolProp", "EES (Engineering Equation Solver)", "MATLAB", "Aspen Plus", "ANSYS Fluent", "OpenFOAM", "CycleTEMPO", "ThermoOpt", "HEMHAC", "IAR-3", "Thermo-Engineer", "Dewar (杜瓦瓶)", "Cryostat (低温恒温器)", "Calorimeter (量热计)", "Differential Scanning Calorimeter", "Psychrometer (干湿球温度计)", "Refrigerant Test Bench", "Heat Exchanger Tester", "Thermocouple (K-type)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
