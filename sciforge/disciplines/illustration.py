"""插画学科论文支持：视觉叙事、出版插画、儿童书、漫画、数字插画与商业视觉设计。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="illustration",
    aliases=("illustration", "插画", "illustration_art", "book_illustration", "editorial_illustration", "children_book_illustration", "digital_illustration", "comic_illustration", "commercial_illustration"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 Chicago（艺术与人文学科常用）",
    reporting_standards={"visual_methodology": "视觉方法须报告创作工具链、笔触/图层/分辨率与迭代过程", "visual_rhetoric": "视觉修辞分析须标注构图、色彩、线条、叙事的观察框架", "fieldwork": "田野与访谈须遵循知情同意、伦理审查与版权合规"},
    conventions=("图像作品须标注媒介、尺寸、创作年份与创作者", "引用作品须区分原作与衍生作品的版权关系", "视觉分析术语使用视觉传达学/符号学规范表述", "图表编号遵循图/表分离规则并给出图注", "涉及未成年或敏感题材须遵循伦理审查要求"),
    key_venues=("Book Design Quarterly", "Editorial Illustration", "Comic Studies", "Leonardo: Arts, Sciences, Technology", "Journal of Visual Culture"),
    units_and_formulas_notes=("图像分辨率以 PPI/DPI 表示", "色彩空间标注 RGB/CMYK/PS 与色彩管理", "笔触/矢量单位以 px/inch/pt 表达", "印刷色稿遵循 Pantone 或 CMYK 色号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Procreate", "Clip Studio Paint", "CorelDRAW", "Affinity Photo", "Affinity Designer", "Inkscape", "Krita", "GIMP", "Blender", "Sketchbook", "Cintiq", "Wacom Tablet", "Sketch", "Figma", "Canva", "OpenToonz", "Autodesk Maya", "Lightroom"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
