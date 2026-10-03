"""犯罪学论文支持：犯罪理论、犯罪测量、刑事司法政策、受害学、比较犯罪学。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="criminology",
    aliases=("criminology", "criminal_justice", "犯罪学", "刑事司法"),
    paper_types={
        "research": ("abstract", "introduction", "literature review", "methods", "results", "discussion", "conclusions", "references"),
        "policy": ("abstract", "introduction", "problem statement", "policy analysis", "implementation", "evaluation", "conclusions", "references"),
        "comparative": ("abstract", "introduction", "conceptual framework", "case selection", "analysis", "findings", "discussion", "conclusions", "references"),
    },
    citation_style="APA 7（括号），如 (Author, Year)",
    reporting_standards={
        "survey": "问卷调查须报告样本量、抽样方法、响应率、量表信效度",
        "administrative_data": "官方数据须报告来源机构、时间范围、定义口径（如犯罪分类标准）",
        "qualitative": "质性研究须报告访谈/观察时长、转录方法、编码过程与三角验证",
        "meta_analysis": "元分析须报告文献检索策略、纳入排除标准、效应量计算方法",
    },
    conventions=(
        "犯罪类别用标准分类（UCR/NIBRS/ICD-10-CM）",
        "人名/机构首次出现用全称，后可用缩写",
        "敏感数据须伦理审查声明；受害者信息须匿名化处理",
        "地图须含比例尺、指北针与数据来源",
        "统计须报告置信区间而非仅 p 值",
    ),
    key_venues=(
        "Criminology",
        "Journal of Quantitative Criminology",
        "Journal of Research in Crime and Delinquency",
        "Crime & Justice",
        "British Journal of Criminology",
    ),
    units_and_formulas_notes=(
        "犯罪率用 per 100,000 population",
        "再犯率用 %；监禁率用 per 100,000",
        "时间序列用月/年数据；横截面用城市/国家层级",
        "效应量用 Cohen's d / odds ratio",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
