"""信息学科论文支持：信息内容、传播机制与信息组织的理论研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information",
    aliases=(
        "information",
        "信息",
        "信息内容",
        "信息学",
        "信息传播研究",
        "information (wording and content)",
        "information content and messaging",
        "information studies",
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
    citation_style="APA 7 样式（信息/传播研究）",
    reporting_standards={
        "quantitative_study": "量化研究须报告样本、统计假设与效应量",
        "content_analysis": "内容分析须遵循 coding 规范并报告编码一致性",
        "qualitative_study": "质性研究须遵循 COREQ/SRQR 报告",
        "experimental_design": "实验设计须报告随机化与预测控制",
    },
    conventions=(
        "信息概念须区分 Shannon 信息熵与信息内容（语义）",
        "传播模型须注明框架（如 4C、议程设置）",
        "编码须注明信源与解码一致性（Cohen's κ）",
        "引用标准须注明版本与法域",
        "统计推断须报告 95% CI 与效应量",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Information Processing & Management",
        "Journal of Information Science",
        "New Media & Society",
        "信息工作与研究",
    ),
    units_and_formulas_notes=(
        "信息熵 H 用 bit 或 nats，须注明底数",
        "传播速度用 篇/月，须注明统计窗口",
        "编码一致性用 Cohen's κ 或 Krippendorff's α",
        "效应量（Cohen d、η²）须一并报告",
        "样本量须报告实际与最小可检测差异",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（统计建模）", "NVivo（质性分析）", "Atlas.ti（质性编码）", "Python（pandas 数据处理）", "Stata（面板数据）", "Mannu（媒体内容分析）", "Ivory（网络内容抓取）", "Tweepy（社交媒体 API）", "Jupyter Notebook（可复现性）", "MATLAB（信号与信息处理）", "Elasticsearch（信息检索）", "Rstudio", "QDA Miner（质性内容分析）", "Python（scikit-learn）", "SAS", "Lingua（语料库）", "Tableau（可视化）", "R Shiny（交互式分析）", "Cohen's Kappa 工具"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
