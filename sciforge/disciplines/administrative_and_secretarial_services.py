"""Administrative and secretarial services 学科论文支持：行政/文员/文秘体裁、APA 引用样式与行政实务注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="administrative_and_secretarial_services",
    aliases=("administrative and secretarial services", "行政与秘书服务", "行政秘书",
             "文员", "clerical", "secretarial", "office administration", "办公事务"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
        "practice_review": (
            "abstract",
            "introduction",
            "scope and method",
            "state of practice",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 AAAAM 惯例",
    },
    conventions=(
        "行政术语全文一致：文书/流程/合规/档案等核心概念须定义",
        "案例研究须说明案例选择理由与三角验证方法",
        "问卷与量表须给出 Cronbach's α；信度与效度须报告",
        "办公自动化流程与工具须在方法部分列明",
    ),
    key_venues=(
        "Journal of Business Communication",
        "Journal of Business and Technical Writing",
        "Administrative Quarterly",
        "Journal of Business and Industry Research",
        "Journal of the Operational Research Society",
        "Administrative Science Quarterly",
    ),
    units_and_formulas_notes=(
        "样本量、显著性水平、置信区间须完整给出",
        "效应量报告 Cohen's d/η²/R² 等标准指标",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office (Word/Excel/PowerPoint)", "Google Workspace", "Adobe Acrobat", "Grammarly", "Hemingway Editor", "ProWritingAid", "Zotero", "EndNote", "Trello", "Asana", "Microsoft Project", "SharePoint", "Microsoft Teams", "Slack", "Zoom", "DocuSign", "Adobe Sign", "Qualtrics", "SurveyMonkey", "NVivo", "MAXQDA", "Tableau", "Power BI"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "SSRN"),
)
