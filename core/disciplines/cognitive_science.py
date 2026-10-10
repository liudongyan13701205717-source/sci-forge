"""认知科学学科论文支持：认知科学/心智研究体裁、APA 引用样式与认知科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cognitive_science",
    aliases=("cognitive_science", "认知科学", "认知研究", "心智科学", "认知神经科学",
             "cognitive science", "cognitive neuroscience", "心智研究", "认知建模"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与认知科学问题）",
            "methods（实验设计与被试）",
            "results（行为与神经数据）",
            "discussion（认知机理）",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（模型架构与假设）",
            "simulation（仿真与拟合）",
            "discussion（与行为数据对比）",
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
    citation_style="APA 7 样式（作者-年份；Cognitive Science 遵循 APA 规范）",
    reporting_standards={
        "experimental": "实验研究遵循 APA 报告规范",
        "computational": "计算建模遵循模型设定报告规范",
        "neuroimaging": "神经影像研究遵循 COBIDAS 与 MINIMA/AAAS 声明",
        "fMRI": "fMRI 分析遵循 ARRIVE 与 NeuroVault 数据管理规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "被试信息（年龄、样本量、排除标准）须报告",
        "刺激与任务设计须可复现",
        "反应时与正确率指标须明确",
        "模型拟合指标（BIC、AIC 等）须报告",
        "统计显著性阈值与效应量须明确",
    ),
    key_venues=(
        "Cognitive Science",
        "Topics in Cognitive Science",
        "Cognition",
        "Journal of Experimental Psychology: General",
        "Cognitive Psychology",
        "Trends in Cognitive Sciences",
    ),
    units_and_formulas_notes=(
        "反应时用 ms；正确率用 %",
        "公式用 amsmath；模型与拟合计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PsychoPy", "E-Prime 3", "MATLAB", "Psychtoolbox", "OSF", "SPSS", "R", "Stan", "PyMC", "PyTorch", "TensorFlow", "fSLR", "SPM", "FSL", "AFNI", "FreeSurfer", "EEGLAB", "MNE-Python", "EyeLink", "Tobii Eye Tracker", "OpenSesame", "PsychoJS", "GNU Octave"),
    category="理学",
    databases=("PubMed", "arXiv", "OpenAlex", "Crossref"),
)
