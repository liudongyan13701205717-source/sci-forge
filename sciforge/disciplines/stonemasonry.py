"""石工学科论文支持：石砌结构、石材耐久性与石质文物保护研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stonemasonry",
    aliases=("stonemasonry", "石工", "石砌", "石匠工艺", "石质建筑",
             "stone masonry", "masonry work", "stone construction",
             "石材砌筑", "古建筑石作"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程问题）",
            "materials and methods（材料、试件与试验）",
            "results（强度、耐久性与变形结果）",
            "discussion（工程含义与优化）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（石砌建筑或工程案例）",
            "analysis（结构性能与耐久性分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（石工技术综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份）",
    reporting_standards={
        "materials": "石材、砂浆、灰缝材料须完整报告",
        "testing": "强度、变形、耐久性须按 EN 771/EN 1449 或等效标准测试",
        "structure": "石砌结构分析须符合 EN 1996 或等效规范",
        "conservation": "修复须遵循最小干预与可识别原则",
    },
    conventions=(
        "石料名称须给出地质分类（如石灰石、砂岩、花岗岩、青石）",
        "石块尺寸以 mm 报告",
        "砂浆用 M 级标记（M5、M7.5、M10 等）",
        "灰缝厚度以 mm 报告（常用 10–15 mm）",
        "试验须标注样本量与养护龄期",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Engineering Structures",
        "Masonry International",
        "Journal of Performance of Constructed Facilities",
        "文物保护研究",
    ),
    units_and_formulas_notes=(
        "强度：MPa；尺寸：mm",
        "砂浆 M 级（M5、M7.5、M10、M15、M20）",
        "灰缝厚度：10–15 mm",
        "试验报告均值 ± SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp", "Revit", "Rhino", "Vectorworks", "ANSYS", "SAP2000", "MIDAS", "Laser level", "Penetrometer", "Core drill", "Ultrasonic tester", "Compression tester", "Chipping hammer", "Masonry drill", "Stone cutting machine", "Diamond saw", "Plumb bob", "Mason's trowel", "Stone chisel set"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
