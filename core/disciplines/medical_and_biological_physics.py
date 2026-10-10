"""医学与生物物理学科论文支持：医学影像、辐射剂量学体裁与物理建模注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_and_biological_physics",
    aliases=("medical_and_biological_physics", "医学与生物物理", "medical biophysics", "biomedical physics", "生物医学物理", "医学物理", "nuclear medicine physics", "辐射物理", "核医学物理"),
    paper_types={
        "research": ("abstract", "introduction（物理背景与医学动机）", "methodology（实验设计与物理建模）", "results（测量数据与影像结果）", "discussion（物理机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与物理情境）", "analysis（剂量评估与物理分析）", "results（治疗/诊断结果）", "discussion（技术优化）", "references"),
        "review": ("abstract", "introduction", "physics overview（物理原理综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver（IEEE 风格亦可）",
    reporting_standards={
        "imaging": "医学影像遵循 DICOM 标准（PS3.3）",
        "dosimetry": "剂量学遵循 ICRU 50/62 报告",
        "radiation_safety": "辐射安全遵循 ICRP 103 推荐",
        "radiotherapy": "放疗计划遵循 TG-53/TG-142 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "剂量单位统一用 Gy（吸收剂量）/ Sv（当量剂量）",
        "影像质量参数须报告 MTF、CNR、SNR",
        "物理模型须给出数学表述与参数假设",
        "核医学须报告活度（Bq）、半衰期",
        "实验条件（能量、几何、屏蔽）须完整说明",
    ),
    key_venues=(
        "Medical Physics",
        "Physics in Medicine and Biology",
        "Journal of Medical Physics",
        "Medical Physics Letters",
        "Radiotherapy and Oncology",
        "European Journal of Nuclear Medicine and Molecular Imaging",
    ),
    units_and_formulas_notes=(
        "吸收剂量用 Gy；当量剂量用 Sv；活度用 Bq",
        "线性能量转移 LET 用 keV/μm；质量能量吸收系数用 cm²/g",
        "公式用 amsmath；物理量符号须与 ICRU 定义一致",
        "影像分析给出定量指标（如 SUV、CNR）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CT Scanner", "MRI Scanner", "PET Scanner", "Linear Accelerator", "Brachytherapy Source", "Dosimeter (Ion Chamber)", "Dosimeter (Thermoluminescent)", "Dosimeter (OSL)", "Dosimeter (Film)", "Scintillation Camera", "Gamma Camera", "SPECT Scanner", "Nuclear Medicine System", "Radiation Shielding Equipment", "Medical Ultrasound System", "Mammography Machine", "Imaging Phantoms", "Monte Carlo Simulation (GEANT4/MCNP)", "Treatment Planning System (TPS)", "Radioisotope Generator"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
