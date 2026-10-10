"""服装制作学科论文支持：服装工艺、设计与生产管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dressmaking",
    aliases=(
        "dressmaking", "服装制作", "服装工艺",
        "fashion design", "服装设计",
        "tailoring", "裁缝",
        "textile design", "纺织设计",
        "apparel manufacturing", "服装制造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（服装问题与背景）",
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
        "design": "设计参数须注明（尺寸、比例、色彩）",
        "fabrication": "制作工艺须完整描述",
        "testing": "性能测试须注明标准与方法",
    },
    conventions=(
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "面料成分须标注百分比",
        "缝制工艺须使用行业标准术语",
        "测试结果给出均值与标准差",
    ),
    key_venues=(
        "International Journal of Fashion Design, Technology, Education and Practice",
        "Fashion, Textiles and Culture",
        "Journal of Fashion Marketing and Management",
        "Textile Research Journal",
        "Journal of Textile and Apparel Technology Management",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 表示",
        "色彩用 Pantone 或 CMYK/RGB 表示",
        "面料成分用 % 表示",
        "强度用 N 或 cN 表示",
        "测试结果给出均值 ± SD",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "CorelDRAW", "CLO 3D", "Marvelous Designer", "Tailornest", "True Cut", "Kaledo", "PatternMaster", "Style Master 3D", "Sewer's Companion", "Fitting Model Software", "3D Pattern Design", "CAD Pattern Software", "Textile Testing Machine", "Sewing Machine", "Overlock Machine", "Serger", "Heat Press", "Steam Iron"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Design & Art Exchange"),
)
