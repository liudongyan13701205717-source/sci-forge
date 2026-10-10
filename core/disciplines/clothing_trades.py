"""服装与制衣工艺学科论文支持：服装工艺/制衣制造/工艺设计体裁、ASTM 引用样式与工艺参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clothing_trades",
    aliases=("clothing_trades", "服装与制衣工艺", "服装制作", "制衣",
             "缝纫工艺", "服装工艺设计", "服装制版",
             "tailoring", "garment construction", "sewing", "pattern making",
             "costume construction", "dressmaking"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（材料、工艺、设备与试验方法）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "design_report": (
            "abstract",
            "background（风格定位与目标群体）",
            "process（设计流程、制版与打样）",
            "results（成衣与穿着效果）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "outlook",
            "references",
        ),
    },
    citation_style="ASTM / AATCC 样式（数字编号）",
    reporting_standards={
        "test_method": "测试方法须标注 AATCC/ISO 标准编号与版本年份",
        "experimental": "工艺试验须给出重复数、样本制备与预处理条件",
        "pattern_making": "制版须说明版型基准（如 AAMA / Grays / ISO 13402）",
        "reproducibility": "工艺参数（缝型、针距、线张力）须完全披露",
    },
    conventions=(
        "缝型（seam type）须按 ASTM D4257 编号（如 301、302、406 等）",
        "针距（stitches per inch 或 mm）须给出具体数值与公差",
        "服装版型基准（body form）须声明标准源",
        "测试与工艺须使用标准编号 + 版本年份 + 语言版本",
        "成衣尺寸须给出测量部位与 AAMA 编号",
    ),
    key_venues=(
        "Journal of Fashion Technology and Education",
        "The Dress Code",
        "Fashion Design & Technology",
        "European Research on Design",
        "Costume",
        "Textile Research Journal",
        "Journal of Applied Engineering Science",
    ),
    units_and_formulas_notes=(
        "针距用 SPI 或 mm；线张力用 cN 或 N",
        "缝型编号按 ASTM D4257",
        "版型尺寸用 cm 或 inch，须注明来源标准",
        "试验报告均值 ± SD 与 P 值",
        "公式用 amsmath；工艺变量符号首次出现处定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Bernina", "Juki", "Toyota (Toyota Machine Works)", "Maxx", "Durkopp Adler", "Pfaff", "Singer", "Gerber AccuMark", "Lectra Diamano", "Optitex", "CAD (Style3D)", "CLO 3D", "BrowZwear", "MarkerMaster", "Wintex", "Kaledo", "MATLAB", "Python (numpy)", "SolidWorks", "AutoCAD", "R"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect"),
)
