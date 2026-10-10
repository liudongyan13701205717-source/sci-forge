"""社会与行为科学（其他类）学科论文支持：新兴社会议题、跨学科社会科学与应用研究方法体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_and_behavioural_sciences_not",
    aliases=(
        "social_and_behavioural_sciences_not",
        "社会与行为科学（其他）",
        "social and behavioural sciences not elsewhere classified",
        "其它社会科学",
        "新兴社会议题",
        "Interdisciplinary Social Sciences",
        "Applied Social Science",
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
        "quantitative": "定量研究须报告样本量、效应量与置信区间",
        "qualitative": "质性研究须说明编码方案、反思性立场与伦理审批",
        "mixed_methods": "混合方法研究须说明整合策略（如 CONVERGENT、EXPLANATORY）",
        "ethical": "涉及人类参与者的研究须获得 IRB 或伦理委员会审批",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "统计报告遵循 APA 第 7 版规范（斜体 t/F/p、括号内标准误、95% CI）",
        "研究设计类型须明确（横断/纵向/实验/质性/混合）",
        "所有量表须报告信度（Cronbach's α 或 ω）",
        "跨学科研究须说明整合框架与理论来源",
        "伦理审批号须给出（IRB/伦理委员会编号）",
    ),
    key_venues=(
        "Social Science & Medicine",
        "Journal of Rural Studies",
        "International Journal of Social Research Methodology",
        "Qualitative Research",
        "Sociological Methods, Models & Data",
    ),
    units_and_formulas_notes=(
        "效应量 Cohen's d、η²、r² 按 APA 第 7 版格式报告",
        "显著性水平 α = 0.05；p 值精确到小数点后三位",
        "参与者特征以 n 与 % 报告；缺失值须说明处理方式",
        "跨学科指标须明确定义并给出测量方式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "RStudio", "Python（pandas/statsmodels）", "JASP", "Stata", "Mplus", "MAXQDA", "Dedoose", "SurveyMonkey", "Qualtrics", "NetDraw", "Gephi", "Vos Viewer", "CiteSpace", "NodeXL", "Social Network Analysis", "NVivo", "LaTeX", "Endnote", "UCINET"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "SSCI", "ERIC"),
)
