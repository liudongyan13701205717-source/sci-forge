"""市场营销学科论文支持：消费者/品牌/渠道体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marketing",
    aliases=("marketing", "市场营销", "营销学", "消费者行为"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "experimental_study": (
            "abstract",
            "introduction",
            "study 1（研究一）",
            "study 2（研究二）",
            "general discussion（总体讨论）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "field setting（现场设置）",
            "data（数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Marketing 遵循 APA 规范）",
    reporting_standards={
        "experimental": "实验研究遵循实验报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "field_study": "现场研究遵循现场实验报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "meta_analysis": "元分析遵循 PRISMA 声明",
    },
    conventions=(
        "理论与假设须明确",
        "刺激材料与操纵检验须报告",
        "构念测量须注明信效度",
        "样本与招募须说明",
        "效应量与显著性须报告",
    ),
    key_venues=(
        "Journal of Marketing",
        "Journal of Marketing Research",
        "Journal of Consumer Research",
        "Marketing Science",
        "Journal of the Academy of Marketing Science",
        "Journal of Consumer Psychology",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "信度用 Cronbach's α",
        "样本量须报告",
        "金额用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("SPSS", "R（统计与可视化）", "Python（scikit-learn/Pandas）", "Tableau（销售与漏斗可视化）",
           "AMOS（结构方程模型）"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)