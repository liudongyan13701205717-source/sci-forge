"""技术制图学科论文支持：工程制图、CAD 与可视化技术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="drawing_technical",
    aliases=(
        "drawing_technical", "技术制图", "工程制图",
        "technical drawing", "技术制图",
        "engineering drawing", "工程制图",
        "CAD", "计算机辅助设计",
        "blueprint", "蓝图",
        "drafting", "制图",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术问题与背景）",
            "methodology（制图方法、CAD 实现、测试）",
            "results（制图效果与精度评估）",
            "discussion（技术改进方向）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project description（项目描述）",
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
    citation_style="ASME",
    reporting_standards={
        "drawing": "制图标准须注明（如 GB/T、ISO、ASME）",
        "CAD": "CAD 软件须注明版本与设置",
        "testing": "精度测试须注明方法与工具",
    },
    conventions=(
        "尺寸用 mm 表示",
        "线型须符合制图标准（粗实线、细实线、虚线等）",
        "字体须符合制图标准（长体字、斜体等）",
        "比例须注明（如 1:1、1:5、1:10）",
        "图纸格式须符合标准（A4、A3、A2 等）",
    ),
    key_venues=(
        "Journal of Engineering Design",
        "Engineering Design Graphics Journal",
        "CAD Computer-Aided Design",
        "Journal of Mechanical Design",
        "Computers & Graphics",
        "Journal of Engineering Graphics",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 表示",
        "线型须符合制图标准",
        "字体须符合制图标准",
        "比例须注明（如 1:1、1:5、1:10）",
        "图纸格式须符合标准（A4、A3、A2 等）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "Fusion 360", "Rhino 3D", "SketchUp", "Blender", "3ds Max", "Maya", "CATIA", "NX", "Creo", "Inventor", "KeyShot", "Adobe Illustrator", "Adobe Photoshop", "Inkscape", "CorelDRAW", "LibreCAD", "FreeCAD", "OpenSCAD"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore"),
)
