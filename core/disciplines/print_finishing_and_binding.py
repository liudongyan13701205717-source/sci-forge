"""印后加工与装订学科论文支持：切纸、折页、装订与覆膜烫印工艺、设备参数与成品质量检验注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="print_finishing_and_binding",
    aliases=("print_finishing_and_binding", "印后加工与装订", "印后工艺", "装订工艺", "print finishing", "印后加工", "bookbinding", "装订", "finishing and binding"),
    paper_types={
        "research": ("abstract", "introduction（印后质量与研究动机）", "methodology（工艺路线、设备参数与试验设计）", "results（成品尺寸、外观与力学性能）", "discussion（工艺参数对质量的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（印件规格、承印物与装订形式）", "analysis（折页、模切、覆膜与装订工艺分析）", "results（成品尺寸与外观检验结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（印后工艺与装订原理）", "evidence synthesis（设备与工艺文献综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"k1": "工艺参数须完整报告（含温度、压力、速度与张数）", "k2": "质量检验须注明标准编号、仪器与判定方法", "k3": "成本与效率须注明统计口径与基准条件"},
    conventions=("纸张规格用 g/m² 表示并注明涂层与白度", "成品尺寸与公差用 mm 表示", "覆膜/烫印须注明材料、工艺与工艺参数", "色彩以 CMYK 或 Pantone 表示并标注白点", "引用标准须写明编号与年份"),
    key_venues=("包装工程", "印刷学报", "印刷工业", "The Color Research and Application", "Packaging Technology and Science"),
    units_and_formulas_notes=("纸张用 g/m²；成品与公差用 mm", "烫印温度用 ℃、压力用 MPa", "色差用 ΔE*ab 并标注白点与观察者角度", "效率用 张/h 或 本/h 表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Heidelberg Speedmaster", "Komori Lithrone", "Roland SM-1000", "Heidelberg Prinect", "EFI Fiery", "Adobe Acrobat Preflight", "HP Indigo", "Xerox iGen", "Canon Vela", "折页机", "自动模切机", "覆膜机", "烫印机", "切纸机", "骑马订与无线胶订设备", "圆版平贴机", "X-Rite i1 Pro 3", "印刷密度计", "EndNote", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
