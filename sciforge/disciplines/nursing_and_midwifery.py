"""护理与助产学科论文支持：围产护理/母婴健康体裁、APA 7 引用样式与产科指标注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursing_and_midwifery",
    aliases=(
        "nursing_and_midwifery",
        "护理与助产",
        "Nursing and Midwifery",
        "Midwifery",
        "Maternal Care",
        "Obstetric Care",
        "Perinatal Nursing",
        "Woman-Centred Care",
        "助产学",
    ),
    paper_types={
        "research": ("abstract", "introduction（母婴健康问题与理论框架）", "methodology（产科设计与结局测量）", "results（母婴结局与安全性指标）", "discussion（护理实践含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（围产病例）", "analysis（助产过程分析）", "results（母婴结局）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（助产理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "cohort": "STROBE",
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
        "case_series": "CARE",
    },
    conventions=(
        "产科结局指标按 ICM 分类报告（顺产/剖宫产/胎吸/产钳）",
        "母婴安全性指标给定义与统计口径（孕产妇死亡率、新生儿死亡率）",
        "助产干预达到可复现粒度（体位、导乐、镇痛方案）",
        "伦理委员会批准与知情同意须说明",
        "患者信息去标识化",
    ),
    key_venues=(
        "Midwifery",
        "Journal of Obstetric, Gynecologic & Neonatal Nursing",
        "Birth",
        "Journal of Midwifery & Women's Health",
        "Journal of Clinical Nursing",
    ),
    units_and_formulas_notes=(
        "孕产妇死亡率与新生儿死亡率以每 10 万为单位",
        "产程时间按阶段（潜伏期、活跃期、娩出期）记录",
        "Apgar 评分 0-10 分钟给分",
        "母婴满意度用 Likert 5 分制",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic EHR", "Cerner Millennium", "Microsoft Excel", "SPSS", "R", "Stata", "NVivo", "ATLAS.ti", "Tableau", "EndNote", "Mendeley", "Zotero", "CINAHL", "SIMBABY 助产模拟人", "助产训练系统", "产程监测系统", "RevMan", "GraphPad Prism", "REDCap", "Qualtrics"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Google Scholar", "Cochrane Library", "Web of Science"),
)
