"""互联网使用项目学科论文支持：数字素养、在线学习与平台使用研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="internet_use_programmes",
    aliases=("internet use programmes", "互联网使用", "数字素养", "在线学习", "数字教育", "e-learning", "网络培训", "数字化培训"),
    paper_types={
        "research": ("abstract", "introduction（背景与数字鸿沟问题）", "methodology（学习者样本与干预设计）", "results（学习与行为发现）", "discussion（政策与推广）", "references"),
        "case_study": ("abstract", "introduction", "case description（机构、课程与受众）", "analysis（参与度、完成率与学习成效）", "results（成效数据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（数字素养与 TPACK 框架）", "evidence synthesis（项目证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "学习者样本给规模、人口学与来源",
        "k2": "干预与对照设计说明",
        "k3": "学习效果指标（前测、后测与留存率）",
    },
    conventions=(
        "研究问题与教学干预对应",
        "学习成效指标在引言定义",
        "伦理与隐私（同意、数据脱敏）在方法说明",
        "数字素养框架明确（如 EUDIC 或 DIGITAL competency）",
        "工具使用与学习行为分开分析"
    ),
    key_venues=(
        "Computers and Education",
        "The Internet and Higher Education",
        "Journal of Computer-Assisted Learning",
        "Educational Technology Research and Development",
        "International Journal of Educational Technology"
    ),
    units_and_formulas_notes=(
        "完成率与留存率以 % 表示并给分母",
        "学习时长用分钟或小时",
        "学习效果以 % 或分数点与等级",
        "在线行为以点击、浏览或提交事件计数"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Google Workspace", "Microsoft 365", "Google Chrome", "Mozilla Firefox", "Zoom", "Microsoft Teams", "Google Meet", "Coursera", "edX", "Khan Academy", "Internet Archive", "Zotero", "Mendeley", "Notion", "Obsidian", "Slack", "Discord", "Canvas LMS", "Moodle", "Google Forms"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar"),
)
