"""Adventure based activities 学科论文支持：探险/户外/体验式教育体裁、APA 引用样式与户外教育注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="adventure_based_activities",
    aliases=("adventure based activities", "探险活动", "探险教育", "户外教育",
             "outdoor education", "adventure education", "experiential learning",
             "野外教育", "拓展教育"),
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
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program design",
            "implementation",
            "outcome measures",
            "results",
            "reflection",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "program_evaluation": "项目评估遵循 AAPOR 报告规范",
        "safety": "安全风险评估遵循 WFTB / IRATA 行业惯例",
        "empirical": "实证研究遵循 APA 与 AAAAM 惯例",
    },
    conventions=(
        "户外/探险术语全文一致：领导/团队/风险/经验学习等核心概念须定义",
        "活动安全评估与风险管理须在方法部分显式说明",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "案例研究须说明案例选择理由与三角验证方法",
    ),
    key_venues=(
        "Journal of Experiential Education",
        "Outdoor Education Review",
        "Journal of Outdoor and Adventure Education",
        "Journal of Adventure Education and Outward Bound",
        "Teaching and Teacher Education",
        "Journal of Experiential Learning",
    ),
    units_and_formulas_notes=(
        "体能/运动表现数据须报告采样设备与频率",
        "样本量、显著性水平、置信区间须完整给出",
        "学习效果报告 pre/post 均值差与效应量（Cohen's d）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Catapult GPS", "STATSports GPS", "WIMU IMU", "Dartfish", "SkillSprint", "Sportscode", "Petzl", "Black Diamond", "BEAL", "Edelrid", "Windy", "AllTrails", "GaiaGPS", "SPSS", "R", "NVivo", "ATLAS.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "Microsoft Office", "Google Docs", "Canva"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "ERIC"),
)
