"""专科护理学科论文支持：专科循证护理/护理操作规范/护理敏感指标体裁、APA 7 与 CONSORT 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="specialised_nursing",
    aliases=("specialised_nursing", "专科护理", "Specialised Nursing", "专科护士", "临床专科护理", "Advanced Nursing Practice", "护理实践", "循证护理"),
    paper_types={
        "research": ("abstract", "introduction（PICO 问题与理论框架）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；护理期刊主流样式）",
    reporting_standards={
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
        "case_series": "CARE",
        "instrument_validation": "COSMIN",
    },
    conventions=(
        "专科领域须声明（ICU/急诊/肿瘤/手术室/老年/伤口造口/糖尿病等）",
        "护理操作按循证证据分级标注（最佳证据/标准证据/专家共识）",
        "患者信息去标识化，伦理委员会批准号须给出",
        "护理结局指标用 NDNQI 或国内护理敏感指标口径",
        "干预实施达可复现粒度：内容、频次、时长、实施者、理论依据",
    ),
    key_venues=(
        "International Journal of Nursing Studies",
        "Journal of Advanced Nursing",
        "Nursing in Critical Care",
        "Journal of Clinical Nursing",
        "Journal of Nursing Regulation",
    ),
    units_and_formulas_notes=(
        "护理敏感指标（VAP、CAUTI、CLABSI、跌倒率）给定义与统计口径",
        "效应量报 Cohen's d / OR / MD 并附 95% CI",
        "疼痛用 NRS/VAS 0–10 分；意识用 GCS 3–15 分",
        "样本量给先验功效分析（α = 0.05，power ≥ 0.80）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic EHR", "Cerner Millennium", "Meditech Six", "SPSS", "R", "Stata", "SAS", "NVivo", "ATLAS.ti", "Microsoft Excel", "Tableau", "SPSS Process 插件", "Metafor (R 包)", "EndNote", "Zotero", "SIMMAN 3G 模拟人", "iSimula 模拟系统", "Philips IntelliVue 监护仪", "BD Infusomat 输液泵", "Minitab"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
