"""光学假体学科论文支持：义眼、隐形眼镜、角膜接触镜与视力假体光学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optical_prosthetics",
    aliases=("optical_prosthetics", "光学假体", "义眼", "Optical Prosthetics", "ocular prosthetics", "eye prosthesis", "contact lens prosthetics", "义眼学", "视觉假体光学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"CONSORT": "CONSORT 临床试验报告规范", "STARD": "STARD 诊断研究规范", "PRISMA": "PRISMA 综述规范"},
    conventions=("采用临床命名与诊断标准（ICD-11、ICOP）", "光学参数用临床单位（mm、D、°C）", "伦理批件编号与注册号必须报告", "假体适应症、禁忌症与并发症完整报告", "随访时间点标准化并给出置信区间"),
    key_venues=("Investigative Ophthalmology & Visual Science", "American Journal of Ophthalmology", "Acta Ophthalmologica", "Journal of Prosthetics and Orthotics", "Biomedical Optics Express"),
    units_and_formulas_notes=("长度 mm、屈光度 D、角膜曲率以 R1/R2 表示", "屈光度换算 D = 1/f（m）", "等效球镜 SE = 球镜 + 柱镜/2", "随访时间点标准化（1 天、1 周、1 月、3 月、6 月、12 月）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Synopsys Zemax OpticStudio", "Synopsys Code V", "SolidWorks", "ANSYS Workbench", "Blender", "FreeCAD", "Autodesk Fusion 360", "3D 打印机 (SLA/DLP)", "StructureX 3D Scanner", "Heine Lambda 眼底相机", "SD-OCT 光学相干断层扫描", "EyeLink 眼动追踪仪", "MATLAB", "Python", "R", "SPSS", "JASP", "ImageJ/Fiji", "LaTeX", "Microsoft Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "PubMed", "Cochrane Library"),
)
