"""法医学科论文支持：法医病理、法医物证、法医毒理、法医人类学与物证技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forensic_medicine",
    aliases=("forensic_medicine", "forensic medicine", "法医学", "法医病理", "法医人类学", "法医毒理学", "物证技术学", "司法鉴定"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（作者-年份或顺序编号）",
    reporting_standards={
        "autopsy": "尸检须遵循标准法医学尸检报告指南",
        "toxicology": "法医毒理学须遵循标准化分析流程",
        "dna": "DNA 分析须遵循 ISO 17025 认证规范",
        "ballistics": "弹道分析须遵循物证鉴定技术标准",
        "identification": "个体识别须遵循法庭科学命名规范"
    },
    conventions=(
        "法医学名称须用标准化术语",
        "尸检照片须标注方位与比例尺",
        "实验动物须标注品系与来源",
        "数据须报告检测限（LOD）与定量限（LOQ）",
        "不确定度须遵循 GUM 规范"
    ),
    key_venues=(
        "Journal of Forensic Sciences",
        "Forensic Science International",
        "Journal of Forensic Medicine",
        "International Journal of Legal Medicine",
        "Journal of Forensic Odontology and Dentistry"
    ),
    units_and_formulas_notes=(
        "浓度用 ng/mL 或 mg/L",
        "质量用 g 或 mg",
        "体积用 mL 或 L",
        "温度用 °C 或 K",
        "波长用 nm"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DNA sequencer", "PCR amplifier", "GC-MS", "LC-MS/MS", "ToF-MS", "AFM", "SEM", "FTIR", "UV-Vis spectrophotometer", "NMR spectrometer", "Ballistic comparator", "Toolmark comparison system", "Latent fingerprint system", "Handwriting analysis software", "Digital evidence recovery tool", "Forensic database", "Autopsy suite", "Forensic anthropology kit", "Toxicology analyzer", "Crime scene kit"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
