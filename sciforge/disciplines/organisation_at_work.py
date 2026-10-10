"""工作组织学科论文支持：工作场所组织行为、工作设计、职业健康与团队协作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="organisation_at_work",
    aliases=("organisation_at_work", "工作组织", "工作场所组织", "Organisation at Work", "Workplace Organisation", "Workplace Behaviour", "工作组织行为", "职业组织学", "work organization"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"CONSORT": "CONSORT 干预试验规范", "STROBE": "STROBE 观察性研究规范", "PRISMA": "PRISMA 综述规范"},
    conventions=("量表与信效度（Cronbach's α、AVE、CR）必报告", "统计软件与版本声明（SPSS/R/Stata）", "研究伦理批件编号必报", "样本量与统计功效分析", "变量命名遵循惯例（如 JD、WB、TS）"),
    key_venues=("Journal of Occupational Health Psychology", "Work & Stress", "Journal of Applied Psychology", "Journal of Management Studies", "European Journal of Work and Organizational Psychology"),
    units_and_formulas_notes=("使用 SI 单位或心理测量标准单位", "Likert 量表 5/7 点报告 Cronbach's α 与 ω", "效度系数 β、χ²/df、CFI、RMSEA 必报", "样本量与功效分析（1-β ≥ 0.80）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Stata", "Mplus", "AMOS", "NVivo", "ATLAS.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "MATLAB", "Python (pandas/scikit-learn)", "Microsoft Excel", "LaTeX", "Microsoft Word", "Hays Analytics", "Excel Solver", "R/Studio Shiny"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "Web of Science", "CNKI"),
)
