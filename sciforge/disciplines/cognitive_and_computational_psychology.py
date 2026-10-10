"""认知与计算心理学学科论文支持：实验心理学/计算建模体裁、APA 引用样式与认知建模注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cognitive_and_computational_psychology",
    aliases=("cognitive_and_computational_psychology", "认知与计算心理学",
             "计算心理学", "实验心理学", "认知建模",
             "computational psychology", "cognitive modeling",
             "experimental psychology", "mathematical psychology"),
    paper_types={
        "experiment": (
            "abstract",
            "introduction",
            "experiment N（每实验独立编号，含 method、results、discussion）",
            "general discussion",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（模型架构、参数与假设）",
            "simulation（仿真、拟合、模型比较）",
            "prediction and validation",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；Cognition 与 Cognitive Psychology 遵循 APA 规范）",
    reporting_standards={
        "experiment": "实验研究遵循 APA 7 与 COPE 报告规范",
        "computational": "计算建模遵循 Model Reporting Guidelines",
        "eye_tracking": "眼动研究遵循 eyeXplain 报告清单",
        "preregistration": "预注册研究遵循预注册报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "被试信息（年龄、样本量、排除标准、伦理批件）须完整报告",
        "刺激与任务设计须可复现，材料须公开或说明获取方式",
        "反应时（RT）须报告单位（ms）、剔除规则（如 ±3SD 或 < 200/5000 ms）",
        "模型参数须报告估计方法（如 Maximum Likelihood / Bayesian MCMC）与先验",
        "统计显著性使用 α=0.05；贝叶斯分析给出 Bayes Factor",
    ),
    key_venues=(
        "Cognition",
        "Cognitive Psychology",
        "Psychonomic Bulletin & Review",
        "Journal of Mathematical Psychology",
        "Computational Brain & Behavior",
        "Cortex",
        "Behavioral and Brain Sciences",
    ),
    units_and_formulas_notes=(
        "反应时用 ms；正确率用 %",
        "公式用 amsmath；模型参数、拟合优度（BIC、AICc、WAIC）须报告",
        "显示公式仅在被正文引用时编号",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
        "贝叶斯模型报告后验分布与 95% HPD 区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PsychoPy", "E-Prime 3", "OSF", "PsychoJS", "OpenSesame", "MATLAB", "Psychtoolbox", "GNU Octave", "Stan", "PyMC", "Pyro", "PyTorch", "NumPyro", "CORSIKA", "Psychomotor", "iEEG", "EyeLink (Tobii)", "Tobii Eye Tracker", "Pupil (EyeTracking)", "R", "R (lme4, brms)", "Python", "PsychoPy-IO"),
    category="理学",
    databases=("PubMed", "arXiv", "PsyArXiv", "OpenAlex", "Crossref"),
)
