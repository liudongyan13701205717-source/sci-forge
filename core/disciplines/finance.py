"""金融学论文支持：资产定价、实证识别、稳健性检验。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="finance",
    aliases=("finance", "asset pricing", "corporate finance", "金融学", "金融", "资产定价"),
    paper_types={
        "research": ("abstract", "introduction", "hypothesis development", "data",
                     "methodology", "results", "robustness", "conclusion", "references"),
        "asset_pricing": ("abstract", "introduction", "model", "empirical strategy",
                          "portfolio sorts", "factor regressions", "GMM tests", "references"),
        "event_study": ("abstract", "introduction", "event definition", "sample",
                        "abnormal returns methodology", "results", "cross-sectional tests", "references"),
    },
    citation_style="Chicago Author-Date 或 APA（JF/JFE 系）",
    reporting_standards={
        "data": "数据来源（CRSP/Compustat/Wind/CSMAR）与样本期、筛选标准须列全",
        "identification": "内生性处理（IV/DID/RDD）与安慰剂检验必做",
        "returns": "收益率计算口径（简单/对数；含/不含红利）注明；新股/退市处理说明",
        "factors": "因子模型引用具体版本（Fama-French 3/5 因子；Carhart 动量）",
        "stats": "Newey-West 或聚类稳健标准误报告；多重假设检验校正",
    },
    conventions=(
        "表格给出系数、t 值（或标准误）、R²、观测数；显著性星号约定统一",
        "货币单位与通胀调整（实际/名义；基年）注明",
        "事件研究给估计窗与事件窗定义；CAR/AR 图示置信区间",
        "稳健性检验至少 3 组（替代变量/子样本/替代模型）",
    ),
    key_venues=(
        "Journal of Finance",
        "Journal of Financial Economics",
        "Review of Financial Studies",
        "Journal of Financial and Quantitative Analysis",
        "Management Science",
    ),
    units_and_formulas_notes=(
        "收益率 %（月/年化注明）；波动率年化给 √t 缩放说明",
        "市值亿元或 USD mn；换手率 %；利差 bp",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Python", "R", "Stata", "MATLAB"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
