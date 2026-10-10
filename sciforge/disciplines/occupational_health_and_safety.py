"""职业健康与安全学科论文支持：职业安全/风险评估体裁、ANSI/OSHA 引用样式与安全记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="occupational_health_and_safety",
    aliases=("occupational_health_and_safety", "职业健康与安全", "职业安全", "工作场所安全", "ohs", "safety management"),
    paper_types={
        "research": ("abstract", "introduction（背景与安全议题）", "methodology（安全评估方法）", "results（风险量化）", "discussion（对策与启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（事故/事件描述）", "analysis（原因分析）", "results（后果与损失）", "discussion（经验教训）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（安全理论）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="OSHA/ANSI Z535 样式",
    reporting_standards={"observational": "遵循 STROBE 声明", "case_report": "遵循 CARE 指南", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("事故记录须遵循 ILO 分类", "损失统计须给出 LR 与 LTIR", "风险矩阵须注明分级", "法规引用须注明条款", "干预措施须报告前后对比"),
    key_venues=("Safety Science", "Accident Analysis & Prevention", "Work", "Journal of Loss Prevention in the Process Industries", "Safety Science International"),
    units_and_formulas_notes=("事故率用 per 200000 h", "损失用百万工时", "热应力用 WBGT", "能量用 J", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SafetyCulture iAuditor", "Intelex EHS", "Enablon EHS", "SAP EHS", "Risk Register 工具", "热应力 WBGT 仪", "PPE 合规检测", "职业风险矩阵软件", "事故调查软件", "Hazard ID 系统", "OSHA 300/301 报告工具", "OSHA 300 Log", "ISO 45001 认证工具", "ANSI Z535 指南", "Python 数据分析", "R", "SPSS", "ArcGIS", "Epi Info", "Tableau"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
