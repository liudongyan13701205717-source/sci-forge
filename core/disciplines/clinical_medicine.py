"""临床医学学科论文支持：临床研究/病例报告/系统综述体裁、AMA 引用样式与临床报告记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clinical_medicine",
    aliases=("clinical_medicine", "临床医学", "临床", "内科", "外科",
             "clinical medicine", "内科学", "外科学", "妇产科学"),
    paper_types={
        "research": (
            "abstract（结构化摘要：目的/方法/结果/结论）",
            "introduction（临床问题与证据缺口）",
            "methods（设计、对象、干预、结局指标、统计）",
            "results（主要结局与亚组）",
            "discussion（临床意义、局限）",
            "conclusion",
            "references",
        ),
        "case_report": (
            "case presentation（病史、查体、辅助检查、诊疗经过）",
            "discussion（文献对照）",
            "conclusion",
            "references",
        ),
        "systematic_review": (
            "abstract",
            "introduction（PICO 问题）",
            "methods（检索策略、纳入排除、质量评价）",
            "results（筛选流程、证据汇总表）",
            "discussion（证据强度与临床应用）",
            "references",
        ),
    },
    citation_style="AMA 样式（数字编号，参考文献不超过 30 条为宜，期刊缩略名依 PubMed）",
    reporting_standards={
        "randomized_trial": "随机对照试验遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 清单",
        "diagnostic_test": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "摘要采用结构化四段式：目的、方法、结果、结论",
        "结果必须同时报告数值与 95% 置信区间，注明检验水准 α=0.05",
        "干预措施、疗程与结局指标在 methods 中预先定义，不得事后更换",
        "利益冲突、基金资助与作者贡献须按 ICMJE 标准披露",
        "缩写词首次出现处给出全称；剂量与单位遵循 SI 单位",
    ),
    key_venues=(
        "The New England Journal of Medicine",
        "The Lancet",
        "JAMA",
        "BMJ",
        "Annals of Internal Medicine",
        "Circulation",
        "The Journal of Bone and Joint Surgery",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/kg 并注明给药途径与频率",
        "生存分析用 Kaplan-Meier 曲线与 Log-rank 检验；Cox 模型报告 HR 与 95% CI",
        "诊断试验报告敏感度、特异度、PPV/NPV 与似然比",
        "数值结果报告均值 ± SD（正态）或中位数（IQR）（偏态）",
        "公式用 amsmath；统计检验量须注明来源（如 χ²、F、t）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic", "Cerner (Oracle Health)", "REDCap", "SPSS", "SAS", "R", "Python (pandas)", "Stata", "UpToDate", "DxPath", "SPECTRA", "LabKey", "OpenMRS", "Power BI", "REView", "GraphPad Prism", "Meta-Disc", "OpenCEX", "EndNote", "Zotero"),
    category="医学",
    databases=("PubMed", "Cochrane Library", "OpenAlex", "Crossref", "Medline / PubMed"),
)
