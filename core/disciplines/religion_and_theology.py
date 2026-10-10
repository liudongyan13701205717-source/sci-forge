"""宗教与神学学科论文支持：教义、神学阐释与圣经研究体裁注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="religion_and_theology",
    aliases=(
        "religion_and_theology",
        "宗教与神学",
        "神学",
        "教义学",
        "Religion and Theology",
        "Systematic Theology",
        "Biblical Theology",
        "Doctrine"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "sources（经文/教父/文献）",
            "analysis（神学分析）",
            "conclusions（结论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（教会/礼仪/文本）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（神学传统）",
            "evidence synthesis（研究进展）",
            "future directions",
            "references"
        ),
    },
    citation_style="Chicago 样式（注-书目制；神学主流）",
    reporting_standards={
        "biblical_study": "圣经研究须注明文本传统（MT/LXX/NA/ESV 等）与译本",
        "patristic": "教父研究须给出文献版本与引文段落",
        "systematic": "系统神学须明确神学传统（改革宗/大公/东正/灵恩等）"
    },
    conventions=(
        "经文引用给出经卷-章节（如 罗 1:1）与文本传统",
        "神学术语首现英文原词加中文译名",
        "教父引用须给出 PG/JB 编号与页码",
        "神学传统与教派术语须准确",
        "尊重神圣传统的伦理声明"
    ),
    key_venues=(
        "The Journal of Religion",
        "Harvard Theological Review",
        "Theological Studies",
        "Scottish Journal of Theology",
        "Journal of Biblical Literature"
    ),
    units_and_formulas_notes=(
        "引文给出页码（PG/JB/NA/ESV）",
        "经文引用须注明版本（和合本/RSV/NRSV/NA28）",
        "教父文献引用须注明卷号与页码",
        "神学历史时期统一使用 AD/BC 或世纪纪年"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Bible Works", "Accordance Bible Software", "Logos Bible Software", "SBL Biblical Hebrew and Aramaic Online", "Biblical Hebrew Online", "Greek New Testament Online", "ATLA Religion Database", "ETS Theses", "Brill Online", "Google Books", "Internet Archive", "DigiVatLib (梵蒂冈数字图书馆)", "e-Codices", "Wikisource", "Voyant Tools", "Digital Philology Software", "Zotero", "EndNote", "NVivo", "Bible Hub"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest Religion and Theology", "JSTOR", "Google Scholar"),
)
