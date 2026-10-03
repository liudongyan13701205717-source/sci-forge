"""科学技术研究（STS）学科论文支持：科学知识/技术社会/创新体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="science_technology_studies",
    aliases=("science_technology_studies", "科学技术研究", "STS", "科技与社会"),
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
        "ethnographic_study": (
            "abstract",
            "introduction",
            "fieldwork（田野）",
            "data（数据）",
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
    citation_style="APA 样式（作者-年份；Science, Technology, & Human Values 遵循 SAGE/APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethnography": "民族志研究遵循民族志报告规范",
        "discourse": "话语分析遵循话语分析报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与立场须明确",
        "田野与数据收集须交代",
        "伦理与知情同意须报告",
        "反思性须讨论",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "Science, Technology, & Human Values",
        "Social Studies of Science",
        "Science & Technology Studies",
        "Minerva",
        "Research Policy",
        "Public Understanding of Science",
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
    tools=("NVivo（质性编码）", "R（计量分析与文献计量）", "Python（网络/文本分析）", "CORI",
           "ATLAS.ti（质性分析）"),
    category="交叉学科",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "arXiv"),
)