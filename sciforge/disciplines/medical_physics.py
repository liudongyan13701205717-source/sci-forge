"""Medical physics 学科论文支持：辐射剂量学、医学影像与放疗物理体裁、ICRU/ICRP 规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_physics",
    aliases=("medical_physics", "医学物理", "medical radiological physics", "辐射物理", "放疗物理", "radiotherapy physics", "nuclear medicine physics", "影像物理", "medical imaging physics", "辐射安全", "radiation safety"),
    paper_types={
        "research": ("abstract", "introduction（物理背景与临床需求）", "methods（剂量学测量与物理建模）", "results（剂量数据与物理参数）", "discussion（剂量学与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与物理背景）", "analysis（剂量评估与影像分析）", "results（治疗/诊断结果）", "discussion（物理优化建议）", "references"),
        "review": ("abstract", "introduction", "physics overview（物理原理综述）", "evidence synthesis（剂量学证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver（IEEE 风格亦可）",
    reporting_standards={
        "dosimetry": "剂量学遵循 ICRU 50/62 报告",
        "radiation_protection": "辐射防护遵循 ICRP 103 推荐",
        "radiotherapy": "放疗计划遵循 TG-53/TG-142/AAPM Task Group 规范",
        "imaging_physics": "影像物理遵循 DICOM 与 IEC 61217 标准",
        "nuclear_medicine": "核医学遵循 EANM/SNMMI 指南",
    },
    conventions=(
        "剂量单位统一用 Gy（吸收剂量）/ Sv（当量剂量）/ mSv（有效剂量）",
        "活度用 Bq；线能量传递 LET 用 keV/μm",
        "剂量率用 Gy/min 或 mSv/h；照射时间须注明",
        "探测器校准因子须报告；剂量计类型与能量范围须说明",
        "物理模型须给出方程与参数假设",
    ),
    key_venues=(
        "Medical Physics",
        "Physics in Medicine and Biology",
        "Journal of Medical Physics",
        "Radiotherapy and Oncology",
        "Medical Physics Letters",
        "Medical Dosimetry",
        "Dose and Response",
    ),
    units_and_formulas_notes=(
        "吸收剂量用 Gy；当量剂量用 Sv；有效剂量用 mSv",
        "活度用 Bq；质量能量吸收系数用 cm²/g",
        "线能量传递 LET 用 keV/μm；阻止本领用 MeV·cm²/g",
        "公式用 amsmath；物理量符号须与 ICRU 定义一致",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CT Scanner", "MRI Scanner", "PET Scanner", "SPECT Scanner", "Linear Accelerator", "Brachytherapy Source", "Gamma Camera", "Ion Chamber Dosimeter", "Thermoluminescent Dosimeter", "Optically Stimulated Luminescence Dosimeter", "Radiation Film Dosimeter", "Monte Carlo Simulation (GEANT4/MCNP)", "Treatment Planning System (TPS)", "Dosimetry Phantom", "Imaging Phantom", "Radioisotope Generator", "Dosimetry Reference System", "Quality Assurance (QA) Equipment", "Radiation Shielding Equipment", "Electron Beam Therapy System"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
