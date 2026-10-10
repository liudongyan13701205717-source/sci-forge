"""电子传感器与数字硬件学科论文支持：传感器技术、数字电路与嵌入式系统研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronics_sensors_and_digital_hardware",
    aliases=(
        "electronics_sensors_and_digital_hardware", "电子传感器与数字硬件",
        "electronic sensors", "电子传感器",
        "digital hardware", "数字硬件",
        "sensor technology", "传感器技术",
        "embedded hardware", "嵌入式硬件",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（传感器问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（传感器性能与硬件评估）",
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
        "design": "设计参数须完整（灵敏度、分辨率、响应时间等）",
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
        "IEEE Sensors Journal",
        "IEEE Transactions on Instrumentation and Measurement",
        "Sensors and Actuators A: Physical",
        "Sensors and Actuators B: Chemical",
        "IEEE Transactions on Industrial Electronics",
        "IEEE Transactions on Circuits and Systems",
    ),
    units_and_formulas_notes=(
        "电压用 V 表示",
        "电流用 A 表示",
        "功率用 W 或 kW 表示",
        "频率用 Hz 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "LabVIEW", "Arduino IDE", "PlatformIO", "STM32CubeIDE", "Keil uVision", "IAR Embedded Workbench", "Altium Designer", "Eagle", "KiCad", "Proteus", "Multisim", "LTspice", "PSpice", "Python (numpy, scipy)", "R (RStudio)", "Excel", "Origin", "FPGA (Vivado)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
