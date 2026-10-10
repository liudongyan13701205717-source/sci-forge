"""管道装配学科论文支持：管道应力分析/工程图/管道设计体裁、ASME 引用样式与管道装配记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pipe_fitting",
    aliases=("pipe_fitting", "管道装配", "管道安装", "piping installation", "管道工程", "piping engineering", "工艺管道", "process piping", "压力管道", "pressure piping", "管道预制", "pipe fabrication"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASME 样式（国内期刊遵循 GB/T 7714）",
    reporting_standards={"ASME B31.3": "化工与工艺管道规范", "ASME B31.1": "动力管道规范", "GB 50235": "工业金属管道工程施工规范", "API 6A": "钻井与完井设备", "NACE MR0175": "硫化氢服务材料"},
    conventions=("管径用 NPS/DN 标注（英寸/公称直径）", "壁厚用 Sch40、STD 或具体 mm 表示", "材料与等级（Grade、Class）须注明", "法兰标准（ANSI/BS/DIN）须说明", "焊口编号与焊缝位置须记录"),
    key_venues=("Journal of Pressure Vessel Technology", "Journal of Engineering Materials and Technology", "ASME Journal of Piping", "管道技术", "压力管道与安全"),
    units_and_formulas_notes=("管径 mm/in（NPS、DN）", "壁厚 mm；压力 MPa", "流速 m/s；流量 m³/h", "温度 ℃；应力 MPa"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "AutoCAD Plant 3D", "AutoCAD P&ID", "Revit MEP", "SolidWorks", "AVEVA E3D Design", "Intergraph SmartPlant 3D", "SmartPlant 3D", "CADWorx", "SmartPlant Foundation", "PipeMaker", "SmartPlant Instrument", "PDMS", "CAESAR II (Bentley)", "ProDESIGNer", "Mepworks", "Aspen HYSYS", "PipeStress", "PipeFlex", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
