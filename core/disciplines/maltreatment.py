"""虐待学科论文支持：儿童/长者/家庭虐待的识别、评估与干预研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="maltreatment",
    aliases=(
        "maltreatment",
        "虐待",
        "儿童虐待",
        "家庭暴力",
        "老人虐待",
        "Child Maltreatment",
        "Abuse",
        "Domestic Violence",
        "Elder Abuse",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="APA 7 样式（心理学与社会工作通用）",
    reporting_standards={
        "intervention": "干预研究遵循 CONSORT 声明",
        "qualitative": "质性研究遵循 COREQ/SRQR 规范",
        "meta_analysis": "元分析遵循 PRISMA 声明",
    },
    conventions=(
        "涉及未成年人的研究须获机构伦理审查与伦理委员会批准",
        "知情同意须区分未成年与成人、单独或监护人",
        "敏感主题须使用标准量表（如 ACE-Q、C-SSRS）",
        "受害者身份须匿名化，案例须去除可识别信息",
        "文化适应版本的量表须报告翻译与回译流程",
    ),
    key_venues=(
        "Child Abuse & Neglect",
        "Child Maltreatment",
        "Journal of Child Sexual Abuse",
        "Violence Against Women",
        "Child Maltreatment Review",
        "Child Maltreatment",
    ),
    units_and_formulas_notes=(
        "量表分数报告原始分与标准化分",
        "效应量使用 Cohen's d 或 η²",
        "信度使用 Cronbach's α",
        "统计显著性水平标注 α = 0.05",
        "年龄以岁/月为单位并附置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ACE-Q", "C-SSRS", "CAPT", "CBCL", "DAP-3", "HITS", "HARK", "SPSS", "R", "Stata", "NVivo", "ATLAS.ti", "MAXQDA", "REDCap", "Qualtrics", "SurveyMonkey", "JASP", "jamovi", "Mplus", "AMOS"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
