"""口腔外科学科论文支持：颌面外科、种植外科、正颌手术与影像诊断。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oral_surgery",
    aliases=("oral_surgery", "口腔外科", "口腔颌面外科", "Oral & Maxillofacial Surgery", "Maxillofacial Surgery", "Dental Surgery", "牙外科", "种植外科", "Orthognathic Surgery"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"CONSORT": "CONSORT 临床试验报告规范", "STARD": "STARD 诊断研究规范", "STROBE": "STROBE 观察性研究规范"},
    conventions=("采用临床命名与诊断标准（ICD-11、ICOP）", "影像测量遵循 ICRS 与 AAPM 标准", "伦理批件编号与注册号必须报告", "随访时间点标准化（3、6、12 月）", "并发症发生率与疼痛评分（VAS）报告完整"),
    key_venues=("Journal of Oral and Maxillofacial Surgery", "Oral Surgery Oral Medicine Oral Pathology", "Journal of Dentistry", "Clinical Oral Investigations", "DentoMaxilloFacial Radiology"),
    units_and_formulas_notes=("长度 mm、骨密度 g/cm³、辐射剂量 mGy", "CBCT 分辨率以 μm/pixel 表示", "种植体稳定性 ISQ 单位以 SHA 报告", "VAS 疼痛评分 0–10 分"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Carestream CS 9600 CBCT", "NewTom GO! CBCT", "3D Slicer", "DolphinViewer", "InVivo Dental Suite", "Materialise Mimics", "Geomagic Design X", "exocad dentalCAD/CAM", "3D Systems ProJet 3D 打印机", "Stryker Navigation System", "SolidWorks", "ANSYS Workbench", "MATLAB", "Python", "R", "SPSS", "JASP", "LaTeX", "Microsoft Excel", "ImageJ/Fiji"),
    category="医学",
    databases=("OpenAlex", "Crossref", "PubMed", "Cochrane Library"),
)
