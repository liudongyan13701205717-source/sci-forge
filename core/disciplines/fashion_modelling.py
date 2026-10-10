"""时尚模特学科论文支持：时尚产业、身体表征与表演实践体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fashion_modelling",
    aliases=(
        "fashion_modelling", "时尚模特", "模特",
        "fashion modelling", "model industry",
        "模特行业", "时尚表演", "形体艺术", "时装表演",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（时尚产业与身体表征问题）",
            "methodology（理论框架：表演性、视觉文化、劳动研究）",
            "results（模特实践与产业分析）",
            "discussion（与时尚研究、劳动社会学对话）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（模特/品牌/活动描述）",
            "analysis（表演实践、身体政治与产业分析）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（时尚模特研究理论脉络）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ 报告规范",
        "interview": "访谈研究遵循 INTERGUIDE 报告规范",
        "ethics": "涉及身体与劳动的伦理审查须注明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "身体描述使用中立客观语言，避免物化术语",
        "模特形象引用须注明拍摄者、年份与版权",
        "访谈数据须获知情同意并匿名化处理",
        "薪资与合同数据须标注来源与时间",
        "文化语境差异须说明（东西方模特工业对比）",
    ),
    key_venues=(
        "Fashion, Textiles and Culture",
        "Fashion Theory",
        "Body & Society",
        "Visual Studies",
        "Journal of Fashion Marketing and Management",
    ),
    units_and_formulas_notes=(
        "身体测量用 cm 表示（身高、三围）",
        "薪资数据注明币种与年份",
        "调查样本量与置信区间须报告",
        "图像分辨率与拍摄参数须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("CLO3D", "Marvelous Designer", "Browzwear", "Optitex", "StyleCAD", "Gerber AccuMark", "Tukatech", "Lectra", "Assyst", "Audaces", "Blender", "Sketchbook", "Inkscape", "Graphtec", "Tuka3D", "Made-to-Measure", "PatternMaker", "iX4i", "Wilcom", "Modaris"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar"),
)
