"""教学学科论文支持：教学法、课程设计与教育研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="didactics",
    aliases=(
        "didactics", "教学", "教学法",
        "teaching methods", "教学方法",
        "pedagogy", "教育学",
        "curriculum design", "课程设计",
        "instructional design", "教学设计",
        "teaching pedagogy", "教学艺术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教学问题与理论背景）",
            "method（研究设计、教学干预、评估工具）",
            "results（教学效果与学生发展）",
            "discussion（教学启示与改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "teaching process（教学过程描述）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教学理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "empirical": "实验设计须明确（组间/组内/准实验）",
        "assessment": "教学评估须注明工具与信效度",
        "statistics": "统计检验须注明效应量与置信区间",
        "ethics": "涉及学生研究须声明伦理审批",
    },
    conventions=(
        "教学干预须详细描述（内容、频率、时长）",
        "评估工具须注明信效度（α、Cronbach's alpha）",
        "学生样本须注明年龄、年级与抽样方法",
        "教学效果须区分短期与长期效果",
        "统计检验注明 α=0.05 与效应量",
    ),
    key_venues=(
        "Teaching and Teacher Education",
        "Educational Research Review",
        "Instructional Science",
        "Journal of Curriculum Studies",
        "Studies in Educational Evaluation",
        "Journal of Research on Teaching and Learning",
    ),
    units_and_formulas_notes=(
        "教学效果用 提升百分比/标准分差 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
        "样本量须报告",
        "干预效果用 Cohen's d 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "Microsoft Teams", "Zoom", "Moodle", "Canvas LMS", "Blackboard", "Kahoot!", "Google Classroom", "Canva", "PowerPoint", "Desire2Learn"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
