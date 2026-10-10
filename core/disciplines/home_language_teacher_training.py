"""母语教师培训学科论文支持：师范教育、语言教师发展与课堂研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="home_language_teacher_training",
    aliases=("home_language_teacher_training", "母语教师培训", "语文教师教育", "语言教师教育", "师范教育", "L1 Teacher Training", "Native Language Teacher Education", "Pedagogy of First Language", "Language Teacher Preparation"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "AERA Standards for Educational Research", "k2": "ERIC 教育研究编码规范", "k3": "GB/T 14283 语文课程标准"},
    conventions=("受试者须匿名并编号", "课堂观察须标注观察框架（如 FIAS/CAT）", "评分须附评分细则与评分者一致性", "访谈转录须区分语言原文与译本", "混合方法须注明量化与质性整合点"),
    key_venues=("Teachers College Record", "Journal of Teacher Education", "Teaching and Teacher Education", "Language Testing", "Linguistic Landscape"),
    units_and_formulas_notes=("班级人数：人", "教学时长：分钟/学期", "量表得分：0–5 或 1–5 Likert", "评分一致性：Cohen's kappa"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("SPSS", "R（教育统计）", "JASP", "Stata", "NVivo（质性分析）", "MAXQDA", "ATLAS.ti", "ELAN（语料对齐）", "Transana", "Audacity（录音）", "OBS Studio（课堂录像）", "FIAS 课堂观察框架", "CLASS 互动评估量表", "Google Forms（问卷）", "Qualtrics", "EndNote", "Zotero", "RefWorks", "LaTeX（论文排版）", "Overleaf"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
