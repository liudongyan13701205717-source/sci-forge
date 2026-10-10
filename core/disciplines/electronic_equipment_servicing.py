"""电子设备维修学科论文支持：电子设备技术、故障诊断与维修工艺研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronic_equipment_servicing",
    aliases=(
        "electronic_equipment_servicing", "电子设备维修", "电子设备服务",
        "electronic equipment servicing", "电子设备维修",
        "electronic repair", "电子维修",
        "equipment maintenance", "设备维护",
        "fault diagnosis", "故障诊断",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（维修问题与背景）",
            "methodology（维修方法、实验条件、效果评估）",
            "results（维修效果与可靠性评估）",
            "discussion（维修优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "repair process（维修过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "repair": "维修步骤须完整描述",
        "testing": "测试方法须注明（万用表、示波器等）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "电压用 V 表示",
        "电流用 A 表示",
        "电阻用 Ω 表示",
        "功率用 W 表示",
        "频率用 Hz 表示",
    ),
    key_venues=(
        "IEEE Transactions on Consumer Electronics",
        "Journal of Electrical Engineering",
        "Electrical Engineering",
        "Journal of Electrical Systems",
        "International Journal of Electrical Engineering",
    ),
    units_and_formulas_notes=(
        "电压用 V 表示",
        "电流用 A 表示",
        "电阻用 Ω 表示",
        "功率用 W 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Multimeter", "Oscilloscope", "Function Generator", "Power Supply", "Soldering Station", "Desoldering Pump", "Wire Stripper", "Crimping Tool", "Insulation Tester", "Earth Tester", "Clamp Meter", "LCR Meter", "Logic Analyzer", "Spectrum Analyzer", "Thermal Camera", "Component Tester", "PCB Repair Kit", "Electrical Safety Tester", "Cable Tester", "Flux Cleaner"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
