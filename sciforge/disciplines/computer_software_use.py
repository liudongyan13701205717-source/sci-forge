"""计算机软件应用学科论文支持：办公软件/信息系统应用/桌面发布体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_software_use",
    aliases=("computer software use", "计算机软件应用", "计算机应用",
             "office automation", "office software", "办公自动化",
             "办公软件", "software application",
             "computer literacy", "计算机基础"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method/approach",
            "case study",
            "results",
            "discussion",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "workflow",
            "implementation",
            "evaluation",
            "conclusion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "experimental": "用户研究须报告样本、任务与耗时",
        "case_study": "应用案例须描述流程、部署与效果",
        "usability": "可用性研究遵循 ISO 9241 / Nielsen 十原则",
        "reproducibility": "宏脚本/模板须公开",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "版本、操作系统与语言环境须明确",
        "操作步骤以流程图或编号步骤给出",
        "宏/脚本给出版本号与变更记录",
        "界面截图标注关键控件与路径",
        "效果对比须在相同数据集上进行",
    ),
    key_venues=(
        "Journal of Computing in Small Colleges",
        "Education and Information Technologies",
        "Computers & Education",
        "Journal of Educational Computing Research",
        "International Journal of Human-Computer Interaction",
        "ACM SIGCUE Interfaces",
        "Journal of Computing in Higher Education",
        "Interactive Learning Environments",
        "Educational Technology & Society",
        "Australasian Journal of Educational Technology",
    ),
    units_and_formulas_notes=(
        "效率对比以任务完成时间（秒/分钟）与错误率（%）计",
        "样本量须声明，结论以描述性统计为主",
        "公式与宏代码单独置于附录或附录文件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Microsoft Access", "Microsoft Outlook", "Microsoft OneNote", "Microsoft Teams", "Microsoft SharePoint", "Microsoft OneDrive", "Microsoft PowerBI", "Microsoft Visio", "Microsoft Project", "Microsoft To-Do", "Microsoft Forms", "LibreOffice", "Apache OpenOffice", "Google Docs", "Google Sheets", "Google Slides", "Google Drive", "Google Forms", "Google Meet", "Google Calendar", "Apple Pages", "Apple Numbers", "Apple Keynote", "Notion", "Slack", "Zoom", "Trello", "Asana", "Jira", "Airtable", "Smartsheet", "Basecamp", "Figma", "Adobe Acrobat", "PDF-XChange Editor", "WPS Office", "OnlyOffice"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "ERIC"),
)
