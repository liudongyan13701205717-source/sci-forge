"""桌面出版软件使用学科论文支持：版面设计/排版/出版生产流程体裁、IEEE 样式与出版记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_for_desktop_publishing_use_of",
    aliases=(
        "software_for_desktop_publishing_use_of",
        "桌面出版",
        "DTP",
        "桌面排版",
        "版面设计",
        "出版制作",
        "desktop publishing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "technical_report": (
            "abstract",
            "introduction",
            "technical overview（技术概述）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者-编号，如 [1]、[2]）",
    reporting_standards={
        "experimental": "实验遵循出版工程实验报告规范",
        "case_study": "案例研究遵循出版案例报告规范",
        "technical": "技术报告遵循出版技术报告规范",
        "benchmark": "基准测试遵循出版生产基准报告规范",
    },
    conventions=(
        "版面尺寸与网格须报告（mm/A4/A5）",
        "字体、字号与字距须说明",
        "色彩模式须注明（CMYK/RGB）",
        "输出格式与分辨率须报告",
        "版本与插件版本须说明",
    ),
    key_venues=(
        "Journal of Digital Media",
        "Design Studies",
        "International Journal of Information Technology",
        "Journal of Publishing Research",
        "Information Design Journal",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm；分辨率用 dpi/ppt",
        "色彩用 CMYK % 或 RGB 0-255",
        "公式用 amsmath；版面参数须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "QuarkXPress", "CorelDRAW", "Affinity Publisher", "Scribus", "Microsoft Publisher", "LaTeX", "Aldus PageMaker", "Adobe Acrobat", "InDesign Server", "XMPie", "SignaWorks", "Enfocus PitStop", "Adobe InCopy", "Adobe FrameMaker", "Canva", "Figma", "Adobe Creative Cloud"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
