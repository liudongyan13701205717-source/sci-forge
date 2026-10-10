"""有学科背景的教师培训师培训学科论文支持：学科教师专业发展/教学能力评估体裁、APA 与微格教学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_of_trainers_with_subject",
    aliases=("training_of_trainers_with_subject", "有学科教师培训师培训",
             "学科教师培训师", "学科教研员培训",
             "subject specialist trainer training",
             "teacher trainer with subject expertise",
             "curriculum specialist training"),
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
            "analysis and implications",
            "references",
        ),
        "teaching_research": (
            "abstract",
            "introduction",
            "literature review",
            "teaching design",
            "implementation",
            "assessment and reflection",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ 报告规范",
        "survey": "调查研究报告遵循 AAPOR 规范",
        "empirical": "实证研究遵循 APA 与教师教育研究惯例",
        "microteaching": "微格教学评估须报告评分维度与观察者信度",
    },
    conventions=(
        "学科能力术语须按课程标准与学科核心素养统一标注",
        "教学设计须说明学科知识结构与重难点",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "培训方案须说明学科教研与课堂观察机制",
    ),
    key_venues=(
        "Teachers and Teaching: Theory and Practice",
        "Educational Evaluation and Policy Analysis",
        "Journal of Teacher Education",
        "中国教师",
        "学科教育研究",
        "Teaching and Teacher Education",
    ),
    units_and_formulas_notes=(
        "学科能力评估用标准化学科测评报告，须注明常模",
        "课堂观察须报告观察时长与编码信度",
        "培训效果须给出前测/后测差异与效应量",
        "样本量、显著性水平与置信区间须完整给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("学科知识图谱系统", "教材分析系统", "课程标准对标工具", "学科能力测评平台", "课堂观察量表系统", "教学设计系统", "学科模拟教学平台", "微格教学系统", "学科竞赛培训平台", "学科知识测试系统", "教材编写系统", "题库管理系统", "360 评估系统", "学习管理系统（LMS）", "在线培训平台", "视频会议平台", "SPSS", "NVivo", "R", "Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "万方"),
)
