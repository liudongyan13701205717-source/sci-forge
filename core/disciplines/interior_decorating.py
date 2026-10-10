"""室内装饰学科论文支持：材料、色彩与施工工艺研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interior_decorating",
    aliases=(
        "interior_decorating",
        "室内装饰",
        "Interior Decorating",
        "Interior Decorator",
        "Residential Decorating",
        "Domicile Decoration",
        "居家装饰",
        "软装设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、对象与问题）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "GB/T 18883（室内空气质量）",
        "k2": "ASTM D4236（颜料/涂料标识）",
        "k3": "LEED 报告规范（可持续认证）",
    },
    conventions=(
        "材料清单须列出规格、颜色与供应商",
        "施工工艺与工序须符合行业规范",
        "色彩方案用 Pantone 或 RAL 标注",
        "甲醛、VOC 等检测报告须附",
        "案例须展示施工前与施工后对比",
    ),
    key_venues=(
        "Interiors Design Magazine",
        "Architectural Digest",
        "Domus",
        "Designs of Consequence",
        "Houzz Magazine",
    ),
    units_and_formulas_notes=(
        "色彩用 Pantone / RAL / HEX 明确标注",
        "面积用 ㎡，长度用 mm 或 cm",
        "照度用 lux（lx）",
        "VOC 与甲醛浓度用 mg/m³ 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "SketchUp", "AutoCAD", "Revit", "V-Ray", "Lumion", "D5 Render", "Procreate", "Crayola Colorific", "Pantone Connect", "Swatch", "Wiggle", "Epson SureColor", "ColorMunki", "Adobe Fresco", "Microsoft Excel", "Canva", "Pinterest"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
