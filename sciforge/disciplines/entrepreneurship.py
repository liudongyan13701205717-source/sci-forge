"""创业学学科论文支持：创业管理、企业创建与创新发展研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="entrepreneurship",
    aliases=(
        "entrepreneurship", "创业学", "创业管理",
        "entrepreneurship", "创业学",
        "new venture creation", "新企业创建",
        "innovation management", "创新管理",
        "startup management", "初创企业管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（创业问题与背景）",
            "method（研究设计、创业案例、评估指标）",
            "results（创业效果与企业发展）",
            "discussion（创业优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "entrepreneurial process（创业过程）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "创业方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及企业数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "创业过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "创业效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Business Venturing",
        "Entrepreneurship Theory and Practice",
        "Strategic Entrepreneurship Journal",
        "Journal of Small Business Management",
        "Small Business Economics",
        "International Journal of Entrepreneurial Behavior & Research",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "创业效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Tableau", "Power BI", "Mplus", "AMOS"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
