"""锁具制作与保险柜修理学科论文支持：机械锁具设计与安防维修技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="locksmithing_and_safe_repairing",
    aliases=(
        "locksmithing_and_safe_repairing",
        "锁具制作",
        "保险柜修理",
        "locksmithing",
        "safe opening",
        "机械锁",
        "安防维修",
        "physical security",
        "pin tumbler",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术背景）",
            "methodology（研究方法）",
            "results（实验结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（技术分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ISO 690",
    reporting_standards={
        "k1": "锁具测试按 EN 12209 或 ANSI/BHMA 标准",
        "k2": "保险柜破坏性测试标注工具与耗时",
        "k3": "维修案例记录型号与故障模式",
    },
    conventions=(
        "锁具等级标注参考 EN 1303 或 UL 558",
        "机械参数使用 SI 单位并给出公差",
        "开锁技术说明标注工具与前提条件",
        "图纸标注遵循 GB/T 4458",
        "材料标注使用 ASTM 或 GB 牌号",
    ),
    key_venues=(
        "Journal of Mechanical Engineering",
        "SAE Transactions",
        "Locksmith Journal",
        "Journal of Materials Engineering and Performance",
        "Security Engineering Review",
    ),
    units_and_formulas_notes=(
        "扭矩以 N·m 报告",
        "硬度以 HRC 或 HV 报告",
        "公差采用 ISO 286 配合制",
        "开锁时间以秒计并给出中位数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SolidWorks", "AutoCAD", "Fusion 360", "Rhino", "CATIA", "ANSYS Mechanical", "Abaqus", "Mastercam", "Grasshopper", "CNC (Haas VF-4)", "CNC (Haas ST-20)", "EDM (Sodick)", "3D Printer (FDM)", "3D Printer (SLA)", "Microscope (Zeiss)", "Oscilloscope (Keysight)", "Multimeter (Fluke)", "Torsion tester (Instron)", "Laser Scanner (Artec)", "Safe Opening Kit (Locksport)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
