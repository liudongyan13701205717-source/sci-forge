"""宝石切割学科论文支持：宝石加工工艺、光学设计与宝石学鉴定研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stone_cutting_precious",
    aliases=("stone_cutting_precious", "宝石切割", "宝石加工", "宝石雕刻",
             "gem cutting", "gemstone cutting", "宝石学", "宝石鉴定",
             "宝石抛光", "钻石切割"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（切割工艺或鉴定方法）",
            "results（光学性能与质量结果）",
            "discussion（优化与商业化讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（宝石加工实例）",
            "analysis（工艺与光学分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（宝石加工技术综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "identification": "宝石鉴定须遵循 GB/T 16552–16554 或 IDA 标准",
        "grinding": "磨削工艺参数（转速、压力、冷却）须报告",
        "optical": "光学性能须报告折射率、色散与双折射",
        "grading": "分级须遵循 GIA 或 IGI 标准",
    },
    conventions=(
        "宝石名称须同时给出中英文与化学成分",
        "重量用克拉（ct）报告",
        "折射率（RI）用四位小数报告",
        "硬度用莫氏硬度（1–10）报告",
        "色散以数值或颜色术语（如 0.044 火彩强）报告",
    ),
    key_venues=(
        "Journal of Gemmology",
        "Gems & Jewellery",
        "Lapidary",
        "International Journal of Precision Engineering and Manufacturing",
        "Jewelers' Circular and World Watch",
    ),
    units_and_formulas_notes=(
        "重量：ct（克拉，1 ct = 0.2 g）",
        "折射率：RI（四位小数，如 2.417–2.419）",
        "色散：数值（如 0.044）",
        "尺寸：mm（长×宽×高）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gem cutting wheel (diamond wheel)", "Hand-held lapidary machine", "Faceting machine", "Diamond saw (band saw)", "Ultrasonic polisher", "Diamond paste polisher", "Refractometer (gemological)", "Pleochroism scope", "Polariscope", "Dichroic viewer", "Diamond loupe (10x/20x)", "Microscope (stereo)", "Spectroscope (mineral)", "Thermal conductivity tester", "Density bottle", "CAD/CAM stone design software (GEMCAD)", "Rhino 3D", "AutoCAD", "3D scanner", "TikZ"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
