"""神经病学学科论文支持：神经临床/基础体裁、AAN/Neurology 引用样式与神经学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="neurology",
    aliases=("neurology", "神经病学", "神经内科", "临床神经科学",
             "clinical neuroscience", "神经科学临床"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与神经问题）",
            "methods（研究设计与人群）",
            "results（量表与影像数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（主要终点与安全性）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按疾病/机制综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="AAN/Neurology 样式（作者-年份；Neurology 遵循 AAN 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "神经量表（NIHSS、MMSE、mRS 等）首次出现给出全称与评分范围",
        "影像学（MRI/CT）参数与序列须报告",
        "药物剂量与给药途径须完整报告",
        "疾病诊断标准（如 McDonald、国际标准）须注明版本",
        "电生理参数（EEG/EMG）缩写首次出现给出全称",
    ),
    key_venues=(
        "Neurology",
        "Annals of Neurology",
        "Brain",
        "The Lancet Neurology",
        "Journal of Neuroscience",
        "Stroke",
    ),
    units_and_formulas_notes=(
        "时间用 ms/s/min；频率用 Hz",
        "公式用 amsmath；量表评分与转换公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存/复发分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("脑电图仪", "事件相关电位（ERP）系统", "肌电图与神经传导检测仪", "头颅 MRI 扫描仪", "R", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "GEO"),
)