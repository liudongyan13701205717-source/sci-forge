"""Survey sampling 学科论文支持：抽样设计/分层抽样/复杂抽样估计/样本量计算。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="survey_sampling",
    aliases=(
        "survey_sampling", "Survey sampling", "调查抽样",
        "抽样调查", "抽样估计", "样本设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与抽样问题）",
            "methods（抽样设计与估计方法）",
            "results（估计精度与偏差）",
            "discussion（讨论与应用建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（调查区域与总体）",
            "analysis（抽样方案与实施）",
            "results（估计结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（抽样理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "sampling_design": "抽样须报告总体定义、抽样框、抽样方法与样本量",
        "estimation": "估计须报告估计量、方差估计方法与置信区间",
        "non_response": "非响应须报告响应率、缺失模式与调整方法",
        "sample_size": "样本量计算须报告设计效应、置信水平与允许误差",
    },
    conventions=(
        "总体定义须明确（空间/时间/对象范围）",
        "抽样方法须注明（简单随机/系统/分层/整群）",
        "抽样误差须报告标准误与置信区间",
        "设计效应（deff）须计算并报告",
        "加权方法须注明权重计算方式与调整策略",
    ),
    key_venues=(
        "Survey Research Methods",
        "Journal of Official Statistics",
        "Journal of Survey Statistics and Methodology",
        "中国统计",
        "数理统计与管理",
    ),
    units_and_formulas_notes=(
        "样本量用 n（个）；总体大小用 N（个）",
        "抽样误差用 百分点或 标准误",
        "设计效应 deff = SRS 方差 / 实际方差",
        "置信水平用 95% 或 99%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R（抽样设计与估计）", "Stata（复杂抽样统计）", "SAS（统计分析与抽样）", "SPSS（统计分析与抽样）", "G*Power（样本量计算）", "nQuery Advisor（样本量计算）", "Epi Info（流行病学抽样）", "Open Refine（数据清洗）", "KoboToolbox（移动抽样采集）", "ODK Collect（移动抽样采集）", "SurveyCTO（在线抽样调查）", "Qualtrics（随机抽样调研）", "Bootstrap 重采样工具（R/Python）", "复杂抽样加权软件（R survey 包）", "系统抽样数表生成器", "分层抽样设计工具", "随机抽样数表生成器", "抽样误差估计工具", "抽样框构建工具（Excel）", "Power Plan（样本量计算）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
