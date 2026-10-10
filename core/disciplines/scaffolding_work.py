"""脚手架作业学科论文支持：施工脚手架/高空作业安全/结构工程体裁与安全规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="scaffolding_work",
    aliases=("scaffolding_work", "脚手架作业", "脚手架施工", "高空作业", "scaffolding", "scaffold erection", "脚手架安装", "高空作业安全"),
    paper_types={
        "research": ("abstract", "introduction（脚手架问题）", "methodology（结构与载荷分析）", "results（应力与变形结果）", "discussion（安全控制讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（脚手架案例）", "analysis（结构安全分析）", "results（施工效果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（脚手架综述）", "evidence synthesis（结构对比）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"structural": "结构分析遵循 GB 50017 规范", "safety": "施工安全遵循 ISO 45001 规范", "case_study": "案例研究遵循 COREQ 规范"},
    conventions=("载荷与材料规格须给出标准（钢材牌号）", "脚手架类型须明确（钢管/门式/悬挑）", "节点连接须给出力学模型", "施工安全评估须引用职业安全规范", "有限元分析须给出网格收敛验证"),
    key_venues=("Engineering Structures", "Journal of Construction Engineering and Management", "International Journal of Steel Structures", "Journal of Building Engineering", "Construction Safety Journal", "Journal of Performance of Constructed Facilities"),
    units_and_formulas_notes=("载荷以 kN 记", "应力以 MPa 记", "变形以 mm 记", "网格尺寸以 m 记"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Mechanical", "ABAQUS", "SAP2000", "MIDAS Gen", "STAAD.Pro", "RISA-3D", "Robot Structural", "SolidWorks Simulation", "AutoCAD", "AutoCAD Civil 3D", "Revit", "Navisworks", "MATLAB", "Mathematica", "OriginLab", "Excel", "SPSS", "R", "Load Test Frame (DIN)", "Structural Vibration Analyzer (Bruel & Kjær)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
