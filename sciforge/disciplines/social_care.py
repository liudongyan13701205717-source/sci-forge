"""社会关怀学科论文支持：老年/残障/家庭照护体裁、APA 引用样式与循证照护实践规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_care",
    aliases=("social_care", "社会关怀", "照护学", "老年护理", "disability support", "care practice", "community care", "palliative care"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与照护需求）",
            "methods（设计、参与者、干预、测量）",
            "results（结果与统计）",
            "discussion（讨论与照护含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（照护情境与个案呈现）",
            "analysis（照护过程与分析）",
            "results（干预结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（文献检索）",
            "evidence synthesis（循证证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="APA 7（Research on Aging、Journal of Aging Studies、Disability & Society 遵循 APA）",
    reporting_standards={
        "randomized_trial": "照护干预 RCT 遵循 CONSORT 声明：分配隐藏、盲法、意向性分析",
        "case_study": "照护个案研究遵循 CDSR（案例研究报告）：情境、过程、结果、反思",
        "systematic_review": "循证综述遵循 PRISMA 与 JBI 系统综述：检索、纳入、证据质量分级（Cochrane 偏倚风险）",
        "qualitative": "质性研究遵循 COREQ/SRQR 清单：照护者视角、家庭参与、反思性"
    },
    conventions=(
        "伦理审批、知情同意与二次告知须报告；涉及弱势群体（残障、老人）时须说明无障碍获取",
        "干预手册化与照护保真度（fidelity）须说明，包括培训、督导与保真度评估",
        "照护负担量表（Zarit、CICAI、CAREGIVES）信度与本土化版本须注明来源",
        "样本流失（尤其中途撤出的照护者）须报告并讨论选择性偏倚",
        "照护含义须讨论：家庭、机构、政策三个层面的可迁移性"
    ),
    key_venues=(
        "Research on Aging",
        "Journal of Aging Studies",
        "Ageing & Society",
        "Disability & Society",
        "Journal of Advanced Nursing"
    ),
    units_and_formulas_notes=(
        "照护负担分数给出量表范围、标准化方法与信度（α、ω）",
        "统计量给出 M/SD/SE/95% CI；效应量用 Cohen's d 或 η²",
        "样本流失率给出分子/分母，注明原因分类",
        "百分比给出基数 N；加权数据注明权重变量与来源"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "Dedoose", "ATLAS.ti", "Transana", "SPSS", "R", "RStudio", "Stata", "Mplus", "JASP", "jamovi", "G*Power", "Excel", "Qualtrics", "SurveyMonkey", "Tableau", "Power BI", "OpenMRS", "OpenEMR"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
