"""听觉植入学 (Auditory Prosthetics) 学科论文支持：助听器/耳蜗植入体/人工听觉。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="auditory_prosthetics",
    aliases=(
        "Auditory prosthetics", "听觉植入", "听觉假体",
        "cochlear implant", "耳蜗植入", "auditory implant",
        "hearing aids", "助听器", "assistive listening devices",
        "ALD", "听觉假体与助听技术", "electroacoustic prosthesis",
        "听觉电生理", "auditory neuroscience prosthetics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "device_study": (
            "abstract",
            "device specification",
            "fitting parameters",
            "outcome measures",
            "discussion",
        ),
        "review": (
            "abstract",
            "technological evolution",
            "current state",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（医学与工程）",
    reporting_standards={
        "device_id": "设备型号、软件版本、通道数、频率范围须完整披露",
        "clinical_outcomes": "言语识别、噪声中理解、音质评分须报告",
        "fitting_protocol": "MAP/PowerFit/Dream/Maxima 等编程策略须声明",
        "surgery": "手术入路与电极植入深度须报告（如涉及）",
        "ethics": "遵循 Helsinki 声明与伦理委员会批准",
    },
    conventions=(
        "助听设备按助听/耳蜗植入/中耳植入/听骨链植入分类明确",
        "频率映射采用 ISO/ANSI 标准（0.25-8 kHz）",
        "听力级 dB HL；刺激强度用 level 或 µA（电刺激）",
        "编程参数（ECIR/HI/L55/L90 等）须用厂商标准命名",
        "言语测听结果报告 PTA、Cochlear Composite Score (CCS)",
        "统计检验：配对 t 检验、Wilcoxon 符号秩、效应量",
    ),
    key_venues=(
        "Ear and Hearing",
        "Journal of the American Academy of Audiology",
        "Trends in Amplification",
        "Clinical & Experimental Otology",
        "Cochlear Implants International",
        "International Journal of Pediatric Otorhinolaryngology",
        "Otol Neurotol",
        "Laryngoscope",
        "Hearing Research",
        "Hearing, Balance & Communication",
        "Ear & Hearing",
    ),
    units_and_formulas_notes=(
        "频率 Hz；刺激强度 µA 或 dB HL",
        "言语识别率 %；噪声中识别 SNR",
        "编程通道数：12/16/22/24 通道",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cochlear Nucleus", "Cochlear Baha", "Advanced Bionics ReSound", "MED-EL SONNET", "MED-EL VIVID", "MED-EL CLARET", "MED-EL SOUNIVERA", "Oticon Opus", "Oticon Xceed", "Oticon Intent", "ReSound Nexia", "ReSound Omni", "Signia Pure", "Signia Marvel", "Signia Comet", "Phonak Audéo", "Phonak Marvel", "Starkey Genesis", "Starkey Evolv AI", "GSI", "Interacoustic", "Otodynamics TympStar", "SoundField", "SoundSweeper", "LingFess", "Speechmap", "AUDIX", "PsychoPy", "SPSS"),
    category="医学",
    databases=("PubMed", "PMC", "Cochrane", "OpenAlex", "Crossref", "CNKI"),
)
