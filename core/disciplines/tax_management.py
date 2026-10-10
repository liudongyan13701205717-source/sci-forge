"""Tax Management 学科论文支持：税收管理/税收征管/税制设计论文体裁、APA 引用样式与税收征管指标记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tax_management",
    aliases=(
        "tax_management",
        "Tax management",
        "税收管理",
        "税收征管",
        "tax compliance",
        "tax administration",
        "tax policy",
        "tax revenue management",
        "税收筹划",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与税收管理问题）",
            "theory and hypothesis",
            "methods（样本、数据与计量模型）",
            "results（实证结果与稳健性检验）",
            "policy implications",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background",
            "analysis（征管流程与政策效果）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（National Tax Journal、Journal of Public Economics 遵循期刊规范）",
    reporting_standards={
        "sample": "样本须报告：期间、国家/地区、企业或行业类型、剔除规则、观测数 N",
        "variables": "核心变量定义：税收征管效能指数 TAI、税基税源管理率、遵从率 compliance rate、稽查覆盖率",
        "model": "计量模型须报告：面板固定效应、聚类标准误、内生性处理（GMM、工具变量、DID）",
        "robustness": "稳健性检验须包括：替换指标、DID 平行趋势检验、安慰剂检验、异质性分析",
        "policy": "涉及具体政策评估须报告政策时间、覆盖范围与反事实识别策略",
    },
    conventions=(
        "税收征管效能遵循 WBTI（World Bank Tax Administration Diagnostic Assessment Tool）与国际公认指标体系",
        "税收遵从率 compliance rate = 实际申报纳税额/应申报纳税额 × 100%；稽查覆盖率 = 稽查户数/纳税人总数 × 100%",
        "税收弹性 elasticity = 税收增长率/税基增长率；宏观税负比率 burden ratio = 税收总额/GDP × 100%",
        "符号约定：税率用 t、税基用 B、税额用 R；t×B=R 为税收恒等式",
        "计量公式用 amsmath；系数报告附标准误；显著性用 *, **, *** 对应 10%/5%/1%",
        "政策评估遵循 DID/RDD/PSM 规范；报告处理组、控制组、事件时间与安慰剂检验结果",
    ),
    key_venues=(
        "National Tax Journal",
        "Journal of Public Economics",
        "Journal of Economic Behavior & Organization",
        "Public Finance Review",
        "Tax Notes International",
        "Journal of Fiscal Affairs",
    ),
    units_and_formulas_notes=(
        "金额单位：元/百万元；税率用百分数 %；比率用小数或百分数；时间用年度或月度",
        "税收恒等式：R = t × B（税额 = 税率 × 税基）；税收弹性 = ΔR/R ÷ ΔB/B",
        "宏观税负 ratio = 税收总额/GDP；征收成本比 = 征收成本/税收总额；稽查覆盖率 = 稽查户数/纳税人总数",
        "公式用 amsmath；系数报告附标准误；显著性用 *, **, *** 对应 10%/5%/1%；样本量 N 须标注",
        "所有比率保留 4 位小数；政策效应估计用处理组与对照组差异报告；DID 报告事件研究结果",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("金税工程三期", "Oracle Fusion Cloud Tax", "SAP Tax", "Thomson Reuters Tax", "Tax Administration Diagnostic Tool (TADAT)", "World Bank WBTI", "Tax Compliance Index (TAXI)", "OECD Tax Compliance Toolkit", "Stata", "R (plm/fixest)", "Python (pandas, linearmodels)", "Power BI", "Tableau", "Excel", "NVivo", "ATLAS.ti", "SPSS", "EndNote", "Zotero", "OpenRefine"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "WSS", "OECD Statistics"),
)
