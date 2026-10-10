"""政治经济学论文支持：制度变迁、经济史、政治经济分析与经济政策评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="political_economics",
    aliases=("political_economics", "政治经济学", "马克思主义政治经济学", "Political Economics", "经济史", "Economic History", "经济政策", "经济与社会", "经济体制", "Economics and Society"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式",
    reporting_standards={"AEA": "经济学研究协会论文报告规范", "JOE": "经济学期刊报告规范", "JSTOR": "经济史数据报告规范"},
    conventions=("数据来源须注明机构与版本", "时间序列须注明频率与调整方法", "变量定义须给出操作化方案", "计量模型须报告标准误与拟合优度", "稳健性检验须提供"),
    key_venues=("American Economic Review", "Journal of Political Economy", "Quarterly Journal of Economics", "Economic Journal", "经济研究"),
    units_and_formulas_notes=("GDP 用万元或亿美元", "利率用 %", "时间序列用年/季/月数据", "通胀率用 %"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python (NumPy/SciPy/Pandas)", "MATLAB", "EViews", "SPSS", "SAS", "JASP", "Mplus", "LaTeX", "EndNote", "Zotero", "World Bank Open Data", "IMF Data", "UN Data", "OECD Data", "Eurostat", "Tableau", "Power BI", "Microsoft Excel"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "JSTOR"),
)