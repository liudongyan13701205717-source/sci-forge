"""管理学论文支持：战略与组织、实证识别、案例研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business",
    aliases=("management", "business", "strategy", "管理学", "工商管理", "战略", "组织"),
    paper_types={
        "research": ("abstract", "introduction", "theory and hypotheses", "empirical setting",
                     "data and methods", "results", "discussion", "references"),
        "case_study": ("abstract", "introduction", "case selection", "data sources（三角验证）",
                       "analysis", "propositions", "references"),
        "review": ("abstract", "introduction", "theory review", "framework", "future research", "references"),
    },
    citation_style="APA 7th（JOM/AMJ 系）",
    reporting_standards={
        "hypotheses": "假设须理论推导支撑，逐条编号对应检验",
        "endogeneity": "内生性处理（工具变量/固定效应/Heckman）须说明并做稳健性",
        "sample": "样本选择标准与偏差讨论（survivor bias）须给出",
        "case": "案例研究给三角验证（访谈+档案+观察）与构念效度表",
        "measure": "构念测量给信效度（Cronbach α/AVE/CR）与区分效度检验",
    },
    conventions=(
        "理论贡献对话具体文献（哪些假设被挑战/延伸）",
        "管理启示与实践含义分开；避免空泛建议",
        "变量描述统计表与相关矩阵必须出现",
        "结构方程给模型拟合指标（CFI/RMSEA/SRMR）",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Strategic Management Journal",
        "Administrative Science Quarterly",
        "Journal of Management",
    ),
    units_and_formulas_notes=(
        "效应量给 f² 或 R² 变化；调节效应画交互图",
        "财务数据给会计准则口径（IFRS/GAAP）与币种",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("SPSS", "Stata", "NVivo", "Tableau"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
