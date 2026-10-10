"""保险学科论文支持：精算与风险管理体裁、APA 引用样式与保险精算注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="insurance",
    aliases=("insurance", "保险", "保险学", "保险精算", "actuarial science", "风险管理", "risk management", "社会保险", "social insurance", "财产险", "寿险"),
    paper_types={
        "research": ("abstract", "introduction（保险问题与贡献）", "methodology（精算模型与数据）", "results（风险/收益量化）", "discussion（管理启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（保险制度/产品背景）", "analysis（机制与制度分析）", "results（评估结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（保险与精算理论）", "evidence synthesis（实证与制度证据）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"stochastic_model": "精算模型须声明随机假设与校准数据", "regulation": "监管口径（IFRS 17/Solvency II）须注明适用版本", "backtesting": "风险模型须提供回溯检验"},
    conventions=("精算符号（死亡率 μ、利率 i、准备金 V）须统一", "贴现率/名义收益率口径须明确", "保费/纯保费/附加保费区分清晰", "样本区间与生存期假设须声明", "监管口径变更须注明时间效力"),
    key_venues=("Journal of Risk and Insurance", "North American Actuarial Journal", "ASTIN Bulletin", "Insurance: Mathematics and Economics", "Annals of Actuarial Science"),
    units_and_formulas_notes=("货币金额用统一币种与年度基准", "利率以小数记（如 0.05）并注明单/复利", "精算现值记号须与寿险模型教材一致", "公式用 amsmath；生存函数与力死亡率记法统一"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("LifeOffice", "MOSEY", "R (actuarial)", "R (Life)", "Python (sactl)", "MATLAB Actuarial Toolbox", "SPSS", "SAS", "Minitab", "Gretl", "G*Power", "Crystal Ball", "@RISK", "Excel Solver", "Oracle Financial Modeling", "Planful", "Python (PyPortfolioOpt)", "Python (SciPy)", "Excel", "Tableau"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
