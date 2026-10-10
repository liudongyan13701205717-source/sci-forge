"""档案学学科论文支持：元数据、著录规范、数字化、开放档案与长期保存。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="archival_sciences",
    aliases=(
        "archival sciences",
        "档案学",
        "archives",
        "archivistics",
        "档案管理",
        "档案管理与保护",
        "digital archiving",
        "数字档案",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "case analysis",
            "findings",
            "implications",
            "references",
        ),
        "technical_report": (
            "abstract",
            "introduction",
            "system or repository description",
            "metadata and encoding",
            "preservation workflow",
            "validation and results",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "institutional context",
            "archival holdings",
            "findings",
            "recommendations",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-日期或注-书目；亦可用 APA 7）",
    reporting_standards={
        "descriptive": "著录遵循 EAD/ISAD(G)/DIA 元素集；层级完整",
        "preservation": "长期保存给格式（PDF/A/IMF/AAF）、校验和（SHA-256）与迁移策略",
        "metadata": "元数据方案给元素定义、必填性与映射表（PREMIS/EAD/SIP-AIP-DIP）",
        "system": "系统评估给用例、权限模型与审计日志",
    },
    conventions=(
        "档案来源（fonds/series/file/item）层级须交代",
        "著录元素按 ISAD(G) 或 EAD 元素名称书写",
        "数字档案给容器格式、校验和与来源说明",
        "限制与开放状态须说明依据与期限",
    ),
    key_venues=(
        "Archival Science",
        "American Archivist",
        "Archives and Manuscripts",
        "Records Management Journal",
        "IFLA Journal",
        "Journal of Information Management",
    ),
    units_and_formulas_notes=(
        "文件尺寸用 B/M/GB 标注；图像分辨率 dpi",
        "保留期限以年为单位并注明法规依据",
        "著录按 8.2 位（数字档案可给十六进制校验和）",
        "数字档案格式遵循 PREMIS 元数据标准；校验和用 SHA-256",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Archivematica", "AtoM", "Preservica", "ArchivesSpace", "DSpace", "CONTENTdm", "CollectiveAccess", "Omeka", "Tropy", "PRONOM", "DROID", "Tesseract OCR", "EAD", "ISAD(G)", "EARKS", "Open Refine", "Metanorma", "Axiell", "Rosetta", "Python"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "DOAJ", "CORE"),
)
