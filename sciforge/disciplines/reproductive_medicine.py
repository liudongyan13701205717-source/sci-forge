"""生殖医学学科论文支持：辅助生殖、生殖内分泌与生育力评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="reproductive_medicine",
    aliases=(
        "reproductive_medicine",
        "生殖医学",
        "reproductive medicine",
        "辅助生殖技术",
        "ART",
        "辅助生殖",
        "IVF",
        "试管受精",
        "生育力保存",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="Vancouver",
    reporting_standards={
        "clinical_trials": "CONSORT 或 SPIRIT 报告规范；临床注册号须列出",
        "cohort_case_control": "STROBE 规范；纳入/排除标准须完整",
        "systematic_review": "PRISMA 规范；检索词与文献筛选流程须说明",
        "ivf_cycles": "ESHRE 术语定义；周期数、移植次数、临床妊娠率口径须统一",
    },
    conventions=(
        "生殖激素报告单位按 SI（pmol/L、mIU/mL）并注换算关系",
        "胚胎发育按发育日龄 D0/D3/D5 标记；活检/冻融注明方案",
        "活产率与临床妊娠率口径分开报告",
        "伦理审批与知情同意须报告；伦理委员会缩写给出全称",
        "随访时长与失访率须报告",
    ),
    key_venues=(
        "Human Reproduction",
        "Fertility and Sterility",
        "Human Reproduction Update",
        "Reproductive Biomedicine Online",
        "BMC Medical",
    ),
    units_and_formulas_notes=(
        "激素浓度常用 pmol/L、mIU/mL、ng/mL；卵泡监测超声单位 cm",
        "HCG 阈值定义妊娠临床期；妊娠结局以妊娠囊/胎心为准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IVF/ICSI Lab System", "Time-lapse Incubator", "Transvaginal Ultrasound", "Oocyte Cryopreservation System", "Embryo Biopsy Micromanipulator", "Flow Cytometer", "PCR Amplification System", "Follicular Fluid Assay Kit", "Hormone Quantification ELISA Kit", "Chromosomal Microarray Analyzer", "Next-Generation Sequencer", "Embryo Grading AI Platform", "Hysteroscopy System", "Laparoscopic Surgery Suite", "Sperm Motility Analyzer CASA", "Endometrial Biopsy System", "Preimplantation Genetic Testing Panel", "Sex Steroid Immunoassay Analyzer", "IVF Electronic Case Record System", "Clinical Data Management System REDCap"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
