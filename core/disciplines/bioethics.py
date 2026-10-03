"""生命伦理学科论文支持：生命伦理/医学伦理体裁、APA 引用样式与生命伦理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bioethics",
    aliases=("bioethics", "生命伦理", "医学伦理", "生物伦理", "bioethics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与伦理问题）",
            "methods（研究设计与分析）",
            "results（伦理分析数据）",
            "discussion（伦理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（临床/研究案例）",
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
    citation_style="APA 样式（作者-年份；Bioethics 遵循 Wiley 规范）",
    reporting_standards={
        "case_study": "案例研究遵循案例研究报告规范",
        "empirical": "实证研究遵循 APA 报告规范",
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "伦理原则（自主、行善、公正等）须定义",
        "知情同意与隐私保护须说明",
        "临床与研究情境须交代",
        "文化与社会背景须考虑",
        "伦理权衡与局限须讨论",
    ),
    key_venues=(
        "Bioethics",
        "Journal of Medical Ethics",
        "Hastings Center Report",
        "American Journal of Bioethics",
        "Kennedy Institute of Ethics Journal",
        "Medicine, Health Care and Philosophy",
    ),
    units_and_formulas_notes=(
        "比例用 %；指标无量纲",
        "公式用 amsmath；伦理评估指标计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "定性判断须给出证据来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("伦理审查与 IRB 案例检索工具", "伦理决策树软件", "生命伦理专家访谈方法平台"),
    category="交叉学科",
    databases=("OpenAlex", "PubMed", "Crossref", "CNKI"),
)