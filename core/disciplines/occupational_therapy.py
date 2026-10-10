"""康复治疗学（作业治疗）学科论文支持：OT 干预/康复评价体裁、APA 引用样式与治疗记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="occupational_therapy",
    aliases=("occupational_therapy", "作业治疗", "康复治疗学", "职业治疗", "occupational therapy", "ot"),
    paper_types={
        "research": ("abstract", "introduction（背景与功能障碍）", "methodology（干预设计与量表）", "results（康复结局）", "discussion（机制与转归）", "references"),
        "case_study": ("abstract", "introduction", "case description（患者与功能基线）", "analysis（评估与目标）", "results（干预过程）", "discussion（疗效与意义）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论模型）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"randomized_trial": "遵循 CONSORT 声明", "systematic_review": "遵循 PRISMA 声明", "qualitative": "遵循 COREQ 指南"},
    conventions=("ICF 编码须注明", "量表须注明版本", "干预时长与强度须报告", "结局指标须报告最小临床重要差异", "样本量须报告"),
    key_venues=("Journal of Occupational Therapy", "British Journal of Occupational Therapy", "Disability and Rehabilitation", "Hand Therapeutics", "Archives of Physical Medicine and Rehabilitation"),
    units_and_formulas_notes=("时间用 min", "强度用 mmHg 或 Nm", "量表分数须注明满分", "数值给出均值±SD", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ICF 编码平台", "Job Analysis and Synthesis System", "Fugl-Meyer 量表", "Barthel 指数", "FIM 量表", "Wolf Motor Function Test", "Action Research Arm Test", "Virtual Reality 治疗平台", "MyoRep 上肢训练", "Polaris Exoskeleton", "Hocoma ARMin", "Bionik L2", "Wii Balance Board", "Myoelectric 电刺激", "R", "SPSS", "Excel", "Qualtrics", "NVivo", "Motion Capture 系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
