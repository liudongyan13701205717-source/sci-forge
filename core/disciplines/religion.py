"""宗教学科论文支持：宗教教义、宗教实践与宗教现象研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="religion",
    aliases=(
        "religion",
        "宗教",
        "宗教研究",
        "宗教现象学",
        "Religion Studies",
        "Theology",
        "Sociology of Religion",
        "Phenomenology of Religion"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "sources（材料与方法）",
            "analysis（分析）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（宗教实践/仪式）",
            "analysis（意义与结构）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（宗教理论）",
            "evidence synthesis（研究进展）",
            "future directions",
            "references"
        ),
    },
    citation_style="Chicago 样式（注-书目制；Religion/Numen 遵循此规范）",
    reporting_standards={
        "phenomenological": "现象学研究须报告观察场景与参与方式",
        "textual_analysis": "文本研究须注明版本、译本与经文段落",
        "comparative": "比较研究须给出比较框架与宗教传统背景"
    },
    conventions=(
        "术语首现英文原词加中文译名并附原文音译",
        "神圣话语尊重规范（避免冒犯性表述）",
        "教派、宗派术语须准确（如佛教宗派、基督教教派）",
        "文献版本与版次须注明",
        "田野与知情同意须交代"
    ),
    key_venues=(
        "Religion",
        "Numen",
        "Journal of the American Academy of Religion",
        "The Journal of Religion",
        "Harvard Theological Review"
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "术语用原文并注译（含音译）",
        "版本与版次须注明（含经卷卷数/段落号）",
        "时间用统一纪年格式（公元前后或世纪）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Bible Works", "Accordance Bible Software", "Logos Bible Software", "ATLA Religion Database", "Brill Online Reference", "ETS Theses", "Wikisource", "Google Books", "Internet Archive", "Voyant Tools", "NVivo", "Atlas.ti", "Bible Hub", "Internet Sacred Text Archive", "e-Codices", "DigiVatLib (梵蒂冈数字图书馆)", "Zotero", "EndNote", "SBL Biblical Hebrew and Aramaic Online", "Greek New Testament Online"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest Religion", "Google Scholar"),
)
