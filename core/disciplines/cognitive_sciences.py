"""认知科学（Cognitive Sciences）学科论文支持：多学科交叉认知研究体裁、APA 引用样式与跨模态记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cognitive_sciences",
    aliases=("cognitive_sciences", "认知科学", "认知科学学", "认知与神经科学",
             "cognitive sciences", "认知心理学", "神经科学", "认知建模"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methods",
            "results",
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
        "commentary": (
            "abstract",
            "argument",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；跨学科投稿须按目标期刊规范）",
    reporting_standards={
        "experimental": "实验研究遵循 APA 报告规范",
        "neuroimaging": "神经影像研究遵循 COBIDAS、MINIMA/AAAS 声明",
        "computational": "计算建模遵循模型设定报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "被试信息（年龄、样本量、排除标准）须报告",
        "跨模态数据（行为、脑电、脑影像、眼动）须分别说明采集参数与时间同步",
        "模型与算法须给出版本、参数与随机种子",
        "反应时与正确率指标须明确；统计显著性阈值与效应量须报告",
        "跨学科术语首次出现处给出定义与非正式说明",
    ),
    key_venues=(
        "Cognition",
        "Cognitive Science",
        "Topics in Cognitive Science",
        "Cortex",
        "Neuropsychologia",
        "Journal of Cognitive Neuroscience",
        "Trends in Cognitive Sciences",
    ),
    units_and_formulas_notes=(
        "反应时用 ms；正确率用 %",
        "EEG 数据用 μV；fMRI 用 BOLD 与 % 变化",
        "公式用 amsmath；模型与拟合计算式须明确",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PsychoPy", "E-Prime 3", "OSF", "MATLAB", "Psychtoolbox", "fSLR", "FSL", "SPM", "AFNI", "FreeSurfer", "EEGLAB", "MNE-Python", "Brainstorm", "BrainViewer", "EyeLink", "Tobii Eye Tracker", "BrainVoyager", "Brainnetome", "R", "Python", "Stan", "PyMC", "OpenSesame"),
    category="理学",
    databases=("PubMed", "arXiv", "OpenAlex", "Crossref"),
)
