"""合作技能学科论文支持：教育/职业培训体裁、APA 引用样式与技能评估约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cooperation_skills",
    aliases=(
        "合作技能", "协作能力", "团队技能", "Co-operation skills",
        "Cooperation Skills", "Teamwork Skills", "Interpersonal Skills",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "training_program": (
            "项目概述",
            "目标人群",
            "培训内容",
            "评估方法",
            "结果分析",
            "结论",
        ),
        "review": (
            "摘要",
            "引言",
            "技能框架综述",
            "训练方法综述",
            "整合与讨论",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "competency_framework": "合作技能须基于公认的胜任力框架（如 TMM、Team Skills Model）",
        "assessment_tools": "评估工具须报告信效度与适用范围",
        "training_effectiveness": "训练效果须报告前后测对比与统计检验",
        "context": "须说明应用场景（学术、职场、社区等）",
    },
    conventions=(
        "技能分类须引用标准框架（如 Tuckman 团队发展模型）",
        "量表中文版须说明修订与标准化过程",
        "区分技能水平（basic/intermediate/advanced）并报告分布",
        "效应量报告 Cohen's d 或 Hedges' g",
        "质性研究须说明编码信度（inter-rater reliability）",
    ),
    key_venues=(
        "Journal of Workplace Learning",
        "Small Group Research",
        "Training Evaluation and Development",
        "International Journal of Educational Research",
        "Journal of Managerial Psychology",
        "教育研究",
    ),
    units_and_formulas_notes=(
        "技能评分使用 Likert 量表（如 1-5 或 1-7）",
        "前后测比较使用配对 t 检验或 Wilcoxon 检验",
        "多因子分析使用主成分分析或探索性因子分析",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Moodle（学习管理系统）", "Blackboard", "Canvas LMS", "SurveyMonkey（团队技能调查）", "Qualtrics", "SPSS", "AMOS", "Mplus", "NVivo", "ATLAS.ti", "Miro（团队白板协作）", "Asana", "Microsoft Teams", "Google Forms", "Kahoot!（团队竞赛学习工具）", "Tabletop Simulator（团队模拟训练）", "Second Life（虚拟协作培训）", "VirtualTeam（虚拟团队实验平台）", "Team Skills Assessment Tool (TSAT)", "Collaboration Skills Inventory (CSI)"),
    category="教育学",
    databases=("Scopus", "PsycINFO", "Web of Science", "中国知网"),
)
