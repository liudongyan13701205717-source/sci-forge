"""社会与个性心理学学科论文支持：社会影响、态度改变与人格结构体裁，APA 7 引用样式与心理测量统计规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_and_personality_psychology",
    aliases=("social_and_personality_psychology", "社会与个性心理学", "社会心理学", "个性心理学", "人格心理学", "社会与人格心理学", "social psychology", "personality psychology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与假设）",
            "method（参与者、材料、程序、测量）",
            "results（数据、统计与效应量）",
            "discussion（讨论、理论含义与局限）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction（问题与理论框架）",
            "case presentation（个案呈现与背景）",
            "analysis（分析与解释）",
            "results（结果与讨论）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction（综述范围与研究问题）",
            "literature search（文献检索与筛选）",
            "evidence synthesis（证据综合与异质性）",
            "future directions",
            "references"
        )
    },
    citation_style="APA 7（第 7 版；Journal of Personality and Social Psychology、Journal of Personality 遵循 APA）",
    reporting_standards={
        "empirical": "遵循 APA 心理科学报告规范：参与者、方法、结果三段式；效应量、95% CI 与缺失数据处理透明",
        "randomized_control_trial": "随机对照试验遵循 CONSORT 声明：分配隐藏、盲法、意向性分析",
        "meta_analysis": "元分析遵循 PRISMA 声明：检索式、纳入排除、异质性 I²、发表偏倚评估"
    },
    conventions=(
        "量表分数注明标准化方法与信度（Cronbach's α、ω）；本土化版本注明来源",
        "统计量给出 M/SD/SE/95% CI；效应量与 p 值并列，避免仅报 p 值",
        "假设检验先声明：预注册、检验方向、显著性水平须在方法中报告",
        "操纵检验须在讨论前独立报告，验证独立变量有效；中介/调节分析给出 Bootstrap CI",
        "研究流程遵循 APA 结构：摘要、引言、方法、结果、讨论、参考文献"
    ),
    key_venues=(
        "Journal of Personality and Social Psychology",
        "Journal of Personality",
        "British Journal of Social Psychology",
        "Social Psychological and Personality Science",
        "European Journal of Social Psychology"
    ),
    units_and_formulas_notes=(
        "百分比给出基数 N；加权数据注明权重变量与来源",
        "效应量报告 Cohen's d、ηp²、Cramér's V；多组比较给 Hedges's g 校正",
        "量表信度报告内部一致性（α、ω）与两周重测相关",
        "多层/面板数据说明层级结构、时点数与样本流失"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Stata", "NVivo", "Mplus", "AMOS", "JASP", "jamovi", "G*Power", "PsychoPy", "E-Prime", "Tobii Pro Eye Tracker", "iMotions", "Psychtoolbox", "Qualtrics", "Prolific", "MTurk", "BrainVision Analyzer", "Shimmer EDA"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
