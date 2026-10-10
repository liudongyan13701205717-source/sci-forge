"""假释官员培训学科论文支持：假释官培训/矫正实务体裁、法学引用样式与风险评估记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="parole_officer_training",
    aliases=("parole officer training", "假释官员培训", "假释官培训", "矫正培训", "probation officer training", "社区矫正", "假释实务", "刑事执行"),
    paper_types={
        "research": ("abstract", "introduction（假释与培训问题）", "methodology（培训设计与评估方法）", "results（成效与再犯数据）", "discussion（实务启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（假释对象个案）", "analysis（风险评估与干预）", "results（个案结局）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（培训与矫正理论）", "evidence synthesis（培训效果证据）", "future directions", "references"),
    },
    citation_style="APA 样式（法学/刑事执行领域；政策文本按官方文号引用）",
    reporting_standards={"risk_assessment": "风险评估工具须说明量表名称、版本与信效度指标", "recidivism": "再犯率须注明统计口径（定罪再犯/重新监禁/技术违规）与观察期", "sampling": "抽样与样本量须报告；个案报告遵循 CARE 精神", "ethics": "数据脱敏与伦理审查（IRB/委员会批准）须声明"},
    conventions=("专业术语（假释、缓刑、社区矫正、技术违规）首次出现给出定义", "犯罪人描述脱敏处理，禁用可识别信息", "法域不同（英美/大陆法系）须明确标注", "量表引用给出版本与版权归属", "政策对比按国别与年份标注"),
    key_venues=("Criminology", "Crime and Delinquency", "Journal of Experimental Criminology", "Journal of Corrections and the Law", "Prisons, Probation & Parole Association Bulletin"),
    units_and_formulas_notes=("刑期与观察期用月/年表述并注明起算点", "再犯率以百分比呈现，报告观察窗口", "量表分数给出原始分、切分点与常模", "统计结果报告效应量（如 Cohen's d、OR）与 95% 置信区间"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("HCR-20 V3 量表", "L-SLORP2 再犯风险工具", "OASIS 风险-需求评估系统", "COMPAS 再犯风险平台", "NVivo 质性分析软件", "SPSS 统计软件", "R 统计软件", "ArcGIS 地理信息系统", "Pandas 数据分析库", "Stata 统计软件", "Elasticsearch 案例检索", "G-POWER 检验力分析", "Jupyter Notebook", "Lexicoder 主题编码", "Uppsala 冲突数据", "QGIS 地理信息系统", "Tableau 数据可视化", "Qualtrics 调查平台", "HmIS（刑事司法信息系统）", "COMPASS（刑事风险评估工具）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "WorldCat 文献检索", "Scopus 文献数据库", "CNKI 中国知网", "ACLED 冲突事件数据库", "GEO 基因组数据库"),
)
