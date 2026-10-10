"""塑料制造学科论文支持：注塑/挤出/吹塑/模具设计体裁、ASE 引用样式与塑料制造记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plastic_manufacturing",
    aliases=("plastic_manufacturing", "塑料制造", "塑料加工", "plastics manufacturing", "塑料成型", "plastics processing", "注塑成型", "injection molding", "挤出成型", "extrusion molding", "吹塑成型", "blow molding", "模具设计", "mold design"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（工艺与实验方法）", "results（工艺与性能数据）", "discussion（工艺与产品意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例与产品）", "analysis（工艺与模具）", "results（性能与经济性）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（塑料加工工艺综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASE 样式（作者-年份；Polymer Engineering & Science 遵循 ASE 规范）",
    reporting_standards={"ISO 3053": "塑料注塑工艺规范", "ASTM D638": "塑料拉伸测试", "ASTM D648": "热变形温度测试", "ASTM D1238": "熔体流动速率测试", "ISO 1147": "塑料标记与分类"},
    conventions=("塑料材料标注牌号与牌号（如 PP 5010A、ABS G-16）", "工艺参数（温度、压力、速度、时间）须完整", "熔体流动速率 MFR g/10min 须报告", "模具材料与热处理须注明", "产品性能（拉伸强度、模量、断裂伸长率）标准化"),
    key_venues=("Polymer Engineering & Science", "Journal of Applied Polymer Science", "Additive Manufacturing", "Composites Part A", "先进塑料"),
    units_and_formulas_notes=("温度 ℃；压力 MPa；速度 mm/s", "时间 s；周期 min/shot", "MFR g/10min；MFRD g/10h", "拉伸强度 MPa；模量 GPa；断裂伸长率 %"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "Fusion 360", "CATIA", "Siemens NX", "PTC Creo", "ANSYS Fluent", "ANSYS CFX", "Autodesk Moldflow Adviser", "Autodesk Moldflow Xpert", "Moldflow Plastics Adviser", "Engel EasyNet", "KraussMaffei K-STAR", "ENGEL iMOVE", "Sumitomo Shizumi Controller", "Haitian Smart Control", "Haitian Intelligent Controller", "Engel MC 08", "ENGEL iMOVE Pro", "KraussMaffei K200 Controller"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
