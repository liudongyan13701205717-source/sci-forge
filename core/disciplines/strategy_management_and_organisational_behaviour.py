"""战略管理学科论文支持：战略理论与组织行为、管理创新与领导力研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="strategy_management_and_organisational_behaviour",
    aliases=(
        "strategy_management_and_organisational_behaviour",
        "战略管理",
        "组织行为",
        "组织行为学",
        "战略与组织行为",
        "strategic management",
        "organisational behaviour",
        "organizational behaviour",
        "strategy and OB",
        "组织战略",
        "管理战略",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与理论框架）",
            "methods（研究设计与实证方法）",
            "results（发现与检验结果）",
            "discussion（理论贡献与实践含义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业或组织案例）",
            "analysis（战略行为与组织动态分析）",
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
    citation_style="APA 7 样式",
    reporting_standards={
        "empirical": "实证研究须报告样本量、数据来源与置信区间",
        "survey": "问卷研究须报告 Cronbach's alpha 与因子载荷",
        "case": "案例研究须遵循 Eisenhardt 多案例设计规范",
        "meta_analysis": "元分析须遵循 PRISMA 与 META 报告规范",
    },
    conventions=(
        "构念名称须使用理论文献中的标准术语",
        "测量工具须注明量表来源（如 validated scale）",
        "模型须报告效应量（f² 或 R²）与显著性",
        "控制变量须列出并说明纳入理由",
        "中介/调节效应须区分直接效应与间接效应",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Strategic Management Journal",
        "Organization Science",
        "Journal of Management Studies",
        "Journal of Business Research",
    ),
    units_and_formulas_notes=(
        "效应量：f² 或 R²；显著性：p 值",
        "信度：Cronbach's alpha（≥0.7）",
        "构念区分效度：AVE 或 Fornell-Larcker",
        "时间跨度：年；样本规模：N",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "STATA", "AMOS", "Mplus", "SmartPLS", "Harman (structural equation modeling)", "R (lavaan, plm)", "Python (pandas, statsmodels)", "Jupyter Notebook", "NVivo", "Atlas.ti", "Qualtrics", "SurveyMonkey", "MROG (interview recording)", "Tableau", "Power BI", "Excel (Data Analysis ToolPak)", "LaTeX", "Endnote", "Prism"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSCI"),
)
