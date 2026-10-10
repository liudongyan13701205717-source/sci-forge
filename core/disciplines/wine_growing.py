"""酿酒葡萄种植学科论文支持：葡萄园管理、栽培技术与品质调控研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wine_growing",
    aliases=(
        "wine growing",
        "酿酒葡萄种植",
        "葡萄栽培",
        "葡萄园管理",
        "viticulture",
        "vineyard management",
        "grape cultivation",
        "酿酒葡萄栽培",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "study area and materials（研究区域与材料）",
            "methods（栽培管理与采样方法）",
            "results（品质指标与产量结果）",
            "discussion（品质调控机理讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "vineyard description（葡萄园概况描述）",
            "management practices（栽培管理措施）",
            "harvest and quality evaluation（采收与品质评价）",
            "economics and sustainability（经济性与可持续性）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "varietal adaptation（品种适应性综述）",
            "training systems（架式与整形技术综述）",
            "canopy management（群体管理综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "vineyard description": "须报告纬度/海拔/坡度/坡向、土壤类型与理化性质",
        "cultivar and rootstock": "葡萄品种与砧木须标注（如赤霞珠/3309C 砧木）",
        "sampling protocol": "采样须说明株数、果穗位置、采样时间与重复次数",
        "analytical methods": "品质分析须标注方法标准（如 AOAC/国标/文献引用）",
    },
    conventions=(
        "品种名首次出现时标注中文名与拉丁学名（如赤霞珠 Cabernet Sauvignon）",
        "产量单位 t/ha；果穗重量单位 g；单果重单位 g",
        "可溶性固形物单位 °Bx；总酸单位 g/L（以酒石酸计）",
        "土壤质地按 USDA 或中国土壤分类标注",
        "温度数据区分月均温/年均温/生长季积温（≥10℃）",
    ),
    key_venues=(
        "American Journal of Enology and Viticulture",
        "Journal of the Science of Food and Agriculture",
        "Agriculture journal (MDPI)",
        "Acta Horticulturae",
        "South African Journal of Enology and Viticulture",
    ),
    units_and_formulas_notes=(
        "生长季积温（GDD）= Σ(Tmax+Tmin)/2（℃·天，≥10℃）",
        "光合有效辐射（PAR）单位 mol·m⁻²·s⁻¹",
        "土壤含水量单位 % 或 mm（体积含水量）",
        "灌溉定额单位 mm 或 m³/ha",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("土壤质地分析仪（激光粒度分析仪）", "土壤水分测定仪（TDR 时域反射仪）", "便携式土壤养分速测仪", "葡萄叶片叶绿素仪（如 SPAD-501）", "果实可溶性固形物计（手持糖度计）", "果实总酸测定仪（滴定法/HPLC）", "葡萄园气象站（气象自动监测站）", "土壤墒情监测仪（原位监测）", "无人机遥感系统（NDVI 植被指数）", "遥感卫星（Sentinel-2、Landsat）", "葡萄园灌溉控制系统（水肥一体化）", "激光叶面积仪（LI-3100C）", "便携式叶绿素荧光仪（如 PAM-200）", "近红外光谱仪（NIR 品质快速检测）", "LaTeX 学术排版", "EndNote 文献管理", "Python 数据处理（pandas）", "R 语言统计分析", "SPSS 统计分析软件", "QGIS 葡萄园 GIS 分析"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
