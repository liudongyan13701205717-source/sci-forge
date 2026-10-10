"""听力学 (Audiology and Hearing Sciences) 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="audiologyhearing_sciences",
    aliases=(
        "Audiology/hearing sciences", "听力学", "听力科学",
        "audiology", "hearing science", "hearing sciences",
        "听觉科学", "听力康复", "hearing rehabilitation",
        "speech perception", "言语听觉", "听觉神经科学",
        "otology", "耳科学", "clinical audiology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_report": (
            "abstract",
            "case presentation",
            "diagnosis and treatment",
            "follow-up",
            "discussion",
        ),
        "review": (
            "abstract",
            "historical overview",
            "evidence synthesis",
            "gaps and future directions",
            "references",
        ),
    },
    citation_style="APA 7（听力学与医学惯例）",
    reporting_standards={
        "ethics": "涉及人受试者研究须伦理委员会批准，遵循 Helsinki 声明",
        "informed_consent": "受试者书面知情同意须获取",
        "acoustic_environment": "测试声场须符合 ANSI S3.1 / ISO 8253",
        "measurement_chain": "音频校准链（听力计→耳模→耦合腔）须声明",
        "stats": "报告均值±SD、95%CI；配对/独立 t 检验或 Mann-Whitney",
    },
    conventions=(
        "声压级用 dB SPL；听力级用 dB HL，转换参照 ISO 389",
        "听力图（audiogram）绘制遵循 ISO 226 惯例：横轴频率 log、纵轴 dB HL",
        "言语测听报告 WRS / SRT 值及最佳信噪比",
        "耳蜗电图（ECochG）、ABR 波形标记 I-V 峰，报告阈值与潜伏期",
        "统计显著性 *p<0.05, **p<0.01；效应量 Cohen's d",
    ),
    key_venues=(
        "Ear and Hearing",
        "Journal of the American Academy of Audiology",
        "Trends in Amplification",
        "Clinical Linguistics & Phonetics",
        "International Journal of Audiology",
        "Hearing Research",
        "Journal of the Acoustical Society of America (JASA)",
        "Frontiers in Audiology and Communication Sciences",
        "听力学言语障碍学杂志",
        "中国听力语言康复研究中心学报",
    ),
    units_and_formulas_notes=(
        "频率 Hz；声压级 dB SPL；听力级 dB HL",
        "时程 ms；阈值 dB HL",
        "信噪比 dB；言语清晰度百分比 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Madsen Vibest", "GSI 21", "GSI 61", "Interacoustic AC Atlas", "Otodynamics TympStar", "Otodynamics MIMO", "SoundField", "SoundSweeper", "PureTones Plus", "PureTones Professional", "Speechmap", "LingFess", "AUDIX", "Ibsen", "Cadwell", "Activa", "Natus Knowleda", "Rion OAE", "PsychoPy", "Python (NumPy/SciPy)", "MATLAB", "SPSS"),
    category="医学",
    databases=("PubMed", "PMC", "Cochrane", "CNKI", "OpenAlex", "Crossref"),
)
