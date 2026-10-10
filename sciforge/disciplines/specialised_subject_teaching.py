"""专科学科教学学科论文支持：学科教学法/课程与教材/教师专业发展体裁、APA 7 与 SQUIRE 2.0 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="specialised_subject_teaching",
    aliases=("specialised_subject_teaching", "专科学科教学", "Specialised Subject Teaching", "学科教学", "学科教学法", "Subject Didactics", "学科教师教育", "学科教研", "课程与教学论"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "intervention": "SQUIRE 2.0（教学干预与教育改进型研究）",
        "case_series": "CARE（案例系列）",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
    },
    conventions=(
        "须声明学科领域与学段（如物理·初中 / 语文·高中）",
        "教学干预描述达可复现粒度：教材版本、课时、班型、教师背景",
        "教学效度用前后测差值+协变量校正（ANCOVA），并报告效应量",
        "质性研究给出编码饱和过程与双编码者一致性",
        "伦理批准与教师/学生/家长知情同意须说明",
    ),
    key_venues=(
        "Teaching and Teacher Education",
        "Educational Research Review",
        "Journal of Research in Science Teaching",
        "Studies in Science Education",
        "Journal of Curriculum Studies",
    ),
    units_and_formulas_notes=(
        "学习增益报前后测标准化差值 g = (M_post − M_pre) / SD_pre",
        "效应量用 Cohen's d 或 d_gc（Hedges 校正小样本）",
        "课堂观察编码按 SOLO / FAS 等框架分类并给 κ 值",
        "测验信度报 Cronbach's α；难度 P、区分度 D 分列",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "JASP", "NVivo", "ATLAS.ti", "MaxQDA", "TeachLivE 课堂录像分析", "Tobii Pro 眼动仪", "Camtasia", "Desmos", "GeoGebra", "Google Classroom", "PowerSchool", "EndNote", "Zotero", "Microsoft Excel", "Tableau", "LaTeX", "Scratch"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
