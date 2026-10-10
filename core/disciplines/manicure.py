"""美甲学科论文支持：指甲美学、光疗胶工艺与数字美甲设计研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="manicure",
    aliases=(
        "manicure",
        "美甲",
        "指甲艺术",
        "光疗美甲",
        "Nail Art",
        "Nail Care",
        "美甲艺术",
        "手工美甲",
        "假指甲",
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
    citation_style="APA 7 样式（艺术学与化妆品科学通用）",
    reporting_standards={
        "art_practice": "艺术创作研究遵循艺术研究实践报告规范",
        "user_study": "用户研究遵循 UX 报告规范",
        "cosmetic_safety": "化妆品安全性遵循 ISO 10993 与 IEC 60335 规范",
    },
    conventions=(
        "美甲作品须附作品照片与创作说明",
        "材料成分须以 INCI 名称标注",
        "UV/LED 光疗灯须报告功率与照射时间",
        "色值以 CIE L*a*b* 或 Pantone 报告",
        "作品摄影须使用标准光源（5500K D65）",
    ),
    key_venues=(
        "Journal of Cosmetic Science",
        "Makeup Art International",
        "Nail Magazine",
        "International Journal of Cosmetic Science",
        "Nail Art Magazine",
        "Makeup International",
    ),
    units_and_formulas_notes=(
        "色值以 CIE L*a*b* 或 Pantone 报告",
        "光源标注色温 K 值",
        "光疗灯功率以 W 报告并标注 UV/LED",
        "照射时间以秒报告",
        "成分浓度以 wt% 或 mg/g 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SunEater UV/LED Lamp 48W", "Meow UV/LED Lamp", "Zoya UV/LED Lamp", "Modelones UV/LED Lamp", "e-file 电动打磨机", "Nail Tips（甲片）", "Acrylic Powder（甲粉）", "OPI Nail Polish", "CND Shellac", "Essie Base Coat", "OPI Top Coat", "Nail Art Brush", "Stamping Plate", "Stamping Gel", "Nail Stickers", "Nail Art Liquid", "Cuticle Scissors", "Cuticle Pusher", "Nail File", "Disinfectant Wipes"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
