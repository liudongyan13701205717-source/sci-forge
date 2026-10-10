"""通信设备学科论文支持：硬件设计/微波射频/电磁兼容体裁、IEEE 引用样式与设备记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications_equipment",
    aliases=("communications equipment", "通信设备", "通信硬件", "微波射频",
             "天线设计", "RF设备", "RF and microwave engineering",
             "antenna design", "communications hardware"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与硬件问题）",
            "design（硬件方案与原理）",
            "implementation（实现与仿真）",
            "results（测试与验证）",
            "conclusions",
            "references",
        ),
        "device_design": (
            "abstract",
            "introduction",
            "design methodology（设计方法）",
            "prototype（原型制作）",
            "test results（测试结果）",
            "conclusions",
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
    citation_style="IEEE 样式（编号制；IEEE 期刊遵循 IEEE 规范）",
    reporting_standards={
        "experimental": "实验研究遵循 IEEE 实验报告规范",
        "emc_test": "电磁兼容测试遵循 CISPR/IEC 61000 标准",
        "thermal_test": "热测试遵循 JEDEC/IEC 热测试标准",
        "manufacturing": "生产测试遵循 IPC 标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "硬件设计须说明元器件选型、容差与替代方案",
        "EMC 测试须报告测试条件、限值标准与天线配置",
        "热设计须给出散热路径、温升曲线与热阻值",
        "生产测试须说明测试覆盖率与缺陷率统计",
        "器件参数须标注测试条件与频率范围",
    ),
    key_venues=(
        "IEEE Transactions on Microwave Theory and Techniques",
        "IEEE Microwave and Wireless Components Letters",
        "IEEE Transactions on Antennas and Propagation",
        "IEEE Journal of Microwaves",
        "Electronics Letters",
        "IET Microwaves, Antennas & Propagation",
        "IEEE Transactions on Electromagnetic Compatibility",
    ),
    units_and_formulas_notes=(
        "频率用 Hz/kHz/MHz/GHz；波长用 m/cm/mm",
        "功率用 mW/W/dBm/dBW；增益用 dBi/dB",
        "阻抗用 Ω；电压用 V；电流用 A",
        "公式用 amsmath；S 参数与传输线方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与测试次数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "ANSYS HFSS", "CST Studio Suite", "COMSOL Multiphysics", "Altium Designer", "Cadence Allegro", "KiCad", "Proteus", "Multisim", "Keysight ADS", "NI LabVIEW", "R&S ZVA Network Analyzer", "R&S FSW Spectrum Analyzer", "Tektronix Oscilloscope", "Rohde & Schwarz Signal Generator", "Anritsu Power Meter", "Thermal Chamber", "Soldering Station", "AOI Inspection System", "ICT Tester", "Fiber Optic Tester", "EMI Chamber", "Reflow Oven", "X-ray Inspection"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "IEEE Xplore", "CNKI"),
)
