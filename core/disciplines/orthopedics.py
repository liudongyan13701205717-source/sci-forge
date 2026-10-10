"""骨科学学科论文支持：创伤/脊柱/关节与运动医学临床与基础研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="orthopedics",
    aliases=(
        "orthopedics",
        "骨科学",
        "骨科",
        "Orthopedic Surgery",
        "运动医学",
        "脊柱外科",
        "关节外科",
        "骨创伤学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与假设）",
            "methodology（样本与临床方案）",
            "results（临床与影像结果）",
            "discussion（机制与应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与手术描述）",
            "analysis（术式与并发症）",
            "results（随访结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver（Surgical Orthopaedic Journals）/ GB/T 7714（中文）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "diagnostic_test": "STARD 声明",
        "systematic_review": "PRISMA 声明",
        "bone_metabolism": "ISOT 骨代谢评估报告规范",
    },
    conventions=(
        "样本纳入排除与随访时间须列出",
        "影像测量须给出误差与 ICC",
        "疼痛/功能评分使用标准化量表（VAS/HOOS/OFAS）",
        "统计学须给出检验方法与 α=0.05",
        "临床试验须在 ClinicalTrials.gov 注册",
    ),
    key_venues=(
        "The Journal of Bone and Joint Surgery (JBJS)",
        "The Spine Journal",
        "Clinical Orthopaedics and Related Research",
        "Journal of Arthroplasty",
        "Chinese Journal of Orthopaedics",
    ),
    units_and_formulas_notes=(
        "疼痛评分 VAS 0–10",
        "骨密度用 T 值/BMD (g/cm²)",
        "手术时长以 min 报告",
        "并发症按 Clavien-Dindo 分级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PACS 影像系统", "CT / MRI (SIEMENS, GE)", "Surgical Navigation (Zeiss)", "Arthroscope (Karl Storz)", "Biopsy Punch & Bone Cement", "DEXA Scanner (Hologic)", "SPSS 26（统计）", "R（统计分析）", "Excel（数据整理）", "Origin（绘图）", "EndNote", "LaTeX", "Photoshop", "Imaging Analysis ImageJ", "Cortical Thickness / Bone Micro-CT", "SEM (Scanning Electron Microscope)", "Stereomicroscope Zeiss", "Lactate Analyzer Lactate Pro", "OpenMR / DICOM Viewer", "Vicon / BTS 运动捕捉"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
