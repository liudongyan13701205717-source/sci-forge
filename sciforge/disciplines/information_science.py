"""信息科学学科论文支持：信息检索/系统/行为体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_science",
    aliases=(
        "information_science",
        "信息科学",
        "情报学",
        "信息管理",
        "信息检索",
        "information science",
        "information retrieval",
        "information systems",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（JASIST 遵循 APA 规范）",
    reporting_standards={
        "systematic_review": "系统综述须遵循 PRISMA 声明",
        "user_study": "用户研究须遵循用户研究报告规范",
        "survey": "调查须遵循 AAPOR 报告规范",
        "qualitative": "质性研究须遵循 COREQ/SRQR 报告规范",
        "system_evaluation": "系统评估须报告 P/R/F1/nDCG 与基线",
    },
    conventions=(
        "评测数据集与指标须说明来源与规模",
        "基线方法须报告版本与参数",
        "用户样本与招募须交代抽样与响应率",
        "统计检验须说明方法并报告效应量",
        "可复现性配置须附代码与参数清单",
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
        "评测指标用 P/R/F1、nDCG、MAP，须注明 cutoff",
        "统计量给出 M/SD/SE/95% CI",
        "显著性用 p 值与效应量（Cohen d、η²）",
        "样本量须报告实际与最小可检测差异",
        "时间须用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Elasticsearch（信息检索系统）", "Lucene（Java 检索库）", "Python（scikit-learn/rank_bm25 检索评测）", "R（统计与文本挖掘）", "SPSS", "NVivo（用户行为质性分析）", "Atlas.ti", "Stata（面板数据）", "Mplus（结构方程模型）", "Manning/RankLib（信息检索工具）", "TREC 评测框架", "COCOAL/MS MARCO 基准", "OpenSearch", "Solr", "PostgreSQL（全文检索）", "Milvus（向量检索）", "FAISS（相似性检索）", "Jupyter Notebook（可复现性）", "Tableau（可视化）", "Docker（可复现部署）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
