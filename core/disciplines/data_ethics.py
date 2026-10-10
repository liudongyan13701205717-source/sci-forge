"""数据伦理学科论文支持：数据伦理/数据治理体裁、APA 引用样式与数据伦理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_ethics",
    aliases=(
        "data_ethics", "数据伦理", "数据治理", "数据隐私", "data ethics",
        "data privacy", "数据保护", "信息伦理", "information ethics",
        "AI ethics", "AI 伦理", "human rights and data",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与数据伦理问题）",
            "methods（研究设计与分析）",
            "results（伦理分析数据）",
            "discussion（伦理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（案例背景）",
            "analysis（伦理问题分析）",
            "conclusions（伦理启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Data Ethics 期刊遵循 APA 规范）",
    reporting_standards={
        "case_study": "案例研究遵循案例研究报告规范",
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "discourse": "话语分析遵循话语分析报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "伦理框架与原则（公平、透明等）须定义",
        "数据来源与处理流程须报告",
        "隐私与同意机制须明确",
        "利益相关者分析须完整",
        "伦理权衡与局限须讨论",
    ),
    key_venues=(
        "Ethics and Information Technology",
        "Data & Policy",
        "Big Data & Society",
        "Journal of Data Ethics",
        "AI and Ethics",
        "Philosophy & Technology",
        "Responsible Engineering",
    ),
    units_and_formulas_notes=(
        "比例用 %；指标无量纲",
        "公式用 amsmath；公平性指标计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "定性判断须给出证据来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("OpenDP (Open Differential Privacy)", "Microsoft Differential Privacy Library", "Google RAPPOR", "Google DP Library", "Apple Private Relay", "IBM Watson OpenScale", "Fairlearn", "IBM AI Fairness 360 (AIF360)", "Presidio (Microsoft)", "IBM Watson Discovery", "Amazon Macie", "Google Cloud DLP", "Symantec DLP", "Nightingale AI", "ARX (ARX.de)", "OpenAnonymizer", "ARX Anonymizer", "Microsoft Purview", "Palantir Foundry", "Databricks Unity Catalog", "HashiCorp Vault", "Snowflake Cortex Guard", "IBM Watson Governance", "AWS Lake Formation", "Caylent Data Fabric", "BigID", "Varonis Systems", "Nightfall AI", "Credo AI", "Evidently AI", "IBM Trustworthy ML"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
