"""枪械制造与修理学科论文支持：枪机配合、精密测量、加工与弹药装填的公差与安全规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gunsmithing",
    aliases=("gunsmithing", "枪械制造", "枪支修理", "firearms manufacturing", "枪机配合", "action fitting", "精密测量", "precision metrology", "弹药装填"),
    paper_types={
        "research": ("abstract", "introduction（枪械缺陷与研究动机）", "methodology（解体、测量与加工方案）", "results（公差、射击精度与强度）", "discussion（配合与加工对性能的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（枪型、故障与作业背景）", "analysis（枪机、复进与膛线分析）", "results（修理后精度与安全检验）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（枪械原理与公差理论）", "evidence synthesis（加工工艺与弹道研究综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"tolerances": "关键配合公差与测量仪器（含分辨率）须报告", "fire_safety": "试验弹种、药量与试射条件须说明，并注明在合规场地进行", "ethics": "涉枪研究须遵守当地法律法规并说明许可编号"},
    conventions=("公差按孔轴公差带与配合代号报告（如 H7/g6）", "射击精度以规定距离弹着散布圆直径（m）报告", "弹种按口径与药量（g）标注", "测量结果保留到仪器分辨率最后一位", "引用军用或行业标准须写明编号与年份"),
    key_venues=("Precision Engineering", "Journal of Manufacturing Processes", "Engineering Failure Analysis", "Journal of Materials Processing Technology", "轻兵器"),
    units_and_formulas_notes=("尺寸用 mm；公差与分散度用 mm 或 μm", "射击精度用散布圆直径（m，如 0.11 m @ 100 m）", "药量用 g；初速用 m/s；枪口动能用 J", "公式用 LaTeX（amsmath）；散布圆直径 = 最远两点距离"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("RockTula", "Brownells Gunsmiths Tool Set", "Accu-Stock", "McMillan Stock Systems", "Boyd's", "Hahn Precision", "Mitutoyo Micrometer", "Mitutoyo Dial Indicator", "Starrett Vernier Calipers", "Mitutoyo Dial Bore Gauge", "Pin and Ring Gauges", "Brownells", "Peregrine Armament", "SolidWorks", "Autodesk Fusion 360", "Haas VF CNC", "Zeiss Calypso CMM", "Speer", "Hornady", "Nosler"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
