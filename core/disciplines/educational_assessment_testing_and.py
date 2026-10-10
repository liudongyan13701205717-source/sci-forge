"""教育评估与测试学科论文支持：教育测量、心理测试与评估方法研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="educational_assessment_testing_and",
    aliases=(
        "educational_assessment_testing_and", "教育评估与测试",
        "educational assessment", "教育评估",
        "educational measurement", "教育测量",
        "psychological testing", "心理测试",
        "test development", "测试开发",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（评估问题与背景）",
            "method（研究设计、测试开发、评估指标）",
            "results（测试效果与信效度）",
            "discussion（评估优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "assessment process（评估过程）",
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
    citation_style="APA 7",
    reporting_standards={
        "reliability": "信度须报告（Cronbach's alpha 等）",
        "validity": "效度须报告（内容效度、结构效度等）",
        "norming": "常模须注明样本量与代表性",
    },
    conventions=(
        "测试分数用 标准分/原始分 表示",
        "信度系数用 0-1 范围表示",
        "效度系数用 0-1 范围表示",
        "常模样本量须报告",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Educational and Psychological Measurement",
        "Journal of Educational Measurement",
        "Applied Measurement in Education",
        "Educational Assessment",
        "Psychological Testing and Assessment",
    ),
    units_and_formulas_notes=(
        "测试分数用 标准分/原始分 表示",
        "信度与效度系数用 0-1 范围表示",
        "常模样本量须报告",
        "统计检验注明 t/F/χ² 值、p 值与效应量"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Mplus", "AMOS", "LISREL", "EQS", "Winsteps", "ConQuest", "BILOG-MG", "PARSCALE", "Iteman", "RasWin", "Stata", "SAS", "TestOut", "LTM (Latent Trait Measurement)", "WAT (Watershed)", "SIBTEST"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
