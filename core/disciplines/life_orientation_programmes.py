"""生命定向课程学科论文支持：生涯教育、生活指导与青少年发展体裁，APA 引用与教育记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="life_orientation_programmes",
    aliases=("life_orientation_programmes", "生命定向课程", "生涯规划",
             "life orientation", "career guidance", "life skills",
             "青少年发展", "生涯教育", "生活指导", "人格发展"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）",
                     "methodology（方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（案例情境）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "programme_evaluation": "CIPP 项目评估框架",
        "intervention": "CONSORT 干预研究报告规范",
        "case_study": "CASI 案例研究报告规范",
        "survey": "AAPOR 调查报告规范",
        "systematic_review": "PRISMA 系统综述声明",
        "qualitative": "COREQ/SRQR 质性研究报告规范",
    },
    conventions=(
        "干预设计与控制组须明确",
        "样本量与基线特征须报告",
        "测量工具须给出信效度",
        "伦理审查须声明",
        "参考文献遵循 APA 7 格式",
    ),
    key_venues=(
        "Journal of Career Development",
        "Educational Psychology Review",
        "International Journal of Educational Research",
        "Journal of Adolescent Health",
        "Educational Research Review",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "量表分数给出范围与信度（Cronbach α）",
        "效应量给出 Cohen's d",
        "p 值小于 0.05 视为显著",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "SPSS", "RStudio", "Jupyter Notebook", "NVivo", "MAXQDA", "ATLAS.ti", "Qualtrics", "SurveyMonkey", "Google Forms", "EndNote", "Zotero", "Mendeley", "Microsoft Excel", "PowerPoint", "Tableau", "Google Docs", "LaTeX", "Overleaf"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
