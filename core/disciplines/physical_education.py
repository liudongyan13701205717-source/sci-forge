"""体育教育学学科论文支持：体育教育/学校体育体裁、APA 引用样式与体育教育学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_education",
    aliases=("physical_education", "体育教育", "学校体育", "体育教学", "PE"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与体育教育问题）",
            "methods（研究设计与样本）",
            "results（教学与学习数据）",
            "discussion（教育意义）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "methods（干预设计与实施）",
            "results（干预效果终点）",
            "discussion（与既往研究对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；JTPE 遵循 APA 规范）",
    reporting_standards={
        "intervention": "教学干预研究遵循教育干预报告规范",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "qualitative": "质性研究遵循 COREQ/SRQR 声明",
        "survey": "问卷调查遵循 AAPOR 报告规范",
    },
    conventions=(
        "课程与教学干预描述须完整（时长、频率、内容）",
        "学生样本特征与学校背景须报告",
        "测量工具（量表、体能测试）须注明信效度",
        "教学情境（班级规模、师资）须描述",
        "统计显著性阈值与效应量须明确",
    ),
    key_venues=(
        "Journal of Teaching in Physical Education",
        "Physical Education and Sport Pedagogy",
        "European Physical Education Review",
        "Research Quarterly for Exercise and Sport",
        "Journal of School Health",
        "Sport, Education and Society",
    ),
    units_and_formulas_notes=(
        "体能指标用标准单位（m、s、次/min）",
        "公式用 amsmath；量表得分与效应量计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "教案与教材"),
    tools=(
        "教案与课程设计软件",
        "运动技能评估量表（TGFI-U）",
        "PEACH 体育课程分析框架",
        "SPSS 教学数据统计分析",
    ),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "PubMed"),
)