"""砖石工程学科论文支持：砌体结构/耐久性体裁、EN/ASCE 引用样式与砌筑记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="brickwork_and_masonry",
    aliases=(
        "brickwork_and_masonry",
        "brickwork",
        "masonry",
        "Brickwork and masonry",
        "砖石工程",
        "砖石结构",
        "石工",
        "stone masonry",
        "masonry engineering",
        "masonry construction",
        "砖石砌筑",
        "砌体结构",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（试件、材料、试验）",
            "results（强度、变形、耐久性）",
            "discussion",
            "conclusion",
            "references",
        ),
        "structural": (
            "abstract",
            "design brief",
            "structural modeling",
            "analysis and design",
            "conclusion",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份）",
    reporting_standards={
        "materials": "砖、石、砂浆、灰缝材料须完整报告",
        "specimens": "试件尺寸、养护条件须符合 EN 771/EN 1449",
        "testing": "强度、变形、耐久性须按规范测试",
        "structure": "砌体结构分析须符合 EN 1996 或 ACI 530",
    },
    conventions=(
        "砌体类型符号用中文术语（全顺、半顺、十字、梅花、花砌等）",
        "砖/石规格用 mm 报告",
        "砂浆用 M 级（M5、M7.5、M10、M15、M20）标记",
        "灰缝厚度 10-15 mm",
        "砌体试验须标注样本量与养护龄期",
    ),
    key_venues=(
        "Masonry International",
        "Construction and Building Materials",
        "Engineering Structures",
        "Journal of Performance of Constructed Facilities",
        "Journal of Structural Engineering",
        "Building and Environment",
        "Construction and Building Materials",
    ),
    units_and_formulas_notes=(
        "强度用 MPa 报告",
        "砖/石尺寸用 mm 报告",
        "砂浆用 M 级（M5、M7.5、M10、M15、M20）",
        "灰缝厚度 10-15 mm",
        "砌体试验须标注样本量与养护龄期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp", "Revit", "Vectorworks", "Rhino", "RISA-3D", "ETABS", "SAP2000", "STAAD.Pro", "MIDAS", "Laser Level", "Penetrometer", "Core Drill", "Ultrasonic Tester", "Compression Tester", "Masonry Drill", "Chipping Hammer", "Brick Cutter", "Plumb Bob", "Mason's Trowel"),
    category="工学",
    databases=("OpenAlex", "Google Scholar", "ScienceDirect", "Elsevier"),
)
