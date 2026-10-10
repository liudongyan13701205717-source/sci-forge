"""社会与行为科学学科论文支持：社会科学实证研究、心理学实验与政策评价体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_and_behavioural_sciences",
    aliases=(
        "social_and_behavioural_sciences",
        "社会与行为科学",
        "social and behavioural sciences",
        "社会行为科学",
        "Social Sciences",
        "Behavioural Sciences",
        "社会科学",
        "行为科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "data and sample（数据与样本）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（第 7 版，作者-年份）",
    reporting_standards={
        "quantitative": "定量研究须报告样本量、效应量与置信区间，遵循 APA 报告规范",
        "qualitative": "质性研究须说明编码方案、信度（κ 值）与反思性立场",
        "experimental": "心理学实验须遵循 APA 报告标准（如信度、效度、盲法）",
        "ethics": "涉及人类参与者的研究须遵循 APA 伦理准则或《赫尔辛基宣言》",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "统计报告遵循 APA 第 7 版规范（斜体 t/F/p、括号内标准误、95% CI）",
        "研究设计类型须明确（横断/纵向/实验/准实验/质性）",
        "参与者特征须报告（年龄、性别、社会经济地位）",
        "所有量表须报告信度（Cronbach's α 或 ω）",
        "伦理审批号须给出（IRB/伦理委员会编号）",
    ),
    key_venues=(
        "Annual Review of Psychology",
        "Journal of Personality and Social Psychology",
        "American Sociological Review",
        "American Political Science Review",
        "Journal of Economic Behavior & Organization",
    ),
    units_and_formulas_notes=(
        "效应量 Cohen's d、η²、r² 按 APA 第 7 版格式报告",
        "显著性水平 α = 0.05；p 值精确到小数点后三位（或 p < .001）",
        "李克特量表按 1-7 或 1-5 计分；信度以 Cronbach's α 报告",
        "样本量以 n 报告；总体以 N 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "RStudio", "Python（pandas/statsmodels）", "JASP", "Stata", "Mplus", "AMOS", "NVivo", "ATLAS.ti", "Harmonic (Lavaan)", "Qualtrics", "SurveyMonkey", "Google Forms", "OpenSurvey", "LaTeX", "Endnote", "Vos Viewer", "CiteSpace", "Ngram Viewer", "Google Trends"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "SSCI", "ERIC"),
)
