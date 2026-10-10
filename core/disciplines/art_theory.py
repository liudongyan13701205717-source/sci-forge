"""艺术理论学科论文支持：本体论、形式分析、阐释学与批判理论。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="art_theory",
    aliases=(
        "art theory",
        "艺术理论",
        "美学理论",
        "philosophy of art",
        "art philosophy",
        "aesthetics",
        "美学",
        "art critique",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "argument（论证）",
            "objections（反驳）",
            "conclusion",
            "references",
        ),
        "expository": (
            "introduction",
            "conceptual analysis（概念分析）",
            "illustration（例证）",
            "implications（推论）",
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
    citation_style="Chicago 样式（注-书目优先；美学/哲学论文亦接受 APA 7）",
    reporting_standards={
        "conceptual": "概念分析须给定义边界、来源与替代定义",
        "interpretive": "阐释须区分文本、作者与观者三层",
        "qualitative": "质性材料遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论概念首次使用须给原文、出处与译名",
        "命题须可反驳；显式列出反对意见并回应",
        "例证须给作品标题、作者、年代与来源",
        "假设须显式标注，禁止以例证替代论证",
    ),
    key_venues=(
        "Critical Inquiry",
        "The Journal of Aesthetics and Art Criticism",
        "Art Journal",
        "Art History",
        "October",
        "SubStance",
        "Leonardo",
        "Journal of Visual Culture",
    ),
    units_and_formulas_notes=(
        "概念首次出现给定义与出处",
        "示例作品给标题/年代/材质",
        "引文给出页码；版本与版次须注明",
        "逻辑命题须注明推理规则与前提",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "EndNote", "ARTstor", "Omeka", "Tropy", "Getty Open Content", "The Met Open Access", "Google Arts & Culture", "Europeana", "Wikidata", "Phaidon", "e-flux", "Adobe Photoshop", "Miro", "Hypothes.is", "Scrivener", "Obsidian", "Lucidchart", "Notion", "Scribe"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "JSTOR", "DOAJ", "CNKI"),
)
