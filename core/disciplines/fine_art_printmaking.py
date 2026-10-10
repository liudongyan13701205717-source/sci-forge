"""版画艺术学科论文支持：版画创作、技法分析与艺术史研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fine_art_printmaking",
    aliases=(
        "fine_art_printmaking", "版画艺术", "版画",
        "printmaking", "fine art print",
        "版画创作", "木刻版画", "铜版画", "丝网版画",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（版画问题与艺术语境）",
            "methodology（技法实验、图像分析、艺术史脉络）",
            "results（创作成果与分析）",
            "discussion（与版画史、当代艺术对话）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（艺术家/版画作品描述）",
            "analysis（技法分析与图像学）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（版画艺术史论综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目）",
    reporting_standards={
        "technique": "版画技法须注明版种、材质与工艺流程",
        "materials": "材料须注明纸张、油墨、版材规格",
        "edition": "版画版数须注明（如 1/50）与艺术家签名",
        "conservation": "保存状态须注明光照、湿度与酸化程度",
    },
    conventions=(
        "尺寸用 cm 表示",
        "版数与签名须注明（如 1/50 AP）",
        "材质须完整（纸张/油墨/版材）",
        "技法分类使用国际版画分类标准",
        "年代与纪年格式统一",
    ),
    key_venues=(
        "Leonardo",
        "Journal of Print and Graphic Art",
        "Third Text",
        "Print Quarterly",
        "Visual Arts Review",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 表示",
        "纸张克重 g/m²",
        "油墨粘度用 cP 表示",
        "光照用 lux 表示",
        "年代用统一纪年格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Procreate", "GIMP", "Inkscape", "CorelDRAW", "Blender", "3D 打印（SLA/DLP）", "喷墨打印机（艺术级）", "平板扫描仪", "刻刀与刻版工具", "雕版与腐蚀设备", "丝网制版工具", "丝网印刷台", "木刻工具组", "铜版画腐蚀槽", "压印台（压印机）", "Endnote", "Zotero", "NVivo"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
