"""陶瓷（工艺）学科论文支持：陶瓷材料/釉料配方/烧成工艺/装饰技术体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ceramics",
    aliases=(
        "ceramics",
        "pottery",
        "porcelain",
        "stoneware",
        "ceramic glaze",
        "ceramic kiln",
        "陶瓷",
        "制陶",
        "瓷器",
        "炻器",
        "陶瓷釉",
        "陶瓷烧成",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料需求与配方设计动机）",
            "materials and methods（原材料、配方与烧成制度）",
            "results（相组成、显微结构与性能）",
            "discussion（工艺-结构-性能关系）",
            "conclusions",
            "references",
        ),
        "materials": (
            "abstract",
            "introduction",
            "formulation and processing（配方与成型工艺）",
            "microstructure and phases（物相与显微结构）",
            "properties and application（性能与应用）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按釉色/装饰/工艺分类）",
            "historical development",
            "state of the art and outlook",
            "references",
        ),
    },
    citation_style="Journal of the American Ceramic Society 样式；材料类引用 Elsevier 编号",
    reporting_standards={
        "glaze": "釉料组成须报告各组分 wt% 与熔融指数（IG）",
        "body": "坯体须报告烧结温度、升温速率与保温时间",
        "firing": "烧成曲线须图示（分段温度-时间）；气氛（氧化/还原）须注明",
        "density": "坯体致密度须报体积吸水率与视密度",
        "decoration": "装饰工艺（青花/斗彩）须说明釉上与釉下、窑次",
    },
    conventions=(
        "釉料组成须报告各组分 wt% 与熔融指数（IG）",
        "坯体须报告烧结温度、升温速率与保温时间",
        "烧成曲线须图示（分段温度-时间）；气氛（氧化/还原）须注明",
        "坯体致密度须报体积吸水率与视密度",
        "装饰工艺（青花/斗彩）须说明釉上与釉下、窑次",
    ),
    key_venues=(
        "Journal of the American Ceramic Society",
        "Ceramics International",
        "Journal of the European Ceramic Society",
        "Clay Minerals",
        "Materials Research Bulletin",
        "中国陶瓷",
    ),
    units_and_formulas_notes=(
        "温度用 ℃；升温速率用 ℃/min；保温时间用 min/h",
        "吸水率用 %；视密度用 g/cm³",
        "釉料配方用 wt% 或 mol% 表示；须注明熔融指数（IG）",
        "XRD 数据须注明 Cu Kα 与扫描步长；SEM 须注明加速电压",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Skutt 电窑", "倒焰窑", "拉坯机", "利坯机", "釉磨球磨机", "施釉喷涂机", "坯体干燥箱", "高温马弗炉", "Hamer 温度曲线控制器", "Bruker D8 X 射线衍射仪", "ZEISS 扫描电子显微镜", "Mettler TGA 热重分析仪", "Micromeritics 比表面仪", "Datacolor 白度仪", "色差仪", "莫氏硬度计", "Stratasys 陶瓷 3D 打印机", "Shining 3D 3D 扫描仪", "KORL 气相法氧化铝粉体", "陶瓷电窑温度记录仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
