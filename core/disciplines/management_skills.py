"""管理技能学科论文支持：领导力、沟通、决策与团队协作技能研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management_skills",
    aliases=(
        "management_skills",
        "管理技能",
        "领导力",
        "沟通技巧",
        "Management Skills",
        "Leadership Skills",
        "Management Competencies",
        "职场技能",
        "团队领导",
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
    citation_style="APA 7 样式（管理学与心理学通用）",
    reporting_standards={
        "intervention": "干预研究遵循 CONSORT 声明",
        "qualitative": "质性研究遵循 COREQ 规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
    },
    conventions=(
        "技能测量须使用标准化量表（如 MSQ、MSI）",
        "干预效果须报告效应量（Cohen's d 或 Hedges' g）",
        "技能发展轨迹须报告前测与后测对比",
        "质性研究须附编码饱和与信度",
        "参与者的职业背景须报告并匿名化",
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Human Resource Management Review",
        "Journal of Management Research",
        "Journal of Management Studies",
        "Journal of Organizational Behavior",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "技能量表报告原始分与标准化分",
        "效应量报告 Cohen's d 或 η²",
        "信度报告 Cronbach's α",
        "时间以年/月为单位报告干预时长",
        "样本量须报告并附置信水平",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "Microsoft Project", "Microsoft PowerPoint", "Microsoft Word", "Microsoft Outlook", "Microsoft Teams", "Microsoft OneNote", "Microsoft Loop", "Microsoft Planner", "Microsoft Visio", "Google Workspace", "Google Drive", "Google Calendar", "Google Keep", "Google Forms", "Notion", "Trello", "Asana", "Airtable", "Monday.com"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
