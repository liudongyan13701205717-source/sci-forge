"""神经病学学科论文支持：神经临床/基础体裁、AAN/Neurology 引用样式与神经学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="neurology",
    aliases=("neurology", "神经病学", "神经内科", "clinical neurology",
             "神经科", "neurologie", "神经系统疾病", "神经科临床", "clinical neuroscience"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与神经问题）", "methodology（研究设计与人群）", "results（量表与影像数据）", "discussion（机理与临床意义）", "references"),
        "clinical_trial": ("abstract", "introduction", "case description（研究设计与随机化）", "analysis（主要终点与安全性）", "results（与既往试验对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（疾病/机制综述）", "evidence synthesis（临床与基础证据综合）", "future directions", "references"),
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
    ),
    units_and_formulas_notes=(
        "时间用 ms/s/min；频率用 Hz；量表用原始评分",
        "公式用 amsmath；量表评分与转换公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "生存/复发分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MRI Scanner", "CT Scanner", "EEG System", "EMG System", "ERP System", "fMRI", "DTI", "PET", "SPECT", "MEG", "TMS", "tDCS", "DBS", "NIRS", "EIT", "Nerve Conduction Study", "Visual Evoked Potential", "Auditory Evoked Potential", "Somatosensory Evoked Potential", "Polysomnography"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
