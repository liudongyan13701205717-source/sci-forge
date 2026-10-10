"""牙科护理学科论文支持：口腔预防护理、临床护理与患者教育体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_nursing",
    aliases=(
        "dental_nursing", "牙科护理", "口腔护理",
        "dental nursing", "oral health nursing", "牙科卫生护理",
        "dental hygienist", "牙科辅助员",
        "oral healthcare", "口腔健康教育",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（口腔健康问题与护理背景）",
            "methods（研究设计、护理干预、评估工具）",
            "results（护理效果与患者满意度数据）",
            "discussion（护理模式优化建议）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、护理干预方案、结局指标）",
            "results（疗效与安全性）",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "case presentation（患者口腔状况与护理过程）",
            "nursing care plan（护理计划）",
            "outcome（护理效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "RCT": "CONSORT 声明",
        "observational": "STROBE 声明",
        "systematic_review": "PRISMA 声明",
        "case_report": "CARE 指南",
        "nursing_intervention": "干预细节须完整描述（频率、时长、内容）",
    },
    conventions=(
        "口腔检查记录使用标准牙位标记法（FDI 两位数）",
        "护理评估工具（如 OHI-S、OHIS）须注明版本与信度",
        "患者知情同意与伦理审批须声明",
        "护理干预方案须区分控制组与干预组",
        "健康教育内容须注明形式（图文/视频/一对一）",
    ),
    key_venues=(
        "Journal of Dental Education",
        "Community Dentistry and Oral Epidemiology",
        "Journal of Clinical Nursing",
        "International Journal of Nursing Studies",
        "BMC Oral Health",
    ),
    units_and_formulas_notes=(
        "菌斑指数（PLI）用 0-4 分级",
        "牙龈指数（GI）用 0-3 分级",
        " probing 深度用 mm 表示",
        "满意度评分用 Likert 5 级量表",
        "统计显著性 α=0.05，95% CI 须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IBM SPSS Statistics", "R (RStudio)", "Stata", "Epic Systems", "Oracle Cerner", "Microsoft Excel", "Power BI", "Qualtrics", "SurveyMonkey", "NVivo", "Google Forms", "Zoom", "Microsoft Teams", "Canva", "Desire2Learn", "Canvas LMS", "Blackboard", "Kahoot!", "Anki", "OpenDental"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
