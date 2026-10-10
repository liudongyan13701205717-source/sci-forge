"""Curriculum and pedagogy 学科论文支持：教学设计与教学法研究体裁、教育学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="curriculum_and_pedagogy",
    aliases=(
        "curriculum_and_pedagogy",
        "curriculum and pedagogy",
        "课程与教学论",
        "教学法",
        "教学论",
        "pedagogy",
        "didactics",
        "teaching methods",
        "instructional practice",
        "pedagogy and curriculum",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "classroom_study": (
            "abstract",
            "introduction",
            "context（学校与班级背景）",
            "intervention（教学设计描述）",
            "data collection（课堂观察、访谈、作业样本）",
            "findings（发现）",
            "implications（教学启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review（教学法综述）",
            "trends and challenges（趋势与挑战）",
            "recommendations（建议）",
            "references",
        ),
    },
    citation_style="APA 第7版（教育学主流规范，APA 7）",
    reporting_standards={
        "rct": "随机对照实验遵循 CONSORT 声明与教育实验报告规范",
        "quasi_experimental": "准实验设计须报告对照组构成、前测与效应量（Cohen's d / Hedges' g）",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethics": "涉及未成年学生须报告伦理审查批号、知情同意（学生与监护人）方式",
        "measurement": "测验工具须报告信度（KR-20/α）与效度证据",
    },
    conventions=(
        "教学设计须遵循统一框架陈述（如 UbD/逆向设计、5E 学习循环或 SOLO 分类），并注明框架版本",
        "学习者匿名化：学生代号规则统一（如 S1-S24），班级与学校化名须声明对应关系",
        "量表与测验须报告信效度与计分区间；开放作答须说明评分者与评分标准（rubric）",
        "课堂观察须说明观察时段、频次与编码框架（如 FIAS/弗兰德斯互动分析）",
        "效应量与统计显著性并行报告，避免仅以 p<.05 作结论",
        "教学材料样本、访谈片段引用须给出脱敏处理说明",
    ),
    key_venues=(
        "Educational Researcher",
        "Review of Educational Research",
        "Contemporary Educational Psychology",
        "Teaching and Teacher Education",
        "Journal of Research on Teaching in Mathematics",
        "The Elementary School Journal",
        "教师教育研究",
    ),
    units_and_formulas_notes=(
        "教学时长按课时（40/45/50 min）统一计量，跨学期研究注明校历差异",
        "效应量报告 Cohen's d 或 Hedges' g，并给出 95% CI",
        "量表采用标准分（T 分/Z 分）时注明换算公式",
        "百分比给出基数 N；缺失数据须说明处理方式（剔除/插补）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas (Instructure)", "Blackboard Learn", "D2L Brightspace", "Google Classroom", "Flipgrid", "Edpuzzle", "Kahoot!", "Socrative", "Nearpod", "Pear Deck", "ClassDojo", "Seesaw", "Padlet", "CLASS (Classroom Assessment Scoring System)", "NVivo", "MAXQDA", "ATLAS.ti", "JASP", "Jamovi", "SPSS", "RStudio", "Canva for Education", "H5P"),
    category="教育学",
    databases=("ERIC", "CNKI", "万方", "OpenAlex", "Crossref", "Web of Science"),
)
