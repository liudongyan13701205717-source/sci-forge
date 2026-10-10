"""助产学学科论文支持：助产临床实践、母婴健康与证据综合研究、案例与综述体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="midwifery",
    aliases=("midwifery", "助产学", "助产", "obstetric_care", "maternal_health", "midwife", "childbirth", "birth_attendance", "perinatal_care", "midwifery_practice", "maternal_child_health"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（受试者、助产干预与测量）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（产妇与分娩过程）", "analysis（评估与分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（助产护理证据综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式（助产学常用 APA 或护理学样式）",
    reporting_standards={"k1": "临床研究遵循 STROBE / CONSORT 声明", "k2": "质性研究遵循 COREQ / SRQR 声明", "k3": "系统综述遵循 PRISMA 声明"},
    conventions=("妊娠周期与产次须明确标注（如 G2P1）", "胎儿体重、宫高、羊水量须注明测量方法与单位", "助产操作须记录时间线与操作者", "风险因素须区分生理性与病理性", "结果须附置信区间与样本量"),
    key_venues=("Journal of Midwifery and Women's Health", "Midwifery", "Birth", "BJMOG: British Journal of Obstetrics and Gynaecology", "International Journal of Gynecology and Obstetrics"),
    units_and_formulas_notes=("体重用 kg；宫高用 cm；体温用 °C", "心率用 bpm；血压用 mmHg", "孕周用周数或月数（注明计法）", "统计结果用均值 ± 标准差与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Stethoscope", "Doppler ultrasound (fetal)", "Fetal monitor", "Partograph", "Electronic fetal monitoring", "Amniocentesis equipment", "Fetal kick counter", "Cervical dilator", "Vacuum extractor", "Forceps", "Episiotomy set", "Nebulizer", "Vital signs monitor", "EHR system", "Electronic health records", "Statistical software (SPSS)", "Statistical software (R)", "Patient education tools", "Clinical guidelines library", "Microsoft Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Reference database (Cochrane)"),
)
