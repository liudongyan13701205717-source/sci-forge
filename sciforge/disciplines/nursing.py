"""护理学科论文支持：APA 7、COREQ/COSMIN 按研究设计路由与干预报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursing",
    aliases=("nursing", "护理", "护理学", "nurse", "临床护理",
             "nursing research", "midwifery", "助产"),
    paper_types={
        "quantitative_intervention": (
            "abstract",
            "introduction（PICO 问题与理论框架）",
            "methods（设计、对象、干预描述、测量工具）",
            "results（量表得分、效应量、脱落处理）",
            "discussion（临床护理意义与实施条件）",
            "references",
        ),
        "qualitative_study": (
            "abstract",
            "introduction（现象与研究问题）",
            "methods（方法学传统、受访者、资料收集、饱和与信实性）",
            "results（主题/范畴结构，引语佐证）",
            "discussion（体验解释与护理实践含义）",
            "references",
        ),
        "mixed_methods": (
            "abstract",
            "introduction",
            "methods（设计类型：顺序/并行解释，定量与定性分支）",
            "results（定量与定性结果及整合）",
            "discussion（整合后的推论）",
            "references",
        ),
        "instrument_validation": (
            "abstract",
            "introduction（构念与目标人群）",
            "methods（条目生成、信效度检验、COSMIN 流程）",
            "results（信度、结构效度、反应性）",
            "discussion（适用人群与使用限制）",
            "references",
        ),
        "literature_review": (
            "abstract",
            "introduction",
            "methods（检索式、纳排、质量评价）",
            "results（证据表与主题综合）",
            "discussion（实践启示与研究缺口）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，护理期刊主流样式；文末悬挂缩进）",
    reporting_standards={
        "case_series": "CARE",
        "cohort": "STROBE",
        "case_control": "STROBE",
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
        "instrument_validation": "COSMIN",
        "quality_improvement": "SQUIRE 2.0",
    },
    conventions=(
        "干预描述达到可复现粒度：内容、频次、时长、实施者与理论依据",
        "量表给出信度（Cronbach's α/ICC）与效度证据，注明版本与语言",
        "质性研究明确方法学传统与研究者位置性（reflexivity）",
        "伦理：IRB/伦理委员会批准与知情同意；脆弱人群保护措施",
        "患者信息去标识化；引语避免可识别细节",
    ),
    key_venues=(
        "International Journal of Nursing Studies",
        "Journal of Advanced Nursing",
        "Nursing Research",
        "Journal of Nursing Scholarship",
        "Nurse Education Today",
    ),
    units_and_formulas_notes=(
        "效应量 Cohen's d / OR / 均数差（MD）给 95% CI；脱落率报告",
        "信度报 Cronbach's α 与重测 ICC；量表分值给出范围与计分方向",
        "样本量给先验功效分析（效应量、α、power）与招募完成情况",
        "质性样本以信息饱和为准并说明受访者特征（人数、访谈时长）",
        "护理敏感指标给定义口径（如压疮发生率 per 1000 patient-days）",
    ),
)
