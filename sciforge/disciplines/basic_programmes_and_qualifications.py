"""Basic programmes and qualifications 学科论文支持：基础项目与资格认证体裁、APA 引用样式与教育项目记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="basic_programmes_and_qualifications",
    aliases=(
        "basic_programmes_and_qualifications",
        "basic programmes and qualifications",
        "基础项目与资格认证",
        "基础教育项目与资格",
        "basic qualifications",
        "basics programmes",
        "basic education",
        "基础教育",
        "primary education",
        "elementary programmes",
        "初级项目与资格",
        "basic skills programmes",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与项目/资格问题）",
            "literature review（文献综述）",
            "methods（设计、样本、工具、伦理）",
            "results（结果）",
            "discussion（讨论与教育/政策启示）",
            "conclusion（结论）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context（政策背景）",
            "methods（政策分析框架）",
            "findings（发现）",
            "recommendations（建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（项目/资格综述）",
            "outlook（趋势展望）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Educational Research Review 遵循 Elsevier 规范）",
    reporting_standards={
        "experimental": "教育实验遵循 SAGE 实验报告规范",
        "quasi_experimental": "准实验遵循 QUASI 报告规范",
        "policy_analysis": "政策分析遵循政策分析框架报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "教育研究伦理遵循 IRB 审批与儿童保护要求",
    },
    conventions=(
        "项目须明确目标群体、课程框架、认证标准与发证机构",
        "资格认证须列出认证机构、认证等级、有效期与续证要求",
        "评估工具须报告信效度指标（Cronbach's α、KR-20）与规范分数",
        "统计方法须报告检验类型、显著性水平、效应量（如 Cohen's d）",
        "禁止以「提升」等模糊词替代具体指标变化",
    ),
    key_venues=(
        "Education Policy",
        "Educational Research Review",
        "Studies in Educational Evaluation",
        "Assessment & Evaluation in Higher Education",
        "Journal of Research on Educational Effectiveness",
        "Assessment in Education",
        "Journal of Educational Measurement",
        "Journal of Vocational Technology Research",
        "Assessment & Evaluation",
    ),
    units_and_formulas_notes=(
        "年龄用岁（整数或小数），分数用百分制或等级",
        "资格认证等级用罗马数字或等级名称（如 Level 1-5）",
        "效应量用 Cohen's d 或 g（准实验）",
        "样本量须报告 n 与保留率（retention rate）",
        "统计结果用 M±SD、p 值与 CI，p<0.05 视为显著",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS 26", "R (psych, lavaan)", "JASP", "Stata 17", "SAS 9.4", "Mplus 8.6", "AMOS", "NVivo 14", "ATLAS.ti", "Dedoose", "MAXQDA", "Qualtrics", "SurveyMonkey", "REDCap", "Canvas LMS", "Moodle", "Blackboard", "Schoology", "Google Classroom", "Microsoft Teams for Education", "Khan Academy", "Duolingo", "Quizlet", "Kahoot!", "Socrative", "ClassDojo", "Nearpod", "Pear Deck", "Edulastic", "Edmodo", "G*Power", "PISA", "TIMSS", "NAEP"),
    category="教育学",
    databases=("ERIC", "OpenAlex", "CNKI", "万方", "Crossref"),
)
