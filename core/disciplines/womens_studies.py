"""女性研究学科论文支持：性别与社会分析体裁、APA 引用样式与质性研究记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="womens_studies",
    aliases=("women's studies", "女性研究", "性别研究", "妇女研究", "女性学",
             "gender studies", "feminist studies", "women and gender studies"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与研究问题）",
            "literature review（文献综述与理论框架）",
            "methods（数据、方法与伦理）",
            "results（发现与主题）",
            "discussion（理论与社会意义）",
            "references",
        ),
        "qualitative": (
            "abstract",
            "introduction",
            "theoretical framework（理论框架）",
            "methods（抽样、访谈与编码）",
            "findings（主题与引语）",
            "discussion（反思与局限）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Feminist Studies 等多用 Chicago/APA）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethics": "涉及人类被试须报告伦理审查与知情同意",
        "positionality": "须报告研究者立场与反思（positionality）",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "性别相关术语须采用包容性语言并说明用法",
        "访谈引语须匿名化并说明转录规则",
        "理论框架（如交叉性）须明确界定",
        "样本特征与招募方式须交代",
        "伦理审查与知情同意须报告",
    ),
    key_venues=(
        "Feminist Studies",
        "Signs: Journal of Women in Culture and Society",
        "Gender & Society",
        "Feminist Theory",
        "Women's Studies International Forum",
        "Journal of Gender Studies",
    ),
    units_and_formulas_notes=(
        "定性主题用主题-引语结构呈现",
        "编码信度用 Cohen's Kappa 或共识法报告",
        "定量指标须报告样本量与统计检验",
        "引语标注须给出受访者编号与人口学标签",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "Dedoose", "Transana", "Qualtrics", "SurveyMonkey", "SPSS", "R", "Stata", "Python (pandas)", "Gephi (网络分析)", "Voyant Tools (文本分析)", "Zotero", "EndNote", "Mendeley", "Tableau", "LaTeX", "Git (版本管理)", "Excel"),
    category="法学",
    databases=("JSTOR", "OpenAlex", "Crossref", "CNKI"),
)
