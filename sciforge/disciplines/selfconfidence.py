"""自信心学科论文支持：自信量表/建构主义干预/自我效能体裁、APA 引用样式与心理测量学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="selfconfidence",
    aliases=("selfconfidence", "self-confidence", "自信心", "自信", "自我效能",
             "self-esteem", "self-efficacy", "self-belief"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与自信构念界定）",
            "methods（量表、被试与施测流程）",
            "results（描述统计与因子分析）",
            "discussion（机制与教学启示）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "theoretical framework（理论基础）",
            "methods（干预设计与对照）",
            "results（前后测与效应量）",
            "discussion（推广性与局限）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（构念与量表谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，心理学与社会科学主流）",
    reporting_standards={
        "measurement": "量表须报告 Cronbach's α 与验证性因子分析（CFA）拟合指数",
        "effect_size": "实验/干预结果须报告 Cohen's d 或 η²p 与 95% CI",
        "systematic_review": "系统综述遵循 PRISMA 声明并注册 PROSPERO",
    },
    conventions=(
        "自信构念须区分自我效能（Bandura）与自尊（Rosenberg）两条谱系",
        "量表翻译/跨文化使用须报告信效度与项目反应理论（IRT）拟合",
        "报告量表分（含均值、SD、区间）与标准化后分数（z-score/T-score）",
        "干预研究须注册方案、报告脱落率与敏感性分析",
        "被试特征、抽样与统计假设须完整披露",
    ),
    key_venues=(
        "Personality and Individual Differences",
        "British Journal of Educational Psychology",
        "Educational Psychology Review",
        "Journal of Applied Sport Psychology",
        "Contemporary Educational Psychology",
    ),
    units_and_formulas_notes=(
        "量表分用 Likert 5/7 点；报告 Cronbach's α（≥.70 为可接受）",
        "相关用 Pearson r 或 Spearman ρ；效应量用 Cohen's d、η²p、Cohen's f²",
        "因子分析用 amsmath；SEM 拟合指数 CFI、TLI、RMSEA、SRMR",
        "样本量按先验功效（power ≥ .80）报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Microsoft Excel", "Qualtrics", "NVivo", "Mplus", "LISREL", "AMOS", "SmartPLS", "JASP", "Jamovi", "Stata", "Python（pandas/NumPy）", "lavaan", "BayesFactors", "REDCap", "Google Forms", "SurveyMonkey", "OSF"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
