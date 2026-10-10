"""技术制图学科论文支持：工程图/技术图示与标注规范的体裁、ISO/GAS 引用样式与制图注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="technical_drawing",
    aliases=(
        "technical_drawing",
        "技术制图",
        "工程制图",
        "工程图",
        "技术图示",
        "technical illustration",
        "engineering drawing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与制图问题）",
            "methods（绘图方法/软件与制图规范）",
            "results（图示结果与可读性验证）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（对象与制图需求）",
            "drawing process（制图流程与图幅组织）",
            "results（成果与标注完整度核查）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "evidence synthesis（规范演变与流派比较）",
            "future directions",
            "references",
        ),
    },
    citation_style="ISO 样式（标准文件按编号与年份引用，如 ISO 128:2002）",
    reporting_standards={
        "drawing_standard": "工程图遵循 ISO 128 系列（技术制图通则）",
        "dimensioning": "尺寸标注与公差遵循 ISO 1101（几何公差）与 ISO 2768",
        "gd_and_fl": "几何尺寸与公差标注遵循 ISO 1101 / ASME Y14.5",
        "schematic": "流程与系统图遵循 ISO 14517（技术图示通则）",
        "quality_control": "图纸审校遵循 ISO 9001 文件控制要求",
    },
    conventions=(
        "线型与线宽按 ISO 128 分级：粗实线用于可见轮廓，细虚线用于不可见轮廓",
        "视图方向采用第一角或第三角投影，须在标题栏注明",
        "剖面线倾角统一 45°，间距与比例成图一致",
        "尺寸标注只标一次，避免重复标注与封闭尺寸链",
        "字体、图幅、比例、公差代号须在标题栏完整填写"
    ),
    key_venues=(
        "Engineering Design Graphics Journal",
        "Computer-Aided Design",
        "Design Studies",
        "Journal of Engineering Design",
        "ISO Journal",
    ),
    units_and_formulas_notes=(
        "线性尺寸用 mm（未标单位时默认 mm）；角度用 ° 或 rad",
        "公差按 ISO 286 字母制标注（如 H7/g6），不写数值偏差",
        "公式用 amsmath；面积/体积/展开系数公式须编号并被引用",
        "比例标注用 1:n 形式（如 2:1、1:50），不使用百分比"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "AutoCAD Mechanical", "SolidWorks", "Fusion 360", "CATIA V5", "Creo Parametric", "Inventor", "Onshape", "FreeCAD", "LibreCAD", "QCAD", "DraftSight", "Alibre Design", "OpenSCAD", "SketchUp", "Rhino 3D", "Visio", "CorelDRAW", "Adobe Illustrator", "LibreOffice Draw"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
