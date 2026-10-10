"""采购、招投标与合同学科论文支持：招标流程/合同管理/契约治理体裁、CIPS/GB-T 25400 采购标准注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="purchasing_procurement_and_contracts",
    aliases=("purchasing_procurement_and_contracts", "采购招投标与合同", "招标与投标", "合同管理", "契约治理", "purchasing procurement contracts", "tendering", "contract management"),
    paper_types={
        "research": ("abstract", "introduction（采购/合同问题）", "methodology（方法与数据）", "results（合同绩效数据）", "discussion（管理启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（招标/合同案例）", "analysis（流程与条款分析）", "results（履约结果）", "discussion（条款改进）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论与条款综述）", "evidence synthesis（条款与判例综合）", "future directions（合同技术趋势）", "references"),
    },
    citation_style="APA 7（合同与法规引用注明法源与修订版）",
    reporting_standards={"contract_survey": "合同调查遵循 AAPOR 报告规范", "tender_experiment": "招标实验报告随机化处理", "contract_audit": "合同审计给出条款覆盖率与执行率"},
    conventions=("合同条款须引用原文并注明版本", "招标流程注明法定阶段（公告/评审/中标）", "金额给统一币种与年份", "术语（业主/发包/承包/总包）须界定", "合规性区分国内法规与国际惯例"),
    key_venues=("Journal of Purchasing", "International Journal of Project Management", "Supply Chain Management Review", "Contract Management", "中国招标与投标"),
    units_and_formulas_notes=("合同金额给绝对值与工期基准", "履约指标（工期延误率/违约率）给口径", "付款条件注明节点与百分比", "条款覆盖与执行率给百分点"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python（Pandas）", "Excel", "Tableau", "MATLAB", "Minitab", "JMP", "EViews", "Qualtrics", "SurveyMonkey", "NVivo", "Gephi", "Gurobi", "CPLEX", "Word", "LaTeX", "EndNote", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
