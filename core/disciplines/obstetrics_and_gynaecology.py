"""妇产科学（英拼）学科论文支持：妇产/生殖医学体裁、ACOG 引用样式与妇产科记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="obstetrics_and_gynaecology",
    aliases=("obstetrics_and_gynaecology", "妇产科学", "妇产科", "妇产科医学", "obstetrics gynaecology", "obgyn", "obg"),
    paper_types={
        "research": ("abstract", "introduction（背景与临床问题）", "methodology（研究设计与人群）", "results（妊娠/手术结局）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例信息）", "analysis（诊断与评估）", "results（干预与结局）", "discussion（鉴别与经验）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述主题）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="ACOG/Obstetrics & Gynecology 样式",
    reporting_standards={"randomized_trial": "遵循 CONSORT 声明", "observational": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("孕周须注明计算依据", "妊娠结局术语须明确", "FIGO 分期须注明版本", "剂量与手术方式须完整报告", "知情同意须说明"),
    key_venues=("Obstetrics & Gynecology", "American Journal of Obstetrics and Gynecology", "BJOG", "Human Reproduction", "Fertility and Sterility"),
    units_and_formulas_notes=("孕周用 weeks+days", "体重用 g", "数值给出均值±SD 与样本量", "结局给出 RR/OR 与 95% CI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("超声诊断仪", "3D 子宫超声探头", "经阴道超声探头", "胎儿多普勒", "胎心监护仪", "宫腔镜", "腹腔镜手术系统", "手术显微镜", "宫颈成熟度评估仪", "CerviSense 宫颈弹性检测仪", "VirtaMed GynoS 模拟器", "HPV/宫颈癌筛查仪", "IVF-ICSI 辅助生殖设备", "冷冻胚胎存储系统", "电子病历 HIS 系统", "SPSS", "R", "Stata", "Epi Info", "VirtaMed LaparoS"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
