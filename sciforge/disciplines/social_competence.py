"""社会胜任力学科论文支持：社会技能训练、青少年发展与行为干预体裁，APA 引用样式与教育评估规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_competence",
    aliases=("social_competence", "社会胜任力", "社会能力", "社会技能", "life skills education", "social skills training", "youth development", "competence development"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与胜任力框架）",
            "methods（参与者、干预设计、测量、程序）",
            "results（结果、效应量与稳健性）",
            "discussion（讨论与推广性）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案呈现与基线行为）",
            "analysis（干预过程与分析）",
            "results（前后测与对比）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（文献检索与筛选）",
            "evidence synthesis（社会技能训练证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="APA 7（Journal of Educational Psychology、Child Development 遵循 APA）",
    reporting_standards={
        "randomized_control_trial": "学校干预 RCT 遵循 CONSORT 与 CONSORT-Education 声明：分配隐藏、教师盲法、缺失值处理",
        "quasi_experimental": "准实验研究遵循 QUASI-REPT 规范：匹配、等效组假设、敏感性分析",
        "single_case_design": "单被试设计遵循 SCR（Single-Case Reporting Guidelines）：设计类型、干预时长、行为基线",
        "qualitative": "质性研究遵循 COREQ 清单：参与者视角、观察与访谈、饱和判断"
    },
    conventions=(
        "胜任力维度须先给出操作化定义（如 OSHI 或 CASEL 框架）并声明测量工具来源",
        "干预手册、课时、教师培训、保真度评估须报告，未达阈值须讨论",
        "单被试设计用 D/P 值（overlap of non-equivalent groups）与视觉分析，避免仅用统计检验",
        "多层数据（学生嵌套班级、班级嵌套学校）说明随机效应结构、聚类标准误",
        "社会敏感变量（如欺凌、心理健康）报告伦理审查与自愿参与"
    ),
    key_venues=(
        "Journal of Educational Psychology",
        "Child Development",
        "Journal of Research on Adolescence",
        "Developmental Psychology",
        "Journal of Consulting and Clinical Psychology"
    ),
    units_and_formulas_notes=(
        "胜任力量表分数给出 T 分数/百分位/标准分与信度（α、ω）",
        "效应量报告 Cohen's d、Glass's Δ、ηp²、SMD，注明是否校正小样本",
        "D/P 值给出重叠比例并配合基线趋势与干预趋势的视觉比较",
        "百分比给出基数 N；缺失值处理（多重插补、成对删除）须在方法中说明"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Stata", "NVivo", "Mplus", "JASP", "jamovi", "G*Power", "Excel", "Qualtrics", "SurveyMonkey", "Behavior Observer PACER", "Kahoot", "Google Classroom", "Canvas LMS", "Moodle", "Blackboard", "Tableau", "Power BI"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
