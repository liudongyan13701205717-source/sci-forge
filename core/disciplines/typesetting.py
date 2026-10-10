"""排版学科论文支持：文字编排与版面设计体裁、Chicago/APA 引用样式与排版记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="typesetting",
    aliases=("typesetting", "排版", "文字编排", "版面设计", "桌面出版",
             "typography", "page layout", "desktop publishing"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与排版问题）",
            "methods（字体、网格与排版规则）",
            "results（可读性与版面评价）",
            "discussion（设计机理与应用）",
            "references",
        ),
        "design_case": (
            "abstract",
            "introduction",
            "design brief（设计需求）",
            "process（排版过程与决策）",
            "evaluation（评价与反馈）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago/APA 样式（作者-年份或注释-参考文献；设计类期刊多用 Chicago）",
    reporting_standards={
        "design_documentation": "排版方案须报告字体、字号、行距、字距与网格参数",
        "readability": "可读性研究须报告被试、任务与测量指标",
        "reproducibility": "须说明所用字体授权与渲染环境以便复现",
        "typographic_metrics": "须报告度量单位（pt/em/px）与页面尺寸",
    },
    conventions=(
        "字体名称与版本须完整给出（含字重与字宽）",
        "版面参数以 pt/em 为单位并说明基准字号",
        "颜色以 CMYK/RGB/HEX 注明色彩空间",
        "网格系统与栏宽须量化描述",
        "特殊字符与标点遵循目标语言的排版规则",
    ),
    key_venues=(
        "Visible Language",
        "The Journal of Typographic Research",
        "Design Issues",
        "Typography Papers",
        "Journal of Design History",
        "Information Design Journal",
    ),
    units_and_formulas_notes=(
        "字号/行距用 pt；字距用 em 或 1/1000 em",
        "页面尺寸用 mm；版心与栏宽用 mm/pt",
        "分辨率用 dpi/ppi；色彩用 CMYK/RGB/HEX",
        "基线网格与行距倍数须显式说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "TeX Live", "Overleaf", "Adobe InDesign", "QuarkXPress", "Scribus", "Adobe Illustrator", "Adobe Photoshop", "Affinity Publisher", "Pandoc", "XeLaTeX", "LuaLaTeX", "BibTeX", "Biber", "MakeIndex", "FontForge", "Glyphs", "Inkscape", "KOMA-Script", "ConTeXt"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
