"""人文学科论文支持：人文研究/文本分析/诠释学体裁、Chicago 引用样式与质性研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="humanities",
    aliases=("humanities", "人文学科", "人文", "文学", "哲学", "历史", "古典学", "神学", "艺术史"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与论点）", "methodology（方法与文本基础）", "results（分析发现）", "discussion（诠释与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（文本/个案）", "analysis（文本分析）", "results（论点展开）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论与诠释学框架）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（作者-日期；人文期刊常用 MLA 脚注体）",
    reporting_standards={
        "interpretive": "诠释学研究遵循文本/语境报告规范",
        "philological": "文献学遵循原典校勘与出处规范",
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
        "The Journal of Modern Ideas",
        "Critical Inquiry",
        "The American Historical Review",
        "Poetics Today",
        "The Journal of Aesthetics and Art Criticism",
        "New German Critique",
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
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest", "JSTOR", "Web of Science"),
)
