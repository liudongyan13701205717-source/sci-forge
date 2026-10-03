"""妇产科学学科论文支持：妇产临床/生殖体裁、ACOG/Obstetrics & Gynecology 引用样式与妇产科记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="obstetrics_gynecology",
    aliases=("obstetrics_gynecology", "妇产科学", "妇产科", "产科", "妇科",
             "obstetrics", "gynecology", "生殖医学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与妇产问题）",
            "methods（研究设计与人群）",
            "results（妊娠/手术结局数据）",
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
    citation_style="ACOG/Obstetrics & Gynecology 样式（作者-年份；Green Journal 遵循 ACOG 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "孕周（gestational age）须注明计算依据（末次月经/超声）",
        "妊娠结局术语（活产、流产、早产等）定义须明确",
        "手术方式（剖宫产、腹腔镜等）与分级须报告",
        "FIGO 分期（妇科肿瘤）须注明版本",
        "激素/药物剂量与方案须完整报告",
    ),
    key_venues=(
        "Obstetrics & Gynecology",
        "American Journal of Obstetrics and Gynecology",
        "BJOG",
        "Human Reproduction",
        "Fertility and Sterility",
        "The Lancet",
    ),
    units_and_formulas_notes=(
        "孕周用 weeks+days；新生儿体重用 g",
        "公式用 amsmath；孕周计算与校正公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "围产结局给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("超声诊断仪", "胎心监护仪", "腹腔镜手术系统", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "万方"),
)