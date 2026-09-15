"""政治学论文支持：因果识别、民调与实验方法、比较政治。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="political_science",
    aliases=("political science", "politics", "govt", "政治学", "公共行政",
             "policy", "ir", "国际关系"),
    paper_types={
        "research": ("abstract", "introduction", "theory and hypotheses", "research design",
                     "data and measurement", "results", "robustness", "conclusion", "references"),
        "experiment": ("abstract", "introduction", "design（RCT/调查实验）", "subjects",
                       "manipulation check", "results", "limitations", "references"),
        "comparative": ("abstract", "introduction", "cases selection", "mechanisms",
                        "evidence", "scope conditions", "references"),
    },
    citation_style="APSA style（作者-年份）或 Chicago",
    reporting_standards={
        "identification": "因果识别策略（DID/IV/RDD）与假设须显式陈述并做安慰剂检验",
        "measurement": "变量操作化与信度须给出；关键指标给描述统计",
        "inference": "聚类稳健标准误报告；多重假设检验校正（FWER/FDR）",
        "transparency": "预注册与分析代码仓库链接须给出（DA-RT 原则）",
        "cases": "案例选择标准（most similar/different systems）须论证",
    },
    conventions=(
        "假设用 H1/H2 编号并与检验一一对应",
        "回归表给系数、标准误（或置信区间）、观测数与模型拟合",
        "图表注明显著性星号约定（*/**/***）",
        "机制讨论与统计结果分开；外部效度边界说明",
    ),
    key_venues=(
        "American Political Science Review",
        "American Journal of Political Science",
        "Journal of Politics",
        "World Politics",
        "Comparative Political Studies",
    ),
    units_and_formulas_notes=(
        "效应量给标准化系数或边际效应；民调给抽样误差（±%）与置信水平",
        "时间序列给单位根检验；面板数据给固定/随机效应选择依据",
    ),
)
