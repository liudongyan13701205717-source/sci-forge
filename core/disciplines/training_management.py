"""培训管理学科论文支持：学习迁移/胜任力建模/培训评估体裁、APA 与培训效果注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_management",
    aliases=("training_management", "培训管理", "培训与开发管理",
             "人力资源培训", "企业培训管理",
             "training and development", "workforce learning", "L&D",
             "training evaluation", "competency-based training"),
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
            "evaluation design（柯氏四级/四级评估）",
            "results（四级评估数据）",
            "discussion（培训投资回报率）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "training_evaluation": "培训效果评估遵循柯氏四级模型（Kirkpatrick's Four Levels）",
        "survey": "培训满意度调查遵循 AAPOR 规范",
        "empirical": "实证研究遵循 APA 与人力资源研究惯例",
        "roi": "培训投资回报须给出计算公式与基准对照",
    },
    conventions=(
        "培训项目须报告目标、受众、内容与评估方法",
        "培训效果须给出基线对比与效应量",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "培训方案须说明学习迁移机制与维持措施",
    ),
    key_venues=(
        "Journal of Training and Development",
        "Human Resource Development International",
        "Training Research International",
        "Journal of Workplace Learning",
        "中国人力资源开发",
        "Training & Development Quarterly",
    ),
    units_and_formulas_notes=(
        "培训满意度用李克特量表（如 5 点）报告，须注明信度系数",
        "行为改变须报告行为频率变化与观察时间窗",
        "学习迁移效果须给出前测/后测均值差与效应量",
        "培训投资回报 ROI = (培训收益 - 培训成本) / 培训成本 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("学习管理系统（LMS）", "TalentLMS", "Docebo", "SAP SuccessFactors Learning", "Moodle", "Cornerstone OnDemand", "360 反馈系统", "胜任力建模平台", "人才盘点工具", "学习地图系统", "在线考试系统", "视频采编平台", "直播授课平台", "学习分析平台", "SPSS", "AMOS", "R", "Excel", "Power BI", "NVivo"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "SSRN"),
)
