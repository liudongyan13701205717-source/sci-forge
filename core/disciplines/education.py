"""教育学论文支持：教学干预、学习测量、系统性教育综述。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="education",
    aliases=("education", "教育学", "教学", "learning", "pedagogy", "课程", "curriculum"),
    paper_types={
        "research": ("abstract", "introduction", "theoretical framework", "methodology",
                     "results", "discussion", "implications for practice", "references"),
        "intervention": ("abstract", "introduction", "intervention design", "participants/setting",
                         "measures", "results", "effect size & fidelity", "references"),
        "review": ("abstract", "introduction", "review protocol（PRISMA）", "inclusion criteria",
                   "findings", "implications", "references"),
    },
    citation_style="APA 7th",
    reporting_standards={
        "design": "研究设计（RCT/准实验/质性）须声明；对照组与分配机制描述",
        "measures": "测量工具的信效度（Cronbach α/重测）须引用来源与版本",
        "effect": "效应量（Cohen's d/Hedges' g）与置信区间必报；不只给 p 值",
        "fidelity": "干预保真度（fidelity of implementation）须测量并报告",
        "equity": "样本的人口学特征（性别/SES/语言）须完整披露",
    },
    conventions=(
        "理论与实践框架分开陈述；教育情境描述具体（年级/学科/班额）",
        "量表条目数与计分方式给出；数据表用三线表",
        "质性研究给编码方案与信度检验（inter-rater reliability）",
        "政策建议与研究局限分开章节；避免过度推广",
    ),
    key_venues=(
        "American Educational Research Journal",
        "Review of Educational Research",
        "Teaching and Teacher Education",
        "Learning and Instruction",
        "Educational Psychologist",
    ),
    units_and_formulas_notes=(
        "效应量给标准化均值差；ICC（组内相关）用于多层数据",
        "样本量按 power analysis 报告；缺失数据处理方式写明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告", "教案与教材"),
    tools=("SPSS", "Stata", "R", "NVivo", "LaTeX"),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
