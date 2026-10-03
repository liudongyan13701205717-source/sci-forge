"""和平与冲突研究学科论文支持：冲突/和平/调解体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="peace_conflict_studies",
    aliases=("peace_conflict_studies", "和平与冲突研究", "和平研究", "冲突研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "hypotheses（假设）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例选择）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "conflict context（冲突背景）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Conflict Resolution 遵循 SAGE/APA 规范）",
    reporting_standards={
        "quantitative": "定量研究遵循冲突数据报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "冲突数据来源须注明",
        "案例选择标准须说明",
        "理论框架与假设须明确",
        "伦理与安全须交代",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "Journal of Conflict Resolution",
        "Journal of Peace Research",
        "Conflict Management and Peace Science",
        "International Peacekeeping",
        "Peace & Change",
        "Journal of Peace Education",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "冲突事件用频数与基数",
        "回归系数给出标准误与显著性",
        "样本量须报告",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("NVivo（质性与访谈编码）", "Stata（事件数据与生存分析）", "R（统计与可视化）", "Python（Pandas 冲突事件数据处理）",
           "SPSS"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)