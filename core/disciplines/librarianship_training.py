"""图书馆员培训学科论文支持：图书馆员培训、职业发展与服务技能研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="librarianship_training",
    aliases=(
        "librarianship_training",
        "图书馆员培训",
        "图书馆员教育",
        "library profession training",
        "librarianship education",
        "图书馆员职业",
        "librarian training",
        "library profession",
        "图书馆员继续教育",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "培训课程评估须报告样本量、前后测对比与统计方法",
        "k2": "技能测评须引用能力模型或国家标准",
        "k3": "职业发展研究须声明样本来源与统计年份",
    },
    conventions=(
        "书目记录采用 MARC 21 或 RDA 元数据",
        "主题标引采用 LCSH 或汉语主题词表",
        "分类号采用中图法或杜威十进分类法",
        "馆藏量单位册或万册",
        "读者满意度用 Likert 量表评分",
    ),
    key_venues=(
        "Library Journal",
        "College & Research Libraries",
        "Journal of Academic Librarianship",
        "图书馆杂志",
        "大学图书馆学报",
    ),
    units_and_formulas_notes=(
        "馆藏量单位 万册",
        "借阅率 = 借阅册次 / 馆藏总量",
        "读者满意度用均值报告",
        "培训时长以学时或周计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Koha", "汇文", "津云", "Aleph ex Libris", "Polaris Libraries", "SirsiDynix Symphony", "FAST WebFinder", "RefWorks", "Zotero", "Mendeley", "EndNote", "NoteExpress", "OCLC Connexion", "NVivo", "SPSS", "Python", "MARC 编辑工具", "图书馆员培训模拟器", "LMS 学习管理系统", "Blacklight"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "WorldCat"),
)
