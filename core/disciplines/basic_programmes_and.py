"""Basic programmes and 学科论文支持：基础教育项目体裁、APA 引用样式与基础教育记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="basic_programmes_and",
    aliases=(
        "basic_programmes_and",
        "basic programmes",
        "基础教育项目",
        "基础教育",
        "primary education",
        "elementary education",
        "basics programmes",
        "basic skills",
        "基础教育项目",
        "elementary programmes",
        "初级教育",
        "初级项目",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与教育问题）",
            "literature review（文献综述）",
            "methods（设计、样本、工具、伦理）",
            "results（结果）",
            "discussion（讨论与教育启示）",
            "conclusion（结论）",
            "references",
        ),
        "action_research": (
            "abstract",
            "introduction",
            "context（项目背景）",
            "methods（行动研究循环：计划-行动-观察-反思）",
            "results（迭代过程与成效）",
            "discussion（反思与推广建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（政策/项目综述）",
            "outlook（趋势展望）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Education Policy/Review of Educational Research 遵循 AERA 规范）",
    reporting_standards={
        "experimental": "教育实验遵循 SAGE 实验报告规范",
        "quasi_experimental": "准实验遵循 QUASI 报告规范",
        "qualitative": "质性研究遵循 COREQ 或 SRQR",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "教育研究伦理遵循 IRB 审批与儿童保护要求",
    },
    conventions=(
        "研究须报告样本年龄、性别、教育阶段、社会经济背景，避免仅用匿名化编号",
        "干预须明确课程内容、课时、教师资质、教学方法与评估工具",
        "评估工具须报告信效度指标（Cronbach's α、KR-20）与规范分数",
        "统计方法须报告检验类型、显著性水平、效应量（如 Cohen's d）",
        "禁止以「提升」等模糊词替代具体指标变化",
    ),
    key_venues=(
        "Educational Researcher",
        "American Educational Research Journal",
        "Educational Evaluation and Policy Analysis",
        "Review of Educational Research",
        "Journal of Educational Psychology",
        "Educational Psychology Review",
        "Learning and Instruction",
        "Educational Research and Evaluation",
        "Journal of Educational Action Research",
    ),
    units_and_formulas_notes=(
        "年龄用岁（整数或小数），分数用百分制或等级",
        "效应量用 Cohen's d 或 g（准实验）",
        "样本量须报告 n 与保留率（retention rate）",
        "标准化得分用 z-score 或标准分（M=500, SD=100）",
        "统计结果用 M±SD、p 值与 CI，p<0.05 视为显著",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS 26", "R (psych, lavaan)", "JASP", "Stata 17", "SAS 9.4", "Mplus 8.6", "AMOS", "NVivo 14", "ATLAS.ti", "Dedoose", "MAXQDA", "Qualtrics", "SurveyMonkey", "REDCap", "Canvas LMS", "Moodle", "Blackboard", "Schoology", "Google Classroom", "Microsoft Teams for Education", "Khan Academy", "Duolingo", "Quizlet", "Kahoot!", "Socrative", "ClassDojo", "Nearpod", "Pear Deck", "Edulastic", "Edmodo", "G*Power", "Harvard's Data Tools (data.practice)", "PISA", "TIMSS", "NAEP"),
    category="教育学",
    databases=("ERIC", "OpenAlex", "CNKI", "万方", "Crossref"),
)
