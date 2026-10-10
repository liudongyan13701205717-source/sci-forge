"""绘画学科论文支持：视觉艺术、创作技法与艺术理论研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="drawing",
    aliases=(
        "drawing", "绘画", "绘画艺术",
        "visual arts", "视觉艺术",
        "art", "艺术",
        "painting", "绘画",
        "sketching", "素描",
        "illustration", "插画",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（艺术问题与理论背景）",
            "methodology（创作分析、技法研究、观众研究）",
            "results（艺术效果与视觉分析）",
            "discussion（艺术理论与实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "work analysis（作品分析）",
            "technique analysis（技法分析）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（艺术理论综述）",
            "major works（重要作品分析）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "creation": "创作过程须注明材料、尺寸与时间",
        "analysis": "视觉分析须注明方法与理论框架",
        "exhibition": "展览须注明地点、时间与作品编号",
    },
    conventions=(
        "作品首次出现给出标题、作者、年份与媒介",
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "技法名称须使用行业标准",
        "引用作品图片须注明版权与来源",
    ),
    key_venues=(
        "Art Journal",
        "Art Journal",
        "October",
        "The Art Bulletin",
        "Journal of Aesthetic Education",
        "Critical Inquiry",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "技法名称须使用行业标准",
        "引用作品图片须注明版权与来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Procreate", "Affinity Designer", "Affinity Photo", "Inkscape", "GIMP", "Clip Studio Paint", "MediBang Paint", "Sketchbook", "Watercolor Paper", "Oil Paint", "Acrylic Paint", "Watercolor Paint", "Graphite Pencils", "Charcoal", "Pastels", "Ink", "Brushes", "Easel"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Design & Art Exchange"),
)
