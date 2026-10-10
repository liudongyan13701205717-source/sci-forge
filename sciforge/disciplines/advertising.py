"""Advertising 学科论文支持：广告学/传播/营销体裁、APA 引用样式与广告研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="advertising",
    aliases=("advertising", "广告", "广告学", "广告传播", "ad design",
             "ad strategy", "广告文案", "整合营销", "advertising communication"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "theory and hypotheses",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
        "creative_analysis": (
            "abstract",
            "introduction",
            "object（广告对象与创意）",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "creative": "广告创意研究遵循 ICC 广告标准",
        "survey": "消费者调查遵循 AAPOR 报告规范",
        "empirical": "实证研究遵循 APA 与 AAAAM 惯例",
    },
    conventions=(
        "广告/传播术语全文一致：受众/曝光/点击率/转化率等核心概念须定义",
        "广告投放数据须给出平台、时段、受众定向与样本量",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "创意与文案须给出原文/画面描述；引用作品须注明来源与授权",
    ),
    key_venues=(
        "Journal of Advertising",
        "Journal of Advertising Research",
        "Journal of Marketing",
        "Journal of Marketing Research",
        "International Journal of Advertising",
        "Public Relations Quarterly",
        "Journal of Consumer Research",
    ),
    units_and_formulas_notes=(
        "广告效能指标 CTR/CPM/CPC/ROAS 须定义并注明平台",
        "样本量、显著性水平、置信区间须完整给出",
        "创意版本对比须给出效应量（Cohen's d 或 η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe After Effects", "Adobe Premiere Pro", "DaVinci Resolve", "Figma", "Sketch", "Canva", "Google Analytics (GA4)", "Google Ads", "Facebook Ads Manager", "TikTok Ads", "Hootsuite", "Sprout Social", "Nielsen", "Semrush", "Ahrefs", "Grammarly", "ProWritingAid", "Tableau", "Power BI", "SPSS", "R", "NVivo", "MAXQDA", "Qualtrics", "SurveyMonkey", "HubSpot", "Salesforce"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "SSRN"),
)
