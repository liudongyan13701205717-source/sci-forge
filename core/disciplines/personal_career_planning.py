"""个人职业规划学科论文支持：生涯规划、职业发展测评与咨询服务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_career_planning",
    aliases=("personal_career_planning", "职业规划", "生涯规划", "职业发展", "career planning", "career development", "生涯辅导", "职业辅导", "职业发展咨询"),
    paper_types={
        "research": ("abstract", "introduction（生涯议题背景）", "methodology（量表/访谈设计）", "results（职业测评结果）", "discussion（生涯启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（个体生涯案例）", "analysis（生涯发展过程）", "results（规划效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（生涯理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("生涯量表信效度须报告", "访谈数据须说明编码方式", "生涯阶段须依据理论定义", "研究伦理审批须给出", "结果给出标准化分"),
    key_venues=("Journal of Vocational Behavior", "The Career Development Quarterly", "International Journal for Educational and Vocational Guidance", "Career Development International", "Journal of Career Assessment"),
    units_and_formulas_notes=("量表得分保留 2 位小数", "T 分数或百分位须说明", "生涯量表采用标准化版本", "样本量与信效度须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Holland Code", "Strong Interest Inventory", "Myers-Briggs", "Schunk Career Vision", "Career Key", "O*NET", "MyNextMove", "LinkedIn Learning", "Coursera", "EDAP", "Gordon Career Development", "SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "Python", "Jupyter"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
