"""刺绣学科论文支持：刺绣工艺、图案设计与纺织艺术研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="embroidery",
    aliases=(
        "embroidery", "刺绣", "刺绣工艺",
        "embroidery craft", "刺绣工艺",
        "embroidery design", "刺绣设计",
        "textile art", "纺织艺术",
        "needlecraft", "针线活",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（刺绣问题与背景）",
            "methodology（设计方法、工艺测试、效果评估）",
            "results（工艺效果与设计评估）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（工艺分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（工艺对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "design": "设计参数须注明（尺寸、色彩、针法）",
        "fabrication": "制作工艺须完整描述",
        "testing": "色牢度测试须注明标准与方法",
    },
    conventions=(
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "线材成分须标注百分比",
        "针法名称须使用行业标准",
        "测试结果给出均值与标准差",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Textile and Apparel Technology Management",
        "Fashion, Textiles and Culture",
        "Journal of Fashion Marketing and Management",
        "Textile History",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "线材成分用 % 表示",
        "色牢度用 1-5 级表示",
        "测试结果给出均值 ± SD",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "CorelDRAW", "Wilcom EmbroideryStudio", "Pulse Microsystems", "Hatch Embroidery", "Embrilliance", "SewArt", "Ink/Stitch", "PE-Design", "Embird", "Pulse", "Wilcom", "Tajima", "Barudan", "ZSK", "Melco", "Brother", "Janome", "Singer"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Design & Art Exchange"),
)
