"""法医学技术学科论文支持：法医学分析方法、物证检验技术与司法鉴定技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forensic_medicine_technology",
    aliases=("forensic_medicine_technology", "法医学技术", "法医学检验", "法医学分析", "法医学分析技术", "物证技术", "法医毒物分析", "法医遗传学技术"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
        "methodology": ("abstract", "introduction", "method description（方法描述）", "validation（验证）", "results（结果）", "references")
    },
    citation_style="Vancouver（顺序编号式）",
    reporting_standards={
        "method_validation": "方法验证须遵循 CLSI EP23 指南",
        "quality_control": "质量控制须遵循 ISO 15189 规范",
        "uncertainty": "不确定度评估须遵循 GUM 规范",
        "traceability": "溯源性须遵循 ISO/IEC 17025 要求",
        "software_validation": "软件验证须遵循 FDA 21 CFR Part 11"
    },
    conventions=(
        "方法名称须用标准化术语",
        "仪器须标注型号与序列号",
        "试剂须标注批号与有效期",
        "实验条件须完整报告（温度、湿度、时间）",
        "数据须报告重复性与精密度"
    ),
    key_venues=(
        "Journal of Forensic Sciences",
        "Forensic Science International",
        "Journal of Analytical Toxicology",
        "International Journal of Forensic Medicine",
        "Journal of Forensic Identification",
        "Journal of Forensic Toxicology"
    ),
    units_and_formulas_notes=(
        "浓度用 ng/mL 或 mg/L",
        "吸光度用 AU（无单位）",
        "电泳迁移率用 μm²/(V·s)",
        "测序错误率用 %（误差率）",
        "不确定度用相对标准偏差（RSD, %）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Capillary electrophoresis system", "DNA sequencer (Illumina)", "Mass spectrometer (Orbitrap)", "GC-MS system", "LC-MS/MS system", "Real-time PCR system", "DNA fingerprinting kit", "Toxicology analyzer", "Fingerprint comparison system (ACE-V)", "Toolmark comparison microscope", "Stereomicroscope", "Forensic database", "Case management software", "Digital evidence system", "Latent print system (IAFIS)", "AFIS system", "STR typing kit", "Y-STR typing kit", "mtDNA sequencing kit", "Forensic anthropology software"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
