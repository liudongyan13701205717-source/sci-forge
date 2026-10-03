"""放射学学科论文支持：影像诊断/介入体裁、RSNA/Radiology 引用样式与影像学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radiology",
    aliases=("radiology", "放射学", "医学影像学", "影像诊断", "介入放射学",
             "medical imaging", "影像科"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与影像问题）",
            "methods（成像方案与人群）",
            "results（影像特征与诊断数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "diagnostic_accuracy": (
            "abstract",
            "introduction",
            "methods（参考标准与阅片方案）",
            "results（灵敏度/特异度/AUC）",
            "discussion（与既往研究对比）",
            "references",
        ),
        "technical": (
            "abstract",
            "introduction",
            "methods（成像序列/参数）",
            "results（图像质量与定量数据）",
            "discussion（技术要点与局限）",
            "references",
        ),
    },
    citation_style="RSNA/Radiology 样式（作者-年份；Radiology 遵循 RSNA 规范）",
    reporting_standards={
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "radiomics": "影像组学研究遵循 IBSI 规范",
    },
    conventions=(
        "成像参数（序列、层厚、磁场强度）须完整报告",
        "阅片者数量与一致性（κ 值）须报告",
        "参考标准（病理/随访）须明确",
        "辐射剂量（CTDIvol、DLP）单位须规范",
        "病灶描述用标准术语（如 BI-RADS、LI-RADS）",
    ),
    key_venues=(
        "Radiology",
        "RadioGraphics",
        "European Radiology",
        "Journal of Nuclear Medicine",
        "American Journal of Roentgenology",
        "Investigative Radiology",
    ),
    units_and_formulas_notes=(
        "辐射剂量用 mGy（CTDIvol）与 mGy·cm（DLP）",
        "公式用 amsmath；AUC 与 κ 统计式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "诊断性能给出灵敏度/特异度与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("影像归档与传输系统（PACS）", "影像后处理工作站（ITK-SNAP）", "AI 影像分析平台", "CT 扫描仪", "MRI 扫描仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Zenodo"),
)