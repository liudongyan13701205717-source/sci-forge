"""图书情报与档案学科论文支持：文献管理、档案保管、数字化与信息管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="library_information_and_archival",
    aliases=(
        "library_information_and_archival",
        "图书情报与档案",
        "档案管理",
        "archival science",
        "records management",
        "档案学",
        "信息管理与档案",
        "document management",
        "档案与图书馆",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical framework（理论框架）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "档案管理须引用 DA/T 或 GB/T 档案标准",
        "k2": "数字化须声明扫描分辨率、色彩空间与元数据格式",
        "k3": "评估须报告样本量、抽样方法与统计年份",
    },
    conventions=(
        "档案保管期限分永久、30 年、10 年三类",
        "档案分类号采用一级类目 A-S",
        "元数据遵循 EAD、PREMIS 或 Dublin Core",
        "数字化分辨率以 dpi 单位报告",
        "文件字号格式为 (年) X 字第 X 号",
    ),
    key_venues=(
        "Archival Science",
        "Records Management Journal",
        "Journal of the Society of Archivists",
        "档案学通讯",
        "档案与建设",
    ),
    units_and_formulas_notes=(
        "保管期限以年为单位",
        "扫描分辨率以 dpi 表示（300/600）",
        "馆藏量单位 卷或件",
        "档案数字化率 = 已数字化件数 / 总件数 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("档案综合管理系统", "DSSOA", "汇友档案", "兰大档案", "Archivematica", "AtoM", "Archives Space", "Fedora Commons", "DSpace", "Zeutschel 高速扫描仪", "Bookcatcher 扫描枪", "ABBYY FineReader", "Adobe Acrobat", "电子档案管理系统", "EAD 元数据编辑器", "PREMIS 元数据工具", "Dublin Core 编辑器", "数字档案长期保存平台", "数字水印工具", "电子签章系统"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
