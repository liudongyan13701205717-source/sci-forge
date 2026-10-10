"""宗教学学科论文支持：比较宗教、田野与文本研究体裁注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="religious_studies",
    aliases=(
        "religious_studies",
        "宗教学",
        "宗教研究",
        "比较宗教学",
        "Religious Studies",
        "Comparative Religion",
        "Study of Religion",
        "Religionswissenschaft"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "sources（材料）",
            "analysis（分析）",
            "discussion（讨论）",
            "references"
        ),
        "ethnographic_study": (
            "abstract",
            "introduction",
            "fieldwork（田野）",
            "data（数据）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references"
        ),
        "comparative_study": (
            "abstract",
            "introduction",
            "traditions（比较对象）",
            "framework（框架）",
            "analysis（分析）",
            "conclusions（结论）",
            "references"
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；JAAR 遵循 Chicago 规范）",
    reporting_standards={
        "ethnography": "民族志研究遵循民族志报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明"
    },
    conventions=(
        "材料来源与版本须注明",
        "田野与知情同意须交代",
        "比较框架须明确",
        "术语用原文并注译",
        "解释框架（现象学/社会学/心理学）须明确"
    ),
    key_venues=(
        "Journal of the American Academy of Religion",
        "Numen",
        "Religion",
        "The Journal of Religion",
        "Method & Theory in the Study of Religion"
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "术语用原文并注译",
        "版本与版次须注明",
        "时间用统一纪年格式"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("田野民族志记录与整理", "口述史转录软件", "EndNote", "Zotero", "NVivo", "Atlas.ti", "Bible Works", "Logos Bible Software", "Accordance Bible Software", "ATLA Religion Database", "Brill Online", "ETS Theses", "Google Books", "Internet Archive", "Voyant Tools", "Otter.ai", "LaTeX（学术排版）", "SPSS（统计分析）", "RefWorks（文献管理）", "VOSviewer（文献计量可视化）"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest", "Google Scholar"),
)
