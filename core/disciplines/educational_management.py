"""教育管理学科论文支持：学校管理、教育领导与教育政策研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="educational_management",
    aliases=(
        "educational_management", "教育管理", "学校管理",
        "educational management", "教育管理",
        "school leadership", "学校领导",
        "education administration", "教育行政",
        "education governance", "教育治理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（管理问题与背景）",
            "method（研究设计、管理干预、评估指标）",
            "results（管理效果与学校发展）",
            "discussion（管理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "management process（管理过程）",
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
        "intervention": "管理方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及学生数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "教学过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "教学效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Educational Administration Quarterly",
        "Journal of Educational Administration",
        "Educational Management Administration & Leadership",
        "International Journal of Educational Management",
        "School Effectiveness and School Improvement",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "教学效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Tableau", "Power BI", "HLM (Hierarchical Linear Modeling)", "G*Power"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
