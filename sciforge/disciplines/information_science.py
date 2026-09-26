"""信息科学学科论文支持：信息检索/系统/行为体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_science",
    aliases=("information_science", "信息科学", "情报学", "信息管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "system_design": (
            "abstract",
            "introduction",
            "system architecture（系统架构）",
            "implementation（实现）",
            "evaluation（评估）",
            "discussion（讨论）",
            "references",
        ),
        "user_study": (
            "abstract",
            "introduction",
            "participants（参与者）",
            "tasks（任务）",
            "measures（测量）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；JASIST 遵循 APA 规范）",
    reporting_standards={
        "evaluation": "系统评估遵循信息检索评测报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "user_study": "用户研究遵循用户研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "评测数据集与指标须说明",
        "基线方法须报告",
        "用户样本与招募须交代",
        "统计检验须说明",
        "可复现性配置须提供",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Information Processing & Management",
        "Journal of Information Science",
        "Information Research",
        "Journal of Documentation",
        "Scientometrics",
    ),
    units_and_formulas_notes=(
        "评测指标用 P/R/F1、nDCG、MAP",
        "统计量给出 M/SD/SE/CI",
        "显著性用 p 值与效应量",
        "样本量须报告",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("Python（scikit-learn/rank_bm25 检索评测）", "Elasticsearch/Lucene（信息检索系统）", "R（统计与文本挖掘）",
           "SPSS", "NVivo（用户行为质性分析）"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)