"""生物学心理学论文支持：脑行为关系、神经成像与应激/情绪生理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biological_psychology",
    aliases=(
        "biological_psychology",
        "biopsychology",
        "psychobiology",
        "neurobehavioral_science",
        "cognitive_neuroscience",
        "生物学心理学",
        "神经心理学",
        "行为神经科学",
        "神经行为学",
        "心理生理学",
        "psychophysiology",
        "cognitive neuroscience",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、假设与理论背景）",
            "participants and design（被试、样本量、随机化与分组）",
            "materials and methods（行为范式、生理采集与统计方案）",
            "results（行为结果与神经/生理结果分列）",
            "discussion（机制解释、局限与未来方向）",
            "acknowledgments",
            "references",
        ),
        "pre-registration_report": (
            "abstract",
            "introduction",
            "hypotheses（编号、可证伪表述）",
            "design and analysis plan（含先验分析计划与数据可用性声明）",
            "deviations（执行中与预注册的偏离及理由）",
            "results",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按理论/证据组织）",
            "unresolved questions",
            "references",
        ),
    },
    citation_style="APA 第 7 版（作者-年份）",
    reporting_standards={
        "human_neuroimaging": "fMRI 研究按 MINIMA 与 SHARE-MINIMA 建议报告；EEG 按 EEG Reporting Recommendation",
        "behavioral": "按 CONSORT/SPR 声明报告被试、随机化、盲法与流失",
        "animal": "动物实验按 ARRIVE 2.0 报告，含伦理批准与替代方案讨论",
        "preregistration": "预注册编号（OSF/AsPredicted）须在方法与致谢中给出",
        "psychometrics": "使用心理量表须报告信度（Cronbach α/ω）与常模来源",
    },
    conventions=(
        "脑区用规范命名（如 Brodmann 编号加功能名），左右半球统一用 L/R 或 MNI 坐标",
        "统计报告给出效应量（d、ηp²、Cohen's g）与置信区间，非仅 p 值",
        "生理指标给出采样率、电极/传感器位置与滤波参数",
        "被试数用 n，试验数用 N；独立样本与重复测量统计量用不同符号区分",
        "图表按 APA 规范：纵轴先于横轴、误差棒标注含义（SD/SEM）",
    ),
    key_venues=(
        "Biological Psychology",
        "Psychophysiology",
        "Behavioral and Brain Sciences",
        "Journal of Cognitive Neuroscience",
        "Neuropsychologia",
        "Cerebral Cortex",
        "Psychological Science",
        "Trends in Cognitive Sciences",
    ),
    units_and_formulas_notes=(
        "反应时用 ms；皮电用 μS 或 S（siemens）；心率变异性用 ms（RMSSD）",
        "fMRI 统计用 MNI152 空间，坐标给出 (x, y, z) 三元组",
        "EEG 频谱用 Hz 与 μV；功率密度用 dB 或 μV²/Hz",
        "t/F/χ² 统计量标注自由度；相关性用 r 并给出 p 与 n",
        "被试/事件/神经元计数一律用 n 或 N 显式标注单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPM（Statistical Parametric Mapping）", "FSL", "AFNI", "FreeSurfer", "BrainVoyager", "Connectome Workbench", "NiftyNet", "Nilearn", "MATLAB", "EEGLAB", "LSL（Lab Streaming Layer）", "PsychoPy", "OpenSesame", "Tobii PRO 60 眼动仪", "Neuroscan SynAmps 2", "Brain Products ActiCHamp Plus", "BioPac MP155", "ActiGraph GT9X", "NIRSport 3（近红外光谱）", "Siemens MAGNETOM Prisma 3T MRI", "MMPI-2"),
    category="理学",
    databases=("PubMed", "PsycINFO", "OpenAlex", "PsyArXiv", "Zenodo"),
)
