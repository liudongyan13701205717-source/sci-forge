"""人文学科（未细分）学科论文支持：泛人文综合研究/文本诠释体裁、Chicago 引用样式与质性研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="humanities_not",
    aliases=("humanities_not", "人文学科（未细分）", "人文学科", "人文", "古典研究", "哲学", "语言学", "比较研究", "诠释学", "人文综合"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与论点）", "methodology（方法与文本基础）", "results（分析发现）", "discussion（诠释与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案/文本）", "analysis（诠释分析）", "results（论点展开）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论谱系）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（作者-日期；脚注体亦常见）",
    reporting_standards={
        "interpretive": "诠释学研究遵循文本/语境报告规范",
        "philological": "文献学遵循原典校勘规范",
        "historical": "史学研究遵循史料考证与脚注规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "archive": "档案研究遵循档案来源与引用规范",
    },
    conventions=(
        "论点须前置并贯穿",
        "直接引文与脚注/尾注须规范",
        "引文转译与原文并置",
        "史料/文本来源须注明",
        "理论框架须交代",
    ),
    key_venues=(
        "Critical Inquiry",
        "Poetics Today",
        "The Journal of Modern Ideas",
        "New Literary History",
        "Theory & Event",
        "The American Historical Review",
    ),
    units_and_formulas_notes=(
        "引文页码用脚注或尾注体",
        "年代与纪年须注明朝代/世纪",
        "术语首现给原文与译名",
        "译名与音译遵循惯例",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "NVivo", "Atlas.ti", "MAXQDA", "Tropy", "Transkribus", "Omeka S", "Gephi", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "FairCopy", "LaTeX", "Nodegoat", "Recogito", "Dia"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest", "Web of Science"),
)
