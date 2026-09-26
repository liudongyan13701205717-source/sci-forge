"""自然语言处理学科论文支持：语言模型/文本分析体裁、ACL 引用样式与 NLP 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="natural_language_processing",
    aliases=("natural_language_processing", "自然语言处理", "NLP", "计算语言学",
             "文本挖掘"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "experiments（实验）",
            "conclusion（结论）",
            "references",
        ),
        "resource_paper": (
            "abstract",
            "introduction",
            "resource（资源构建）",
            "annotation（标注方案）",
            "evaluation（评估）",
            "availability（可用性）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACL 样式（作者-年份；ACL 系列会议遵循其规范）",
    reporting_standards={
        "experimental": "实验遵循 ACL 论文检查清单",
        "annotation": "标注研究遵循 ACL 标注指南",
        "human_eval": "人工评估遵循 ACL 人工评估规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循 ACL 可复现性清单",
    },
    conventions=(
        "数据集与语言须明确",
        "分词/预处理流程须说明",
        "评估指标（BLEU、ROUGE、F1 等）定义须一致",
        "模型规模与训练配置须报告",
        "人工评估须报告标注者与一致性",
    ),
    key_venues=(
        "ACL",
        "EMNLP",
        "NAACL",
        "Computational Linguistics",
        "Transactions of the Association for Computational Linguistics",
        "Journal of Artificial Intelligence Research",
    ),
    units_and_formulas_notes=(
        "概率用 p；困惑度用 PPL；温度用 τ",
        "公式用 amsmath；注意力与损失方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "参数量用 B（十亿）；词表用 V",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("HuggingFace Transformers", "spaCy", "LANGCHAIN", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "HuggingFace", "Zenodo"),
)