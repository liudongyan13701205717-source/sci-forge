"""未在其他分类的个人服务学科论文支持：美容、健康、生活服务等个人服务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_services_not_elsewhere",
    aliases=("personal_services_not_elsewhere", "个人服务", "美容服务", "健康服务", "生活服务", "personal services", "beauty services", "生活管理", "服务消费"),
    paper_types={
        "research": ("abstract", "introduction（服务议题背景）", "methodology（消费者/服务者）", "results（服务数据）", "discussion（服务意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（服务案例）", "analysis（服务模式）", "results（服务效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（服务理论）", "evidence synthesis（服务证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("服务类型须清晰定义", "消费者抽样方法须说明", "服务满意度量表须报告信效度", "伦理审批须给出", "结果给出置信区间"),
    key_venues=("Journal of Service Research", "Service Industries Journal", "International Journal of Consumer Studies", "Journal of Retailing and Consumer Services", "European Management Journal"),
    units_and_formulas_notes=("价格单位用元或美元", "满意度量表采用 5 点 Likert", "统计结果保留 2 位小数", "样本量须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "Tableau", "Power BI", "Python", "Jupyter", "Excel", "Adobe Illustrator", "Photoshop", "Canva", "Notion", "Moodle", "Zoom"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
