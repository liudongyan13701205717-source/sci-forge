"""教育管理学科论文支持：学校治理、教育资源配置与教育政策研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management_of_education",
    aliases=(
        "management_of_education",
        "教育管理",
        "学校管理",
        "教育行政",
        "Education Management",
        "School Leadership",
        "教育政策",
        "教育治理",
        "教育领导",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="APA 7 样式（教育学通用）",
    reporting_standards={
        "intervention": "教育干预遵循 CONSORT 与 SQUIRE 声明",
        "qualitative": "质性研究遵循 COREQ 规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
    },
    conventions=(
        "教育干预研究须报告效应量（Hedges' g）",
        "学生成绩须使用标准分与效应量",
        "学校案例须匿名化并报告地域背景",
        "涉及未成年人的研究须获伦理审查与监护人同意",
        "教师/管理者访谈须使用半结构化访谈提纲",
    ),
    key_venues=(
        "Educational Administration Quarterly",
        "Educational Researcher",
        "Educational Evaluation and Policy Analysis",
        "Journal of Educational Administration",
        "Review of Educational Research",
        "中国教育学刊",
    ),
    units_and_formulas_notes=(
        "成绩报告标准化均值差（SMD）",
        "教育干预效应量用 Hedges' g 或 Cohen's d",
        "样本量须报告并附置信水平",
        "时间以学年/学期为单位",
        "财政数据以每生教育经费报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Google Workspace", "Google Classroom", "Microsoft Teams", "Microsoft OneNote", "Microsoft SharePoint", "Blackboard LMS", "Canvas LMS", "Moodle", "Schoology", "Edmodo", "Notion", "Trello", "Asana", "Confluence", "Airtable", "Lucidchart", "Miro", "FigJam", "Figma", "Google Drawings"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
