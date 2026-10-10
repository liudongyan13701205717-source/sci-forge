"""卫生管理学科论文支持：医院管理、卫生经济学与卫生政策研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_administration",
    aliases=("health_administration", "卫生管理", "医院管理", "卫生政策", "医疗管理", "卫生事业管理", "健康管理"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（方法与数据来源）", "results（结果与指标）", "discussion（讨论与政策启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（管理机制分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("卫生统计指标须注明统计口径与年份", "医院等级与类型须标注", "费用数据须注明价格水平与调整方式", "政策名称须注明颁布机构与文号", "样本量与代表范围须明确"),
    key_venues=("Health Affairs", "Journal of Health Services Research & Policy", "Health Policy", "International Journal for Equity in Health", "中国医院管理"),
    units_and_formulas_notes=("卫生费用：%GDP", "服务可及性：标准化得分", "病床使用率：%（实际/计划×100%）", "人均卫生支出：元/人"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Hospital Information System（HIS）", "Health Economics Modeling Software", "WHO Health Accounts Framework", "WHO HIS 2013 工具包", "SPSS", "Stata", "SAS", "R（卫生经济学建模）", "Stata 生存分析模块", "Excel 数据透视表", "Power BI 仪表板", "Tableau 数据可视化", "Epi Info 统计分析", "OpenMRS 电子病历", "HL7 FHIR API 数据接口", "卫生政策仿真模型（Agent-Based）", "卫生经济学评价软件（TreeAge Pro）", "卫生服务利用调查工具", "医院绩效考核系统", "WHO Quality and Safety Framework"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
