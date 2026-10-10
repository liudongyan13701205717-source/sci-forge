"""太平洋人民教育学科论文支持：太平洋岛屿教育系统、教学法、语言政策与文化学习研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_education",
    aliases=("Pacific Peoples Education", "太平洋人民教育", "Pacific Island Education", "Pacific Education Policy", "Pacific Pedagogy", "Pacific Teacher Education", "Pacific Literacy", "Pacific Early Childhood Education"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "教育评价遵循CIPP框架", "k2": "定性研究遵循OREAS原住民研究伦理准则", "k3": "教育干预遵循PICO研究设计"
    },
    conventions=("教育学文献引用须含教学对象、学段与教学法", "涉及学生学习数据须遵循儿童隐私保护准则", "文化适切性(Culturally Responsive)须说明理论依据", "评价工具须报告信度（Cronbach α）与效度证据", "多学段研究须给出样本构成、教师背景与教学环境描述"),
    key_venues=("Pacific Education Journal", "Journal of Pacific Teachers Education", "International Journal of Educational Research", "Teachers College Record", "Research in Comparative and International Education", "Education Policy Analysis Archives"),
    units_and_formulas_notes=("教育评价工具须报告信度（Cronbach α≥0.7）与内容效度", "学生成绩报告须使用标准化分（z分/Z分）并附常模", "学习成果数据须区分前测与后测并标注时间间隔", "教学干预研究须报告干预时长、频次与教师培训背景"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "JASP", "NVivo", "ATLAS.ti", "Qualtrics", "SurveyMonkey", "Google Forms", "Google Classroom", "Canvas LMS", "Moodle", "Turnitin", "iCUBE Learning", "ClassDojo", "Zotero", "Endnote", "LaTeX", "Overleaf", "Microsoft Word"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
