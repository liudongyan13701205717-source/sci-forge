"""放射技术学科论文支持：影像检查、放射防护与影像诊断技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radiography",
    aliases=("radiography", "放射技术", "radiography", "放射影像", "medical radiography", "影像技术", "放射技师", "radiologic technology", "医学影像技术"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "RCR 影像质量评估报告规范", "k2": "ICRP 放射防护建议", "k3": "GBZ 158-2013 放射工作人员职业健康监护规范"},
    conventions=("影像检查使用标准体位与投照条件", "剂量参数须列出 kV、mAs 与 mGy", "解剖部位须用标准解剖术语", "防护剂量须区分患者与操作者", "参考文献按 Vancouver 著录"),
    key_venues=("Radiography", "Journal of Radiological Science", "European Journal of Radiology", "放射学杂志", "中华放射学杂志"),
    units_and_formulas_notes=("辐射剂量使用毫西弗（mSv）", "X 线管电压使用千伏（kV）", "曝光量使用毫安秒（mAs）", "图像分辨率使用线对/厘米（lp/cm）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GE Digital Radiography System", "Siemens Digital Radiography", "Philips Digital Radiography", "Canon Medical DR System", "Fujifilm DR System", "Carestream DR System", "Kodak DR System", "Portable Mobile X-ray", "Hologic Selenia Mammography", "GE Revolution CT Scanner", "Siemens Magnetom MRI Scanner", "GE Voluson Ultrasound", "Siemens Biograph PET/CT", "C-Arm Fluoroscopy", "Carestream PACS System", "RIS System", "DICOM Viewer", "Agfa PACS", "Philips PACS", "DoseCalibur Dose Calculator"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
