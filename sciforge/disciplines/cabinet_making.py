"""家具制造/木工学科论文支持：板式家具、木材加工、CNC 设计与木材科学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cabinet_making",
    aliases=(
        "cabinet_making",
        "木工",
        "家具制造",
        "家具制作",
        "板式家具",
        "家具工程",
        "Cabinet Making",
        "Woodworking",
        "Furniture Making",
        "Furniture Engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review",
            "materials and methods",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "product_design": (
            "abstract",
            "introduction",
            "design brief（设计任务书）",
            "concept design",
            "prototyping（样机）",
            "testing and evaluation",
            "conclusion",
            "references",
        ),
        "wood_science": (
            "abstract",
            "introduction",
            "materials",
            "methods（力学/理化/干燥检测）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 或 GB/T 7714；木材期刊多采用 Wood Science and Technology 体例",
    reporting_standards={
        "wood_test": "木材检测须注明树种、含水率、试样规格与检测方法（ASTM、GB）",
        "manufacturing": "加工工艺须说明设备型号、刀具参数、切削速度",
        "design": "设计研究须说明设计任务书、材料与工艺约束",
        "ergonomics": "人机工程须报告被试数、任务与测量指标",
    },
    conventions=(
        "木材尺寸须以 mm 报告并注明含水率",
        "力学性能须注明检测方向（顺纹/横纹/径向/切向）",
        "木材等级须使用 FSC/PEFC 或国标分级",
        "CNC 加工须说明刀具、进给速度、主轴转速",
    ),
    key_venues=(
        "Wood Science and Technology",
        "Construction and Building Materials",
        "International Journal of Wood Science",
        "The International Journal of Advanced Manufacturing Technology",
        "Journal of Wood Chemistry and Technology",
        "Wood Fiber Science",
        "Journal of Materials Science - Materials in Engineering",
        "木材科学与技术",
        "家具",
        "林产工业",
    ),
    units_and_formulas_notes=(
        "尺寸以 mm 报告",
        "木材力学性能以 MPa 报告",
        "含水率以 % 报告",
        "加工速度以 m/min 或 mm/min 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Homag CNC 木工雕刻机", "Biesse CNC", "Felder CNC", "Festool 电木工具套装", "Makita", "DeWalt", "Hitachi 电动工具", "台锯（Table Saw）", "带锯（Band Saw）", "平刨（Jointer）", "压刨（Planer）", "镂铣机（Router）", "榫眼机（Mortiser）", "封边机（Edgebander）", "SolidWorks", "AutoCAD", "SketchUp", "Fusion 360", "Rhinoceros 3D", "V-Ray", "KeyShot", "Woodshop Manager", "Cabinet Vision", "HAFAS Software", "Pinpoint Pro 木材湿含量仪", "数显卡尺", "甲醛检测仪", "Microsoft Excel", "MATLAB"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "ScienceDirect", "DOAJ"),
)
