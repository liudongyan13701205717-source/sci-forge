"""原住民研究论文支持：殖民史、自决权、文化治理、语言复兴、土地权利与知识主权。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="indigenous_studies",
    aliases=("indigenous_studies", "原住民研究", "aboriginal_studies", "native_studies", "first_nations_studies", "decolonization", "postcolonial_studies", "OCAP_principles", "indigenous_knowledge"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（人文学科常用）或 Chicago",
    reporting_standards={"fieldwork": "田野调查须遵循知情同意、文化安全协议与社区批准", "data_governance": "数据共享须遵循 OCAP 与 CARE 原则（集体、赋权、责任、 ethics）", "community_approval": "出版前须获得社区/部落研究伦理委员会批准"},
    conventions=("引用原住民知识与历史须遵循 OCAP/CARE 原则",         "术语区分原住民自述与他者描述（如 原住民 vs 印第安）", "案例须标注社区、族群与地理位置", "叙述尊重多元语言/方言语境", "致谢原住民族贡献者与知识持有者"),
    key_venues=("Journal of Indigenous Studies", "AlterNative", "Indigenous Studies Quarterly", "Journal of Intercultural Studies", "Australian Aboriginal Studies"),
    units_and_formulas_notes=("人口数据引用官方普查口径并标注年份", "历史时间线按部落口径与外部殖民口径并列", "地理范围用官方保留地/社区边界", "经济数据以社区口径优先"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "Atlas.ti", "ELAN", "Anviz", "QGIS", "ArcGIS", "Google Earth Pro", "KoboToolbox", "Central", "ODK", "Qualtrics", "SurveyMonkey", "Google Forms", "Audacity", "FieldRecorder", "Zotero", "EndNote", "LaTeX", "Transana", "AIATSIS"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
