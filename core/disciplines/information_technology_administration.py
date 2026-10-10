"""信息技术管理学科论文支持：IT 管理/治理体裁、APA 引用样式与 IT 管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_technology_administration",
    aliases=("information_technology_administration", "信息技术管理", "IT 管理", "IT 治理", "ITAM", "IT 项目管理", "信息技术战略", "IT 运维管理", "digital governance", "IT 审计"),
    paper_types={
        "research": ("abstract", "introduction（管理问题与贡献）", "methodology（研究设计与数据）", "results（实证/管理发现）", "discussion（管理启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（组织 IT 管理背景）", "analysis（管理过程分析）", "results（成效与经验教训）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（IT 管理理论框架）", "evidence synthesis（管理实践证据）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"cohort_reporting": "管理成效须报告前后对照与统计口径", "framework_adoption": "框架（COBIT/ITIL/ISO27001）须注明采用版本", "ethics": "组织数据须说明伦理审查与脱敏"},
    conventions=("管理命题须可操作化定义", "成熟度/能力等级须声明评估模型", "成本/收益用统一货币口径与折现率", "利益相关者分析须完整", "实践证据须注明组织规模/行业情境"),
    key_venues=("Journal of Management Information Systems", "Information Systems Journal", "MIS Quarterly", "International Journal of Information Management", "The Data & Management Insights"),
    units_and_formulas_notes=("KPI 定义须注明计算口径与周期", "财务指标注明货币单位与折现率", "统计显著性检验方法须声明", "公式用 amsmath；比率口径一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("COBIT 2019", "ITIL 4", "ISO/IEC 27001", "Jira", "ServiceNow", "Confluence", "Planview", "Microsoft Project", "Tableau", "Power BI", "Python (Pandas)", "Stata", "SPSS", "Looker", "Klipfolio", "Trello", "Asana", "Minitab", "CMMI", "NIST CSF"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
