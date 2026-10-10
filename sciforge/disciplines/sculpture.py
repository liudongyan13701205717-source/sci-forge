"""雕塑学科论文支持：雕塑艺术/造型艺术/空间造型体裁与艺术研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sculpture",
    aliases=("sculpture", "雕塑", "雕塑艺术", "造型艺术", "sculpture art", "造型设计", "空间造型", "雕刻艺术"),
    paper_types={
        "research": ("abstract", "introduction（艺术问题与研究动机）", "methodology（创作或分析方法）", "results（作品效果）", "discussion（艺术讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品案例）", "analysis（形式与观念分析）", "results（阐释结果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（雕塑理论综述）", "evidence synthesis（风格演变）", "future directions", "references"),
    },
    citation_style="Chicago 风格（艺术史研究常用芝加哥引用）",
    reporting_standards={"case_study": "案例研究遵循 COREQ 规范", "conservation": "保护修复遵循 ISO 11790 规范", "interview": "访谈遵循 SRQR 规范"},
    conventions=("材料须给出规格与来源", "尺寸须给出 cm 或 m", "创作过程须配图", "艺术作品引用须注明来源与作者", "风格术语须统一（巴洛克/现代/当代）"),
    key_venues=("Art Journal", "October", "Critical Inquiry", "Journal of Aesthetics and Art Criticism", "Art Bulletin", "Apollo Magazine"),
    units_and_formulas_notes=("尺寸以 cm 记", "重量以 kg 记", "年代以年或世纪记", "比例以无量纲记"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe Premiere Pro", "Figma", "Blender", "ZBrush", "Mudbox", "3ds Max", "Maya", "Cinema 4D", "Rhino 3D", "SolidWorks", "Fusion 360", "MATLAB", "3D Scanner (Artec)", "3D Printer (Formlabs)", "Stone Carving Tools", "Bronze Casting Kit", "Sculpting Software (Geomagic)", "PhotoStudio Pro"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
