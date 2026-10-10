"""行政管理学科论文支持：管理学/公共管理体裁、APA 引用样式与管理学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="administration",
    aliases=("administration", "行政管理", "管理学", "公共管理", "business administration",
             "management", "行政", "管理科学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "literature review（文献综述）",
            "theory and hypotheses（理论与假设）",
            "methodology（方法、样本、数据）",
            "results（描述性与推断性统计）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methodology（系统综述）",
            "findings",
            "discussion",
            "conclusions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 APA 与 AAAAM 惯例",
        "qualitative": "质性研究遵循 COREQ/SRQR",
    },
    conventions=(
        "管理学术语全文一致：领导/管理/治理/组织等核心概念须定义",
        "样本、方法与测量工具须显式说明；问卷与量表须给出 Cronbach's α",
        "统计显著性用 p 值与效应量并列报告；置信区间给出",
        "案例研究须说明案例选择理由与三角验证方法",
        "理论假设须与文献脉络对应，避免悬空",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Strategic Management Journal",
        "Journal of Management Studies",
        "Journal of Business Research",
        "California Management Review",
        "Administrative Science Quarterly",
    ),
    units_and_formulas_notes=(
        "样本量、显著性水平、置信区间须完整给出",
        "效应量报告 Cohen's d/η²/R² 等标准指标",
        "时间序列数据注明采样周期与季节性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office (Excel/Word/PowerPoint)", "SPSS", "Stata", "R", "Python", "NVivo", "ATLAS.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Tableau", "Power BI", "SAP", "Oracle", "Salesforce", "AnyLogic", "Simul8", "FlexSim", "Bloomberg Terminal", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "SSRN"),
)
