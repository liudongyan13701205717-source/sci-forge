"""耳鼻咽喉科学学科论文支持：耳鼻喉临床/听力学体裁、AAO-HNS 引用样式与耳鼻咽喉科记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="otolaryngology",
    aliases=("otolaryngology", "耳鼻咽喉科学", "耳鼻喉科", "头颈外科",
             "otorhinolaryngology", "head and neck surgery", "耳鼻咽喉头颈外科"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与耳鼻喉问题）",
            "methods（研究设计与人群）",
            "results（听力/嗓音与手术数据）",
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
        "case_series": (
            "abstract",
            "introduction",
            "case presentation（病例详述）",
            "discussion（鉴别诊断与治疗）",
            "references",
        ),
    },
    citation_style="AAO-HNS/Otolaryngology–Head and Neck Surgery 样式（作者-年份）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "听力参数（PTA、听力级 dB HL）单位须规范",
        "嗓音评估（GRBAS、VHI）首次出现给出全称",
        "肿瘤分期（TNM）须注明版本",
        "手术方式（内镜/开放）与范围须报告",
        "内镜/影像参数须完整报告",
    ),
    key_venues=(
        "Otolaryngology–Head and Neck Surgery",
        "The Laryngoscope",
        "JAMA Otolaryngology–Head & Neck Surgery",
        "Hearing Research",
        "Ear and Hearing",
        "International Journal of Pediatric Otorhinolaryngology",
    ),
    units_and_formulas_notes=(
        "听力用 dB HL；频率用 Hz；声压用 dB SPL",
        "公式用 amsmath；听力阈值与言语识别计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("纯音测听仪（听力计）", "电子喉镜（鼻咽喉镜）", "多导睡眠监测仪", "声导抗与耳蜗电图仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)