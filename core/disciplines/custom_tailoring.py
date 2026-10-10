"""Custom tailoring 学科论文支持：定制裁剪/成衣设计与版型工艺体裁、服饰工程报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="custom_tailoring",
    aliases=(
        "custom_tailoring",
        "custom tailoring",
        "bespoke tailoring",
        "定制裁剪",
        "服装定制",
        "高级定制",
        "bespoke garment making",
        "pattern drafting",
        "裁缝工艺",
        "made-to-measure clothing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与动机）",
            "materials and methods（面料、制版与工艺方法）",
            "results（试穿结果与测量数据）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "technical_study": (
            "abstract",
            "introduction",
            "specification（工艺规格：版型、用料、工序）",
            "process record（工序记录）",
            "fit evaluation（合身度评价）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review（版型与工艺综述）",
            "trends and challenges（趋势与挑战）",
            "references",
        ),
    },
    citation_style="APA 第7版；工程技术类成果遵 IEEE 样式",
    reporting_standards={
        "anthropometry": "人体测量须报告测量点定义、姿势标准、量具精度与重复次数",
        "fit": "合身度评价须采用统一量表（如 5 级合身度评分）并报告评分者一致性",
        "measurements": "成品尺寸须声明量测部位、方法与容差（mm）",
        "materials": "面料须报告成分、克重、幅宽、幅向/纬向缩率与色号",
        "reproducibility": "制版参数须可复现（基础尺寸 + 放量/收量值）",
    },
    conventions=(
        "尺寸统一用 cm（或 mm，须全文一致），容差用 ±mm 表述；不得与英寸混用",
        "制版参数须给出「基准尺寸 + 放量（ease）值」，放量按部位分项列示",
        "面料参数完整报告：成分、克重 g/m²、幅宽 cm、缩率 %、色号（Pantone）",
        "工序按编号顺序记录，关键工序标注设备与参数（如缝纫机型号、针距 mm）",
        "图片展示须标明拍摄角度、光线条件与是否含后整理",
        "合身度与舒适性评分须说明评分者、量表与统计口径",
    ),
    key_venues=(
        "Journal of the Textile Institute",
        "Clothing and Textiles Research Journal",
        "Journal of Fashion Marketing and Management",
        "Fashion and Textiles",
        "IATMI (The International Association of Textile Manufacturers and Industry)",
        "International Journal of Design",
        "纺织学报",
    ),
    units_and_formulas_notes=(
        "长度用 cm/mm；面积用 cm² 或 m²；重量用 g/g/m²（克重）",
        "缩率用 %（湿/干、经/纬分别报告）",
        "针距用 mm/针，缝纫线张力用 cN 或 N",
        "色号引用 Pantone 系列时须注明介质（TPG/TCX/S）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AccuMark (Gerber)", "Modaris (Lectra)", "Optitex", "Kaledo", "CLO 3D", "Style3D (Bozhi Technology)", "Marvelous Designer", "WONDER 3D", "Bozzano 3D", "Browzwear", "NuCompare", "VScan 4D", "3DLOOK", "Shining 3D", "Garment Scanner (Lectra)", "Adobe Illustrator", "AutoCAD", "Pantone Match System", "X-Rite i1Pro2", "TexScan (SGS)", "WGSN", "Heuritech", "Juki DDL-8700Q", "JUKI HVL-036F", "Pfaff 7740"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Scopus", "Web of Science", "Google Patents"),
)
