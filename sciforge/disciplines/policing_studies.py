"""警务研究论文支持：警务策略评估、犯罪预测、执法效果研究与政策分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="policing_studies",
    aliases=("policing_studies", "警务研究", "警察学", "Policing Studies", "警务学", "警务管理", "警察管理", "警务科学", "Policing Science", "警务治理"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"CONSORT": "警务干预试验报告规范", "PRISMA": "系统综述报告规范", "STROBE": "观察性研究规范"},
    conventions=("干预试验须报告样本量与效应量", "犯罪预测模型须报告准确率、召回率与 AUC", "政策评估须使用准实验设计", "数据匿名化与伦理审查", "统计须报告置信区间与效应量"),
    key_venues=("Policing: A Journal of Policy and Practice", "Police Quarterly", "Journal of Criminal Justice", "Criminology", "Crime, Delinquency and Social Control"),
    units_and_formulas_notes=("犯罪率 per 100,000 population", "干预效应量 Cohen's d 或 odds ratio", "预测准确率 %", "空间分析单元须注明"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo", "ATLAS.ti", "QGIS", "ArcGIS Pro", "CrimeStat", "PredPol Analytic", "Tableau", "Power BI", "REDCap", "Qualtrics", "SurveyMonkey", "JASP", "Mplus", "SAS", "MATLAB", "Microsoft Excel"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "ICPSR"),
)