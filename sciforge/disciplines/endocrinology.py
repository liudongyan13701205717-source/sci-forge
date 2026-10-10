"""内分泌学科论文支持：内分泌学、激素与代谢疾病研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="endocrinology",
    aliases=(
        "endocrinology", "内分泌学", "内分泌",
        "endocrine system", "内分泌系统",
        "hormone research", "激素研究",
        "metabolic disease", "代谢疾病",
        "endocrine disorders", "内分泌疾病",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（内分泌问题与背景）",
            "method（研究设计、激素检测、评估指标）",
            "results（激素水平与代谢评估）",
            "discussion（治疗优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "endocrine analysis（内分泌分析）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "hormone": "激素检测方法须注明（RIA、ELISA 等）",
        "metabolism": "代谢指标须注明测量时机与方法",
        "ethics": "涉及患者数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "激素水平须注明单位与参考范围",
        "代谢指标须注明测量时机与方法",
        "治疗效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Clinical Endocrinology & Metabolism",
        "Endocrine Reviews",
        "Diabetes Care",
        "Endocrine",
        "European Journal of Endocrinology",
        "Journal of Endocrinology",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "激素水平须注明单位与参考范围",
        "代谢指标须注明测量时机与方法",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "Hormone Analyzer", "ELISA Reader", "RIA Kit", "Blood Glucose Meter", "HbA1c Analyzer", "Thyroid Function Test", "Cortisol Test", "Insulin Assay", "Hormone Assay", "GLP-1 Receptor Assay", "DEXA Scanner"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
