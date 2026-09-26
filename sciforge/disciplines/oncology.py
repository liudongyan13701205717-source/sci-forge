"""肿瘤学学科论文支持：肿瘤临床/转化体裁、ASCO/JCO 引用样式与肿瘤学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oncology",
    aliases=("oncology", "肿瘤学", "癌症研究", "肿瘤内科", "肿瘤外科",
             "cancer research", "肿瘤"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与肿瘤问题）",
            "methods（研究设计与人群）",
            "results（疗效与生物标志物数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（入组、随机化与统计）",
            "results（ORR/PFS/OS 等终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "translational": (
            "abstract",
            "introduction",
            "results（分子/免疫学发现）",
            "discussion（转化意义）",
            "materials and methods",
            "references",
        ),
    },
    citation_style="ASCO/JCO 样式（作者-年份；JCO 遵循 ASCO 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "biomarker": "生物标志物研究遵循 REMARK 指南",
    },
    conventions=(
        "疗效终点（ORR/PFS/OS）首次出现给出定义与评估标准（RECIST 1.1 等）",
        "分期用 AJCC/TNM 系统并注明版本",
        "分子分型（如 MSI、TMB）须注明检测方法与阈值",
        "药物剂量方案（如 mFOLFOX6）须完整",
        "生存数据给出中位随访时间",
    ),
    key_venues=(
        "Journal of Clinical Oncology",
        "Cancer Cell",
        "Nature Cancer",
        "The Lancet Oncology",
        "Cancer Research",
        "Annals of Oncology",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/m² 或 mg/kg（须注明体表面积/体重依据）",
        "公式用 amsmath；ORR/PFS/OS 定义式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("SPSS", "R", "GraphPad Prism", "病理切片扫描仪", "免疫组化工作站", "流式细胞仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "GEO", "Expression Atlas", "Zenodo"),
)