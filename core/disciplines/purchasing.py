"""采购学学科论文支持：需求管理/供应绩效/采购伦理体裁、CIPS 报告规范与供应指标注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="purchasing",
    aliases=("purchasing", "采购学", "采购", "供应管理", "供应链采购", "采购管理", "purchasing management", "supplier management"),
    paper_types={
        "research": ("abstract", "introduction（采购问题与背景）", "methodology（方法与样本）", "results（采购绩效数据）", "discussion（管理启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（采购案例）", "analysis（策略与流程分析）", "results（成本与绩效结果）", "discussion（改进建议）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（采购趋势）", "references"),
    },
    citation_style="APA 7（可参考 CIPS 出版体例）",
    reporting_standards={"supplier_survey": "供应商调查遵循 AAPOR 报告规范", "cost_benchmark": "成本基准对比须说明口径与年份", "procurement_experiment": "招标实验报告随机化处理与安慰剂检验"},
    conventions=("采购分类（直接/间接/服务）须说明", "成本口径区分采购价、TCO、总成本", "样本企业与采购金额须报告", "供应商评价给出权重与打分表", "币种与汇率年须注明"),
    key_venues=("Journal of Purchasing", "Supply Chain Management Journal", "International Journal of Physical Distribution & Logistics Management", "European Journal of Procurement & Supply Chain Management", "中国采购与招标网研究"),
    units_and_formulas_notes=("成本节约给出绝对值与百分比并注明基线", "绩效指标（OTD/PPM/合格率）给口径", "金额给统一币种与年份", "样本量与缺失率须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python（Pandas/PyTorch）", "Excel", "Tableau", "MATLAB", "Minitab", "JMP", "EViews", "Qualtrics", "SurveyMonkey", "NVivo", "Gephi", "Gurobi", "CPLEX", "Word", "LaTeX", "EndNote", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
