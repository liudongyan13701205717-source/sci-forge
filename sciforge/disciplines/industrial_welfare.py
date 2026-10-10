"""员工福利学科论文支持：企业福利制度设计、员工满意度与福利政策效果评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="industrial_welfare",
    aliases=(
        "industrial_welfare",
        "员工福利",
        "企业福利制度",
        "劳动关系与福利",
        "工业福利",
        "员工保障研究",
        "industrial welfare systems",
        "employee benefits",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（人力资源管理）",
    reporting_standards={
        "survey_study": "调查须报告响应率、信度系数与抽样方法",
        "experimental_design": "实验/准实验设计须报告随机化与预测控制",
        "meta_analysis": "荟萃分析须遵循 PRISMA 与报告效应量置信区间",
        "policy_evaluation": "政策评估须说明对照设计与因果识别策略",
    },
    conventions=(
        "福利类型分类须注明框架（现金/非现金、法定/企业自主）",
        "员工满意度量表须注明版本与信度系数",
        "跨行业比较须控制企业规模与地域变量",
        "福利成本须用统一口径核算",
        "统计推断须报告效应量而非仅 p 值",
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Human Resource Management",
        "Journal of Labor Economics",
        "Work, Employment and Society",
        "中国人力资源管理",
    ),
    units_and_formulas_notes=(
        "满意度分数须注明量表等级（如 5 级 Likert）",
        "福利成本用元/人/年或占工资比例报告",
        "回归系数须注明标准误与显著性水平",
        "留存率、出勤率须用同一统计期",
        "效应量（Cohen d、r）须一并报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R（多层线性模型）", "Mplus（结构方程模型）", "NVivo（质性分析）", "SurveyMonkey（在线调查）", "Qualtrics（调查平台）", "Python（pandas/numpy）", "SAS（面板数据）", "EpiData（数据录入核查）", "GSS 美国综合社会调查", "中国统计年鉴", "Econometrics（meta-analysis 工具）", "AMOS（结构方程建模）", "PLS-SEM SmartPLS", "IBM SPSS AMOS", "EViews（时间序列分析）", "Tableau（结果可视化）", "Harvard Business School Case（案例研究工具）", "Microsoft Access（个案管理）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "World Values Survey 数据库", "ILO 劳动力统计数据库"),
)
