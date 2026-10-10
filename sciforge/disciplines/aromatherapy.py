"""芳香疗法学科论文支持：精油成分分析、气味识别、生理心理效应与循证评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aromatherapy",
    aliases=(
        "aromatherapy",
        "芳香疗法",
        "精油疗法",
        "essential oil therapy",
        "芳香学",
        "芳香治疗",
        "aroma therapy",
        "phitoaromatherapy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "clinical_trial": (
            "background",
            "methods（随机化/盲法/分组/剂量）",
            "results",
            "discussion",
            "limitations",
            "references",
        ),
        "analytical": (
            "abstract",
            "introduction",
            "materials and extraction",
            "analytical methods",
            "results",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver 或 APA 7（临床试验遵循 CONSORT）",
    reporting_standards={
        "analytical": "精油成分给分析方法（GC-MS/HS-GC/GC-O）、色谱柱与鉴定依据（谱图库）",
        "clinical": "随机对照试验遵循 CONSORT 声明；给注册号、随机化与盲法",
        "systematic_review": "系统综述遵循 PRISMA 与 Cochrane 手册",
        "safety": "毒性/皮肤刺激试验给剂量、动物种系与重复次数",
    },
    conventions=(
        "精油名称给拉丁学名与英文名，标注批次与提取方法",
        "浓度与剂量给体积分数或 mg/mL，注明稀释介质",
        "GC-MS 峰面积归一化后给相对含量 %",
        "临床结论须区分相关性与时机，禁止因果推论",
    ),
    key_venues=(
        "Journal of Essential Oil Research",
        "Journal of Essential Oil Bearing Plants",
        "Flavour and Fragrance Journal",
        "Molecules",
        "PLOS ONE",
        "Journal of Chromatography A",
        "Complementary Therapies in Medicine",
    ),
    units_and_formulas_notes=(
        "浓度 % 或 mg/mL；相对含量 %（峰面积归一化）",
        "剂量 mg/kg；嗅闻时间 min",
        "色谱保留时间 min；信号强度峰面积归一",
        "感官评分用 Likert 5 点量表；心率 bpm、血压 mmHg",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GC-MS", "HS-GC-MS", "GC-TOFMS", "GC-O", "Electronic Nose", "HS-SPME", "ChemStation", "Agilent OpenLAB", "Skyline", "Metabolite Workbench", "ChemDraw", "SPSS", "R", "Python", "Qualtrics", "NVivo", "Google Forms", "Excel", "HPLC", "UV-Vis Spectrophotometer"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "DOAJ"),
)
