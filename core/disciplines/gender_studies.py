"""性别研究学科论文支持：性别/女性主义/交叉性体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gender_studies",
    aliases=("gender_studies", "性别研究", "女性研究", "女性主义研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "methods（方法）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "qualitative_study": (
            "abstract",
            "introduction",
            "participants（参与者）",
            "data collection（数据收集）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "theoretical_paper": (
            "abstract",
            "introduction",
            "conceptual framework（概念框架）",
            "argument（论证）",
            "implications（启示）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Gender & Society 遵循 APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "discourse": "话语分析遵循话语分析报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与立场须明确",
        "样本与招募须交代",
        "伦理与知情同意须报告",
        "交叉性视角须考虑",
        "局限与反思性须讨论",
    ),
    key_venues=(
        "Gender & Society",
        "Signs",
        "Feminist Studies",
        "Gender, Work & Organization",
        "Journal of Gender Studies",
        "Women's Studies International Forum",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "频数与百分比给出基数",
        "样本量须报告",
        "引文给出页码",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("NVivo（质性编码）", "R（统计与可视化）", "SPSS", "Python（Pandas 文本分析）", "MAXQDA"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)