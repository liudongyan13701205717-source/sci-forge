"""远程教育方法论学科论文支持：在线学习、混合式教学与教育技术研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="distance_education_methodology",
    aliases=(
        "distance_education_methodology", "远程教育方法论",
        "distance education methodology", "远程教育方法论",
        "online learning", "在线学习",
        "e-learning", "电子学习",
        "blended learning", "混合式学习",
        "virtual learning", "虚拟学习",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（远程教育问题与背景）",
            "method（研究设计、在线干预、评估工具）",
            "results（学习效果与在线体验）",
            "discussion（远程教学方法优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "course description（课程描述）",
            "implementation（实施过程）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（远程教育理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "empirical": "实验设计须明确（组间/组内/准实验）",
        "online": "在线学习平台与工具须注明",
        "assessment": "学习评估须注明方式（测试/作业/讨论）",
        "ethics": "涉及学生数据须声明隐私保护",
    },
    conventions=(
        "在线平台须注明名称与版本（如 Moodle、Canvas）",
        "学习分析须注明数据来源与隐私保护措施",
        "学习效果须区分知识、技能与态度维度",
        "满意度评估使用标准量表（如 ISU 量表）",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "International Journal of Educational Technology",
        "Distance Education",
        "Journal of Educational Technology & Society",
        "Computers & Education",
        "British Journal of Educational Technology",
        "Internet and Higher Education",
    ),
    units_and_formulas_notes=(
        "学习效果用 标准分差/提升百分比 表示",
        "参与度用 登录次数/讨论帖数 表示",
        "满意度用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Moodle", "Canvas LMS", "Blackboard", "Google Classroom", "Zoom", "Microsoft Teams", "Webex", "Qualtrics", "SurveyMonkey", "Google Forms", "NVivo", "Atlas.ti", "H5P", "EdPuzzle", "Kahoot!", "Mentimeter"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
