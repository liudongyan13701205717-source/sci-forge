"""Automotive electrical systems 学科论文支持：E/E 架构、车载总线、汽车电子与线束工程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="automotive_electrical_systems",
    aliases=(
        "automotive_electrical_systems",
        "汽车电气系统",
        "车载电子",
        "汽车电子",
        "汽车电气",
        "Automotive Electrical Systems",
        "Automotive Electronics",
        "E/E Architecture",
        "车载总线",
        "车载以太网",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（架构、建模、标定与试验）",
            "results（性能、仿真与实测）",
            "discussion（机理与工程意义）",
            "conclusion（结论与展望）",
            "references",
        ),
        "technical_note": (
            "abstract",
            "introduction（问题陈述与范围）",
            "architecture（E/E 架构与总线拓扑）",
            "implementation（实现、标定与 HIL）",
            "validation（仿真与实测对比）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制，作者-文献编号，如 [1]、[2]）",
    reporting_standards={
        "emc_testing": "EMC 遵循 CISPR 25 / ISO 11452 / ISO 7637 / ISO 10605",
        "functional_safety": "功能安全遵循 ISO 26262（ASIL A/B/C/D）与 ISO PAS 8800",
        "bus_compliance": "CAN/CAN-FD/LIN 遵循 ISO 11898 / ISO 17987 / ISO 17988",
        "ethernet": "车载以太网遵循 IEEE 802.3 / AUTOSAR Ethernet / ARINC 664",
        "diagnostics": "车载诊断遵循 ISO 14229 (UDS) / ISO 15765 (DoIP)",
        "simulation": "仿真遵循 AUTOSAR/MDA 分层（MLR/ASW/BSW/BSW-M）",
    },
    conventions=(
        "整车电子电气架构（E/E 架构）须完整描述总线拓扑（CAN/CAN-FD/LIN/车载以太网/AVB）",
        "报文信号（信号名、周期、长度、字节序）须以 DBC/A2L 或 ARXML 附带",
        "电气负载与母线压降须给出实测数据与仿真对比",
        "EMC 测试遵循 CISPR 25 / ISO 11452 / ISO 7637 并标注版本",
        "功能安全等级遵循 ISO 26262 ASIL 分级并显式报告 ASIL",
        "HIL/SIL 试验须给出测试脚本与执行环境版本",
    ),
    key_venues=(
        "IEEE Transactions on Vehicular Technology",
        "SAE International Journal of Connected and Automated Vehicles",
        "SAE International Journal of Electrical and Hybrid Vehicles",
        "SAE International Journal of Vehicles and Machines",
        "IEEE Transactions on Industrial Electronics",
        "IFAC-PapersOnLine (World Congress, AutoMod)",
        "IEEE Conference on Vehicular Technology (VTC)",
        "SAE World Congress",
        "IEEE International Conference on Power Electronics (ECCE)",
    ),
    units_and_formulas_notes=(
        "电压用 V、电流用 A、电阻用 Ω；总线速率用 bps（bit/s）",
        "CAN 帧用 Data Frame / Remote Frame 表示；位段用 bit offset + length 描述",
        "信号精度/分辨率用 factor/offset 表示（DBC 语法）",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "时序图按 1 kHz / 10 kHz / 100 kHz 分档标注时钟",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Vector CANoe", "Vector CANalyzer", "Vector INCA", "Vector VT System", "dSPACE SCALEXIO", "Lauterbach TRACE32", "National Instruments PXI", "NI VeriStand", "NI TestStand", "NI Multisim", "NI DIAdem", "MATLAB/Simulink", "Simulink Embedded Coder", "Green Hills MULTI", "Wind River Simics", "TI Code Composer Studio", "Keysight ADS", "ANSYS Electronics Desktop", "ANSYS HFSS", "ANSYS Icepak", "Aldec HyperLynx", "Altium Designer", "OrCAD", "Cadence Xcelium", "KiCad", "LTspice"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "IEEE Xplore", "SAE Mobilus"),
)
