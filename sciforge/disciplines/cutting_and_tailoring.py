"""Cutting and tailoring 学科论文支持：服装设计/制版/工艺分析体裁、Chicago 样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cutting_and_tailoring",
    aliases=(
        "cutting_and_tailoring", "cutting and tailoring", "裁剪与缝纫", "服装裁剪",
        "服装制版", "服装工艺", "garment construction", "fashion technology",
        "textile engineering", "缝纫工艺", "时装工艺", "pattern making",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与工艺动机）",
            "methodology（制版/打样/试验方法）",
            "results（试样数据与成品评估）",
            "discussion（工艺与功能权衡）",
            "conclusions（结论与建议）",
            "references",
        ),
        "design_case": (
            "abstract",
            "introduction",
            "concept（设计概念）",
            "pattern and construction（版样与工艺）",
            "samples（试样与迭代）",
            "reflection（反思与迭代）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（工艺/设备/材料综述）",
            "outlook（趋势与展望）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；Fashion and Textile History 遵循 Chicago 规范）",
    reporting_standards={
        "experimental": "工艺试验遵循服装样品评估报告规范",
        "case_study": "设计案例遵循设计实践报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "historical": "工艺史研究遵循史料来源报告规范",
    },
    conventions=(
        "样片信息（尺码、面料、工艺版本、制作日期）须完整",
        "缝制工艺（针码、缝份、工艺步骤）须以标准符号或明确文字标注",
        "面料克重、悬垂、拉伸、透气等性能参数须给出数值与测量标准（如 ISO/GM 号）",
        "试样照片须含正面/背面/关键部位特写，尺度参照物清晰",
        "涉及人体测量的研究须报告测量人数、性别、年龄段与标准",
    ),
    key_venues=(
        "International Journal of Fashion Design, Technology and Education",
        "Clothing and Textiles Research Journal",
        "Journal of Industrial Textile Science",
        "Textile Research Journal",
        "Fashion, Textiles and Culture",
        "Journal of Fashion Marketing and Management",
        "International Journal of Fashion Studies",
    ),
    units_and_formulas_notes=(
        "长度用 mm 或 cm；面积用 cm²；质量用 g 或 g/m²",
        "针码密度用 stitches/cm 或 SPI",
        "时间用 分:秒 或 秒",
        "面料幅宽、克重须注明来源与检测方法",
        "所有工艺参数首次出现时给出符号与单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gerber Accumark", "Gerber AccuMark 3D", "CLO 3D", "Lectra Modaris", "Lectra Diamino", "Tukatech", "Optitex", "Browzwear VStitcher", "Marvelous Designer", "Tailor's CAD (V4)", "Style3D", "Kronos 3D Designer", "InkStitch", "LibreCAD", "Inkscape", "Adobe Illustrator", "Adobe Photoshop", "SolidWorks", "Fusion 360", "PatternMaster SE", "Digital Pattern Lab", "Tailor's CAD", "Krita", "GIMP", "WishList Collection Manager"),
    category="艺术学",
    databases=("DOAJ", "OpenAlex", "Crossref", "CNKI"),
)
