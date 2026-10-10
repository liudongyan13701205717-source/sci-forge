"""办公机械操作学科论文支持：办公机器使用与设备管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="operation_of_office_machines",
    aliases=("operation_of_office_machines", "办公机械操作", "办公设备", "Office Machine Operation", "办公设备管理", "复印机操作", "打印机操作", "Office Equipment"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "设备使用效率评估规范", "k2": "办公自动化流程报告", "k3": "设备维护记录标准"},
    conventions=("设备型号与参数标注", "操作效率指标定义", "故障率统计方法", "成本效益分析框架"),
    key_venues=("Journal of Information Systems", "Information Technology & People", "办公自动化", "计算机应用", "Information Management & Computerization"),
    units_and_formulas_notes=("打印速度页/分钟", "故障率以次/月", "设备利用率以%", "运营成本以元/千页"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office", "SPSS", "R", "Python (pandas)", "SAP", "Oracle", "Excel", "Access", "ERP System", "Printer (HP)", "Copier (Ricoh)", "Scanner (Fujifilm)", "Plotters", "Fax Machine", "Multifunctional (MFP)", "Document Management (M-Files)", "BPM (Camunda)", "SharePoint", "EndNote", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
