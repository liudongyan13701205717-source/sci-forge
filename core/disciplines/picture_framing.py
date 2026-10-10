"""画框装裱学科论文支持：装裱设计/画框工艺/文物修复体裁、艺术学领域引用样式与装裱记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="picture_framing",
    aliases=("picture_framing", "画框装裱", "画框制作", "picture framing", "画框工艺", "picture frame", "装裱艺术", "framing art", "画框设计", "frame design", "文物修复", "artifact conservation"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与装裱问题）", "methodology（材料、工艺与设计）", "results（工艺参数与成品）", "discussion（艺术与文化意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例与文物）", "analysis（工艺与修复）", "results（成品与保护效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（装裱史与理论）", "evidence synthesis（工艺流派综述）", "future directions", "references"),
    },
    citation_style="APA 7（艺术学科常见）",
    reporting_standards={"material_info": "画框/衬纸/玻璃材料须报告", "preservation": "文物级装裱遵循 AIC 保护准则", "dimensions": "尺寸单位与精度须给出", "lighting": "悬挂光照条件须报告（lux、色温）", "documentation": "装裱前后影像记录须给出"},
    conventions=("画框尺寸以 mm 为单位（长×宽×深）", "衬纸留白宽度按黄金比例或 1:3 经验", "玻璃用防紫外 UV 玻璃须标注", "画框木材须注明树种与含水率", "装裱作品标注作者/年代/尺寸/材质"),
    key_venues=("FrameMaker", "Art Journal", "Journal of Museum Management and Curatorship", "Restaurator", "Studies in Conservation"),
    units_and_formulas_notes=("尺寸用 mm/cm", "光照用 lux（50-200 lux 建议）", "玻璃透光度 %（UV 玻璃阻挡 99% UV）", "公式用 amsmath；黄金比 1:1.618 须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp Pro", "CorelDRAW", "Adobe Illustrator", "Adobe Photoshop", "Adobe InDesign", "Adobe Lightroom", "Affinity Publisher", "Vectric Aspire", "Vectric VCarve Pro", "Fusion 360", "SolidWorks", "Rhinoceros 3D", "ArtCAM", "Mastercam", "BobCAD-CAM", "Avid CNC FrameMill", "Avid CNC CanvasTaut", "Sanderline Frame Moulder", "FrameCAD"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
