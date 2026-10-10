"""Clinical and Health Psychology 学科论文支持：临床/健康心理学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clinical_and_health_psychology",
    aliases=(
        "Clinical and Health Psychology", "临床与健康心理学",
        "Clinical Psychology", "临床心理学", "Health Psychology",
        "健康心理学", "Clinical Mental Health", "临床心理健康",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "apa_7": "统计报告须遵循 APA 7 规范（效应量、置信区间）",
        "consort": "随机对照试验遵循 CONSORT 报告规范",
        "prisma": "系统综述遵循 PRISMA 声明",
        "ethics": "伦理审查（IRB）与知情同意须声明",
    },
    conventions=(
        "使用 APA 7 报告规范",
        "心理测量使用标准化量表与信效度指标（α、Cronbach α）",
        "引用伦理审查（IRB/Ethics）与 informed consent",
        "统计报告遵循 PRISMA/SRQR 与 CONSORT",
        "使用 SPSS、JASP 或 R 时说明软件版本",
    ),
    key_venues=(
        "Journal of Consulting and Clinical Psychology",
        "Clinical Psychology Review",
        "Psychological Medicine",
        "The Lancet Psychiatry",
        "Journal of Affective Disorders",
        "Annual Review of Clinical Psychology",
        "Psychotherapy and Psychosomatics",
        "Clinical Psychological Science",
    ),
    units_and_formulas_notes=(
        "心理测量信度以 Cronbach α 表示（0–1），须附题项数",
        "组间差异效应量用 Cohen's d 或 Hedges' g，须附置信区间",
        "量表得分须注明分值范围、计分方向与理论最大分",
        "统计检验须给出检验类型、自由度、p 值与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "JASP", "RStudio", "R", "REDCap", "Qualtrics", "SurveyMonkey", "G*Power", "JMV", "NVivo", "Atlas.ti", "MAXQDA", "Microsoft Excel", "OpenEMR", "OpenClinica", "MedDRA Browser", "PsychoPy", "OpenSesame", "Pajero", "Jamovi"),
    category="医学",
    databases=("OpenAlex", "PubMed", "PsycINFO", "Crossref"),
)
