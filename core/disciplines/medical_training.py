"""医学培训学科论文支持：医师教育与临床培训。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_training",
    aliases=("medical_training", "医学培训", "residency", "clinical education", "培训评估", "住院医师", "CME"),
    paper_types={
        "research": ("abstract", "introduction（教育背景）", "methodology（干预设计）", "results（效果数据）", "discussion（教育意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（培训案例）", "analysis（教学反思）", "results（学习成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（教育理论）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "教育研究须报告教学对象与样本量", "k2": "能力评估须使用标准化量表（如 DOPS、Mini-CEX）", "k3": "培训干预须报告对照设计与效应量"},
    conventions=("教学术语首次出现标注定义", "量表名称与版本须注明", "统计结果报告 95% CI", "伦理审查与知情同意须声明", "教学场景须脱敏处理"),
    key_venues=("Medical Education", "Academic Medicine", "Acad Med", "BMC Medical Education", "Journal of General Internal Medicine"),
    units_and_formulas_notes=("培训时长以学时计", "能力评分采用 Likert 量表", "效应量以 Cohen's d 报告", "完成率 = 结业人数/入组人数"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Mini-CEX", "DOPS", "OSCE", "Kilcarney Assessment", "Lectora", "Epidata", "Qualtrics", "SPSS", "R (lme4)", "STATA", "Power Analysis", "GraphPad Prism", "Moodle LMS", "SimMan", "VR Training", "ePortfolio", "SurveyMonkey", "EndNote", "Zotero", "LaTeX"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
