"""社区发展学科论文支持：社区发展/社会组织体裁、APA 引用样式与社区研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="community_development",
    aliases=(
        "community_development", "社区发展", "community development",
        "community organizing", "社区组织", "community building",
        "社区建设", "community empowerment", "社区赋权",
        "community action", "社区行动", "community engagement",
        "社会发展",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与社区问题）",
            "literature review（文献综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "site description（社区概况）",
            "method（研究方法）",
            "findings（发现）",
            "analysis（分析）",
            "implications（启示）",
            "references",
        ),
        "evaluation": (
            "abstract",
            "introduction",
            "program description（项目描述）",
            "evaluation design（评估设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Community Development 遵循 APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "quantitative": "定量研究遵循 CONSORT 或 PRISMA 声明",
        "participatory": "参与式研究遵循 CARE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "社区发展研究报告须区分定量与定性方法，并说明数据来源",
        "居民参与过程须如实描述（如参与阶段、反馈机制）",
        "涉及伦理审查的研究须声明伦理审批编号",
        "政策建议须基于证据并说明假设与适用条件",
        "社区术语首次出现处须给出定义",
    ),
    key_venues=(
        "Journal of Community Development",
        "Community, Environment, Society",
        "Community Development Quarterly",
        "Journal of the Association for Consumer Research",
        "Social Policy and Society",
        "Community Work",
    ),
    units_and_formulas_notes=(
        "时间用统一纪年格式；货币用统一币种并注明年份",
        "参与率以百分比报告，给出分子与分母",
        "量表得分须说明计分方式与信度系数",
        "涉及统计检验时给出效应量（Cohen's d、η²）",
        "地图数据须注明数据源与地理投影",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "SPSS", "Stata", "R (RStudio)", "Python (Jupyter)", "ArcGIS", "QGIS", "Tableau", "Microsoft Power BI", "Google Analytics", "KoboToolbox", "ODK (Open Data Kit)", "CommCare", "SurveyMonkey", "Qualtrics", "MPOWER", "DHIS2", "Google Sheets", "Notion", "Miro", "EndNote", "Zotero", "LaTeX", "OpenRefine", "Microsoft Project", "Google Maps", "GeoBound", "Datawrapper"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "PubMed", "ERIC"),
)
