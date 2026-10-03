"""流行病学学科论文支持：流行病学/公共卫生体裁、IEA/IJE 引用样式与流行病学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="epidemiology",
    aliases=("epidemiology", "流行病学", "疾病流行病学", "临床流行病学",
             "clinical epidemiology", "流行病"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与流行病学问题）",
            "methods（研究设计与人群）",
            "results（关联与效应估计）",
            "discussion（偏倚与因果解释）",
            "references",
        ),
        "cohort_study": (
            "abstract",
            "introduction",
            "methods（队列建立与随访）",
            "results（发病率与风险比）",
            "discussion（与既往研究对比）",
            "references",
        ),
        "systematic_review": (
            "abstract",
            "introduction",
            "methods（检索与纳入标准）",
            "results（meta 分析与异质性）",
            "discussion（证据等级与局限）",
            "references",
        ),
    },
    citation_style="IEA/IJE 样式（作者-年份；Int J Epidemiol 遵循 IEA 规范）",
    reporting_standards={
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "meta_analysis": "meta 分析遵循 PRISMA 声明",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
        "genetic_epidemiology": "遗传关联研究遵循 STREGA 指南",
    },
    conventions=(
        "研究设计（队列/病例对照/横断面）须明确",
        "效应量（RR/OR/HR）与 95% CI 须报告",
        "混杂与偏倚控制（匹配/校正）须说明",
        "人群来源与纳入排除标准须完整",
        "因果推断（Bradford Hill 等）讨论须谨慎",
    ),
    key_venues=(
        "International Journal of Epidemiology",
        "American Journal of Epidemiology",
        "Epidemiology",
        "European Journal of Epidemiology",
        "The Lancet",
        "BMJ",
    ),
    units_and_formulas_notes=(
        "发病率用 1/10 万人年；患病率用 %",
        "公式用 amsmath；RR/OR/HR 计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出效应量与 95% CI",
        "meta 分析给出 I² 与合并效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "报告"),
    tools=("R", "Python", "Stata", "SPSS", "Epi Info"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI", "Zenodo"),
)