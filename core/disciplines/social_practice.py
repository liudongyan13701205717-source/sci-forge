"""社会实践学科论文支持：教育实习/服务学习/专业实践体裁、APA 引用样式与教育评估规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_practice",
    aliases=("social_practice", "社会实践", "教育实习", "专业实践", "field education", "service learning", "internship", "practicum"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与实践框架）",
            "methods（设计、参与者、观察、反思日志）",
            "results（结果、编码与主题）",
            "discussion（讨论与教育含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（实践情境与个案）",
            "analysis（实践过程与反思）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（文献检索）",
            "evidence synthesis（实践教育证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="APA 7（Teaching and Teacher Education、Journal of Teacher Education 遵循 APA）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ 与 SSI（服务学习）报告规范：参与观察、反思日志、饱和判断",
        "reflection": "反思性实践遵循 Schön 反思模式：情境描述、反思、行动、再评估",
        "case_study": "实践个案遵循 CDSR 规范：情境、过程、结果、反思",
        "mixed_methods": "混合设计用联合展示表整合观察、访谈与量表数据"
    },
    conventions=(
        "实践框架须声明：服务学习、教育实习、临床实践、社区参与等类型定义",
        "伦理审批、知情同意、二次告知须报告；涉及未成年人与弱势群体时须说明保护措施",
        "反思日志使用结构化编码（如 Schön、Johns、Mezirow）并说明编码者信度",
        "观察场次、录音时长、转写字数须在方法中报告",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）"
    ),
    key_venues=(
        "Teaching and Teacher Education",
        "Journal of Teacher Education",
        "Journal of Social Work Education",
        "Journal of Experiential Education",
        "Reflective Practice"
    ),
    units_and_formulas_notes=(
        "反思日志条数给出总量、编码频次与主题饱和度判断",
        "观察场次给出总时长与人均时长；质性引用格式（受访者编号：行号）",
        "量表分数给出 T 分数/百分位与信度（α、ω）",
        "百分比给出基数 N；加权数据注明权重变量"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Canvas LMS", "Blackboard", "Moodle", "Google Classroom", "Seesaw", "Google Forms", "Qualtrics", "SurveyMonkey", "SPSS", "R", "RStudio", "NVivo", "MAXQDA", "Dedoose", "Obsidian", "Notion", "Miro", "Padlet", "Kahoot", "Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
