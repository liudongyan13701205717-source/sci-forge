"""劳动福利学科论文支持：员工福利、薪酬体系、工作生活质量与人力资本管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="labour_welfare",
    aliases=(
        "labour_welfare",
        "劳动福利",
        "Employee Benefits",
        "Workplace Wellness",
        "Labour Welfare",
        "Human Capital Welfare",
        "Compensation and Benefits",
        "Employee Wellbeing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
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
    citation_style="APA",
    reporting_standards={
        "k1": "ILO C102 社会保障最低标准公约",
        "k2": "GB/T 19001 质量管理（体系与福利评估关联）",
        "k3": "EU Directive 2010/18/EU 父母与育儿假指令",
    },
    conventions=(
        "福利成本须区分固定福利与弹性福利",
        "薪酬数据须注明币种与购买力平价",
        "员工满意度须采用标准化量表（如JDI、GSS）",
        "福利政策须注明覆盖范围与生效时间",
        "人力资本ROI须注明计算周期与贴现率",
    ),
    key_venues=(
        "Human Relations",
        "Academy of Management Journal",
        "Journal of Occupational Health Psychology",
        "Journal of Business and Psychology",
        "中国人力资源开发",
    ),
    units_and_formulas_notes=(
        "薪酬总额（TC）=固定薪酬+浮动薪酬+福利",
        "福利成本占薪酬比%：福利总额/薪酬总额×100%",
        "员工满意度指数（ESI）：加权平均百分制",
        "人力资本投资回报=净收益/总投资×100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Workday", "SAP SuccessFactors", "Oracle HCM", "ADP", "UKG", "Cornerstone", "BambooHR", "Culture Amp", "Lattice", "15Five", "Betterworks", "Qualtrics", "SurveyMonkey", "HR Cloud", "Zoho People", "ADP Workforce Now", "Workforce Analytics", "Power BI", "Tableau", "HRmetrics"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
