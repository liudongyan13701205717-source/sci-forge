"""金属装配、车削与机加工学科论文支持：机加工与装配工艺。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metal_fitting_turning_and_machining",
    aliases=("metal_fitting_turning_and_machining", "金属装配车削与机加工", "machining", "fitting", "lathe", "CNC", "精密加工", "装配"),
    paper_types={
        "research": ("abstract", "introduction（工艺背景）", "methodology（试验设计）", "results（加工数据）", "discussion（工艺改进）", "references"),
        "case_study": ("abstract", "introduction", "case description（加工案例）", "analysis（误差分析）", "results（精度结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（机加工理论）", "evidence synthesis（工艺对比）", "future directions", "references"),
    },
    citation_style="ASME",
    reporting_standards={"k1": "切削试验须报告刀具牌号、前角与冷却方式", "k2": "尺寸精度须注明测量仪器与公差等级", "k3": "表面粗糙度须注明评定长度与测量方向"},
    conventions=("材料牌号按标准标注（GB/ASTM/DIN）", "工艺参数注明单位（mm/min、rpm、mm）", "尺寸公差按 ISO 286 标注", "表面粗糙度以 Ra 报告", "刀具磨损数据须注明磨损带长度"),
    key_venues=("International Journal of Machine Tools and Manufacture", "Journal of Manufacturing Processes", "Precision Engineering", "CIRP Annals", "International Journal of Advanced Manufacturing Technology"),
    units_and_formulas_notes=("切削速度 m/min，进给 mm/rev，切深 mm", "表面粗糙度 Ra μm，公差 μm", "材料去除率 MRR = v×f×d×60", "刀具寿命以切削长度 m 报告", "统计以均值±标准差报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CNC Lathe", "Milling Machine", "Grinding Machine", "EDM (Wire Cut)", "Turning Center", "Coordinate Measuring Machine", "Surface Roughness Tester", "Tool Tread", "Cutting Machine", "Spectrometer", "Ansys", "MATLAB", "SolidWorks", "Fusion 360", "Mastercam", "Excel", "OriginLab", "GraphPad Prism", "SPSS", "EndNote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
