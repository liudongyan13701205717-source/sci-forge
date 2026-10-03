"""公共卫生学科论文支持：STROBE/CDC/MMWR 按人群研究设计路由与 Vancouver 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_health",
    aliases=("public health", "公共卫生", "预防医学", "preventive medicine",
             "global health", "全球健康", "卫生政策", "health policy"),
    paper_types={
        "cohort_study": (
            "structured abstract",
            "introduction（研究问题与目标人群）",
            "methods（设计、抽样、暴露与结局定义、混杂控制）",
            "results（随访流程、基线表、效应量与亚组分析）",
            "discussion（因果推断、偏倚与公共卫生意义）",
            "references",
        ),
        "cross_sectional_survey": (
            "abstract",
            "introduction",
            "methods（抽样框、问卷与测量、加权与应答率）",
            "results（患病率/流行率表、分层比较）",
            "discussion（代表性与政策含义）",
            "references",
        ),
        "outbreak_investigation": (
            "abstract",
            "introduction（疫情背景与病例定义）",
            "methods（病例搜索、流行曲线、暴露溯源）",
            "results（病例分布、罹患率、关联分析）",
            "discussion（控制措施与监测建议）",
            "references",
        ),
        "health_economic_evaluation": (
            "abstract",
            "introduction",
            "methods（分析视角、成本采集、模型与敏感性分析）",
            "results（成本-效果比、增量分析、不确定性）",
            "discussion（预算影响与可推广性）",
            "references",
        ),
        "policy_brief": (
            "executive summary",
            "background（证据综述）",
            "options（政策选项与利弊权衡）",
            "recommendations（行动建议与实施条件）",
            "references",
        ),
    },
    citation_style="Vancouver（按引用顺序编号）",
    reporting_standards={
        "case_series": "CARE（病例系列/病例报告条目）",
        "cohort": "STROBE",
        "case_control": "STROBE",
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "outbreak": "CDC 现场流行病学调查框架（MMWR 报告体例）",
        "surveillance": "CDC MMWR 数据要素（病例定义与罹患率口径）",
        "economic_evaluation": "CHEERS 2022",
    },
    conventions=(
        "人群描述必须分层报告：年龄/性别/地区/社会经济状态与数据年份",
        "伦理：人群研究给出 IRB 批准或豁免；二次数据说明来源与许可",
        "率与风险表述区分 incidence rate 与 prevalence，分母口径明确",
        "因果语言谨慎：观察性研究用 association 而非因果表述",
        "健康公平术语一致，避免污名化措辞（人群优先于标签）",
    ),
    key_venues=(
        "CDC MMWR (Morbidity and Mortality Weekly Report)",
        "New England Journal of Medicine",
        "The Lancet Public Health",
        "American Journal of Public Health",
        "Bulletin of the World Health Organization",
    ),
    units_and_formulas_notes=(
        "发病/患病率给每 10 万人口径（deaths per 100,000 person-years）",
        "效应量 RR/OR/HR 给点估计与 95% CI；归因分值（PAF）注明口径",
        "疾病负担用 DALY/QALY 并说明贴现率与年龄权重",
        "抽样调查给出应答率、设计效应与加权方法",
        "时间序列注明病例定义变更对趋势比较的影响",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("R", "SPSS", "ArcGIS", "Epi Info"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
