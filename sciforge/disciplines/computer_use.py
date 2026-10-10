"""计算机使用/普及学科论文支持：计算机教育、数字化素养与使用研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_use",
    aliases=(
        "computer use", "计算机使用", "计算机应用", "computer literacy",
        "数字素养", "digital literacy", "computer education", "计算机教育",
        "ICT 普及", "information technology adoption", "技术采纳",
        "computer applications",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "methodology（研究设计与数据收集）",
            "results（数据分析与发现）",
            "discussion（解释与启示）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（场景与参与者）",
            "intervention（培训/技术引入）",
            "results",
            "discussion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "survey design",
            "results（描述统计与相关分析）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7（教育/信息科学通用）",
    reporting_standards={
        "survey": "问卷研究须报告样本量、回收率与信效度",
        "experimental": "实验须遵循随机对照与效应量报告规范",
        "case": "案例须遵循证据三角与信度报告",
    },
    conventions=(
        "数字化素养术语（literacy/literacy/digital competence）须先定义并统一",
        "问卷须附量表来源与 Cronbach α；量表分数须报告标准化口径",
        "样本须给出人口统计分层与缺失数据处理",
        "术语表首次出现即给出缩写与全称",
    ),
    key_venues=(
        "Computers & Education",
        "Journal of Research on Technology in Education (JRTE)",
        "Computers in Human Behavior",
        "International Journal of Educational Technology Research",
        "Journal of Educational Computing Research",
        "TechTrends",
        "ReCALL",
    ),
    units_and_formulas_notes=(
        "统计量给出均值 ± 标准差、置信区间与 p 值",
        "效应量用 Cohen d / η² 并给出解释阈值",
        "公式用 amsmath；相关与回归系数须标注显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SurveyMonkey", "SPSS", "R (psych/sem)", "AMOS", "Mplus", "NVivo", "MAXQDA", "Python (pandas/scikit-learn)", "Google Forms", "JotForm", "REDCap", "Open Data Kit", "KoboToolbox", "Microsoft Access", "Stata", "Excel", "JASP", "G*Power", "lavaan (R)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ERIC", "PubMed"),
)
