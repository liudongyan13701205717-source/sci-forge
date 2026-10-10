"""赛马护理学科论文支持：马匹训练、健康与骑乘竞技管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="race_horse_care",
    aliases=("race_horse_care", "赛马护理", "race horse care", "horse care", "equine care", "赛马", "马术", "equine welfare", "马匹健康"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "IRWHP 国际马福利评估规程", "k2": "FEI 兽医检查标准", "k3": "马匹药物使用遵循马匹治疗用药指南"},
    conventions=("马匹编号使用国际注册编号", "训练计划须列出强度与时长", "健康监测数据按时间序列展示", "药物剂量以毫克/千克计算", "参考文献按 APA 7 著录"),
    key_venues=("Equine Veterinary Journal", "Journal of Equine Veterinary Science", "Equine Veterinary Education", "Animal Welfare", "Equine Veterinary Medicine"),
    units_and_formulas_notes=("体重使用千克（kg）", "心率使用次/分钟（bpm）", "血氧饱和度使用百分比（%）", "药物剂量使用毫克/千克（mg/kg）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("VetScan Hematology Analyzer", "Mindray Hemavet", "Idexx Reference Lab", "Digital Veterinary Radiography", "Equine Ultrasound (MyLab OneVet)", "Equine Lameness Locator", "Equine Gait Analysis System", "Equine Dental Rotary Tool", "Farrier Smithy & Anvil", "Horseshoe Fitting Set", "Equus Wearables Fitness Tracker", "FitBark Horse Monitor", "Equinova Horse Management Software", "EquiTrack Horse Management", "EquiBase Horse Management", "Equine Stall Equipment", "Equine Feed Calculator", "Paddock Fence System", "Hay Feeder & Net", "Equine Temperature Monitor"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
