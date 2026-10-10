"""早期儿童教育学科论文支持：学前教育、儿童发展教学与研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="early_childhood_teaching_within_formal",
    aliases=(
        "early_childhood_teaching_within_formal", "早期儿童教育",
        "early childhood education", "学前教育",
        "preschool education", "幼儿教育",
        "childhood teaching", "儿童教学",
        "formal early education", "正规早期教育",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教育问题与背景）",
            "method（研究设计、教学干预、评估指标）",
            "results（教学效果与儿童发展）",
            "discussion（教育优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "teaching process（教学过程）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教育理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "教学方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及儿童数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "教学过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "教学效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Early Childhood Research Quarterly",
        "Early Childhood Education Journal",
        "Journal of Research in Early Childhood Education",
        "Early Education and Development",
        "Infants and Young Children",
        "Early Childhood Education",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "教学效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Google Classroom", "Moodle", "Zoom", "Microsoft Teams", "Kahoot!", "Canva", "PowerPoint", "Desire2Learn", "Canvas LMS", "Blackboard", "H5P", "EdPuzzle"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
