"""酿造工艺学科论文支持：啤酒发酵/工艺优化体裁、食品科学引用样式与酿造记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="brewing",
    aliases=(
        "brewing",
        "Brewing",
        "酿造",
        "啤酒酿造",
        "精酿啤酒",
        "发酵工艺",
        "酿造工程",
        "啤酒工艺",
        "饮料工程",
        "craft brewing",
        "fermentation",
        "brewing technology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（原料、工艺、发酵条件、检测）",
            "results（理化、风味、感官）",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical background",
            "main developments",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7（食品科学/工程引用样式）",
    reporting_standards={
        "materials": "原料（麦芽、酵母、水质）须完整报告",
        "process": "糖化、煮沸、发酵、过滤条件须完整",
        "measurements": "理化指标（原麦汁浓度、酒精度、苦度）须报告",
        "sensory": "感官评分标准与评估者须明确",
    },
    conventions=(
        "原麦汁浓度用 °P（Plato 或 Balling）标记",
        "酒精度用 % vol 报告",
        "苦度用 IBU 报告",
        "酵母用 Saccharomyces 属学名（S. cerevisiae）",
        "温度用 ℃ 全文一致",
    ),
    key_venues=(
        "Journal of the Institute of Brewing",
        "Brewing Science",
        "Journal of Brewing",
        "Food Chemistry",
        "LWT - Food Science and Technology",
        "Journal of Cereal Science",
        "Food Research International",
    ),
    units_and_formulas_notes=(
        "原麦汁浓度 °P（Plato 或 Balling）",
        "酒精度 % vol",
        "苦度 IBU",
        "温度 ℃，压力 kPa",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("BeerSmith", "Bru'n Water", "Brewtarget", "Promash", "Gas Chromatograph (GC)", "GC-MS", "HPLC", "NMR", "Refractometer", "Hydrometer", "pH Meter", "Colorimeter", "Turbidity Meter", "Viscometer", "Spectrophotometer", "Brewer's Thermometer", "Fermentation Monitor", "Yeast Starter Kit", "Fermentation Chamber", "Fermentation Temperature Controller"),
    category="工学",
    databases=("OpenAlex", "ScienceDirect", "Elsevier", "Google Scholar", "arXiv"),
)
