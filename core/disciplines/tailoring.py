"""Tailoring 学科论文支持：服装设计与制作、版型/工艺/材料论文体裁、APA 引用样式与服装计量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tailoring",
    aliases=(
        "tailoring",
        "服装设计与制作",
        "制版",
        "服装工艺",
        "custom tailoring",
        "pattern making",
        "garment construction",
        "dressmaking",
        "couture",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与设计问题）",
            "design development（概念、草图与材料研究）",
            "methods（制版、材料与工艺）",
            "results（成衣与穿着测试）",
            "discussion（设计意图与工艺可行性）",
            "references",
        ),
        "design_study": (
            "abstract",
            "introduction",
            "concept and brief",
            "development（打样与迭代）",
            "final construction",
            "critique",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（工艺史与设计史）",
            "technique review",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Fashion and Textile Research、Textile Research Journal 遵循 SAGE/APA 规范）",
    reporting_standards={
        "construction": "成衣工艺须报告：针脚数（SPI）、线迹类型、缝制顺序、辅料清单、工时估算",
        "materials": "面料参数须报告：克重 gsm、经纬纱支数、组织、成分（含涤/棉/麻/羊毛百分比）、拉伸回弹、透湿性",
        "anthropometry": "人体测量须报告：量体方法（静态/动态）、样本人数 n、测量维度与仪器精度",
        "wearability_test": "穿着测试须报告：试样数、试穿者人数、测试时长与场景、评价量表",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "服装部位命名统一（如前片 body front、后片 body back、驳头 lapel、门襟 placket、袖山 cap）",
        "计量单位：长度 cm/mm，面料重 g/m²，纱线支数 Ne 或 Tex，针脚数 SPI（stitches per inch）",
        "线迹代号遵循 ISO 4915（01 回针、02 平缝、03 链式、04 编织、05 覆盖、06 特殊）",
        "版型记法：前片 F、后片 B、袖 L/R、省道 dart 用箭头标示；放缩按 6 号码体系标注",
        "面料缩率、弹性、垂性须注明；图案/配色遵循 Pantone TCX/TPG 色号",
        "设计草图标注尺寸、缝份（seam allowance，通常 1.0–1.5 cm）与工艺细节",
    ),
    key_venues=(
        "Fashion and Textile Research",
        "Textile Research Journal",
        "International Journal of Fashion Design, Technology and Education",
        "Clothing and Textiles Research Journal",
        "Journal of Fibre and Textile Research and Technology",
        "Fashion Practice: The Journal of Design, Creative Arts and Fashion",
    ),
    units_and_formulas_notes=(
        "长度用 cm/mm；面料克重用 g/m²；针脚数用 SPI；温度（熨烫）用 °C；纱线密度用 Tex 或 Ne",
        "版型放量公式：成衣净尺寸 + 放缩量（按款式类别而定）；省道转移量 Δ = 净体 + 松量 - 面料弹性补偿",
        "面料缩率公式：R = (L_0 - L_1)/L_0 × 100%（L_0 为洗涤前长度，L_1 为洗涤后长度）",
        "公式用 amsmath；显示公式仅在正文引用时编号；行内公式避免复杂分式；数值结果给出均值 ± SD",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Modaris", "Lectra Dyvigo", "Optitex CAD", "CLO 3D", "Style3D", "Adobe Illustrator", "Adobe Photoshop", "Gerber AccuMark", "Wild AIMS", "Browzwear", "Vestilo 3D Body Scanner", "Shining3D FreeScan", "Juki 平车", "Juki Coverstitch", "Barudan Interfacer", "Kamakura Embroidery", "BROTHER Overlock", "Kawakami Press", "CASSI Fiber Diameter Analyzer", "Drapery & Draping Table"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Scopus"),
)
