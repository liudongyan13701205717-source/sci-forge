"""临床科学学科论文支持：临床转化研究体裁、ICMJE 引用样式与转化医学报告注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clinical_sciences",
    aliases=("clinical_sciences", "临床科学", "转化医学", "临床科研",
             "clinical science", "translational medicine", "临床基础研究",
             "精准医学"),
    paper_types={
        "research": (
            "abstract（结构化摘要）",
            "introduction（转化问题与临床相关性）",
            "materials and methods（设计、样本、干预、检测、统计）",
            "results",
            "discussion（转化意义与临床转化路径）",
            "limitations",
            "references",
        ),
        "protocol": (
            "background",
            "rationale",
            "methods（试验设计、入组、终点、伦理与数据管理）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main content",
            "translation path（从基础到临床的转化路径）",
            "outlook",
            "references",
        ),
    },
    citation_style="ICMJE / Vancouver 样式（数字编号；参考文献期刊用 PubMed 官方缩写）",
    reporting_standards={
        "randomized_trial": "遵循 CONSORT 声明",
        "observational": "遵循 STROBE 声明",
        "systematic_review": "遵循 PRISMA 声明",
        "diagnostic_test": "遵循 STARD 声明",
        "protocol": "临床试验方案遵循 SPIRIT 声明",
    },
    conventions=(
        "研究假设必须与临床终点或临床相关替代终点（surrogate endpoint）明确挂钩",
        "样本量计算与统计检验须在 methods 中给出，包含 α、power 与最小效应量",
        "数据收集与分析须说明盲法、中心实验室与质量控制措施",
        "利益冲突、伦理批件号与患者知情同意须在文中标注",
        "数值报告给出均值 ± SD 或中位数（IQR）；P 值使用小数点后两位或三位",
    ),
    key_venues=(
        "Clinical Medicine",
        "Clinical Pharmacology & Therapeutics",
        "American Journal of Clinical Research",
        "JAMA Internal Medicine",
        "Lancet Oncology",
        "European Heart Journal",
        "Clinical Pharmacokinetics & Pharmacodynamics",
    ),
    units_and_formulas_notes=(
        "剂量与浓度单位遵循 SI，注明给药途径与频率",
        "生存分析以 Kaplan-Meier 曲线、Log-rank 检验与 Cox 比例风险模型为主",
        "药物动力学参数（Cmax、AUC、t1/2、Cl/F）须报告",
        "统计推断结果给出效应量与 95% CI",
        "公式用 amsmath；统计学量的记号与符号须首次出现处定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("REDCap", "Vanderbilt eConsent", "SPSS", "SAS (Base/STAT/IML)", "R", "Stata", "Cochrane Risk of Bias (RoB 2.0)", "RevMan", "Meta-Disc", "OpenMRS", "LabKey", "Cytoscape", "PrismGraph (GraphPad Prism)", "PowerCalc", "MedDRA", "CTCAE v5.0", "VizR", "SPECTRA", "Epic", "DeepDive"),
    category="医学",
    databases=("PubMed", "Cochrane Library", "ClinicalTrials.gov", "OpenAlex", "Medline / PubMed"),
)
