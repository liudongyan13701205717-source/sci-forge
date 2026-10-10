"""给排水工程论文支持：管网水力设计、污水输送、水质管理与市政基础设施。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plumbing",
    aliases=("plumbing", "给排水工程", "管道工程", "Plumbing Engineering", "Piping Engineering", "建筑给水排水", "建筑给排水", "卫生给排水", "市政给排水", "建筑电气"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASCE 样式（国内期刊遵循 GB/T 7714）",
    reporting_standards={"GB 50015": "建筑给水排水设计标准", "GB 50282": "室外排水设计标准", "ASME B31.3": "工艺管道规范"},
    conventions=("单位 SI 为主（m³/h、MPa、mm）", "管材标注公称直径 DN", "流量计算遵循海曾-威廉公式或达西-魏斯巴赫公式", "水表与电表须标注精度等级", "排水系统按重力流设计"),
    key_venues=("Journal of Plumbing Science", "给水排水", "Journal of Water Process Engineering", "Desalination", "ASCE Journal of Water Resources Planning and Management"),
    units_and_formulas_notes=("流量 m³/h、L/s、m³/d", "压力 MPa、kPa、bar", "管径 mm（DN 公称直径）", "流速 m/s"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit MEP", "SolidWorks", "WaterCAD", "SewerCAD", "HEC-RAS", "SWMM", "InfoWorks ICM", "Trimble StreetGauge", "Hach Water Quality Tester", "Hach Chlorine Analyzer", "Mag Flow Meter", "Pressure Gauge", "Pipeline Inspection Camera", "MATLAB", "Python (NumPy/SciPy)", "SPSS", "Microsoft Excel", "QGIS", "ArcGIS Pro"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)