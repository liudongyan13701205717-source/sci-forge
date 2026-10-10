"""科学计量学学科论文支持：科学计量学/文献计量学/知识图谱体裁与计量研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="scientometrics",
    aliases=("scientometrics", "科学计量学", "文献计量学", "科学学", "scientometrics", "bibliometrics", "引文分析", "科研评价"),
    paper_types={
        "research": ("abstract", "introduction（计量问题与数据源）", "methodology（数据采集与指标计算）", "results（指标与网络结果）", "discussion（趋势与意义讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（计量案例背景）", "analysis（指标分析）", "results（可视化结果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（计量方法综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"bibliometric": "计量研究遵循 PRISMA-B 声明", "meta_analysis": "元分析遵循 PRISMA 声明", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("数据来源与检索式须报告", "计量指标须给出计算式（h 指数/被引次数/共词）", "时间范围须明确", "样本量与去重规则须说明", "可视化须标注参数（节点数/边权阈值）"),
    key_venues=("Scientometrics", "Journal of Informetrics", "Journal of Informetrics (Elsevier)", "Research Policy", "Journal of Web Science", "Journal of the American Society for Information Science and Technology"),
    units_and_formulas_notes=("h 指数无量纲", "被引次数以次记", "共词强度以加权次数记", "网络指标须给出中心度计算式"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("VOSviewer", "CiteSpace", "Publons", "Mendeley", "Zotero", "EndNote", "RefWorks", "R", "MATLAB", "Python", "NetworkX", "Gephi", "GSL", "OriginLab", "Excel", "Matplotlib", "SciPy", "Bibliometrix（R 包）", "Biblioshiny（Web 界面）", "OpenRefine"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "DOAJ", "Web of Science", "Scopus", "Google Scholar", "Dimensions"),
)
