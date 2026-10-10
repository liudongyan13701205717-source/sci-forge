"""牙科研究学科论文支持：口腔临床研究与循证医学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_studies",
    aliases=(
        "dental_studies", "牙科研究", "口腔研究",
        "dental research", "oral health research", "口腔健康研究",
        "evidence-based dentistry", "循证口腔医学",
        "dental epidemiology", "口腔流行病学",
    ),
    paper_types={
        "systematic_review": (
            "structured abstract",
            "introduction",
            "methods（PICO、检索策略、纳排标准、偏倚评估）",
            "results（森林图、GRADE 证据等级）",
            "discussion",
            "references",
        ),
        "original_research": (
            "structured abstract",
            "introduction",
            "methods",
            "results",
            "discussion",
            "references",
        ),
        "epidemiological_study": (
            "abstract",
            "introduction",
            "methods（人群、暴露、结局、混杂因素）",
            "results（患病率、风险因素）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "systematic_review": "PRISMA 声明",
        "RCT": "CONSORT 声明",
        "observational": "STROBE 声明",
        "epidemiological": "STROBE 声明",
        "diagnostic_accuracy": "STARD 声明",
    },
    conventions=(
        "研究注册须注明临床试验注册号（如 ClinicalTrials.gov）",
        "数据收集工具须注明信效度",
        "统计分析须注明软件版本与显著性标准",
        "偏倚评估使用标准工具（如 Cochrane RoB 2.0、QUADAS-2）",
        "利益冲突须声明",
    ),
    key_venues=(
        "Journal of Dental Research",
        "Journal of Dental Education",
        "Community Dentistry and Oral Epidemiology",
        "BMC Oral Health",
        "Journal of Public Health Dentistry",
    ),
    units_and_formulas_notes=(
        "患病率用 % 表示并注明分母",
        "风险因素用 OR/RR 表示并注明 95% CI",
        "Meta 分析用 I² 表示异质性",
        "证据等级用 GRADE 分级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("RevMan", "JBI Review Manager", "SPSS", "Stata", "R (RStudio)", "Metafor (R)", "OpenMeta[Analyst]", "Ovid", "EndNote", "Zotero", "PRISMA Flow Diagram", "Risk of Bias Tool", "GRADE Pro", "Microsoft Excel", "QUADAS-2 诊断试验偏倚评估", "Jadad 评分量表", "VOSviewer 文献计量工具", "CASP Checklists 循证评价工具", "Newcastle-Ottawa 评分量表", "RoB 2.0 偏倚风险评估工具"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Cochrane Library", "Embase", "Web of Science", "ProQuest"),
)
