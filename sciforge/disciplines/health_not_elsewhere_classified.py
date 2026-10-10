"""卫生（未另分类）学科论文支持：跨领域卫生研究、医学教育与公共卫生服务。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_not_elsewhere_classified",
    aliases=("health_not_elsewhere_classified", "卫生（未另分类）", "卫生学", "公共卫生", "医学教育", "卫生服务", "卫生研究"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法与数据）", "results（研究结果）", "discussion（讨论与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析与讨论）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("研究对象须注明纳入与排除标准", "样本量须注明抽样方法与代表性", "卫生统计指标须注明来源与年份", "伦理审批须注明审批机构与编号", "利益冲突须声明"),
    key_venues=("Journal of Clinical Medicine", "Global Health", "International Journal of General Medicine", "中国全科医学", "中华流行病学杂志"),
    units_and_formulas_notes=("死亡率：‰（1/1000）", "发病率：%（实际/理论×100%）", "服务覆盖率：%（实际/目标×100%）", "健康期望寿命：年"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("电子病历系统（EHR）", "医学知识图谱平台", "临床决策支持系统（CDSS）", "医学影像诊断系统（PACS）", "SPSS", "Stata", "SAS", "R（统计分析）", "REDCap 数据收集", "Epi Info 流行病学分析", "Cochrane 系统综述工具 RevMan", "Meta 分析软件（RevMan）", "医学教育仿真系统", "远程医疗会诊平台", "卫生服务质量评价工具", "生物统计学软件（SAS）", "临床指南检索系统（NICE）", "卫生服务需求预测模型", "卫生数据仓库系统", "公共卫生监测预警平台"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "医学文献检索系统（PubMed）"),
)
