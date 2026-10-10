"""宝石与首饰学科论文支持：工艺、材质鉴定与文化价值研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="lapidary_and_jewellery",
    aliases=(
        "lapidary_and_jewellery",
        "宝石与首饰",
        "Lapidary",
        "Jewellery Design",
        "珠宝首饰",
        "Gemology",
        "宝石学",
        "首饰设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与样品）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（工艺/材质分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（背景综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或宝石学专门体例（如 GIA 引注）",
    reporting_standards={
        "k1": "样品描述（产地、颜色、切工、克拉）与来源追溯",
        "k2": "鉴定方法（折射率/密度/光谱/红外）与仪器型号",
        "k3": "热处理与充填处理须披露",
    },
    conventions=(
        "矿物学名与宝石商品名区分",
        "颜色代码按标准色标（如 GRS/AGL）",
        "含杂质数据给百分比与检测限",
        "单位统一使用克拉、mm、nm",
        "参考文献体例全稿一致",
    ),
    key_venues=(
        "Gemology Journal",
        "National Gemmology Journal",
        "Journal of Gemmology",
        "宝石和宝石学杂志",
        "Modern Gemmology",
    ),
    units_and_formulas_notes=(
        "克拉（ct）= 0.2 g；折射率无量纲",
        "硬度采用 Mohs 1–10 或 Vickers HV",
        "光谱波长用 nm，密度用 g/cm³",
        "颜色用 CIE L*a*b* 或色标码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Gem refractometer", "Gem Loupe 10x", "GIA DiamondScope", "UV-Gem Spectrometer", "MinoScan", "X射线荧光光谱仪 (XRF)", "拉曼光谱仪", "傅里叶变换红外光谱仪 (FTIR)", "偏光镜", "二色镜", "比重瓶", "GIA D-Scale", "3D 扫描仪", "Rhino 3D", "SolidWorks", "Photoshop", "ZBrush", "SolidCAM", "AutoCAD", "OriginPro"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
