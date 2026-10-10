"""公安学/公共安全学科论文支持：警务策略/安全评估/风险治理体裁、公共安全报告规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_security",
    aliases=("public_security", "公安学", "公共安全", "警务学", "应急管理", "治安治理", "public safety", "security studies"),
    paper_types={
        "research": ("abstract", "introduction（安全威胁与背景）", "methodology（方法与数据来源）", "results（安全指标结果）", "discussion（治理对策）", "references"),
        "case_study": ("abstract", "introduction", "case description（事件复盘）", "analysis（原因与过程分析）", "results（处置效果）", "discussion（制度建议）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（风险趋势）", "references"),
    },
    citation_style="APA 7（警务实证研究）；中文期刊可用脚注式",
    reporting_standards={"field_survey": "警务实地调查遵循实地研究伦理审查", "incident_analysis": "事件分析须报告分类口径与时间窗", "risk_assessment": "风险评估给出指标权重与敏感性分析"},
    conventions=("涉密与个人隐私信息须脱敏并注明", "事件/案件口径（立案/办结/破案）须一致", "数据来源（公安统计/舆情/调研）须标注", "处置建议区分即时与长效两类", "比较研究注明法域与制度差异"),
    key_venues=("Criminal Justice Review", "Police Quarterly", "Crime, Delinquency and Social Change", "Security Journal", "中国人民公安大学学报"),
    units_and_formulas_notes=("犯罪率给每 10 万人/件口径并注明统计年份", "预警阈值与指标权重须说明构造方法", "敏感性分析给出参数变动区间", "地图呈现注明投影与数据年份"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "NVivo", "Excel", "Tableau", "QGIS", "ArcGIS", "Minitab", "JMP", "EViews", "Python（Pandas/Sklearn）", "MATLAB", "Simulink", "Gephi", "Word", "LaTeX", "EndNote", "Zotero", "PowerPoint"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
