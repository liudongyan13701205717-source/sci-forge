"""教育评估与研究学科论文支持：教育研究方法、数据分析与政策评估体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="educational_evaluation_and_research",
    aliases=(
        "educational_evaluation_and_research", "教育评估与研究",
        "educational evaluation", "教育评估",
        "educational research", "教育研究",
        "policy evaluation", "政策评估",
        "program evaluation", "项目评估",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "method（研究设计、数据收集、分析方法）",
            "results（研究结果与评估）",
            "discussion（研究启示与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析过程）",
            "results（效果评估）",
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
        "data": "数据来源须注明",
        "method": "研究方法须明确",
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
        "Review of Educational Research",
        "Educational Researcher",
        "Journal of Educational Psychology",
        "Educational Research",
        "American Educational Research Journal",
        "Educational Technology Research and Development",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "教学效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Tableau", "Power BI", "HLM (Hierarchical Linear Modeling)", "G*Power"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
