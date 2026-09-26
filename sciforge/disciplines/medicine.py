"""医学学科论文支持：EQUATOR 标准按研究设计路由与 Vancouver 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medicine",
    aliases=("medicine", "medical", "医学", "临床", "clinical", "患者", "patient",
             "诊疗", "therapy", "药物", "drug", "流行病学", "epidemiology"),
    paper_types={
        "rct": (
            "structured abstract",
            "introduction（研究背景与假设）",
            "methods（设计、入排标准、随机化、盲法、结局指标）",
            "results（流程图、基线表、主/次要结局）",
            "discussion（解释、局限与外推性）",
            "references",
        ),
        "systematic_review": (
            "structured abstract",
            "introduction",
            "methods（检索策略、纳排、偏倚评估、PRISMA 流程）",
            "results（森林图、异质性、偏倚风险）",
            "discussion（证据质量与临床意义）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case presentation（主诉、病史、检查、诊疗经过）",
            "discussion（鉴别诊断与文献对照）",
            "patient perspective（患者视角，CARE 要求）",
            "references",
        ),
        "diagnostic_accuracy": (
            "abstract",
            "introduction",
            "methods（参考标准、样本量、盲法、STARD 流程图）",
            "results（敏感性/特异性、ROC、似然比）",
            "discussion",
            "references",
        ),
        "prediction_model": (
            "abstract",
            "introduction",
            "methods（数据来源、候选变量、建模与验证策略）",
            "results（性能：C 统计量、校准曲线、净重分类改善）",
            "discussion（外部验证与临床使用条件）",
            "references",
        ),
    },
    citation_style="Vancouver（AMA 上标编号，按引用顺序）",
    reporting_standards={
        "case_report": "CARE",
        "diagnostic_accuracy": "STARD",
        "prediction_model": "TRIPOD+AI",
        "rct": "CONSORT",
        "systematic_review": "PRISMA",
    },
    conventions=(
        "伦理批准号与知情同意声明必须给出（含豁免说明）",
        "患者隐私：影像/病例细节去标识化，按期刊政策可另行取得同意",
        "药物用通用名（INN），首次出现可附商品名；剂量给 mg/kg/d 与给药途径",
        "主要结局须在方法中预先定义；P 值两位小数，p<0.001 表述为 p<0.001",
        "术语与诊断编码随 ICD/SNOMED CT，检验名称随 LOINC",
    ),
    key_venues=(
        "New England Journal of Medicine",
        "The Lancet",
        "JAMA",
        "BMJ",
        "Nature Medicine",
    ),
    units_and_formulas_notes=(
        "实验室指标优先 SI 单位，惯例单位可并列（如血糖 mmol/L 与 mg/dL）",
        "效应量给点估计与 95% 置信区间：RR/OR/HR、SMD",
        "诊断指标报敏感度/特异度时给出 95% CI 与患病率",
        "样本量计算给出检验效能、α 与最小临床重要差异（MCID）",
        "生存分析注明随访时长、删失规则与比例风险检验",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("SPSS", "R", "GraphPad Prism", "EndNote"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
