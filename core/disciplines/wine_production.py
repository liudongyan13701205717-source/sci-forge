"""葡萄酒酿造学科论文支持：酿酒工艺与发酵控制体裁、ACS 引用样式与酿酒记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wine_production",
    aliases=("wine production", "葡萄酒酿造", "酿酒", "葡萄酒工艺", "葡萄酒酿造学",
             "winemaking", "oenology", "vinification"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与酿酒问题）",
            "materials and methods（原料、工艺与分析方法）",
            "results（发酵、成分与感官数据）",
            "discussion（工艺机理与品质意义）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials and methods（工艺参数与工序）",
            "results（工艺对品质的影响）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份或编号；J. Agric. Food Chem. 遵循 ACS 规范）",
    reporting_standards={
        "analytical": "分析化学须报告方法、仪器、标准品与验证参数",
        "fermentation": "发酵研究须报告酵母菌株、温度与发酵曲线",
        "sensory": "感官评价须报告评价员、标度与统计方法",
        "statistical": "须报告重复数、统计方法与显著性",
    },
    conventions=(
        "葡萄品种须给出学名与品种名（如 Vitis vinifera cv.）",
        "酒精含量用 % v/v；糖度用 °Brix 或 g/L",
        "可滴定酸用 g/L（酒石酸当量）；pH 须报告",
        "SO₂ 用游离/总 mg/L 报告",
        "发酵温度用 °C；酵母菌株须注明",
    ),
    key_venues=(
        "Journal of Agricultural and Food Chemistry",
        "American Journal of Enology and Viticulture",
        "Food Chemistry",
        "Food Research International",
        "Australian Journal of Grape and Wine Research",
        "Molecules",
    ),
    units_and_formulas_notes=(
        "酒精用 % v/v；糖用 °Brix 或 g/L",
        "可滴定酸用 g/L（酒石酸当量）；挥发酸用 g/L（乙酸当量）",
        "SO₂ 用 mg/L；多酚用 mg/L（没食子酸当量）",
        "发酵动力学用 g/L·d；感官评分须说明标度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("气相色谱-质谱联用仪 (GC-MS)", "高效液相色谱 (HPLC)", "紫外-可见分光光度计", "自动滴定仪", "Foss WineScan 葡萄酒分析仪", "pH 计", "密度计 (hydrometer)", "酒精计 (ebulliometer)", "温控发酵罐", "压榨机 (press)", "除梗破碎机 (crusher-destemmer)", "离心机", "膜过滤系统", "橡木桶 (oak barrel)", "SO₂ 分析仪", "酵母活化系统", "氮气保护系统", "Vintrace 酿酒管理软件", "折光仪 (refractometer)", "溶解氧测定仪"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "FSTA"),
)
