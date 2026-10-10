"""社会科学类跨学科项目与学位：研究、案例、综述体裁，Chicago 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_social_sciences",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_social_sciences",
        "社会科学类跨学科项目与学位",
        "Social Sciences Interdisciplinary Programmes",
        "Cross-disciplinary Social Science",
        "Social Science Degree Programme",
        "社会学跨学科",
        "社会科学跨学科项目",
        "社会与公共政策学位",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="Chicago（作者-年份）",
    reporting_standards={
        "k1": "PRISMA（系统综述）",
        "k2": "CORE（质性研究规范）",
        "k3": "ESOP（经济社会学报告规范）",
    },
    conventions=(
        "样本与抽样方法须详细说明",
        "问卷或访谈编码过程须报告",
        "变量操作化定义须给出",
        "跨时空比较须控制背景差异",
        "伦理审查编号须标注",
    ),
    key_venues=(
        "American Journal of Sociology",
        "American Sociological Review",
        "British Journal of Sociology",
        "European Sociological Review",
        "Journal of European Social Policy",
    ),
    units_and_formulas_notes=(
        "比率与时点须明确（横截面/面板）",
        "统计量报告 M/SD 或 中位数(IQR)",
        "样本量与失效率须报告",
        "多变量模型报告 β 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python（Pandas）", "MATLAB", "NVivo", "ATLAS.ti", "MAXQDA", "Mplus", "HAP", "SAS", "JASP", "Qualtrics", "SurveyMonkey", "World Bank Data", "World Economic Outlook", "IMF Data", "EndNote", "Tableau", "Power BI"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science"),
)
