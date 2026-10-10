"""家政服务学科论文支持：家政服务管理、社区服务与服务研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="domestic_services",
    aliases=(
        "domestic_services", "家政服务", "家政管理",
        "housekeeping", "清洁服务",
        "community services", "社区服务",
        "family support services", "家庭支持服务",
        "caregiving", "护理服务",
        "service management", "服务管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（服务问题与背景）",
            "method（研究设计、服务方案、评估指标）",
            "results（服务效果与满意度）",
            "discussion（服务优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（服务实践分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "service overview（服务综述）",
            "comparison（模式对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experiment": "服务方案须完整（内容、时长、频率）",
        "assessment": "满意度评估须注明工具与信效度",
        "ethics": "涉及家庭数据须声明隐私保护",
    },
    conventions=(
        "服务时长用 h 或 min 表示",
        "费用用 元 表示",
        "满意度用 Likert 5 级表示",
        "评分用 1-10 级表示",
        "统计检验注明方法与效应量",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Quality Management",
        "Journal of Consumer Affairs",
        "Journal of Family and Economic Issues",
        "Journal of Leisure Research",
    ),
    units_and_formulas_notes=(
        "时长用 h 或 min 表示",
        "费用用 元 表示",
        "满意度用 1-5 级表示",
        "评分用 1-10 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "Service Management Software", "CRM Software", "Scheduling Software", "Mobile App for Caregivers", "Cleaning Equipment", "Vacuum Cleaner", "Steam Cleaner", "Iron", "Laundry Machine", "Dryer", "Cleaning Supplies"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
