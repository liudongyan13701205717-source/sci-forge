"""视觉艺术学科论文支持：创作/评论/策展/教育体裁、MLA 引用与艺术度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="visual_arts",
    aliases=("visual arts", "视觉艺术", "美术", "fine arts",
             "视觉传达", "视觉文化", "contemporary art", "当代艺术"),
    paper_types={
        "research": (
            "abstract",
            "introduction（艺术问题与研究假设）",
            "methodology（创作方法或研究框架）",
            "analysis（作品分析与阐释）",
            "discussion（艺术语境与理论对话）",
            "references",
        ),
        "exhibition": (
            "abstract",
            "introduction",
            "curatorial statement（策展阐述）",
            "work descriptions（作品描述）",
            "interpretive framework（阐释框架）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="MLA 9（艺术人文学科常用）",
    reporting_standards={
        "research": "艺术研究伦理规范",
        "exhibition": "展览策展报告规范",
        "systematic_review": "PRISMA",
        "creation": "创作过程记录规范",
    },
    conventions=(
        "作品引用须给作者、标题、创作年份、媒介、尺寸与收藏地",
        "图像引用须注明版权所有者与许可方式",
        "创作过程须记录材料、技法与工具选择",
        "展览文本须给展厅名称、日期与地点",
        "翻译作品须注明原作者与译者",
    ),
    key_venues=(
        "Art Journal",
        "October",
        "Art Bulletin",
        "Critical Inquiry",
        "Art in America",
    ),
    units_and_formulas_notes=(
        "作品尺寸给 cm 或 inch，格式为 H×W×D",
        "色彩给 PANTONE / CMYK / RGB / hex 值",
        "材料须注明来源与规格（如丙烯 400ml）",
        "比例给宽高比或像素密度（dpi）",
        "版本给 print number 并注明总量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Photoshop", "Illustrator", "InDesign", "Procreate", "Blender", "Maya", "3ds Max", "Cinema 4D", "After Effects", "Premiere Pro", "DaVinci Resolve", "Unity", "Unreal Engine", "Substance Painter", "ZBrush", "V-Ray", "Corona", "Arnold", "Adobe Color", "Adobe Fonts"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
