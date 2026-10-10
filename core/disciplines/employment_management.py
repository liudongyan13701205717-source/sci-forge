"""就业管理学科论文支持：劳动关系、人力资源与就业政策研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="employment_management",
    aliases=(
        "employment_management", "就业管理", "劳动关系",
        "employment management", "就业管理",
        "labor relations", "劳动关系",
        "human resource management", "人力资源管理",
        "employment policy", "就业政策",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（管理问题与背景）",
            "method（研究设计、管理干预、评估指标）",
            "results（管理效果与员工发展）",
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
        "ethics": "涉及员工数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "管理过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "管理效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Personnel Psychology",
        "Academy of Management Review",
        "Journal of Vocational Behavior",
        "Career Development International",
        "Employee Relations",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "管理效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Tableau", "Power BI", "HLM (Hierarchical Linear Modeling)", "G*Power"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
