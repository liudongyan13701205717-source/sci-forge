"""社会冲突理论学科论文支持：社会分层/不平等/社会运动体裁、Chicago 引用样式与量化-定性混合分析规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_conflict_theory",
    aliases=("social_conflict_theory", "社会冲突理论", "冲突论", "社会分层理论", "stratification theory", "class analysis", "inequality studies", "social movement theory"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与理论传统）",
            "methods（数据、变量、模型、抽样）",
            "results（结果、稳健性与敏感性）",
            "discussion（讨论与理论对话）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与情境）",
            "analysis（冲突过程与机制分析）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（冲突论主要分支综述）",
            "evidence synthesis（跨案例证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份（American Journal of Sociology 遵循 ASA；冲突论传统文献亦常采用 APA 7）",
    reporting_standards={
        "quantitative": "量化研究须报告数据源、变量操作化、样本框、加权与稳健性检验；缺失值处理透明",
        "qualitative": "质性研究遵循 COREQ 清单：受访者位置、编码过程、饱和判断",
        "historical": "历史比较研究须报告档案来源、时间边界与可比性讨论",
        "mixed_methods": "混合设计用联合展示表（joint display）呈现定量与定性整合点"
    },
    conventions=(
        "理论框架先行：明确对话的冲突论传统（马克思、韦伯、达伦多夫、科塞）与关键概念定义",
        "阶级/阶层操作化须透明：收入、教育、职业、家世的分位数与加权口径在方法中给出",
        "不平等测量首选 Gini、Theil、Atkinson 或分位数差；解释须报告基尼系数分解",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）",
        "社会运动研究用时间序列给出事件数、参与者规模与媒体声量"
    ),
    key_venues=(
        "American Journal of Sociology",
        "American Sociological Review",
        "American Journal of Political Science",
        "Socio-Economic Review",
        "Annual Review of Sociology"
    ),
    units_and_formulas_notes=(
        "基尼系数 G = ΣΣ|xi - xj| / (2n²μ)；给出按组分解（Between-Within）",
        "Theil 指数分解为组内（within）与组间（between），报告权重口径",
        "分位数差（P90/P10、P99/P50）给出样本量与截尾/去极端值方法",
        "百分比给出基数 N；加权数据注明权重变量与权重比（design effect）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Stata", "SPSS", "Python", "NVivo", "MAXQDA", "Dedoose", "ATLAS.ti", "ArcGIS Pro", "QGIS", "Tableau", "Power BI", "Gephi", "UCINET", "NetworkX", "igraph", "VOSviewer", "Leximancer", "Excel"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
