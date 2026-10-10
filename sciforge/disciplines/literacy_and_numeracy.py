"""读写与算术能力学科论文支持：基础教育评估、双语识数与学习干预体裁，APA 引用与教育测量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="literacy_and_numeracy",
    aliases=("literacy_and_numeracy", "读写与算术", "读写算能力",
             "basic skills", "functional literacy and numeracy",
             "成人教育技能", "基础教育能力", "算术能力",
             "adult education", "lifelong learning"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）",
                     "methodology（方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（个案/情境描述）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "CONSORT 干预研究报告规范",
        "classroom_studies": "ERIC/教育研究伦理与知情同意",
        "case_study": "CASI 案例研究报告规范",
        "survey": "AAPOR 调查报告规范",
        "systematic_review": "PRISMA 系统综述声明",
        "programme_evaluation": "CIPP 项目评估框架",
    },
    conventions=(
        "读写/算术能力评估工具须明确",
        "样本量、年龄与教育背景须报告",
        "干预设计与对照组须交代",
        "统计检验须说明；效应量须给出",
        "参考文献遵循 APA 7 格式",
    ),
    key_venues=(
        "Literacy and Numeracy",
        "Adult Education Quarterly",
        "International Journal of Educational Research",
        "Journal of Research in Reading",
        "Mathematics Education Research Journal",
        "Educational Psychology Review",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量给出 Cohen's d 或 Hedges g",
        "量表分数给出范围与信度（Cronbach α）",
        "p 值小于 0.05 视为显著",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "SPSS", "RStudio", "Jupyter Notebook", "EndNote", "Zotero", "Mendeley", "RefWorks", "Qualtrics", "SurveyMonkey", "Google Forms", "NVivo", "MAXQDA", "LaTeX", "Overleaf", "Microsoft Excel", "PowerPoint", "Google Docs", "Tableau"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
