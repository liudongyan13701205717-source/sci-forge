"""鞍具制作学科论文支持：鞍具工艺/马术装备制造/皮革加工体裁与鞍具设计注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="saddlery",
    aliases=("saddlery", "鞍具制作", "鞍具工艺", "马具制造", "皮革鞍具", "harness making", "saddle making", "皮革加工"),
    paper_types={
        "research": ("abstract", "introduction（研究背景与鞍具问题）", "methodology（材料与工艺设计）", "results（测试结果）", "discussion（性能与应用讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（鞍具案例背景）", "analysis（工艺与结构分析）", "results（使用效果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（鞍具设计综述）", "evidence synthesis（工艺对比）", "future directions", "references"),
    },
    citation_style="Chicago（制造业与手工技艺研究常用 Chicago 风格）",
    reporting_standards={"case_study": "案例研究遵循 COREQ 报告规范", "survey": "使用者问卷遵循 SAPOR 规范", "workshop": "工坊实践遵循工艺记录惯例"},
    conventions=("鞍具尺寸须给出公制与国际马联单位", "材料规格须给出皮张等级与厚度", "承重/疲劳试验须给出载荷曲线", "马体接触面生物力学分析须引用兽医评估", "工艺步骤须配工艺流程图"),
    key_venues=("Journal of the Royal Society of Medicine (Veterinary Section)", "Journal of Equine Veterinary Science", "Journal of Leather Science and Technology", "Journal of Industrial Textiles", "Leather and Faerie (Craft Guild) Proceedings", "Equestrian Science Journal"),
    units_and_formulas_notes=("厚度以 mm 记，皮张等级给出 hide grade 与 T 值", "强度以 MPa 或 kg/cm² 表示", "载荷曲线给出 N–mm 关系", "工艺参数给出温度 °C 与压力 bar"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SolidWorks", "AutoCAD", "Rhinoceros 3D", "Fusion 360", "InkScape", "Adobe Illustrator", "MATLAB", "OriginLab", "Universal Testing Machine (Instron)", "Leather Tensile Tester (ZwickRoell)", "Moisture Analyzer (Kett)", "Colorimeter (Konica Minolta CM-3600)", "Pressure Mapping (Tekscan)", "Saddle Pressure Pad System", "Horse Motion Capture (Vicon)", "Leather Steaming Machine", "Leather Cutting Press", "Saddle Sewing Machine (Bartholetti)", "Leather Skiving Machine", "Leather Hot Edge Press"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
