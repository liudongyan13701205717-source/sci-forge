"""论证与表达学科论文支持：论证结构、说服策略、演讲表达与评价量表。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="argumentation_and_presentation",
    aliases=(
        "argumentation and presentation",
        "论证与表达",
        "论证学",
        "argumentation",
        "presentation skills",
        "rhetoric",
        "修辞与表达",
        "public speaking",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "design_study": (
            "research question",
            "argument model",
            "intervention design",
            "data collection",
            "analysis",
            "findings",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and methods",
            "thematic findings",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7（或芝加哥注-书目式；心理学/传播学论文用 APA）",
    reporting_standards={
        "quantitative": "给样本量、量表、Cronbach α、效应量与显著性水平",
        "qualitative": "质性研究遵循 COREQ/SRQR；给编码树与信度",
        "experimental": "组间设计给随机化、控制变量与前置测",
        "validity": "论证评价给评价框架（如 Toulmin/PragmaDial/Argument Structure）与标注一致性（κ）",
    },
    conventions=(
        "论点（claim）、论据（grounds）与理据（warrant）须显式区分",
        "反方论点须回应；不得只列单一立场",
        "图表给量表与统计检验，禁止只给 p 值不给效应量",
        "伦理审查与知情同意须声明",
    ),
    key_venues=(
        "Argumentation and Critical Thinking",
        "Informal Logic",
        "Speech Communication",
        "Journal of Logic, Language and Information",
        "Argumentation",
        "The American Rhetorist",
        "Philosophy and Rhetoric",
    ),
    units_and_formulas_notes=(
        "统计显著性 α=0.05；置信区间给 95%",
        "评分量表用 Likert 5/7 点并注明锚点",
        "标注一致性给 Cohen's κ 或 Krippendorff's α",
        "效应量用 Cohen's d 或 η² 报告；p 值精确到 0.001",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Microsoft PowerPoint", "Prezi", "Keynote", "Canva", "Miro", "Toulmin Argument Mapper", "Rationale", "NVivo", "MAXQDA", "SPSS", "R", "Python", "Qualtrics", "Google Forms", "Camtasia", "OBS Studio", "Descript", "Zoom", "Google Docs"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "ERIC", "DOAJ"),
)
