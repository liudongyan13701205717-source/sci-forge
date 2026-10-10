"""预防与社会医学学科论文支持：疾病防控、卫生服务与社会健康影响因素研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="preventive_and_social_medicine",
    aliases=(
        "preventive and social medicine", "预防医学与社会医学",
        "public health", "公共卫生",
        "social medicine", "社会医学",
        "community medicine", "社区医学",
        "health promotion", "健康促进",
        "chronic disease prevention", "慢病防控",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（疾病问题与健康目标）",
            "methodology（设计、抽样、暴露与结局定义）",
            "results（率、风险与干预效果）",
            "discussion（偏倚、因果与卫生政策意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（社区背景与人群特征）",
            "analysis（危险因素与干预流程）",
            "results（指标变化与卫生服务利用）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（预防医学与健康社会决定因素理论）",
            "evidence synthesis（干预与卫生服务证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "观察性研究按 STROBE 报告，干预试验按 CONSORT 报告",
        "k2": "系统综述按 PRISMA 报告并注明检索策略与质量评估",
        "k3": "筛查项目须报告灵敏度、特异度与人群归因分值",
    },
    conventions=(
        "人群描述须分层报告年龄、性别、地区与数据年份",
        "发生率与患病率须区分 incidence 与 prevalence 并明确分母",
        "观察性研究用关联表述，避免因果化措辞",
        "二手数据须说明来源、许可与缺失处理",
        "健康公平术语保持一致，避免污名化表述",
    ),
    key_venues=(
        "Bulletin of the World Health Organization",
        "American Journal of Public Health",
        "Lancet Public Health",
        "The Lancet",
        "International Journal of Epidemiology",
    ),
    units_and_formulas_notes=(
        "率与危险度以每 10 万人口径报告并注明人年分母",
        "RR、OR、HR 须给点估计与 95% CI",
        "疾病负担以 DALY 或 QALY 表示并注明贴现率与年龄权重",
        "筛查指标须报告特异度、灵敏度、阳性预测值及筛出率",
        "成本-效果分析须注明分析视角、货币单位与时间跨度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "SPSS", "SAS", "Stata", "Python (pandas, statsmodels)", "Epi Info", "ArcGIS", "QGIS", "SaTScan", "GeoDa", "Stata Metaplot 荟萃分析", "RevMan 系统评价工具", "JAGS 贝叶斯建模", "Stan 统计建模", "MATLAB", "Excel", "Power BI", "Tableau", "SurveyCT 问卷调查", "NVivo 质性分析"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
