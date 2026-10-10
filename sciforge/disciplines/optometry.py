"""视光学学科论文支持：屈光、接触镜、临床眼科学验光与视觉功能评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optometry",
    aliases=("optometry", "视光学", "验光", "Clinical Optometry", "Clinical Vision Science", "Vision Science", "Contact Lens Optometry", "接触镜学", "视觉科学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"CONSORT": "CONSORT 临床试验报告规范", "STARD": "STARD 诊断研究规范", "PRISMA": "PRISMA 综述规范"},
    conventions=("使用临床命名与诊断标准（ICD-11）", "光学参数用临床单位（mm、D、°C、°）", "伦理批件编号与注册号必须报告", "视觉功能测试遵循 ISO/IEC 17142", "随访时间点标准化并给出置信区间"),
    key_venues=("Optometry and Vision Science", "British Journal of Ophthalmology", "Contact Lens & Anterior Eye", "Ophthalmic & Physiological Optics", "Eye and Vision"),
    units_and_formulas_notes=("长度 mm、屈光度 D、视力以小数或 logMAR 表示", "屈光度换算 D = 1/f（m）", "等效球镜 SE = 球镜 + 柱镜/2", "logMAR = -log₁₀(小数视力)"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Retinomax i-master 电脑验光仪", "Nidek ARK-530 自动验光仪", "Topcon TRC-5000 眼底相机", "Zeiss Cirrus HD-OCT", "Humphrey Visual Field 视野计", "Oculus Pentacam ACR 角膜地形图仪", "Zeiss Wavefront Sensor", "EyeLink 1000+ 眼动追踪仪", "Tonomat 眼压计", "裂隙灯显微镜", "MATLAB", "Python", "R", "SPSS", "JASP", "Synopsys Zemax OpticStudio", "LaTeX", "Microsoft Excel", "ImageJ/Fiji", "Oculus Corvis ST 角膜生物力学分析仪"),
    category="医学",
    databases=("OpenAlex", "Crossref", "PubMed", "Cochrane Library"),
)
