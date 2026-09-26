"""管理学学科论文支持：组织/战略/行为体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management",
    aliases=("management", "管理学", "组织管理", "战略管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory and hypotheses（理论与假设）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例选择）",
            "data collection（数据收集）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "introduction",
            "literature search（文献检索）",
            "inclusion criteria（纳入标准）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Academy of Management Journal 遵循 APA 规范）",
    reporting_standards={
        "survey": "调查研究遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "meta_analysis": "元分析遵循 PRISMA 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论与假设须明确",
        "构念测量须注明信效度",
        "共同方法偏差须讨论",
        "因果识别策略须报告",
        "样本与数据来源须说明",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Strategic Management Journal",
        "Journal of Management",
        "Organization Science",
        "Management Science",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "信度用 Cronbach's α",
        "回归系数给出标准误与显著性",
        "样本量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("SPSS", "Stata（多层次与面板模型）", "NVivo（案例质性编码）", "AMOS（结构方程模型）",
           "R（统计与可视化）"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)