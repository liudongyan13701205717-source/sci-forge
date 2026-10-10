"""读写能力学科论文支持：阅读教学、评估与干预研究体裁，APA 引用与教育测量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="literacy",
    aliases=("literacy", "读写能力", "阅读能力", "识字",
             "reading", "literacy acquisition", "functional literacy",
             "reading skills", "阅读技能", "文字能力"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）",
                     "methodology（方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（个案描述）",
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
        "classroom_studies": "ERIC/education 研究伦理与知情同意",
        "case_study": "CASI 案例研究报告规范",
        "survey": "AAPOR 调查报告规范",
        "systematic_review": "PRISMA 系统综述声明",
        "measurement": "阅读测评使用标准化量表并报告信效度",
    },
    conventions=(
        "评估工具须给出名称、版本与来源",
        "样本量与年龄/年级须明确",
        "教学干预须描述时长、频次与内容",
        "统计检验须说明；效应量须给出",
        "参考文献遵循 APA 7 格式",
    ),
    key_venues=(
        "Reading Research Quarterly",
        "Journal of Research in Reading",
        "Educational Psychology Review",
        "Scientific Studies of Reading",
        "Reading Psychology",
        "Journal of Literacy Research",
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
