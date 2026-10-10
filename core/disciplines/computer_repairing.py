"""计算机维修与故障诊断学科论文支持：硬件检测/故障诊断/案例体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_repairing",
    aliases=("computer repairing", "计算机维修", "计算机维护",
             "computer maintenance", "计算机服务", "IT 服务",
             "计算机组装与维修", "computer hardware repair",
             "硬件维修", "IT 硬件维护"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method/diagnosis process",
            "case study",
            "results",
            "conclusion",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "detection methodology",
            "repair procedure",
            "evaluation",
            "lessons learned",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy of faults",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="IEEE 编号样式",
    reporting_standards={
        "experimental": "诊断报告须给出仪器型号、测试项与判定标准",
        "case_study": "维修案例须描述症状、诊断路径与最终处置",
        "benchmark": "诊断时间/修复率须按统一用例集统计",
        "safety": "高压/静电/热作业须声明安全规程",
        "reproducibility": "检测脚本与配置须公开",
    },
    conventions=(
        "故障现象须记录复现条件、日志与硬件清单",
        "诊断流程以故障树或流程图给出",
        "修复步骤须区分硬件替换、软件恢复与固件升级",
        "维修结果给出成功率与平均修复时间（MTTR）",
        "报废判定须引用厂商维修手册与合规标准",
    ),
    key_venues=(
        "Computer Maintenance Review",
        "Journal of Computer and Communications",
        "IEEE Access",
        "International Journal of Computer Applications",
        "Computers and Electrical Engineering",
        "Microelectronics Reliability",
        "Reliability Engineering & System Safety",
        "Journal of Failure Analysis and Prevention",
    ),
    units_and_formulas_notes=(
        "维修时间以小时/分钟计；成功率以 % 计",
        "静电放电电压以 kV 计",
        "故障率以 FPMI 或 FIT 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Multimeter (Fluke 87V)", "Oscilloscope (Rigol DS1104)", "Multimeter (Uni-T UT61E)", "Hot Air Rework Station (Quick 861DW)", "Soldering Iron (Weller WES51)", "ESD Grounding Mat", "ESD Wrist Strap", "Multimeter (Keysight 34465A)", "Bench Power Supply (Rigol DP832)", "Logic Analyzer (Saleae Logic 8)", "Fluke 87V Multimeter", "Fluke 8508A Oscilloscope", "Postech DTM-1000 Multimeter", "Fluke DSX-5000 Cable Analyzer", "Keysight DTX-1800C Network Analyzer", "PC Speaker Test Tools", "MBF1 Test Adapter", "Memory Test Kit (Kingston Diagnostic Kit)", "HDD Stress Tool (HDD Regenerator)", "CrystalDiskInfo", "HWiNFO64", "AIDA64", "MemTest86", "Linux Live USB (Ubuntu Rescue Remix)", "Windows 11 Installation Media", "Mac OS Recovery USB", "UEFI/BIOS Flash Tool", "Thermal Paste (Arctic MX-4)", "Thermal Imaging Camera (FLIR C5)", "Compressed Air Duster", "Contact Cleaner (DeoxIT D5)"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore"),
)
