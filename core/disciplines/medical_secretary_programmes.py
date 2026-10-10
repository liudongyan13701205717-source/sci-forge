"""医务秘书教育项目学科论文支持：医疗文书与办公管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_secretary_programmes",
    aliases=("medical_secretary_programmes", "医务秘书教育", "医疗行政", "medical office", "health office", "病历管理", "医疗文书"),
    paper_types={
        "research": ("abstract", "introduction（管理背景）", "methodology（研究方法）", "results（发现）", "discussion（实践意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（流程分析）", "results（效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "病例管理实践须符合 HIPAA 等隐私法规", "k2": "文书质量评估须说明评分标准", "k3": "行政流程改进须量化前后对比"},
    conventions=("缩写须注明全称", "文书模板须标注版本与日期", "患者信息脱敏", "引用法规条文须注明版本", "流程改进须附前后对比数据"),
    key_venues=("Journal of Healthcare Administration", "Medical Office Management", "Healthcare Management Journal", "Journal of Health Administration", "Health Policy"),
    units_and_formulas_notes=("工作时间以小时计", "文书错误率 = 错误数/总文书数", "响应时间 = 送达时间 - 请求时间", "统计以均值±标准差报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office", "Epic EHR", "Cerner", "Meditech", "OpenEMR", "PracticeSuite", "eNote Medical Records", "DocuSign", "SharePoint", "Adobe Acrobat Pro", "Grammarly", "EndNote", "SPSS", "SurveyMonkey", "Qualtrics", "Power BI", "Tableau", "Excel", "Word", "Access Database"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
