"""工会课程学科论文支持：工会法律/职工权益体裁、工会论坛样式与劳动法记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="trade_union_courses",
    aliases=("trade_union_courses", "工会课程", "工会教育", "职工权益", "劳动关系",
             "labor union", "union education", "职工培训", "劳动关系协调"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工会问题）",
            "literature review（理论综述）",
            "methods（调查与访谈方法）",
            "results（数据分析与发现）",
            "discussion（理论贡献与实践建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工会案例/事件）",
            "analysis（法律与制度分析）",
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
    citation_style="法律引用样式（Bluebook 样式，法条用「《劳动法》第X条」格式）",
    reporting_standards={
        "legal_basis": "引用法律法规须注明全称与生效日期",
        "case_citation": "案例引用须注明案号或来源",
        "data_collection": "问卷调查样本量与抽样方法须报告",
        "ethical_review": "涉及个人信息的调研须声明匿名化处理",
    },
    conventions=(
        "法律法规用全称并标注年份（如《工会法》2001 年修订）",
        "工会组织层级须明确（全国总工会/地方总工会/基层工会）",
        "劳动数据单位：人、%、元",
        "统计报告遵循学术规范（均值±标准差，p 值）",
        "术语首次出现给出全称与英文对照",
    ),
    key_venues=(
        "中国工会论坛",
        "工会通讯",
        "劳动经济评论",
        "中国劳动关系",
        "工会理论",
    ),
    units_and_formulas_notes=(
        "人数单位：人；比例单位：%",
        "工资单位：元/月 或 万元/年",
        "罢工次数单位：次/年",
        "公式用 amsmath 排版；统计检验须报告方法名与 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Python", "STATA", "NVivo", "MaxQDA", "ATLAS.ti", "Excel", "北大法宝", "SurveyMonkey", "Qualtrics", "MATLAB", "ArcGIS", "Origin Pro", "LaTeX", "EndNote", "Tableau", "Google Docs", "Weave（质性分析软件）", "Camtasia"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "CNKI 中国知网", "Westlaw", "LexisNexis", "Google Scholar"),
)
