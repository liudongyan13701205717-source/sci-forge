"""其他商业管理旅游与服务学科论文支持：跨方向管理与服务科学方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_commerce_management_tourism_and_services",
    aliases=(
        "other_commerce_management_tourism_and_services",
        "其他商业管理旅游与服务",
        "Other Commerce, Management, Tourism and Services",
        "服务管理交叉",
        "Tourism Studies",
        "Business Analytics",
        "Operations Management",
        "Hospitality Management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（样本与研究设计）",
            "results（实证结果）",
            "discussion（讨论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析与讨论）",
            "results（发现）",
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
    citation_style="APA 7（管理学主流）/ Harvard / GB/T 7714（中文）",
    reporting_standards={
        "survey": "APAS 调查规范",
        "empirical": "管理学实证研究规范",
        "systematic_review": "PRISMA 声明",
        "case_study": "Yin 案例研究规范",
    },
    conventions=(
        "样本与抽样方法须说明",
        "问卷信度 Cronbach α 与效度须报告",
        "模型给出控制变量与稳健性检验",
        "量表题项与来源须列出",
        "伦理审批与利益冲突声明",
    ),
    key_venues=(
        "Journal of Management",
        "Tourism Management",
        "Annals of Tourism Research",
        "Journal of Service Research",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/95% CI",
        "回归系数给出 β 与标准误",
        "量表题项用 Likert 5 点或 7 点并注明",
        "检验给出 t/χ²/F 值与 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS 26（统计分析）", "AMOS（结构方程模型）", "Mplus（SEM 分析）", "Stata（面板/回归）", "R / RStudio", "Python（Pandas/Statsmodels）", "NVivo（质性分析）", "Excel（数据整理）", "Origin（绘图）", "Power BI（数据可视化）", "Tableau", "EndNote", "LaTeX", "Photoshop", "SurveyMonkey / Qualtrics（问卷）", "Sawtooth（联合分析）", "SmartPLS（PLS-SEM）", "Harvard Business Review Access", "Google Analytics（服务数据分析）", "CRM 系统（Salesforce）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
