"""行为经济学学科论文支持：实验/现场/理论体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="behavioral_economics",
    aliases=("behavioral_economics", "行为经济学", "行为金融", "实验经济学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "hypotheses（假设）",
            "experimental design（实验设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "laboratory_experiment": (
            "abstract",
            "introduction",
            "design（设计）",
            "procedures（流程）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "field_experiment": (
            "abstract",
            "introduction",
            "setting（现场）",
            "treatment（处理）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Economic Behavior & Organization 遵循 Elsevier 规范）",
    reporting_standards={
        "experimental": "实验研究遵循实验报告规范",
        "field_experiment": "现场实验遵循现场实验报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "meta_analysis": "元分析遵循 PRISMA 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "实验设计与处理须明确",
        "被试招募与报酬须说明",
        "随机化与盲法须报告",
        "假设检验与效应量须给出",
        "预注册须注明",
    ),
    key_venues=(
        "Journal of Economic Behavior & Organization",
        "Journal of Behavioral and Experimental Economics",
        "Journal of Economic Psychology",
        "Experimental Economics",
        "Management Science",
        "American Economic Review",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "p 值与显著性须给出",
        "样本量须报告",
        "金额用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("R（计量与实验分析）", "Python（NumPy/Pandas/Pyomo 优化）", "oTree（行为实验平台）",
           "Stata（面板与稳健性检验）", "z-Tree（实验经济学平台）"),
    category="经济学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)