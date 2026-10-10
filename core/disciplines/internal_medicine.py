"""内科学学科论文支持：临床研究、综述与病例报告体裁，Vancouver 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="internal_medicine",
    aliases=(
        "internal_medicine",
        "内科学",
        "Internal Medicine",
        "Internal Medicine Practice",
        "General Medicine",
        "GP Medicine",
        "Internal Medicine Specialty",
        "内科临床",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "CONSORT（对照试验）",
        "k2": "PRISMA（系统综述）",
        "k3": "STROBE（观察性研究）",
    },
    conventions=(
        "伦理审查编号与知情同意须报告",
        "样本量与失效率须列出",
        "统计量给出 M(SD) 或 中位数(IQR)",
        "置信区间优先 95% CI",
        "临床试验须完成注册",
    ),
    key_venues=(
        "The Lancet",
        "BMJ",
        "JAMA",
        "New England Journal of Medicine",
        "Annals of Internal Medicine",
    ),
    units_and_formulas_notes=(
        "SI 单位为主，医学习惯单位（如 mmHg、mg/dL）标注即可",
        "检验值须给出参考范围",
        "P 值不得直接写 P<0.001（应给具体值）",
        "多变量模型报告 β 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "SAS", "R", "PASS", "MedCalc", "RevMan", "Epi Info", "OPENEPI", "Python（Statsmodels）", "NCSS", "ClinicalTrials.gov Registry", "ClinicalKey", "UpToDate", "Zotero", "EndNote", "GraphPad Prism", "Microsoft Excel", "OpenFDA", "Epic EHR 电子病历系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Library", "NCBI PubMed", "ProQuest", "ClinicalTrials 数据库"),
)
