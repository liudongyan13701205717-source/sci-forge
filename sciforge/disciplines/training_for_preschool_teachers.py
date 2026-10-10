"""学前教育师资培训学科论文支持：幼儿发展评估/教学观摩/家园共育体裁、APA 与教育评价注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_for_preschool_teachers",
    aliases=("training_for_preschool_teachers", "学前教育师资培训", "幼儿教师培训",
             "学前教师教育", "学前教育师资培养",
             "preschool teacher education", "early childhood teacher training",
             "early childhood education", "ECE training"),
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
            "findings and implications",
            "references",
        ),
        "teaching_research": (
            "abstract",
            "introduction",
            "literature review",
            "teaching design",
            "implementation and observation",
            "assessment and reflection",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ 报告规范",
        "survey": "调查研究报告遵循 AAPOR 规范",
        "empirical": "实证研究遵循 APA 与教育研究惯例",
        "developmental": "幼儿发展评估须报告量表名称与常模来源",
    },
    conventions=(
        "术语全文一致：幼儿/儿童/学习者等核心概念须定义",
        "评估工具须注明名称、版本与常模来源",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "案例研究须说明案例选择理由与三角验证方法",
    ),
    key_venues=(
        "Early Childhood Education Journal",
        "Early Child Development and Care",
        "Journal of Research in Early Childhood Education",
        "学前教育研究",
        "幼儿教育",
        "Educational Studies",
    ),
    units_and_formulas_notes=(
        "幼儿发展水平须用标准化量表（如 Gesell、ASQ）标注",
        "教学效果报告 pre/post 均值差与效应量（Cohen's d）",
        "样本量、显著性水平与置信区间须完整给出",
        "教师行为编码须给出观察时长与编码信度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("儿童发展评估量表", "幼儿行为观察记录系统", "课堂录像分析系统", "互动白板", "平板电脑", "智能教具", "儿童绘画作品分析软件", "语言发展量表", "动作发展评估工具", "社会性发展测评工具", "感觉统合训练设备", "电子教案系统", "家园沟通平台", "儿童照片记录系统", "教学评估量表系统", "视频录制系统", "课堂互动反馈系统", "SPSS", "NVivo", "Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "万方"),
)
