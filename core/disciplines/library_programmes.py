"""图书馆项目学科论文支持：馆藏/服务项目设计、评估与影响研究，APA 引用与社科统计记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="library_programmes",
    aliases=("library_programmes", "图书馆项目", "图书馆服务", "图书馆馆藏",
             "图书馆活动", "library service", "library program", "library collection",
             "图书馆评估", "公共图书馆项目", "图书馆社区服务"),
    paper_types={
        "research": ("abstract", "introduction（背景与项目动因）",
                     "methodology（设计/实施/评估方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（案例情境与实施）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "programme_evaluation": "CIPP/逻辑模型/CIRPI 报告标准",
        "case_study": "CASI 案例研究报告规范",
        "survey": "AAPOR 调查报告规范",
        "systematic_review": "PRISMA 系统综述声明",
        "qualitative": "COREQ/SRQR 质性研究报告规范",
    },
    conventions=(
        "项目目标与逻辑模型须图示化",
        "评估指标需区分输入、产出与影响",
        "样本量与响应率须明确报告",
        "参与/满意度使用五级及以上量表并报告信度",
        "参考文献遵循 APA 7 格式",
    ),
    key_venues=(
        "Library Quarterly",
        "Library & Information Science Research",
        "Public Library Quarterly",
        "Library Review",
        "Journal of Library Administration",
    ),
    units_and_formulas_notes=(
        "报告使用样本量、置信区间与效应量",
        "服务时长以小时/年为单位",
        "访问量给日/月/年口径",
        "统计显著性以 p<0.05 为常用阈值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "SPSS", "NVivo", "MAXQDA", "ATLAS.ti", "LibrARI", "Koha", "Aleph", "Evergreen ILS", "Ex Libris Alma", "CLM 图书馆联络管理系统", "EndNote", "Zotero", "Mendeley", "Google Analytics", "Qualtrics", "SurveyMonkey", "Tableau", "Power BI"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
