"""砌筑学科论文支持：砌筑工艺/结构性能体裁、ASME/BS 引用样式与砌筑记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bricklaying",
    aliases=(
        "bricklaying",
        "Bricklaying",
        "砌砖",
        "砌筑",
        "砌筑工艺",
        "砖砌体",
        "砖工",
        "brick masonry",
        "masonry construction",
        "brickwork",
        "砌筑工程",
        "砌筑技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（砌体试件、砂浆、试验）",
            "results（强度、耐久性、变形）",
            "discussion",
            "conclusion",
            "references",
        ),
        "practice": (
            "abstract",
            "design brief",
            "material selection",
            "construction process",
            "quality control",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份，建筑学/土木工程引用规范）",
    reporting_standards={
        "materials": "砖、砂浆、灰缝材料须完整报告",
        "specimens": "试件尺寸、养护条件须符合 EN 771 或 ASTM C1314",
        "testing": "抗压强度、抗拉强度、弹性模量须按规范测试",
        "moisture": "含水率、吸水率须报告",
    },
    conventions=(
        "砌体类型符号用'全顺砌法'、'半顺砌法'、'十字砌法'、'梅花砌法'等术语",
        "砖规格用 mm 报告（如 240×115×53）",
        "砂浆用 M 级（如 M5、M7.5）标记",
        "灰缝厚度用 mm 报告",
        "砌体试验须标注样本量与养护龄期",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Masonry International",
        "Journal of Performance of Constructed Facilities",
        "Engineering Structures",
        "Building and Environment",
        "Journal of Building Construction and Engineering",
        "Materials",
    ),
    units_and_formulas_notes=(
        "强度用 MPa 报告",
        "砖尺寸用 mm 报告",
        "砂浆用 M 级（M5、M7.5、M10、M15）",
        "灰缝厚度 10-15 mm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp", "Revit", "Vectorworks", "Chief Architect", "Rhino", "BricsCAD", "Laser Level", "Digital Level", "Penetrometer", "Compression Tester", "Masonry Drill", "Chipping Hammer", "Brick Cutter", "Plumb Bob", "Trowel", "Brick Setter", "Mason's Trowel", "Masonry Gauge", "Brick Press"),
    category="工学",
    databases=("OpenAlex", "Google Scholar", "ScienceDirect", "Elsevier"),
)
