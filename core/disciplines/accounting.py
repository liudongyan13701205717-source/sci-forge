"""会计学学科论文支持：财务/审计/披露体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="accounting",
    aliases=("accounting", "会计学", "财务会计", "审计学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "hypotheses（假设）",
            "research design（研究设计）",
            "data（数据）",
            "results（结果）",
            "conclusions（结论）",
            "references",
        ),
        "archival_study": (
            "abstract",
            "introduction",
            "sample（样本）",
            "variables（变量）",
            "model（模型）",
            "results（结果）",
            "robustness（稳健性）",
            "references",
        ),
        "analytical_study": (
            "abstract",
            "introduction",
            "model setup（模型设定）",
            "analysis（分析）",
            "propositions（命题）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；The Accounting Review 遵循 APA 规范）",
    reporting_standards={
        "archival": "档案研究遵循会计数据报告规范",
        "analytical": "分析研究遵循模型设定报告规范",
        "experimental": "实验研究遵循实验报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "样本筛选与数据来源须说明",
        "变量定义须给出",
        "模型设定须报告",
        "稳健性检验须提供",
        "内生性问题须讨论",
    ),
    key_venues=(
        "The Accounting Review",
        "Journal of Accounting Research",
        "Journal of Accounting and Economics",
        "Contemporary Accounting Research",
        "Accounting, Organizations and Society",
        "Review of Accounting Studies",
    ),
    units_and_formulas_notes=(
        "金额用统一币种并注明年份",
        "统计量给出 M/SD/SE/CI",
        "回归系数给出标准误与显著性",
        "样本量须报告",
        "t 值与 p 值须给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Stata（面板与固定效应）", "SPSS", "Excel（财务数据整理）", "Python（Pandas/Statsmodels）",
           "R（统计与可视化）"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)