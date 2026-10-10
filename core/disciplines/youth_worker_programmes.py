"""青少年工作者培训项目学科论文支持：青年工作教育与培训研究、APA 引用样式与能力框架注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="youth_worker_programmes",
    aliases=("youth_worker_programmes", "青少年工作者培训项目", "青年工作者培训", "youth worker training", "youth work education"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与培训问题）",
            "literature review（青年工作教育研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "training_evaluation": (
            "abstract",
            "introduction",
            "training design（培训设计）",
            "implementation（实施）",
            "evaluation（评估）",
            "outcomes（结果）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and search（范围与检索）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 第 7 版样式（作者-年份）",
    reporting_standards={
        "training_design": "培训设计须遵循 ADDIE/柯氏四级评估等模型",
        "competency_framework": "能力框架须遵循 IAYW/EYF 等标准",
        "outcome_measurement": "成果测量须报告指标、工具与信效度",
        "ethics": "研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "青年工作术语遵循 IAYW/EYF 等标准",
        "能力框架遵循青年工作者能力框架",
        "培训评估遵循 ADDIE/柯氏四级评估等模型",
        "培训情境描述完整（机构、年龄、文化）",
        "成果测量须明确条件与情境"
    ),
    key_venues=(
        "Journal of Youth Work",
        "Youth & Policy Journal",
        "Journal of Youth Work Education",
        "International Journal of Youth and Adolescence",
        "Journal of Youth Studies"
    ),
    units_and_formulas_notes=(
        "培训时长用小时/周表示",
        "能力水平用李克特量表（1-5 或 1-7）",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SurveyMonkey", "SPSS", "R (lme4)", "Stata", "MPlus", "SmartPLS", "NVivo", "Atlas.ti", "MAXQDA", "Tableau", "Power BI", "Excel", "Moodle", "Canvas LMS", "Blackboard Learn", "Articulate Storyline", "Adobe Captivate", "H5P", "360Learning"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
