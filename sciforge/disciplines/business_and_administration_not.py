"""商业与行政管理（未另分类）学科论文支持：管理、组织行为与运营题材。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_and_administration_not",
    aliases=(
        "business_and_administration_not",
        "商业与行政管理（未另分类）",
        "商业管理（未另分类）",
        "行政管理",
        "企业运营",
        "Business and Administration Not Elsewhere Classified",
        "Business Management",
        "Operations Management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "literature review",
            "research design",
            "data and methods",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background",
            "research design",
            "findings",
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
        "case_study": "案例研究须说明资料来源与三角验证",
    },
    conventions=(
        "引言须清晰陈述研究问题与贡献",
        "理论建构须区分先验假设与后验解释",
        "变量须给出操作化定义与度量口径",
        "实证结果须报告效应量与稳健性检验",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Administrative Science Quarterly",
        "Journal of Management Studies",
        "Management Science",
        "Organization Science",
        "Journal of Operations Management",
        "Journal of Business Ethics",
        "Academy of Management Learning & Education",
        "Management Decision",
    ),
    units_and_formulas_notes=(
        "金额以统一币种报告并注明年份",
        "统计量给出 M/SD/SE/CI",
        "样本量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("用友 U8+", "金蝶 K/3", "SAP S/4HANA", "Oracle E-Business Suite", "Microsoft Dynamics 365", "Salesforce", "HubSpot", "Microsoft Excel", "SPSS", "Stata", "R", "Python（pandas）", "Tableau", "Microsoft Power BI", "NVivo", "Minitab", "Qualtrics", "Google Analytics 4", "Airtable", "Notion", "Asana", "Trello", "Slack", "Zoom"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "JSTOR"),
)
