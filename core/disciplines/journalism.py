"""新闻学学科论文支持：新闻生产/内容/受众体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="journalism",
    aliases=("journalism", "新闻学", "新闻研究", "新闻传播"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "content_analysis": (
            "abstract",
            "introduction",
            "sampling（抽样）",
            "coding scheme（编码方案）",
            "reliability（信度）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "ethnographic_study": (
            "abstract",
            "introduction",
            "fieldwork（田野）",
            "data（数据）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journalism & Mass Communication Quarterly 遵循 APA 规范）",
    reporting_standards={
        "content_analysis": "内容分析遵循编码信度报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethnography": "民族志研究遵循民族志报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "抽样框架与时段须说明",
        "编码者间信度须报告",
        "新闻伦理与知情同意须交代",
        "数据来源须注明",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "Journalism & Mass Communication Quarterly",
        "Journalism",
        "Digital Journalism",
        "Journalism Studies",
        "Newspaper Research Journal",
        "Journalism Practice",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "信度用 Cohen's κ 或 Krippendorff's α",
        "频数与百分比给出基数",
        "样本量须报告",
        "时间用统一时区与格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("新闻剪报与档案检索系统", "NVivo（内容编码）", "R（统计与文本挖掘）", "SPSS",
           "Python（Jieba/NLTK 文本处理）"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)