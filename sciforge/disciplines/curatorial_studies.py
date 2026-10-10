"""Curatorial studies 学科论文支持：展览策划/收藏管理/展示阐释体裁、艺术学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="curatorial_studies",
    aliases=(
        "curatorial_studies",
        "curatorial studies",
        "curatorial practice",
        "策展研究",
        "策展学",
        "展览策划",
        "exhibition curation",
        "museum curation",
        "display studies",
        "curatorship",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "methodology（策展方法与过程）",
            "case study（案例）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "exhibition_analysis": (
            "abstract",
            "introduction",
            "exhibition overview（展览概况：主题、借展、场地）",
            "interpretive framework（阐释框架）",
            "visitor engagement（观众参与与反馈）",
            "evaluation（评价）",
            "references",
        ),
        "object_study": (
            "abstract",
            "introduction（物件背景）",
            "provenance and condition（来源与状况）",
            "formal and material analysis（形式与材质分析）",
            "cultural context（文化语境）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-注；艺术史与博物馆学遵循 Chicago 规范）",
    reporting_standards={
        "provenance": "物件来源须逐年连续记录，任何断代或空白须显式说明",
        "condition": "状况记录遵循状况记录报告规范（摄影条件、检测手段、结论）",
        "attribution": "作品作者归属与真伪判断须给出依据并标注证据等级",
        "ethics": "涉及掠夺文物与归还争议须遵循国际博物馆协会（ICOM）职业伦理准则",
        "reproducibility": "借展清单、借展条件与装拆箱流程须可核查",
    },
    conventions=(
        "物件按机构藏品编号（accession number）引用，格式统一如 1985.12.3",
        "作品署名遵循「作者，作品名（斜体），创作年份，材质与尺寸，收藏机构，藏品编号」",
        "图片说明须含拍摄者/机构授权信息，尊重版权与肖像权",
        "术语中英文并列首次出现（如 借展 / loan）；阐释文本标注译文出处",
        "观众反馈数据须说明采集方式、样本量与统计口径",
        "展览方案须区分既有事实与策展主张（interpretive claim）",
    ),
    key_venues=(
        "Museum and Society",
        "Journal of Curatorial and Museum Studies",
        "International Journal of Curatorial Studies",
        "Museum International",
        "Curator: The Museum Journal",
        "The Australian Journal of Art and Culture",
        "博物馆研究",
    ),
    units_and_formulas_notes=(
        "作品尺寸单位用 cm（长×宽×高），厚度与重量按需注明",
        "展厅照度用 lx（勒克斯），色温用 K，显色指数用 Ra/CRI",
        "温湿度用 °C 与 %RH，给出区间与监测频次",
        "展厅面积用 m²，人流数据区分人次与独立访客数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("The Museum System (TMS)", "Axiell EMu", "CollectiveAccess", "PastPerfect", "Spectrum (NPGallery)", "AGLAYA (AMICA)", "CCO (Culture Change Online)", "Artlogic", "MUSE (Museum Software Suite)", "Omeka", "AtoM (Access to Memory)", "Mirador", "IIIF (International Image Interoperability Framework)", "CONTENTdm (Beacon)", "Rosetta Digital Preservation System", "Preservica", "DSpace", "Fedora Commons", "Tessitura", "SketchUp", "AutoCAD", "Colorimetrix SpectraMagic", "Konica Minolta CM-3600A", "XRF Analyzer (Edison Tech Scientific)", "X-Rite i1Pro2", "Wikidata"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Web of Science", "Europeana", "Getty Open Access"),
)
