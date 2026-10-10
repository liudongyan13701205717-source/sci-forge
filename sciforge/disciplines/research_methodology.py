"""研究方法学学科论文支持：定量定性混合方法与元分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="research_methodology",
    aliases=(
        "research_methodology",
        "研究方法学",
        "research methods",
        "方法论",
        "methodology",
        "方法学",
        "混合方法",
        "元分析",
        "系统综述",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题）",
            "methods（方法设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "systematic_review": (
            "abstract",
            "introduction",
            "search strategy（检索策略）",
            "inclusion criteria（纳入标准）",
            "risk of bias（偏倚评估）",
            "meta-analysis（元分析）",
            "discussion",
            "references",
        ),
        "mixed_methods": (
            "abstract",
            "introduction",
            "design rationale（设计理据）",
            "quantitative arm（定量臂）",
            "qualitative arm（定性臂）",
            "integration（整合）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "systematic_review": "PRISMA 2020 规范；检索词与筛选流程须报告",
        "meta_analysis": "MetaEpi 或 PRISMA; 异质性 I²、随机效应模型须注明",
        "qualitative": "COREQ 或 SRQR 规范；编码与信效度须报告",
        "quantitative": "CONSORT 或 RECORD；样本量计算与统计口径须报告",
    },
    conventions=(
        "样本量计算依检验效能与效应量给出；失访与缺失数据须说明",
        "混合方法遵循 SAR11 报告清单",
        "信度 Cronbach's α、内容效度与三角验证须报告",
        "统计显著性水平 α=0.05 或注明调整（Bonferroni、FDR）",
        "元分析森林图与漏斗图同时给出并讨论异质性来源",
    ),
    key_venues=(
        "Research Policy",
        "Studies in Higher Education",
        "Journal of Research on Educational Effectiveness",
        "International Journal of Research & Evaluation",
        "Evaluation and the Health Professions",
    ),
    units_and_formulas_notes=(
        "效应量以 Cohen's d、Hedges' g、OR、RR 报告并给 95% CI",
        "检验效能 β=0.2（power=0.8）为标准；多重比较调整须注明方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R with metafor and meta", "R with lavaan (SEM)", "Stata", "SPSS", "NVivo", "MAXQDA", "Atlas.ti", "JASP", "Jamovi", "OpenMx", "Hozo for median extraction", "RevMan (Cochrane)", "Rayyan Systematic Review", "Epistasis for evidence mapping", "PROSPERO Registry", "Open MEF", "Catalyst AI Meta Analysis", "QualCoder Open", "OpenRefine", "G*Power（功效分析）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "PubMed", "ERIC", "Cochrane CENTRAL"),
)
