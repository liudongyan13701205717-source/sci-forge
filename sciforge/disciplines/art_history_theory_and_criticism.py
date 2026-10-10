"""艺术史、理论与批评学科论文支持：理论阐释、批评话语与作品阐释三重体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="art_history_theory_and_criticism",
    aliases=(
        "art history, theory and criticism",
        "艺术史、理论与批评",
        "艺术理论与批评",
        "art theory and criticism",
        "视觉艺术批评",
        "visual criticism",
        "art criticism",
        "艺术批评",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "theoretical framework",
            "case analysis",
            "discussion",
            "conclusions",
            "references",
        ),
        "criticism": (
            "work（作品）",
            "formal observation（形式观察）",
            "interpretation（阐释）",
            "context（语境）",
            "evaluation（评价）",
            "references",
        ),
        "essay": (
            "introduction（提出命题）",
            "argument（论证）",
            "counter-argument（反驳）",
            "conclusion（回扣命题）",
            "references",
        ),
    },
    citation_style="Chicago 样式（注-书目优先；理论类论文亦接受 MLA）",
    reporting_standards={
        "visual": "图像观察须描述而非结论；结论另置于阐释段",
        "interpretive": "阐释须区分作者意图、观者反应与文本自身三层",
        "qualitative": "质性材料遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品首次出现须给标题、作者、年代、材质与收藏地",
        "理论概念首次使用须给出处与译名",
        "图像引自数据库须注明图号与版权",
        "阐释不得越过证据；假设须标为推测",
    ),
    key_venues=(
        "October",
        "Critical Inquiry",
        "Art Journal",
        "Art in America",
        "Oxford Art Journal",
        "The Journal of Aesthetics and Art Criticism",
        "Art History",
        "Whitechapel",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 标注；年代给统一纪年",
        "版本与版次须注明；译名给原文",
        "引用图像给图号与来源",
        "分辨率用 dpi；色彩模式须注明 RGB 或 CMYK",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ARTstor", "Omeka", "Tropy", "Getty Open Content", "The Met Open Access", "Google Arts & Culture", "Europeana", "Wikidata", "Zotero", "EndNote", "Phaidon", "Adobe Photoshop", "e-flux", "Miro", "Hypothes.is", "Scrivener", "Figma", "Notion", "Lucidchart", "Photoshop Lightroom"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "JSTOR", "DOAJ", "CNKI"),
)
