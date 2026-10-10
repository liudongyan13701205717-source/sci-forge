"""Clerical Programmes 学科论文支持：文书/文秘/办公室管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clerical_programmes",
    aliases=(
        "Clerical Programmes", "文秘项目", "Clerical Studies",
        "Office Administration", "文书与办公室管理",
        "Administrative Services", "Administrative Programmes",
        "行政文书", "Office Management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "record_keeping": "文件保存与归档须符合 GB/T 33870 或 ISO 30300",
        "privacy_protection": "涉及个人信息的文书须符合 GDPR 或《个人信息保护法》",
        "document_standard": "公文格式须遵循 GB/T 15498 或 ISO 21448",
    },
    conventions=(
        "使用办公自动化与文书处理的标准术语",
        "引用文件时给出标准编号（GB/T、ISO、ANSI）",
        "文书写作规范遵循 GB/T 15498、ISO 21448 等标准",
        "保密信息与身份信息须遵循隐私保护原则",
        "报告与记录应遵循档案管理与电子归档规范",
    ),
    key_venues=(
        "Journal of Business and Finance Education",
        "Administrative Staff Quarterly",
        "Journal of Business Administration",
        "Journal of Business Research",
        "Journal of Business Education",
        "Journal of Administrative Research",
    ),
    units_and_formulas_notes=(
        "工时统计以小时计，跨工作日须注明计入口径（自然日/工作日）",
        "文件周转时间以「收件—归档」工作日数计，并给出中位数与 P90",
        "差错率 = 错误文书数 / 总处理文书数 × 100%，须标注分母口径",
        "效率指标注明单位（件/小时或页/小时）并给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Microsoft Outlook", "Microsoft Teams", "Microsoft SharePoint", "Google Workspace", "Google Docs", "Google Sheets", "Notion", "Trello", "Asana", "Airtable", "Slack", "Grammarly", "DeepL", "OneNote", "Zotero", "Adobe Acrobat Pro", "M-Files"),
    category="管理学",
    databases=("OpenAlex", "Crossref"),
)
