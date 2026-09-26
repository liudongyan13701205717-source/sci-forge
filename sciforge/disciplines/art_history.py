"""艺术史学科论文支持：图像/风格/语境体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="art_history",
    aliases=("art_history", "艺术史", "美术史", "艺术史学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "visual analysis（图像分析）",
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
        "archival_study": (
            "abstract",
            "introduction",
            "archival sources（档案史料）",
            "method（方法）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Art Bulletin 遵循 Chicago 规范）",
    reporting_standards={
        "visual": "图像分析遵循图像分析报告规范",
        "archival": "档案研究遵循史料考证报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品信息（作者/年代/材质/尺寸）须完整",
        "图像来源与版权须注明",
        "风格与流派脉络须交代",
        "引文给出页码",
        "解释框架须明确",
    ),
    key_venues=(
        "The Art Bulletin",
        "Art History",
        "Journal of Art Historiography",
        "The Burlington Magazine",
        "Oxford Art Journal",
        "Art Journal",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 标注",
        "引文给出页码",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品"),
    tools=(
        "数字艺术档案系统",
        "图像数据库检索工具",
        "EndNote 文献管理",
    ),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "DOAJ", "CNKI"),
)