"""工商管理学科论文支持：企业战略/组织行为/HR/市场营销体裁、APA 引用样式与统计记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_administration",
    aliases=(
        "business_administration",
        "工商管理",
        "工商管理学",
        "企业管理",
        "商业管理",
        "Business Administration",
        "Management",
        "Business Management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "literature review（文献综述）",
            "hypotheses（假设）",
            "research design（研究设计）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusion（结论与贡献）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "research background（案例背景）",
            "research design",
            "findings（案例分析）",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework",
            "main arguments",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "archival": "档案/企业数据研究须说明数据源、样本期与筛选规则",
        "survey": "调查须报告样本量、抽样方法与回复率",
        "experimental": "实验研究须报告随机化、盲法与效应量",
        "case_study": "案例研究须说明资料来源、三角验证与理论化路径",
    },
    conventions=(
        "引言须清晰陈述研究问题、贡献与假设",
        "理论建构须区分先验假设与后验解释",
        "变量须给出操作化定义与度量口径",
        "实证结果须报告效应量、置信区间与稳健性检验",
        "案例研究须说明资料来源与三角验证路径",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Administrative Science Quarterly",
        "Strategic Management Journal",
        "Journal of Management Studies",
        "Management Science",
        "Organization Science",
        "Harvard Business Review",
        "Journal of Management & Organization",
        "Academy of Management Learning & Education",
    ),
    units_and_formulas_notes=(
        "金额以统一币种报告并注明年份",
        "统计量给出 M/SD/SE/CI",
        "回归系数给出标准误与显著性",
        "样本量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP S/4HANA", "Oracle E-Business Suite", "用友 U8+", "金蝶 EAS", "Microsoft Dynamics 365", "Salesforce", "HubSpot", "SPSS", "Stata", "R", "Python（pandas/NumPy）", "Microsoft Excel", "Tableau", "Microsoft Power BI", "NVivo", "Minitab", "JMP", "Qualtrics", "SurveyMonkey", "Google Analytics 4", "Microsoft Project", "Jira", "Notion", "Slack"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar", "JSTOR"),
)
