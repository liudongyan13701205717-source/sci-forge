"""工业绳索作业（abseiling）论文支持：高空作业、工业下降技术、救援与设备性能研究。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="industrial_abseiling",
    aliases=("industrial_abseiling", "工业绳索作业", "industrial_ropes_access", "technical_rescue", "high_angle_rescue", "绳索下降技术", "industrial_climbing", "technical_abseiling", "IRATA/SPRAT"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 IEEE（工程类）",
    reporting_standards={"incident_analysis": "事故分析须遵循 HSE/OSHA 事故报告规范", "equipment_test": "装备测试须按 EN 564/EN 12278/ANSI 1048 标准并给出置信区间", "fieldwork": "现场调查须遵循 ISO 45001 安全规程与 IRATA/SPRAT 分级"},
    conventions=("设备型号须标注制造商与认证标准", "载荷测试报告以 kN 与静态倍数表达", "术语遵循 EN/ANSI 规范", "案例报告须匿名并遵循安全规程", "图像须标注拍摄条件与视角"),
    key_venues=("Journal of Occupational Safety and Health", "International Journal of Industrial Ergonomics", "Work, Construction & Occupational Safety", "Journal of Safety Research", "Safety Science"),
    units_and_formulas_notes=("载荷以 kN 表示，倍数以 ×SOL 表达", "绳索直径以 mm、直径系数以 D 表示", "高度以 m、坠落因子以 FF 表达", "摩擦系数以 μ 无量纲表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSI/ASME B30.9", "EN 564 测试台", "力传感器（Load Cell）", "加速度计", "高速摄像机", "CAD SolidWorks", "ANSYS", "MATLAB", "R", "Python", "SPSS", "Motion Capture（Vicon）", "KineSys", "Tableau", "Microsoft Excel", "Zoom", "Drone (DJI)", "NVivo", "LaTeX", "EndNote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
