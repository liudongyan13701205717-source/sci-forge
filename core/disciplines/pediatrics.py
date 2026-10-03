"""儿科学学科论文支持：儿科临床/发育体裁、AAP/Pediatrics 引用样式与儿科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pediatrics",
    aliases=("pediatrics", "儿科学", "儿科", "儿童医学", "新生儿学",
             "neonatology", "儿科临床"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与儿科问题）",
            "methods（研究设计与人群）",
            "results（生长发育与临床数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="AAP/Pediatrics 样式（作者-年份；Pediatrics 遵循 AAP 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明（儿科扩展）",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "growth_study": "生长发育研究须报告年龄别/性别别百分位",
    },
    conventions=(
        "年龄分组须明确（新生儿/婴儿/儿童/青少年）",
        "生长发育指标（身高/体重/BMI）用年龄别百分位或 Z 评分",
        "药物剂量按体重或体表面积计算并注明",
        "知情同意（父母/监护人）与儿童知情同意须声明",
        "疫苗/免疫相关术语首次出现给出全称",
    ),
    key_venues=(
        "Pediatrics",
        "JAMA Pediatrics",
        "The Journal of Pediatrics",
        "Archives of Disease in Childhood",
        "Pediatric Research",
        "The Lancet Child & Adolescent Health",
    ),
    units_and_formulas_notes=(
        "体重用 kg；身高用 cm；BMI 用 kg/m²",
        "公式用 amsmath；Z 评分与百分位计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "剂量计算式（mg/kg/次）须完整",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("婴儿生理监护仪", "小儿肺功能仪", "SPSS", "R", "生长发育评估测量工具"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "GEO", "Zenodo"),
)