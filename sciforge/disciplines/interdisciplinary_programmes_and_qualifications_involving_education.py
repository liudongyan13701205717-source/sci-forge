"""教育类跨学科项目与学位：研究、案例、综述体裁，APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_education",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_education",
        "教育类跨学科项目与学位",
        "Education Interdisciplinary Programmes",
        "Interdisciplinary Education Degree",
        "Cross-disciplinary Education",
        "Educational Interdisciplinarity",
        "教育学跨学科",
        "教育学位项目",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "SAGE/ERA（教育研究综述）",
        "k2": "CORE（质性研究规范）",
        "k3": "AACUB（大学学术诚信）",
    },
    conventions=(
        "研究对象（学生/教师/课程）须明确界定",
        "学校类型与学段须说明",
        "伦理审查编号须标注",
        "质性编码过程须报告",
        "跨学科课程模块与先修关系须明示",
    ),
    key_venues=(
        "Review of Educational Research",
        "Educational Researcher",
        "Educational Evaluation and Policy Analysis",
        "Journal of Educational Psychology",
        "Higher Education",
    ),
    units_and_formulas_notes=(
        "统计量报告 M/SD/SE/CI",
        "标准化效应量报告 Hedges' g 或 d",
        "问卷信度报告 Cronbach's α",
        "样本量与失效率须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "NVivo", "ATLAS.ti", "MAXQDA", "MATLAB", "JASP", "JAMBI", "Moodle", "Blackboard", "Canvas LMS", "Google Analytics for Education", "Turnitin", "iThenticate", "RefWorks", "Zotero", "EndNote", "Qualtrics", "SurveyMonkey"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
