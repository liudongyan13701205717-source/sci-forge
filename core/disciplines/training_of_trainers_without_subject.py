"""无学科背景的培训师培训学科论文支持：通用培训师能力/培训项目管理/柯氏评估体裁、APA 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_of_trainers_without_subject",
    aliases=("training_of_trainers_without_subject", "无学科背景培训师培训",
             "通用培训师培训", "企业内训师培养", "培训师认证培训",
             "non-subject trainer training",
             "general training of trainers", "corporate trainer training",
             "certified trainer development"),
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
            "organizational context",
            "training program description",
            "evaluation and results",
            "lessons learned",
            "references",
        ),
        "evaluation_study": (
            "abstract",
            "introduction",
            "training program overview",
            "evaluation design（柯氏四级评估）",
            "results",
            "discussion（局限与改进）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "training_evaluation": "培训效果评估遵循柯氏四级模型",
        "survey": "满意度调查遵循 AAPOR 规范",
        "empirical": "实证研究遵循 APA 与培训研究惯例",
        "competency": "培训师能力评估须报告能力模型与认证标准",
    },
    conventions=(
        "培训项目须报告目标、受众、内容与评估方法",
        "培训师能力术语须按认证标准（如 ATD、TTT）统一标注",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "培训方案须说明学习迁移与项目管理机制",
    ),
    key_venues=(
        "Journal of Training and Development",
        "Human Resource Development International",
        "Training Research International",
        "Journal of Workplace Learning",
        "中国人力资源开发",
        "Adult Learning Journal",
    ),
    units_and_formulas_notes=(
        "培训满意度用李克特量表报告，须注明信度系数",
        "行为改变须报告行为频率变化与观察时间窗",
        "培训效果须给出前测/后测均值差与效应量",
        "培训投资回报 ROI = (培训收益 - 培训成本) / 培训成本 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("培训需求分析系统", "培训效果评估系统", "能力模型建构平台", "教学设计系统", "教学技能训练平台", "微格教学系统", "课堂观察量表系统", "学员学习分析平台", "培训项目管理平台", "认证培训管理平台", "培训质量管理系统", "培训档案管理系统", "学员满意度调查系统", "学习管理系统（LMS）", "在线培训平台", "视频会议平台", "SPSS", "NVivo", "R", "Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "万方"),
)
