"""办公自动化学科论文支持：办公信息化/流程自动化体裁、ACM 引用样式与办公记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="office_automation",
    aliases=("office_automation", "办公自动化", "OA", "办公自动化系统", "office automation", "oa systems"),
    paper_types={
        "research": ("abstract", "introduction（背景与技术问题）", "methodology（系统与实验）", "results（性能与对比）", "discussion（机理与推广）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例背景）", "analysis（设计与实施）", "results（应用效果）", "discussion（经验与改进）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技术综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="ACM 样式",
    reporting_standards={"systematic_review": "遵循 PRISMA 声明", "empirical": "遵循 DARES 报告", "case_study": "遵循 CBSE 报告"},
    conventions=("工具/版本须注明", "评估指标须一致", "实验环境须报告", "数据集须可复现", "响应时间用 ms 或 s"),
    key_venues=("Journal of Organizational and End User Computing", "Journal of Enterprise Information Management", "International Journal of Electronic Governance", "Proceedings of ACM CHI", "IEEE Transactions on Software Engineering"),
    units_and_formulas_notes=("时间用 ms", "吞吐用 ops/s", "存储用 GB", "公式用 amsmath", "数值给出均值±SD"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office 365", "Google Workspace", "Zoom", "Microsoft Teams", "Slack", "Asana", "Monday.com", "Trello", "Notion", "Airtable", "Confluence", "Jira", "Dropbox", "Google Drive", "SharePoint", "Adobe Acrobat", "DocuSign", "Zapier", "Python 自动化脚本", "Power Automate"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
