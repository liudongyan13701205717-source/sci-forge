"""法医学学科论文支持：法医病理、法医物证、法医毒理、法医人类学与法庭科学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forensic_science",
    aliases=("forensic_science", "forensic science", "法医学", "法庭科学", "法医病理", "法医毒理", "法医物证", "物证检验"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "dna_analysis": "DNA 分析须遵循 ISO 17025 认证规范",
        "fingerprint": "指纹分析须遵循 ACE-V 验证方法",
        "ballistics": "弹道分析须遵循物证鉴定技术标准",
        "toxicology": "毒物检测须遵循标准化分析流程"
    },
    conventions=(
        "法医学名称须用标准化术语",
        "实验动物须标注品系与来源",
        "数据须报告检测限（LOD）与定量限（LOQ）",
        "不确定度须遵循 GUM 规范",
        "照片须标注方位与比例尺"
    ),
    key_venues=(
        "Journal of Forensic Sciences",
        "Forensic Science International",
        "Journal of Forensic Identification",
        "International Journal of Legal Medicine",
        "Forensic Biology"
    ),
    units_and_formulas_notes=(
        "浓度用 ng/mL 或 mg/L",
        "质量用 g 或 mg",
        "体积用 mL 或 L",
        "温度用 °C",
        "波长用 nm"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PCR thermocycler", "DNA sequencer", "CE-SDS system", "GC-MS system", "LC-MS/MS system", "ToF-MS system", "FTIR spectrometer", "SEM-EDS system", "AFM system", "UV-Vis spectrophotometer", "Latent fingerprint system", "ACE-V system", "Toolmark comparison system", "Ballistic comparison system", "Handwriting analysis system", "Digital evidence recovery system", "Forensic database", "Crime scene kit", "Autopsy suite", "Toxicology analyzer"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
