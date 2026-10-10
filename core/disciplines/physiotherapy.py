"""物理治疗学科论文支持：康复评估/运动功能/电生理干预体裁、APTA 引用样式与物理治疗记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physiotherapy",
    aliases=("physiotherapy", "物理治疗", "物理疗法", "physical therapy", "康复治疗", "rehabilitation therapy", "康复医学", "rehabilitation medicine", "运动治疗", "运动机能学"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与临床问题）", "methodology（受试者、方案与测量）", "results（功能/运动/疼痛指标）", "discussion（临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与评估）", "analysis（干预与机制）", "results（前后对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（循证与理论）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（国内期刊遵循 GB/T 7714）",
    reporting_standards={"rct": "RCT 遵循 CONSORT 声明", "clinical_trial": "临床试验遵循 SPIRIT 声明", "systematic_review": "系统综述遵循 PRISMA 声明", "case_report": "病例报告遵循 CARE 指南", "measurement": "测量学评估遵循 COSMIN 声明"},
    conventions=("量表与量具首次出现处给出全称与缩写（如 VAS、FIM）", "剂量与频率（次/周、周期数）须完整报告", "肌力评估遵循 MRC 分级（0-5 级）", "活动度 ROM 用 ° 表示并注明体位", "样本量与统计检验须给出"),
    key_venues=("Journal of Orthopaedic & Sports Physical Therapy", "Physical Therapy", "British Journal of Sports Medicine", "Archives of Physical Medicine and Rehabilitation", "Disability and Rehabilitation"),
    units_and_formulas_notes=("肌力 N、kg、kg·m；活动度 °", "肌电 EMG μV、%MVC；功率 W、W/kg", "速度 m/s；加速度 m/s²", "公式用 amsmath；运动学公式须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Biodex System 4", "Biodex Isokinetic", "Biodex Stability Base", "Biodex Electrostimulation", "Telos G3", "Zebris FDM-S", "Zebris GaitPro", "Vicon Vantage 120", "Qualisys MyoMotion", "Delsys Trigno EMG", "Noraxon Myo 16", "Xbox Kinect", "L-EMS 100 (Hartmann Medical)", "InBody 770", "DXA Hologic Horizon", "Chattanooga C1", "Chattanooga iStim Pro", "Chattanooga Body Tronix+", "Microsoft Kinect v2", "SPSS"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
