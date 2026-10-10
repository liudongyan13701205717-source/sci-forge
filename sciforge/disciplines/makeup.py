"""化妆学科论文支持：彩妆技法、色彩与数字妆容创作研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="makeup",
    aliases=(
        "makeup",
        "化妆",
        "彩妆",
        "美妆",
        "化妆艺术",
        "Cosmetic Art",
        "Makeup Artistry",
        "彩妆技法",
        "数字妆容",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
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
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（艺术学通用）",
    reporting_standards={
        "art_practice": "艺术创作研究遵循艺术研究实践报告规范",
        "user_study": "用户研究遵循 UX 报告规范",
        "ethnography": "民族志研究遵循 COREQ 规范",
    },
    conventions=(
        "妆容作品须附创作说明与色彩配方",
        "妆容评价须附摄影参数（光源、色温、白平衡）",
        "数字妆容须标注建模软件与渲染管线",
        "色卡须使用标准光源（D50/D65）测量",
        "妆容作品须标注模特或志愿者知情同意",
    ),
    key_venues=(
        "Makeup Art Magazine",
        "Journal of Cosmetic Science",
        "Makeup Reference & Techniques",
        "Makeup Artist Magazine",
        "Cosmetic Dermatology",
        "Makeup International",
    ),
    units_and_formulas_notes=(
        "色值以 CIE L*a*b* 或 Pantone 报告",
        "光源标注色温 K 值（如 5500K）",
        "摄影参数标注光圈、快门、ISO",
        "化妆品成分以 INCI 名称标注",
        "妆容时长以分钟/小时报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe Lightroom", "Procreate", "Clip Studio Paint", "Corel Painter", "Wacom Cintiq Pro 24", "Wacom Intuos Pro", "Huion Kamvas Pro 22", "Xencelabs Pen Tablet", "GIMP", "Krita", "Blender", "ZBrush", "SketchBook", "Canon EOS R5", "Sony A7R V", "Nikon Z9", "Canon Speedlite 600EX-RT", "X-Rite Calibrite DisplayIL"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
