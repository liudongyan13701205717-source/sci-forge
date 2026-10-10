"""Basic remedial programmes for youth 学科论文支持：青少年补救教育项目体裁、APA 引用样式与青少年教育记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="basic_remedial_programmes_for_youth",
    aliases=(
        "basic_remedial_programmes_for_youth",
        "remedial education",
        "补救教育",
        "基础补救教育",
        "remedial programmes",
        "remedial education for youth",
        "basic remedial",
        "basic skills for youth",
        "youth remedial programmes",
        "youth education",
        "青少年教育",
        "basic skills education",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与补救教育问题）",
            "literature review（文献综述）",
            "methods（设计、样本、工具、伦理）",
            "results（结果）",
            "discussion（讨论与教育启示）",
            "conclusion（结论）",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program description（项目描述）",
            "evaluation framework（评估框架）",
            "findings（发现）",
            "recommendations（建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（项目/政策综述）",
            "outlook（趋势展望）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Educational Psychology Review 遵循 Springer 规范）",
    reporting_standards={
        "experimental": "教育实验遵循 SAGE 实验报告规范",
        "quasi_experimental": "准实验遵循 QUASI 报告规范",
        "program_evaluation": "项目评估遵循美国教育评估标准（SEA）",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "青少年研究伦理遵循 IRB 审批与儿童保护要求",
    },
    conventions=(
        "研究须报告样本年龄、性别、教育阶段、家庭社会经济背景，避免仅用匿名化编号",
        "干预须明确课程内容、课时、教师资质、教学方法与评估工具",
        "评估工具须报告信效度指标（Cronbach's α、KR-20）与规范分数",
        "统计方法须报告检验类型、显著性水平、效应量（如 Cohen's d）",
        "涉及未成年人的研究须取得家长/监护人书面知情同意",
    ),
    key_venues=(
        "Educational Psychology Review",
        "Journal of Educational Psychology",
        "Review of Educational Research",
        "Educational Evaluation and Policy Analysis",
        "Journal of Youth and Adolescence",
        "Children and Youth Services Review",
        "Journal of Research on Educational Effectiveness",
        "Educational Research and Evaluation",
        "Review of General Psychology",
    ),
    units_and_formulas_notes=(
        "年龄用岁（整数或小数），分数用百分制或等级",
        "补救项目周期用周或月，注明干预频次",
        "效应量用 Cohen's d 或 g（准实验）",
        "样本量须报告 n 与保留率（retention rate）",
        "统计结果用 M±SD、p 值与 CI，p<0.05 视为显著",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS 26", "R (psych, lavaan)", "JASP", "Stata 17", "SAS 9.4", "Mplus 8.6", "AMOS", "NVivo 14", "ATLAS.ti", "Dedoose", "MAXQDA", "Qualtrics", "SurveyMonkey", "REDCap", "Canvas LMS", "Moodle", "Blackboard", "Schoology", "Google Classroom", "Microsoft Teams for Education", "Khan Academy", "Duolingo", "Quizlet", "Kahoot!", "Socrative", "ClassDojo", "Nearpod", "Pear Deck", "Edulastic", "Edmodo", "G*Power", "PISA", "TIMSS", "NAEP", "YouthRisk Behavior Surveillance System (YRBSS)"),
    category="教育学",
    databases=("ERIC", "OpenAlex", "CNKI", "万方", "Crossref"),
)
