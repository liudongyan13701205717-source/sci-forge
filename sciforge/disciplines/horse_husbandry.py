"""马匹饲养学科论文支持：马属营养、健康监测与马房管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="horse_husbandry",
    aliases=("horse_husbandry", "马匹饲养", "马属饲养管理", "马属营养", "马房管理", "Equine Husbandry", "Equine Nutrition", "Equine Health Management", "Pony Care", "Equine Welfare"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "AAEPC 马属动物营养指南", "k2": "FEEDSTUFF 饲料配方规范", "k3": "GB/T 18407 饲料卫生标准"},
    conventions=("日粮配方须标注 NRC 基准", "体重变化须注明测量时间与空腹状态", "血样采集须注明部位与抗凝剂", "行为评分须注明评估工具", "药品使用须标注休药期"),
    key_venues=("Equine Veterinary Journal", "Journal of Equine Veterinary Science", "Equine Veterinary Education", "Animal", "Equine Veterinary Journal Supplement"),
    units_and_formulas_notes=("体况评分：Henneke 1–9", "饲料能量：MJ ME/kg", "粗蛋白：g/kg DM", "心率：bpm"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（统计建模）", "Excel", "Henneke Body Condition Scale 评估表", "Equine Body Condition Scales（BCS 图片集）", "EquiScope 兽医参考", "HemoVet 动物血液分析仪", "Coulter AccepCELL 血细胞计数仪", "ABX Pentra 生化分析仪", "NirSystems 饲料近红外分析仪", "ForageLab 8500 饲料分析仪", "Thermo Electron 消化率代谢笼", "EndNote", "Zotero", "Origin（数据绘图）", "NVivo（马主访谈）", "StableCam 马房监控", "Stable Sensor（智能马项圈）", "PetPace 生命体征监测", "兽医超声诊断仪（马属）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "LexiComp 兽医临床数据库"),
)
