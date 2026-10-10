"""家庭与婚姻咨询学科论文支持：家庭治疗、婚姻咨询与家庭关系研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="family_and_marriage_counselling",
    aliases=(
        "family_and_marriage_counselling", "家庭与婚姻咨询",
        "family and marriage counselling", "家庭与婚姻咨询",
        "family therapy", "家庭治疗",
        "marriage counselling", "婚姻咨询",
        "couples therapy", "伴侣治疗",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（咨询问题与背景）",
            "method（研究设计、咨询干预、评估指标）",
            "results（咨询效果与家庭关系）",
            "discussion（咨询优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "counselling process（咨询过程）",
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
        "intervention": "咨询方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及家庭数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "咨询过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "咨询效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Marital and Family Therapy",
        "Family Process",
        "Journal of Family Psychology",
        "Journal of Couple & Relationship Therapy",
        "Family Relations",
        "Journal of Family Social Work",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "咨询效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Stata", "Python（pandas）", "Tableau", "Power BI"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
