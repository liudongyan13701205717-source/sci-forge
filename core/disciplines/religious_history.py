"""宗教史学科论文支持：宗教历史、思想史与宗教变迁研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="religious_history",
    aliases=(
        "religious_history",
        "宗教史",
        "宗教历史",
        "宗教思想史",
        "Religious History",
        "History of Religions",
        "Religious Studies History",
        "Church History"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与史料基础）",
            "literature review（史学史综述）",
            "sources（史料考辨）",
            "analysis（历史分析）",
            "discussion（史学意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（事件/人物/机构）",
            "analysis（史料与年代考）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（史学方法）",
            "evidence synthesis（研究进展）",
            "future directions",
            "references"
        ),
    },
    citation_style="Chicago 样式（注-书目制；History of Religions 遵循此规范）",
    reporting_standards={
        "primary_source": "一手史料须注明馆藏、卷号、日期与版本",
        "archival": "档案研究须报告检索范围与馆藏编号",
        "chronological": "年代学须给出多种纪年（公历、农历、朝代）"
    },
    conventions=(
        "史料版本与馆藏编号须注明",
        "纪年统一给出公历并注明对应朝代",
        "术语首现英文原词加中文译名",
        "引文给出页码",
        "历史人物与机构名称须注明全称"
    ),
    key_venues=(
        "History of Religions",
        "Church History",
        "Harvard Theological Review",
        "Journal of Ecumenical Studies",
        "Catholic Historical Review"
    ),
    units_and_formulas_notes=(
        "引文给出页码（含馆藏卷号）",
        "纪年统一使用公元（AD/BC）并注明中国朝代",
        "度量衡须注明当时单位与国际单位换算",
        "文献版本须注明版次、编者与出版年"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Bible Works", "Accordance Bible Software", "Logos Bible Software", "ATLA Religion Database", "Brill Online", "ETS Theses", "Google Books", "Internet Archive", "Europeana", "DigiVatLib (梵蒂冈数字图书馆)", "e-Codices", "British Library Endangered Archives", "Oxford Digital Bodleian", "Library of Congress", "Digital Public Library of America", "Voyant Tools", "Zotero", "EndNote", "SBL Biblical Hebrew and Aramaic Online", "Biblical Hebrew Online"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest History", "Google Scholar"),
)
