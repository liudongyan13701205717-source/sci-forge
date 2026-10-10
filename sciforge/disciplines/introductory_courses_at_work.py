"""企业入职课程学科论文支持：新员工培训、入职体验与组织社会化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="introductory_courses_at_work",
    aliases=("introductory courses at work", "入职培训", "新员工培训", "企业培训", "onboarding", "组织社会化", "新员工引导", "员工入职"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（培训设计与测量）", "results（学习效果与留存发现）", "discussion（政策与管理含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（企业、岗位与课程）", "analysis（内容、方式与反馈）", "results（成效数据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（成人学习与组织社会化理论）", "evidence synthesis（企业实证与元分析）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "样本给规模、岗位与年限",
        "k2": "培训设计给目标、内容与评估方法",
        "k3": "学习效果指标明确（考核、行为与留存）",
    },
    conventions=(
        "学习目标与培训内容对应",
        "新员工定义在方法交代",
        "量化与质性证据互补",
        "隐私与伦理（数据脱敏）说明",
        "培训效果指标按 Kirkpatrick 四层评估"
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Personnel Psychology",
        "Journal of Management",
        "Human Resource Management Journal",
        "Research in Personnel and Human Resources Management"
    ),
    units_and_formulas_notes=(
        "学习效果以 %、分数或等级",
        "培训时长以小时",
        "留存率以 % 每月",
        "满意度用 Likert 5 或 7 分量表并说明"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Canvas LMS", "Moodle", "Blackboard", "TalentLMS", "Docebo", "Cornerstone OnDemand", "SAP SuccessFactors Learning", "Workday Learning", "LinkedIn Learning", "Coursera for Business", "Zoom", "Microsoft Teams", "Slack", "Notion", "Trello", "Asana", "Google Workspace", "Microsoft 365", "Qualtrics", "SurveyMonkey"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
