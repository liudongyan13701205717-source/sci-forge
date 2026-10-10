"""整形外科论文支持：显微外科、美容整形、皮瓣修复与组织工程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plastic_surgery",
    aliases=("plastic_surgery", "整形外科", "美容外科", "Plastic Surgery", "Cosmetic Surgery", "显微外科", "Reconstructive Surgery", "Microsurgery", "整形与重建外科"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"CONSORT": "CONSORT 临床试验报告规范", "STARD": "STARD 诊断研究规范", "CARE": "CARE 病例报告规范"},
    conventions=("采用 ICD-11 临床命名与诊断标准", "伦理批件编号与注册号必须报告", "随访时间点标准化（3、6、12 月）", "疼痛评分用 VAS 0–10 分", "并发症发生率按 Clavien-Dindo 分级报告"),
    key_venues=("Plastic and Reconstructive Surgery", "Aesthetic Surgery Journal", "British Journal of Plastic Surgery", "Journal of Plastic, Reconstructive & Aesthetic Surgery", "中华整形外科杂志"),
    units_and_formulas_notes=("长度 mm、骨密度 g/cm³、辐射剂量 mGy", "CBCT 分辨率以 μm/pixel 表示", "VAS 疼痛评分 0–10 分", "皮瓣血流量 mL/g·min"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Zeiss Surgical Microscope", "Harmonic Scalpel (Ethicon)", "Fotona 4D Pro", "Cynosure Elite iQ Plus", "Ulthera HIFU", "3D Systems ProJet 3D 打印机", "Materialise Mimics", "exocad Dental CAD/CAM", "SolidWorks", "3D Slicer", "Adobe Photoshop", "SPSS", "R", "Python", "JASP", "MATLAB", "ImageJ/Fiji", "EndNote", "Carestream CS 9600 CBCT", "NewTom GO! CBCT"),
    category="医学",
    databases=("OpenAlex", "Crossref", "PubMed", "Cochrane Library"),
)