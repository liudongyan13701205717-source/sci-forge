"""服务类跨学科项目与学位：研究、案例、综述体裁，APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_services",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_services",
        "服务类跨学科项目与学位",
        "Services Interdisciplinary Programmes",
        "Service Management Degree",
        "Cross-disciplinary Services",
        "服务管理跨学科",
        "服务科学学位",
        "服务业跨学科项目",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "SERVQUAL（服务质量评价）",
        "k2": "PRISMA（系统综述）",
        "k3": "SERVPERF（服务绩效）",
    },
    conventions=(
        "服务场景与样本来源须说明",
        "客户满意度量表与信度须报告",
        "服务流程节点与时长须记录",
        "跨机构比较须说明背景差异",
        "伦理审查编号须标注",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Operations Management",
        "Journal of Service Management",
        "Service Science",
        "International Journal of Service Industry Management",
    ),
    units_and_formulas_notes=(
        "时长与金额须给出统一单位",
        "NPS 与 CSAT 报告时须说明计算口径",
        "样本量与失效率须报告",
        "统计量报告 M/SD/95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python（Pandas）", "Excel", "Tableau", "Power BI", "NVivo", "ATLAS.ti", "MATLAB", "Minitab", "JMP", "Qualtrics", "SurveyMonkey", "Zendesk", "Salesforce", "ServiceNow", "Moodle", "RefWorks", "EndNote"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
