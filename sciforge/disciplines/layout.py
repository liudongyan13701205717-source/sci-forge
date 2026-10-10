"""版面设计学科论文支持：版式美学、可读性与视觉传达研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="layout",
    aliases=(
        "layout",
        "版面设计",
        "Layout Design",
        "Graphical Layout",
        "Page Layout",
        "Editorial Design",
        "视觉传达设计",
        "排版艺术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与样本）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（视觉分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或 Chicago（设计类常用）",
    reporting_standards={
        "k1": "样本来源（期刊/书籍/网页）与年代分布",
        "k2": "评价方法与评分量表（专家/用户）",
        "k3": "主观评价给评分者信度（如 Krippendorff α）",
    },
    conventions=(
        "设计术语首次出现给中英对照",
        "图示区分原稿与重排版",
        "评价量表题项与刻度统一说明",
        "色彩与字体注明（名称或 Pantone/字体家族）",
        "参考文献体例全稿一致",
    ),
    key_venues=(
        "Design Studies",
        "Leonardo",
        "Journal of Visual Culture",
        "Design Issues",
        "装饰",
    ),
    units_and_formulas_notes=(
        "字号用 pt 或 px，行距用倍率",
        "字号-可读性关系以阅读时间或眼动时长",
        "色彩用 CIELAB L*a*b* 或 Pantone 码",
        "网格单位用 mm 或 pt",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Affinity Publisher", "Scribus", "QuarkXPress", "Illustrator", "Inkscape", "GIMP", "Photoshop", "Affinity Photo", "Figma", "Sketch", "Blender", "LaTeX", "Canva", "CorelDRAW", "Vectornator", "Linearity Curve", "Glyphs", "FontLab", "Preflight"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
