"""原住民工艺论文支持：传统编织、陶器、雕刻、绘画、珠绣、乐器制作等技艺传承与研究。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="indigenous_crafts",
    aliases=("indigenous_crafts", "原住民工艺", "aboriginal_crafts", "traditional_craftsmanship", "native_art", "indigenous_textiles", "aboriginal_art", "craft_studies", "traditional_arts"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（人文学科风格）",
    reporting_standards={"fieldwork": "田野调查须报告知情同意、文化安全协议与研究者身份", "material_analysis": "材料学分析须报告取样位置、分析方法（XRF/FTIR/年代学）与不确定度", "community_recognition": "技艺归属须获得社区确认，尊重受控文化信息分级"},
    conventions=("引用原住民知识与技艺须遵循 OCAP 原则", "描述工艺时区分历史、现代与再生实践", "作品图片须注明来源社区、创作者（若允许）与许可", "术语尊重原住民自有分类而非殖民术语", "报告须包含致谢社区贡献者"),
    key_venues=("Journal of Material Culture", "Craft Research Journal", "Visual Anthropology", "Journal of Australian Indigenous Issues", "Museum Anthropology"),
    units_and_formulas_notes=("纤维与陶器尺寸以 mm/cm 记录", "材质分析标注检测方法（XRF/SEM/FTIR）与不确定度", "年代学结论给出置信区间", "工艺步骤按工序编号记录"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "Inkscape", "CorelDRAW", "SketchUp", "Blender", "Procreate", "GIMP", "Krita", "Lightroom", "Cura", "Tinkercad", "Rhino", "Fusion 360", "NVivo", "QGIS", "Zotero", "Audacity", "ELAN", "LaTeX"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
