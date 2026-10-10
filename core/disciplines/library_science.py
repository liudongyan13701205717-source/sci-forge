"""图书馆学学科论文支持：馆藏/服务/信息行为体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="library_science",
    aliases=("library_science", "图书馆学", "图书馆情报", "图书情报",
             "information science", "library and information science",
             "信息管理", "图书馆学", "信息检索", "知识组织"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）",
                     "literature review（文献综述）",
                     "methods（方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "user_study": ("abstract", "introduction",
                       "participants（参与者）",
                       "measures（测量）", "results（结果）",
                       "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（案例描述）",
                       "analysis（分析）", "findings（发现）",
                       "discussion（讨论）", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；JASIST 遵循 APA 规范）",
    reporting_standards={
        "survey": "AAPOR 调查报告规范",
        "user_study": "用户研究报告规范",
        "case_study": "CASI 案例研究报告规范",
        "qualitative": "COREQ/SRQR 质性研究报告规范",
        "systematic_review": "PRISMA 系统综述声明",
        "bibliometrics": "Bibliometrics Reporting Guidelines",
    },
    conventions=(
        "馆藏与资源范围须说明",
        "用户样本与招募须交代",
        "测量工具须注明信效度",
        "数据来源须注明",
        "实践启示须讨论",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Library & Information Science Research",
        "Journal of Documentation",
        "College & Research Libraries",
        "Library Trends",
        "Scientometrics",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "频数与百分比给出基数",
        "样本量须报告",
        "量表分数给出范围与信度",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "SQL", "SPSS", "RStudio", "Jupyter Notebook", "VOSviewer", "CiteSpace", "Gephi", "Pajek", "EndNote", "Zotero", "Mendeley", "RefWorks", "Qumulo", "Qualtrics", "SurveyMonkey", "Google Analytics", "Power BI", "LaTeX"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "DOAJ"),
)
