"""Commercial Services 学科论文支持：商业服务/服务管理体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="commercial_services",
    aliases=("Commercial Services", "商业服务", "商务服务", "commercial services",
             "business services", "trade services", "商业服务管理", "商务咨询",
             "客户服务管理", "service management"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "theoretical framework（理论框架）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusion（结论与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "company/context overview（背景）",
            "case analysis（案例分析）",
            "findings（发现）",
            "implications（启示）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "quantitative": "遵循 APA 量化研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "service_process": "服务过程研究须遵循服务蓝图规范",
    },
    conventions=(
        "服务过程与服务结果须区分描述",
        "客户满意度与服务质量的测量须注明工具",
        "商业模式与竞争策略须明确定位",
        "服务术语与行业专有名词首次出现时给出中英文对照",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Business Research",
        "European Business Review",
        "Business Strategy and the Environment",
        "Service Industries Journal",
        "International Journal of Service Industry Management",
        "Journal of Retailing and Consumer Services",
        "Management Decision",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "显著性水平标注为 *p < .05, **p < .01, ***p < .001",
        "样本量须报告，百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "NVivo", "Qualtrics", "Tableau", "Minitab", "R", "Python", "AMOS", "EQS", "LISREL", "MAXQDA", "Google Analytics", "Salesforce", "Microsoft Project", "Power BI", "ArcGIS", "Excel", "WEKA", "ServiceNow"),
    category="管理学",
    databases=("OpenAlex", "Scopus", "WoS", "CNKI", "万方"),
)
