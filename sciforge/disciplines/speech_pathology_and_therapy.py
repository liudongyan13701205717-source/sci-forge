"""言语病理与治疗学科论文支持：言语-语言-吞咽障碍评估与干预体裁、APA 7 与 IRACoP 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="speech_pathology_and_therapy",
    aliases=(
        "speech_pathology_and_therapy",
        "言语病理与治疗",
        "Speech Pathology and Therapy",
        "言语治疗",
        "语言治疗",
        "言语康复",
        "speech therapy",
        "speech-language pathology",
        "SLP",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（PICO 问题与理论框架）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；言语病理期刊主流样式）",
    reporting_standards={
        "randomized_trial": "CONSORT（并遵守 IRACoP 言语-语言-吞咽领域报告建议）",
        "systematic_review": "PRISMA",
        "case_report": "CARE",
        "qualitative": "COREQ/SRQR",
        "speech_outcome": "IRACoP 结局措施建议",
    },
    conventions=(
        "言语/语言/吞咽障碍按 SLP 常用分类声明：发音、构音、运动言语、语言、认知-沟通、吞咽障碍等",
        "年龄用「实际年龄/发育年龄」并列（如 CA 6y2m / DA 3y8m），发育商标 DQ",
        "干预描述达可复现粒度：治疗师、频次、时长、靶刺激、反馈类型（如 PONS/CR-PID）",
        "信度报 IRR（组内相关）与 Cohen's κ；诊断标灵敏度/特异度与 Youden J 点",
        "伦理批准与监护人知情同意须说明，患者信息去标识化",
    ),
    key_venues=(
        "Journal of Speech, Language, and Hearing Research",
        "Clinical Linguistics & Phonetics",
        "International Journal of Speech-Language Pathology",
        "Prosthetics and Orthotics International",
        "American Journal of Speech-Language Pathology",
    ),
    units_and_formulas_notes=(
        "语速单位 syl/s（词/秒）或 words/min；流利度报 %IDM 与 %DL",
        "声带功能用 f0（Hz）与 jitter/shimmer（%）报告；单位与测量方法并列",
        "言语清晰度按 % CCV 或 % CPSD，参照语材料须完整给出",
        "吞咽障碍按 IDDSI 分级 0-7；Videofluoroscopy 时间-事件图须给采样率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Praat", "LENA 语言环境分析", "Goldwell Voice", "Kay Elemetrics VSA", "ARTICulate 语音学软件", "Wavesurfer 音频编辑", "Kay Elemetrics Speech Analyzer", "SOFA 音视频标注", "Kinect 运动捕捉", "Delsys EMG 表面肌电", "Teledyne Mantis X-ray", "SPSS", "R", "NVivo", "ATLAS.ti", "LaTeX", "EndNote", "Zotero", "Microsoft Excel", "Noldus Observer 视频标注"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
