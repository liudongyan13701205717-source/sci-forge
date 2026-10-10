"""编辑学科论文支持：文本编辑、出版技术与数字编辑研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="editing",
    aliases=(
        "editing", "编辑", "编辑学",
        "text editing", "文本编辑",
        "copy editing", "文字编辑",
        "publishing", "出版",
        "scholarly editing", "学术编辑",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（编辑问题与背景）",
            "methodology（编辑方法、技术工具、效果评估）",
            "results（编辑效果与技术评估）",
            "discussion（编辑优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "editing process（编辑过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（工具对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "tool": "编辑工具须注明版本与设置",
        "style": "风格指南须注明（如 Chicago、APA）",
        "workflow": "编辑流程须完整记录",
    },
    conventions=(
        "风格指南须统一使用",
        "版本控制须使用 Git",
        "校对标记须使用标准符号",
        "字数用 字 表示",
        "时间用 小时 表示",
    ),
    key_venues=(
        "Editing",
        "Journal of Scholarly Publishing",
        "Book History",
        "Studies in Bibliography",
        "Journal of the Association of College and Research Libraries",
    ),
    units_and_formulas_notes=(
        "字数用 字 表示",
        "时间用 小时 表示",
        "版本用 数字 表示",
        "校对标记须使用标准符号",
        "统计检验注明效应量与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Word", "Google Docs", "LaTeX", "Overleaf", "InDesign", "QuarkXPress", "Adobe Acrobat", "EndNote", "Zotero", "Mendeley", "RefWorks", "ProWritingAid", "Grammarly", "Hemingway Editor", "VivaWriter", "Scrivener", "Pandoc", "Git", "GitHub", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
