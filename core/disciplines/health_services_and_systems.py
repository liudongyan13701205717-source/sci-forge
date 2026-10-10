"""卫生服务与体系学科论文支持：卫生政策与体系研究体裁、APA 7 引用样式与卫生经济注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_services_and_systems",
    aliases=("health_services_and_systems", "卫生服务与体系", "卫生政策", "医疗卫生系统", "公共卫生", "卫生经济学", "卫生管理", "卫生研究", "卫生系统"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "policy_analysis": "政策分析规范",
        "program_evaluation": "项目评估规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "卫生指标口径须明确",
        "人口学变量须分层报告",
        "政策变量须注明来源",
        "数据来源须报告",
        "敏感性分析须报告",
    ),
    key_venues=(
        "Health Policy and Planning",
        "Health Services Research",
        "BMJ",
        "Social Science & Medicine",
        "International Journal for Equity in Health",
    ),
    units_and_formulas_notes=(
        "货币单位须明确（本币/美元）",
        "单位人口指标须报告分母",
        "公式用 amsmath",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Stata", "SPSS", "SAS", "DHIS2", "OpenMRS", "HealthMap", "ODK", "KoboToolbox", "Tableau", "Power BI", "Meta-Analyst", "RevMan", "PRISMA", "ICER", "NICE", "WHO-CHOICE", "GBD", "EndNote", "Microsoft Excel"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
