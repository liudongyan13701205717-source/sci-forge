"""护理教师培训学科论文支持：护理教育/课程与评价体裁、APA 7 引用样式与教育测量注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursing_teacher_training",
    aliases=(
        "nursing_teacher_training",
        "护理教师培训",
        "Nursing Teacher Training",
        "Nursing Education",
        "Nursing Faculty Development",
        "Nursing Pedagogy",
        "Clinical Teaching",
        "Nurse Educator",
        "护理教育",
    ),
    paper_types={
        "research": ("abstract", "introduction（教学问题与理论基础）", "methodology（教学设计、对象与评价工具）", "results（教学效果与满意度）", "discussion（教师发展含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（教学情境）", "analysis（教学行为分析）", "results（学生成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（护理教育理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；教育期刊主流样式）",
    reporting_standards={
        "curriculum": "课程开发遵循 Kern 六步法",
        "survey": "教学满意度调查遵循 AAPOR 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "intervention": "教学干预研究遵循 CONSORT/EQUATOR",
    },
    conventions=(
        "教学目标按 Bloom 认知层级表述",
        "教学设计给输入-过程-产出框架",
        "评价工具信效度证据充分（Cronbach's α、内容效度）",
        "教学效果用前后测比较与效应量",
        "伦理委员会批准与知情同意须说明",
    ),
    key_venues=(
        "Nurse Education Today",
        "Journal of Nursing Education",
        "Nursing Forum",
        "International Journal of Nursing Education",
        "Nurse Education in Practice",
    ),
    units_and_formulas_notes=(
        "教学效果给前后测均值差与 Cohen's d",
        "满意度用 Likert 5 分制",
        "OSCE 通过率与及格线说明",
        "样本量与显著性检验须说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Canvas LMS", "Blackboard", "Moodle", "Schoology", "Microsoft Teams", "Zoom", "Webex", "Microsoft Excel", "SPSS", "R", "NVivo", "ATLAS.ti", "Tableau", "EndNote", "Mendeley", "Zotero", "教学评估软件", "护理模拟教学系统", "教学录像分析软件", "Qualtrics"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Google Scholar"),
)
