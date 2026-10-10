"""医疗技术学科论文支持：医学仪器与诊断技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_technology",
    aliases=("medical_technology", "医疗技术", "diagnostic tech", "imaging", "medical devices", "检测技术", "影像技术"),
    paper_types={
        "research": ("abstract", "introduction（技术背景）", "methodology（设备与方法）", "results（性能数据）", "discussion（应用价值）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（技术原理）", "results（效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技术概览）", "evidence synthesis（对比分析）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "设备参数须注明型号与校准状态", "k2": "诊断性能须报告敏感度/特异度/PPV/NPV", "k3": "临床试验须注册并声明主要/次要结局"},
    conventions=("设备名称首次出现标注全称", "图像须附 scale bar", "统计检验须声明方法", "单位使用 SI 制", "风险声明须包含局限性"),
    key_venues=("Radiology", "Medical Physics", "Journal of Medical Systems", "IEEE Transactions on Biomedical Engineering", "Ultrasound in Medicine & Biology"),
    units_and_formulas_notes=("辐射剂量以 mSv 计", "图像分辨率以 mm/px 或线对/cm", "统计以 mean±SD 报告", "灵敏度 = TP/(TP+FN)", "特异度 = TN/(TN+FP)"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Siemens CT Scanner", "GE MRI System", "Ultrasound Machine", "X-ray Detector", "PET Scanner", "Endoscope", "Catheter Lab Equipment", "ECG Machine", "Blood Analyzer", "PCR System", "Mass Spectrometer", "GraphPad Prism", "MATLAB", "ImageJ", "OpenCV", "SPSS", "R", "Python (scikit-learn)", "LabVIEW", "3D Printing"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
