"""博物馆文档记录学科论文支持：藏品数字化与档案编目体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="museum_documentation",
    aliases=(
        "museum_documentation", "博物馆文档", "Museum documentation",
        "museum cataloguing", "藏品编目", "museum archives",
        "博物馆档案", "digital archiving",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（编目/数字化方法）",
            "results（编目与检索结果）",
            "discussion（发现与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（馆藏背景）",
            "analysis（编目与检索分析）",
            "results（成果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（标准与工具综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式",
    reporting_standards={
        "k1": "编目研究须报告元数据标准（如 EAD、CDWA）",
        "k2": "数字化研究须报告分辨率、色彩管理与元数据完整性",
        "k3": "检索系统评估须报告查准率、查全率与满意度",
    },
    conventions=(
        "藏品编号须遵循 ICOM 分类体系",
        "编目字段须遵循 DACS 或 EAD 规范",
        "引用馆藏数据须给出登记号与访问日期",
        "数字化文件须注明格式与元数据字段",
        "引用档案须遵循 archival 描述规则",
    ),
    key_venues=(
        "Archival Science",
        "Archives and Manuscripts",
        "Journal of the American Society for Information Science and Technology",
        "Museum Management and Curatorship",
        "《档案学通讯》",
    ),
    units_and_formulas_notes=(
        "图像分辨率用 DPI；文件大小用 MB/GB",
        "色彩管理给出色彩空间（sRGB/AdobeRGB）",
        "编目字段数与描述层级须明确",
        "检索性能用查准率、查全率报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArchivesSpace", "Cohesion", "AtoM", "OMeka", "ContentDM", "MediaSpace", "Ephesus", "Axiell AX", "Tine 2.0", "Cultural Heritage Management Systems", "Museum System", "EndNote", "Zotero", "Microsoft Excel", "LibreOffice", "Notepad++", "Python (pandas)", "Adobe Lightroom", "Capture One", "Phase One Capture Pro"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
