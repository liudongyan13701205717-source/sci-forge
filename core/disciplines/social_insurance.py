"""社会保险学科论文支持：养老金/医疗/失业保险体裁、Chicago 引用样式与精算建模规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_insurance",
    aliases=("social_insurance", "社会保险", "社会保障", "养老保险", "health insurance", "pension systems", "social security", "insurance economics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与政策背景）",
            "methods（数据、精算模型、财政可持续性）",
            "results（结果、稳健性与情景）",
            "discussion（讨论与政策含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（制度设计、参保、待遇）",
            "analysis（精算平衡、财政可持续）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（社保制度理论综述）",
            "evidence synthesis（跨国证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份（Journal of Risk and Insurance 遵循 CASSI 规范；SSM 遵循 APA 7）",
    reporting_standards={
        "actuarial_modeling": "精算建模遵循 SOA 与 ISIA 精算报告规范：假设（利率、死亡率、缴费率、替代率）透明，情景与敏感性分析",
        "policy_evaluation": "政策评估遵循 DID/RD/PSM 设计：平行趋势、事件时间图、稳健性与安慰剂检验",
        "household_microdata": "家庭微观数据研究须报告样本框、加权口径与缺失值处理（多重插补）",
        "simulation": "仿真模型报告参数、初始条件与随机种子；结果给出置信区间与误差传播"
    },
    conventions=(
        "制度描述用三层结构：缴费者、雇主、政府三方责任与资金流",
        "精算假设（利率、死亡率、失业率、缴费率）须在方法中列出并给出来源（生命表、劳动统计、财政预测）",
        "替代率、缴费率、覆盖率、财政缺口、可持续年限用统一口径与基数说明",
        "跨制度比较须报告统计单位（人/户/企业）与时间口径",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）"
    ),
    key_venues=(
        "Journal of Risk and Insurance",
        "Social Security Bulletin",
        "Journal of Pension Economics and Finance",
        "IZA Discussion Papers",
        "Journal of Economic Literature"
    ),
    units_and_formulas_notes=(
        "替代率 R = 月养老金 / 缴费期平均工资；覆盖率 = 参保人数 / 应参保人数 × 100%",
        "精算现值 PV = Σ D_t·b_t；折现率、生存概率（lx）须声明",
        "财政缺口 = 累计支付现值 - 累计收入现值；给出可持续年限（年）",
        "工资/养老金以当年价与不变价分别报告；跨制度比较使用购买力平价（PPP）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Stata", "SPSS", "SAS", "Excel", "MATLAB", "Julia", "Python", "Prophet", "EViews", "Tableau", "Power BI", "ChainLadder", "LifeContingencies", "actuar", "survival", "GLM", "MegaSTAT", "LifeTableMaker"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
