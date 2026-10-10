"""Adult literacy and numeracy teacher 学科论文支持：成人扫盲与读写算教师体裁、APA 引用样式与成人教育注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="adult_literacy_and_numeracy_teacher",
    aliases=("adult literacy and numeracy teacher", "成人读写算教师", "成人教育教师",
             "成人扫盲教师", "adult education", "adult literacy", "成人基础教育",
             "literacy teaching"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
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
        "teaching_research": (
            "abstract",
            "introduction",
            "literature review",
            "teaching design",
            "implementation",
            "assessment and results",
            "reflection",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "survey": "学习成效调查遵循 AAPOR 报告规范",
        "empirical": "实证研究遵循 APA 与 AAAAM 惯例",
    },
    conventions=(
        "教学术语全文一致：识字/读写/数算/成人学习者等核心概念须定义",
        "教学方法与教材须在方法部分列明；学习效果须给出测量工具",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "案例研究须说明案例选择理由与三角验证方法",
    ),
    key_venues=(
        "Adult Education Quarterly",
        "Journal of Adult and Continuing Education",
        "British Journal of Educational Technology",
        "Comparative Education Review",
        "Journal of Research on Teaching and Learning",
        "Educational Evaluation and Policy Analysis",
    ),
    units_and_formulas_notes=(
        "样本量、显著性水平、置信区间须完整给出",
        "识字与数算水平须用标准化量表（如 Gates-MacGinitie）标注",
        "学习效果报告 pre/post 均值差与效应量（Cohen's d）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office (Word/Excel)", "Google Classroom", "Moodle", "Canvas", "Blackboard", "Kahoot", "Quizlet", "Khan Academy", "Read&Write", "Grammarly", "Speechify", "Learning Ally", "SPSS", "R", "NVivo", "ATLAS.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "Canva", "Adobe InDesign"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "ERIC"),
)
