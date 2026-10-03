"""发展研究学科论文支持：发展政策/评估/比较体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_studies",
    aliases=("development_studies", "发展研究", "发展经济学", "国际发展"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context（政策背景）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
        "impact_evaluation": (
            "abstract",
            "introduction",
            "intervention（干预）",
            "identification strategy（识别策略）",
            "data（数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；World Development 遵循 Elsevier 规范）",
    reporting_standards={
        "impact_evaluation": "影响评估遵循评估报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "发展指标与数据来源须说明",
        "识别策略须报告",
        "样本与时段须交代",
        "政策背景须交代",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "World Development",
        "Journal of Development Studies",
        "Journal of Development Economics",
        "Development and Change",
        "Journal of International Development",
        "Third World Quarterly",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "回归系数给出标准误与显著性",
        "GDP 等用统一币种并注明年份",
        "样本量须报告",
        "百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Stata（DID/RDD/IV 与面板）", "R（统计与可视化）", "GIS（QGIS/ArcGIS）", "Python（Pandas/Statsmodels）",
           "SPSS"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)