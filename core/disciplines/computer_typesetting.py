"""计算机排印/排版学科论文支持：排印学/字体设计与文档工程体裁、TUG/APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_typesetting",
    aliases=(
        "computer typesetting", "computer type-setting", "计算机排印", "计算机排版",
        "typography", "排印学", "字体设计", "font design",
        "digital typography", "数字排印", "文档排版", "document typesetting",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method（算法/字体设计/度量学）",
            "evaluation（用户研究/统计度量/对比实验）",
            "conclusion",
            "references",
        ),
        "design": (
            "abstract",
            "context",
            "design goals",
            "typographic system",
            "specimen（示例）",
            "discussion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview",
            "taxonomy",
            "open problems",
            "references",
        ),
    },
    citation_style="APA 7 或 TUGboat 样式（排印学社区惯例）",
    reporting_standards={
        "user_study": "用户研究遵循 HCI 实验规范（样本量、随机化、被试内/被试间）",
        "metrics": "统计度量（字距/x 高度/对比）须给出计算式",
        "artifacts": "字体文件、模板与源码须发布至持久位置",
    },
    conventions=(
        "字体度量（em、x 高度、ascender、descender、baseline）术语统一",
        "字形（glyph）与字符（character/codepoint）区分清晰",
        "示例图须标注字体名、字重、字号与渲染条件",
        "引用他人字体须遵循各自许可（OFL/Apache/MIT）",
    ),
    key_venues=(
        "TUGboat",
        "Journal of Design & Computing",
        "IEEE Transactions on Visualization and Computer Graphics",
        "CHI",
        "ACM Transactions on Graphics (TOG)",
        "Design Studies",
        "International Journal of Digital Typography",
    ),
    units_and_formulas_notes=(
        "字号用 pt/px/em 并标注相对或绝对",
        "字距（kerning）用 em 或 fs 单位",
        "公式用 amsmath；度量学定义须明确坐标原点",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "TeX", "LuaTeX", "XeTeX", "Pandoc", "Typst", "Inkscape", "FontForge", "Glyphs", "FontLab", "RoboFont", "Birdfont", "FontTools", "AFDKO", "HarfBuzz", "Scribus", "TeX Live", "MiKTeX", "Tectonic", "Adobe InDesign"),
    category="工学",
    databases=("OpenAlex", "Crossref", "TUGboat"),
)
