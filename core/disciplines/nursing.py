"""护理学学科论文支持：循证护理/质性研究/量表验证体裁、APA 7 引用样式与干预报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursing",
    aliases=(
        "nursing",
        "护理学",
        "Nursing",
        "Nursing Research",
        "Clinical Nursing",
        "Advanced Practice Nursing",
        "Nursing Practice",
        "Evidence-Based Nursing",
        "护理研究",
    ),
    paper_types={
        "research": ("abstract", "introduction（PICO 问题与理论框架）", "methodology（设计、对象、干预与测量）", "results（量表得分、效应量与脱落处理）", "discussion（临床护理意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例概况）", "analysis（护理过程分析）", "results（护理结局）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（文献检索与筛选）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；护理期刊主流样式）",
    reporting_standards={
        "case_series": "CARE",
        "cohort": "STROBE",
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
        "instrument_validation": "COSMIN",
        "quality_improvement": "SQUIRE 2.0",
    },
    conventions=(
        "干预描述达到可复现粒度：内容、频次、时长、实施者与理论依据",
        "量表给出信度（Cronbach's α/ICC）与效度证据",
        "质性研究明确方法学传统与研究者位置性",
        "伦理委员会批准与知情同意须说明",
        "患者信息去标识化",
    ),
    key_venues=(
        "International Journal of Nursing Studies",
        "Journal of Advanced Nursing",
        "Nursing Research",
        "Journal of Nursing Scholarship",
        "Nurse Education Today",
    ),
    units_and_formulas_notes=(
        "效应量 Cohen's d / OR / MD 给 95% CI",
        "信度报 Cronbach's α 与重测 ICC",
        "样本量给先验功效分析",
        "护理敏感指标给定义口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic EHR", "Cerner Millennium", "Meditech", "Microsoft Excel", "SPSS", "R", "Stata", "NVivo", "ATLAS.ti", "Tableau", "EndNote", "Mendeley", "Zotero", "Ovid", "CINAHL", "SIMMAN 3G", "GraphPad Prism", "RevMan", "REDCap", "Qualtrics"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Google Scholar", "Cochrane Library", "Web of Science"),
)
