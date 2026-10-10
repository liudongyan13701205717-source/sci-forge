"""家庭生活教育培训学科论文支持：家庭教育、家庭发展与生活技能培训体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="family_life_development_training",
    aliases=(
        "family_life_development_training", "家庭生活教育培训",
        "family life development training", "家庭生活教育培训",
        "family education", "家庭教育",
        "family development", "家庭发展",
        "life skills training", "生活技能培训",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（培训问题与背景）",
            "method（研究设计、培训方案、评估指标）",
            "results（培训效果与家庭发展）",
            "discussion（培训优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "training process（培训过程）",
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
        "intervention": "培训方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及家庭数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "培训过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "培训效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Family Relations",
        "Journal of Family Social Work",
        "Journal of Family Psychology",
        "Family Process",
        "Journal of Marital and Family Therapy",
        "Journal of Family Issues",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "培训效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Stata", "Jamovi", "G*Power（统计功效）", "REDCap（数据采集）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
