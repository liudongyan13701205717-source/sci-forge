"""儿科学学科论文支持：儿科临床/发育体裁、AAP/Pediatrics 引用样式与儿科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pediatrics",
    aliases=("pediatrics", "儿科学", "儿科", "儿童医学", "新生儿学", "neonatology", "儿科临床", "儿科护理", "儿童健康"),
    paper_types={
        "research": ("abstract", "introduction（儿科问题与研究目标）", "methodology（研究设计与人群）", "results（生长发育与临床数据）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（患儿与病史）", "analysis（诊断与鉴别）", "results（治疗与转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（疾病与发育理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="AAP/Pediatrics 样式（作者-年份；Pediatrics 遵循 AAP 规范）",
    reporting_standards={"randomized_trial": "RCT 报告遵循 CONSORT 声明（儿科扩展）", "observational": "观察性研究遵循 STROBE 声明", "systematic_review": "系统综述遵循 PRISMA 声明", "case_report": "病例报告遵循 CARE 指南", "growth_study": "生长发育研究须报告年龄别/性别别百分位"},
    conventions=("年龄分组须明确（新生儿/婴儿/儿童/青少年）", "生长发育指标（身高/体重/BMI）用年龄别百分位或 Z 评分", "药物剂量按体重或体表面积计算并注明", "知情同意（父母/监护人）与儿童知情同意须声明", "疫苗/免疫相关术语首次出现给出全称"),
    key_venues=("Pediatrics", "JAMA Pediatrics", "The Journal of Pediatrics", "Archives of Disease in Childhood", "Pediatric Research", "The Lancet Child & Adolescent Health"),
    units_and_formulas_notes=("体重用 kg；身高用 cm；BMI 用 kg/m²", "公式用 amsmath；Z 评分与百分位计算式须明确", "显示公式仅在被引用时编号；行内公式避免复杂分式", "数值结果给出均值 ± SD/SEM 与样本量", "剂量计算式（mg/kg/次）须完整"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("婴儿生理监护仪", "新生儿肺功能仪", "儿童肺量计", "小儿超声仪", "生长发育评估测量工具", "儿童发育量表（Gesell/ASQ-3）", "脑干诱发电位仪（BAEP）", "肌电图与神经传导仪（儿科）", "SPSS 统计分析", "R 统计分析", "Python (Pandas)", "Stata 统计", "MedCalc 统计分析", "i2b2 电子病历研究", "NLM-PeR 儿科电子病历", "WHO 儿童生长发育标准", "AAP Clinical Guidelines", "JAMA Network", "MetaForge 荟萃分析", "儿科呼吸机（新生儿）"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Library"),
)
