"""家政学科论文支持：家庭管理、生活科学与家政教育研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="domestic_science",
    aliases=(
        "domestic_science", "家政", "家政学",
        "home economics", "家政学",
        "family science", "家庭科学",
        "home management", "家庭管理",
        "life skills", "生活技能",
        "family and consumer sciences", "家庭与消费者科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（家政问题与背景）",
            "method（研究设计、实验条件、评估指标）",
            "results（效果数据与分析）",
            "discussion（家政优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（管理实践分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experiment": "实验条件须完整（温度、时间、工具）",
        "assessment": "评估指标须注明方法与时机",
        "ethics": "涉及家庭数据须声明隐私保护",
    },
    conventions=(
        "温度用 °C 表示",
        "时间用 min 表示",
        "用量用 g 或 mL 表示",
        "评分用 Likert 量表表示",
        "统计检验注明方法与效应量",
    ),
    key_venues=(
        "Family and Consumer Sciences Research Journal",
        "Journal of Family and Economic Issues",
        "Family Relations",
        "Home Economics Research",
        "Journal of Consumer Affairs",
    ),
    units_and_formulas_notes=(
        "温度用 °C 表示",
        "时间用 min 表示",
        "用量用 g 或 mL 表示",
        "评分用 1-5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "Microsoft Office", "Canva", "PowerPoint", "Google Classroom", "Moodle", "Zoom", "Microsoft Teams", "Kahoot!", "Desire2Learn", "Canvas LMS", "Blackboard"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
