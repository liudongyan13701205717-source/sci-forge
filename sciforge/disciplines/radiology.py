"""放射学科论文支持：影像诊断、核医学与介入放射治疗。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radiology",
    aliases=("radiology", "放射学", "radiology", "影像医学", "核医学", "nuclear medicine", "interventional radiology", "介入放射", "医学影像诊断"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "ACR 影像诊断报告规范", "k2": "PIRADS / BI-RADS 报告标准", "k3": "RECs 介入放射伦理报告规范"},
    conventions=("影像诊断使用 ACR 分级标准", "病灶描述须给出大小、位置与强化特征", "影像报告遵循结构化模板", "随访计划须列出时间节点与检查方式", "参考文献按 Vancouver 著录"),
    key_venues=("Radiology", "European Radiology", "Investigative Radiology", "AJR American Journal of Roentgenology", "中华放射学杂志"),
    units_and_formulas_notes=("辐射剂量使用毫西弗（mSv）", "病灶大小使用厘米（cm）", "增强扫描使用碘对比剂 ml/kg", "PET 代谢值使用 SUV"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GE Revolution CT", "Siemens Magnetom MRI", "Philips Ingenia MRI", "Siemens Biograph PET/CT", "GE Discovery PET/CT", "Philips Spectra CT", "Siemens Somatom CT", "Canon Aquilion CT", "GE Optima CT", "Siemens Acuity DSA", "Philips DriPlex Cath Lab", "Interventional Cath Lab", "Siemens Biograph mMR", "Hologic Selenia Mammography", "GE Optima Ultrasound", "GE Voluson Ultrasound", "Gamma Camera (SPECT)", "Varian TrueBeam LINAC", "MIM Treatment Planning System", "PACS & DICOM Viewer"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
