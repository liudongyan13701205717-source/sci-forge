"""艺术学（艺术研究）学科论文支持：创作实践、图像分析与媒介跨域研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="art_studies",
    aliases=(
        "art studies",
        "艺术学",
        "艺术研究",
        "visual arts studies",
        "art practice",
        "艺术实践研究",
        "visual studies",
        "视觉研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "case analysis",
            "findings",
            "references",
        ),
        "practice_led": (
            "research question",
            "practice description",
            "analytical framework",
            "practice process",
            "reflection",
            "references",
        ),
        "multimodal": (
            "abstract",
            "introduction",
            "materials and media",
            "multimodal analysis",
            "findings",
            "references",
        ),
    },
    citation_style="Chicago 样式或 MLA（艺术学与视觉文化两系常用）",
    reporting_standards={
        "visual": "图像与作品信息须完整（标题/作者/年代/材质/收藏地）",
        "practice": "创作过程给材料、尺度、工序与时间线",
        "qualitative": "质性访谈遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品信息（作者/年代/材质/尺寸）须完整",
        "图像来源与版权须注明",
        "媒介与材料名称给原文与中文对照",
        "引文给出页码",
    ),
    key_venues=(
        "Art Journal",
        "The Journal of Aesthetics and Art Criticism",
        "Art History",
        "Critical Inquiry",
        "Journal of Visual Culture",
        "Leonardo",
        "Performance Research",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 标注；影像分辨率用 px 或 dpi",
        "视频给时长 min 与帧率",
        "版本与版次须注明",
        "色彩模式须注明 sRGB 或 CMYK；输出给 dpi 与尺寸",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("ARTstor", "Omeka", "Tropy", "Getty Open Content", "The Met Open Access", "Google Arts & Culture", "Europeana", "Wikidata", "Zotero", "EndNote", "Phaidon", "Adobe Photoshop", "Procreate", "DaVinci Resolve", "e-flux", "NVivo", "Miro", "Figma", "Obsidian", "Photoshop Lightroom"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "JSTOR", "DOAJ", "CNKI"),
)
