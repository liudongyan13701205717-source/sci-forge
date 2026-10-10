"""非学科专门化教师教育学科论文支持：一般教学法与教师专业发展研究体裁、APA 7 引用样式与注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_without_subject",
    aliases=(
        "teacher_training_without_subject",
        "教师教育",
        "一般教学法",
        "教师专业发展",
        "Teacher training without subject",
        "general pedagogy",
        "teacher professional development",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究问题）",
            "methods（设计、样本与工具）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案与情境）",
            "data and analysis（资料与分析过程）",
            "findings（发现）",
            "discussion and implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，教育科学主流规范）",
    reporting_standards={
        "empirical": "实证研究须报告抽样框、样本量、流失率与代表性",
        "ethics": "涉及教师/学生的研究须取得伦理批准与知情同意",
        "psychometrics": "使用既有量表须报告许可来源与信度重测结果",
        "qualitative": "质性研究遵循 COREQ 或 GRD 报告清单",
        "meta_analysis": "元分析遵循 PRISMA 并报告异质性指标",
    },
    conventions=(
        "教师/学生一律匿名化，机构名称作地区化处理",
        "研究问题须与结果小节一一对应，讨论不重复结果",
        "量表信度报告 Cronbach's α 与组合信度",
        "质性资料须说明转录语言、编码层级与三角验证",
        "政策与课程标准引用须给出年份与文件编号"
    ),
    key_venues=(
        "Teaching and Teacher Education",
        "Journal of Professional Development in Education",
        "Studies in Higher Education",
        "International Journal of Educational Research",
        "Educational Research Review",
    ),
    units_and_formulas_notes=(
        "显著性用 p 值并注明校正方式；组间比较报告效应量",
        "公式用 amsmath；相关与效应量公式须编号并被引用",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "培训投入用学时（hour）而非课时，需说明换算"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "Qualtrics", "SurveyMonkey", "SPSS", "JASP", "Stata", "R", "ELAN", "OBS Studio", "Camtasia", "Weave", "Mural", "Trello", "Microsoft Forms", "Google Forms", "RefWorks", "Mendeley", "Obsidian", "Flip"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
