"""电气安装学科论文支持：电气布线、安装工艺与安全规范研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electrical_fitting",
    aliases=(
        "electrical_fitting", "电气安装", "电气布线",
        "electrical installation", "电气安装",
        "electrical wiring", "电气布线",
        "cable installation", "电缆安装",
        "electrical fitting", "电气装配",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（安装问题与背景）",
            "methodology（安装方法、实验条件、效果评估）",
            "results（安装效果与安全评估）",
            "discussion（安装优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "installation process（安装过程）",
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
        "installation": "安装步骤须完整描述",
        "testing": "测试方法须注明（绝缘测试、接地测试等）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "电压用 V 表示",
        "电流用 A 表示",
        "导线截面积用 mm² 表示",
        "接地电阻用 Ω 表示",
        "绝缘电阻用 MΩ 表示",
    ),
    key_venues=(
        "IEEE Transactions on Industry Applications",
        "Journal of Electrical Engineering",
        "Electrical Engineering",
        "International Journal of Electrical Engineering",
        "Journal of Electrical Systems",
    ),
    units_and_formulas_notes=(
        "电压与电流用 V、A 表示",
        "导线截面积用 mm² 表示",
        "接地电阻用 Ω、绝缘电阻用 MΩ 表示",
        "测试频率用 Hz 表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Multimeter", "Insulation Tester", "Earth Tester", "Clamp Meter", "Cable Tester", "Wire Stripper", "Crimping Tool", "Cable Puller", "Fish Tape", "Conduit Bender", "Cable Tray", "Junction Box", "Circuit Breaker", "Residual Current Device", "Surge Protector", "Cable Gland", "Terminal Block", "Cable Marker", "Voltage Detector", "Torque Wrench"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
