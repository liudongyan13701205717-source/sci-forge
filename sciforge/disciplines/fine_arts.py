"""美术学科论文支持：创作/批评/展览体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fine_arts",
    aliases=(
        "fine_arts", "美术", "造型艺术", "视觉艺术",
        "fine art", "visual arts",
        "绘画", "雕塑", "设计", "美术学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "visual_analysis": (
            "abstract",
            "introduction",
            "object（作品）",
            "formal analysis（形式分析）",
            "context（语境）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "practice_based": (
            "abstract",
            "introduction",
            "creative process（创作过程）",
            "artwork（作品）",
            "reflection（反思）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Art Journal 遵循 Chicago 规范）",
    reporting_standards={
        "visual": "图像分析遵循图像分析报告规范",
        "practice": "实践研究遵循创作实践报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品信息（作者/年代/材质/尺寸）须完整",
        "图像来源与版权须注明",
        "创作语境须交代",
        "引文给出页码",
        "解释框架须明确",
    ),
    key_venues=(
        "Art Journal",
        "Leonardo",
        "Third Text",
        "October",
        "Artforum",
        "Journal of Visual Art Practice",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 标注",
        "引文给出页码",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe Lightroom", "Procreate", "CorelDRAW", "Blender", "3ds Max", "Maya", "GIMP", "Inkscape", "Cinema 4D", "Unreal Engine 5", "Procreate Dreams", "3D 打印（FDM/SLA）", "喷墨打印机（艺术级）", "平板扫描仪", "Endnote", "Zotero", "NVivo"),
    category="艺术学",
    databases=("DOAJ", "OpenAlex", "Crossref", "CNKI"),
)
