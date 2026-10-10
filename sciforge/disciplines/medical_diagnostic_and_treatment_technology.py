"""医学诊断与治疗技术学科论文支持：影像技术、介入治疗技术与诊断设备体裁注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_diagnostic_and_treatment_technology",
    aliases=("medical_diagnostic_and_treatment_technology", "医学诊断与治疗技术", "medical imaging technology", "介入治疗技术", "interventional radiology", "diagnostic imaging", "医学影像技术", "nuclear medicine technology", "endoscopy technology"),
    paper_types={
        "research": ("abstract", "introduction（技术背景与临床需求）", "methods（设备参数与成像方法）", "results（影像质量与诊断效能）", "discussion（技术优化与临床转化）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与技术背景）", "analysis（影像/操作技术评估）", "results（诊断/治疗结果）", "discussion（技术改进）", "references"),
        "review": ("abstract", "introduction", "technology overview（技术综述）", "evidence synthesis（技术证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "imaging": "医学影像报告遵循 DICOM（PS3.3）与 ACR 标准",
        "interventional": "介入放射学遵循 SIR 安全指南",
        "nuclear_medicine": "核医学遵循 EANM/SNMMI 指南",
        "endoscopy": "内镜报告遵循 ESGE 或 JGES 指南",
        "ultrasound": "超声报告遵循 AIUM 或 WFUMB 指南",
    },
    conventions=(
        "设备型号、参数（管电压、管电流、层厚）须注明",
        "造影剂种类、剂量、注射速率须报告",
        "影像测量须注明体位与呼吸相位",
        "介入手术须报告操作时间、造影剂用量与并发症",
        "核医学须报告注射剂量、采集时间与重建参数",
    ),
    key_venues=(
        "Radiology",
        "AJR: American Journal of Roentgenology",
        "Investigative Radiology",
        "European Radiology",
        "Cardiovascular and Interventional Radiology",
        "Journal of Nuclear Medicine",
        "Endoscopy",
    ),
    units_and_formulas_notes=(
        "CT 值用 HU；MRI 信号强度用相对值；PET SUV 用无量纲",
        "剂量用 mGy（CT）或 mSv（介入/核医学）",
        "内镜发现须注明解剖位置与病理分级",
        "超声测量须注明探头频率与深度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CT Scanner", "MRI Scanner", "PET Scanner", "SPECT Scanner", "Digital X-ray Machine", "Mammography Machine", "Ultrasound System", "Digital Angiography (DSA)", "Endoscope (Upper GI/Colonoscopy)", "Bronchoscope", "Laparoscope", "Arthroscope", "Cystoscope", "Radioisotope Generator", "Linear Accelerator (Gamma Knife)", "Brachytherapy System", "Fluoroscopy System", "CT Simulation System", "Image Reconstruction Software", "PACS (Picture Archiving and Communication System)"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
