"""救生（水上救生）学科论文支持：安全培训、事故分析与水域救援体裁，APA 引用与急救记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="life_guarding",
    aliases=("life_guarding", "救生", "水上救生", "救生员",
             "water rescue", "lifeguard", "swimming rescue", "aquatic safety",
             "水上安全", "水域救援", "海滩救生"),
    paper_types={
        "research": ("abstract", "introduction（背景与安全问题）",
                     "methodology（方法）", "results（结果）",
                     "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（案例情境）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "incident_report": "水域事故报告规范（SAHSA/ASIS）",
        "rescue_analysis": "救援行动后分析规范（CAPA）",
        "training": "救生培训标准（ILS/American Red Cross）",
        "systematic_review": "PRISMA 系统综述声明",
        "case_study": "CASI 案例研究报告规范",
        "survey": "AAPOR 调查报告规范",
    },
    conventions=(
        "事故地点与时间须精确到分钟",
        "水情条件须记录（水温、能见度、风力、浪高）",
        "救援工具与流程须标准化描述",
        "培训资质须明确标识",
        "参考文献遵循 APA 7 格式",
    ),
    key_venues=(
        "Journal of Applied Sport Psychology",
        "International Journal of Aquatic Research",
        "Journal of Safety Research",
        "Journal of Occupational Safety",
        "Preventive Medicine",
    ),
    units_and_formulas_notes=(
        "时间响应以秒/分钟为单位",
        "水温以摄氏度（°C）",
        "浪高以米（m）",
        "能见度以米（m）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "SPSS", "NVivo", "MAXQDA", "EndNote", "Zotero", "Mendeley", "Qualtrics", "Google Forms", "Tableau", "Power BI", "ArcGIS", "QGIS", "Excel", "Microsoft Access", "LaTeX", "Google Docs", "Kahoot!", "Moodle"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
