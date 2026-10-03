"""感染病学学科论文支持：感染临床/微生物体裁、IDSA/Clinical Infectious Diseases 引用样式与感染病学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="infectious_disease",
    aliases=("infectious_disease", "感染病学", "感染科", "传染病学",
             "infectious diseases", "感染性疾病"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与感染问题）",
            "methods（研究设计与人群）",
            "results（病原与疗效数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "outbreak_report": (
            "abstract",
            "introduction",
            "methods（病例定义与调查）",
            "results（流行病学曲线与传播链）",
            "discussion（控制措施与启示）",
            "references",
        ),
    },
    citation_style="IDSA/Clinical Infectious Diseases 样式（作者-年份；CID 遵循 IDSA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "outbreak": "暴发调查遵循 ORION 指南",
    },
    conventions=(
        "病原体命名用斜体（如 *Staphylococcus aureus*）",
        "药敏结果（MIC、折点）须注明标准（CLSI/EUCAST）",
        "抗菌药物剂量与疗程须完整报告",
        "流行病学参数（R₀、潜伏期）定义须明确",
        "检测方法（培养/PCR/血清学）与阈值须报告",
    ),
    key_venues=(
        "Clinical Infectious Diseases",
        "The Lancet Infectious Diseases",
        "Journal of Infectious Diseases",
        "Emerging Infectious Diseases",
        "Antimicrobial Agents and Chemotherapy",
        "Nature Reviews Microbiology",
    ),
    units_and_formulas_notes=(
        "MIC 用 mg/L；浓度用 CFU/mL",
        "公式用 amsmath；R₀ 与流行病学参数计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("PCR 仪", "病原培养设备", "流式细胞仪", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "bioRxiv", "Europe PMC", "CNKI"),
)