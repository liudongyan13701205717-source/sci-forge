"""旅游学科论文支持：旅游规划/游客行为体裁、Annals of Tourism Research 引用样式与旅游记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tourism",
    aliases=("tourism", "旅游", "旅游管理", "旅游规划", "游客研究",
             "tourism management", "visitor behavior", "旅游经济学", "文化旅游"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与旅游研究问题）",
            "literature review",
            "methods（调查设计与抽样）",
            "results（数据分析与发现）",
            "discussion（理论贡献与实践建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（景区/目的地案例）",
            "analysis（游客行为与规划分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "sampling": "抽样方法、样本量与抽样框须报告",
        "scale_validation": "量表须经信效度检验（Cronbach's α≥0.7）",
        "ethical_approval": "涉及人类受试者须声明伦理审批",
        "data_analysis": "统计方法与软件版本须注明",
    },
    conventions=(
        "旅游术语遵循 UNWTO 定义",
        "游客量单位：人次（visitor-trips）",
        "经济数据用人民币元（CNY）或美元（USD），注明年份",
        "游客满意度用李克特量表（1-5 或 1-7）",
        "统计报告遵循 APA 7 格式",
    ),
    key_venues=(
        "Annals of Tourism Research",
        "Tourism Management",
        "Journal of Travel Research",
        "Current Issues in Tourism",
        "Tourism Geographies",
    ),
    units_and_formulas_notes=(
        "游客量单位：人次/年",
        "旅游收入单位：万元或亿元",
        "满意度评分：李克特 1-5 或 1-7 分制",
        "公式用 amsmath 排版；回归分析须报告 R² 与显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Python", "MATLAB", "AMOS", "NVivo", "QGIS", "Google Earth Pro", "Excel", "SurveyMonkey", "Qualtrics", "MaxQDA", "Atlas.ti", "Mplus", "Harvard Analytic Markup Language (HAML)", "UNWTO 数据平台", "TripAdvisor API", "Tableau", "Moodle（教学平台）", "Google Trends"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science", "Google Scholar"),
)
