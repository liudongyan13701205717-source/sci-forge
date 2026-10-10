"""劳动关系学科论文支持：劳资关系、集体谈判、劳动争议处理的理论与实证研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="industrial_relations",
    aliases=(
        "industrial_relations",
        "劳动关系",
        "劳资关系",
        "劳动关系管理",
        "工业关系学",
        "集体谈判研究",
        "industrial and labor relations",
        "labor relations",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（社会科学）",
    reporting_standards={
        "quantitative_study": "量化研究须报告样本、效度信度与统计假设检验",
        "qualitative_study": "质性研究须遵循 COREQ 或 SRQR 报告规范",
        "policy_study": "政策分析须说明制度背景与适用法域",
        "longitudinal": "纵向数据须报告流失率与缺失值处理",
    },
    conventions=(
        "核心概念（雇佣关系、集体谈判权等）须在引言界定",
        "引用法条须注明法域与生效版本",
        "集体协议条款须注明所属行业与签署主体",
        "劳动争议统计须区分仲裁、诉讼与调解结案数",
        "比较研究须说明制度背景（威斯康星/德法/北欧体制）",
    ),
    key_venues=(
        "Industrial and Labor Relations Review",
        "Industrial Relations",
        "British Journal of Industrial Relations",
        "Comparative Labor Law and Industrial Relations",
        "中国劳动与社会保障法学研究",
    ),
    units_and_formulas_notes=(
        "工资差距用回归系数或百分比差报告，须注明控制变量",
        "就业弹性、劳动参与率须用官方统计口径",
        "集体谈判覆盖率须注明统计年与来源",
        "劳动争议量用件数/万人，须报告分母",
        "统计量给出均值/中位数与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R（面板数据分析）", "SPSS", "NVivo（质性访谈编码）", "EU-Labour Market Statistics（Eurostat）", "中国劳动统计年鉴", "Econometrics 面板工具（plm/xt）", "World Bank World Development Indicators", "GEPARD（德国企业面板）", "IPUMS 微数据平台", "Qualtrics（调查与数据收集）", "SAS（大型调查数据处理）", "Python（pandas 数据处理）", "EpiData（调查录入与核查）", "Censys 劳动人口统计系统", "E-Discovery 文书检索工具", "ArcGIS（劳动空间分析）", "SurveyMonkey（在线调查）", "Tableau（数据可视化）", "Excel（数据管理）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "NLS 美国劳动统计数据库", "ILO 国际劳工统计数据库", "ILOSTAT 数据库", "OECD 就业数据库"),
)
