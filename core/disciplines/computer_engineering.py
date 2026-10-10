"""计算机工程学科论文支持：嵌入式系统/硬件设计/电路体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_engineering",
    aliases=("computer engineering", "计算机工程", "电子与计算机工程",
             "embedded systems", "嵌入式系统", "硬件设计", "电路设计",
             "微处理器工程", "digital systems", "数字系统", "计算机硬件"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method",
            "implementation",
            "evaluation",
            "conclusion",
            "references",
        ),
        "system": (
            "abstract",
            "introduction",
            "background and motivation",
            "architecture",
            "implementation",
            "evaluation",
            "lessons learned",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="IEEE 编号样式",
    reporting_standards={
        "experimental": "评估须给出硬件版本、仿真平台与实测条件",
        "benchmark": "基准测试遵循 IEEE 标准负载报告规范",
        "simulation": "电路/时序仿真须说明工具与约束",
        "reproducibility": "固件源码、约束文件（XDC/QSF）须公开",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "硬件版本（芯片型号、封装、时钟）须报告",
        "软件-硬件协同设计须分别标注软件栈与固件版本",
        "性能与功耗须同时给出",
        "约束与测试用例须明确",
        "结论须区分硬件改进与整体收益",
    ),
    key_venues=(
        "IEEE Transactions on Computers",
        "IEEE Transactions on Embedded Systems",
        "IEEE Transactions on Very Large Scale Integration (VLSI) Systems",
        "ACM Transactions on Design Automation of Electronic Systems",
        "International Symposium on Applied Reconfigurable Computing (ARC)",
        "Design Automation Conference (DAC)",
        "IEEE Computer Engineering (COMPCON)",
        "Embedded Systems Letters",
    ),
    units_and_formulas_notes=(
        "频率用 MHz/GHz；功耗用 mW/W；延迟用 ns/ms",
        "面积用 mm²；工艺用 nm",
        "时序约束用 Tck 与建立/保持时间标注",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("STM32CubeIDE", "Keil MDK", "IAR Embedded Workbench", "PlatformIO", "Arduino IDE", "Vivado", "Quartus", "ModelSim", "Icarus Verilog", "GTKWave", "OpenOCD", "J-Link", "Logic Analyzer (Saleae)", "Oscilloscope (Keysight)", "Multisim", "LTspice", "KiCad", "Altium Designer", "MATLAB/Simulink", "FreeRTOS", "Zephyr", "CMake", "Docker", "Verilator", "Intel Pin", "SystemC"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore"),
)
