"""原住民教师培训论文支持：文化本位教学、双语教育、教师培养方案与田野课程。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="indigenous_teacher_training",
    aliases=("indigenous_teacher_training", "原住民教师培训", "aboriginal_education", "indigenous_teacher_education", "two-eyed_seeing", "Indigenous_teacher_prep", "bilingual_education", "place_based_education", "decolonial_pedagogy"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（教育研究标准）",
    reporting_standards={"curriculum": "课程须报告文化内容比例、评审流程与社区参与", "practicum": "实地实习须报告社区伦理审查与导师配置", "student_outcomes": "学习成效须遵循 CRESST/CRESST 报告规范（背景、样本、数据、结果）"},
    conventions=("引用原住民教学法须标注社区/部落来源", "术语区分原住民自述与他者描述", "案例须明确文化语境与地理位置", "叙述尊重社区贡献者并致谢", "评估工具须遵循文化适配性"),
    key_venues=("Journal of Canadian Indian Education", "Australian Journal of Indigenous Education", "International Journal of Multiple Perspectives in Indigenous Studies", "Journal of Teacher Education", "Education Canada"),
    units_and_formulas_notes=("学习成效以 Likert/评分报告均值与标准差", "课程比例以学时/百分比表达", "样本量以 N 表示并说明取样框架", "文化适配指标以社区评审结果为主"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "Atlas.ti", "SPSS", "R", "JASP", "QGIS", "KoboToolbox", "Central", "Qualtrics", "SurveyMonkey", "Google Forms", "LaTeX", "Zotero", "EndNote", "Adobe Acrobat", "Canva", "Google Docs", "Microsoft OneNote", "Zoom", "Audacity"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
