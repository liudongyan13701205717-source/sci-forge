"""经济学学科论文支持：模型+识别策略、数据附录与 AER 样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="economics",
    aliases=("economics", "经济学", "计量", "econometrics", "金融", "finance",
             "因果推断", "causal inference", "政策评估", "policy evaluation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、方法预告与贡献）",
            "institutional background（制度背景与事实）",
            "model / theoretical framework（模型与可检验含义）",
            "empirical strategy（识别策略：IV/RDD/DiD 等）",
            "data（数据来源与样本构造）",
            "results",
            "robustness（稳健性与安慰剂检验）",
            "conclusion",
            "references",
        ),
        "theory": (
            "abstract",
            "introduction",
            "model（环境、偏好与均衡概念）",
            "results（命题与比较静态）",
            "discussion（含义与经验对照）",
            "conclusion",
            "references",
        ),
        "replication": (
            "abstract",
            "introduction（复现对象与范围）",
            "data and methods",
            "results（复现结果与差异定位）",
            "discussion（差异原因与原始结论稳健性）",
            "references",
        ),
    },
    citation_style="作者-年份（AER / Chicago 样式，如 Smith (2004)）",
    reporting_standards={
        "identification": "识别策略必须显式：给出识别假设（排除性约束、平行趋势等）并做检验",
        "data": "数据附录：来源、样本构造、变量定义表、缺失数据处理",
        "replication": "复现包（代码+数据）按期刊政策提交（如 AER 复现政策）",
        "ethics": "IRB/伦理审查与利益冲突声明；人体被试研究给出批准信息",
        "inference": "标准误给出聚类层级与稳健性（如省份聚类）",
    },
    conventions=(
        "表格三线制：系数+聚类标准误（括号内），星号注记显著性（*p<0.1, **p<0.05, ***p<0.01）",
        "每张表/图自含：变量定义与样本期在表注给出",
        "稳健性小节惯例化：更换固定效应/样本期/度量方式",
        "引言末尾给出相对文献的贡献段",
        "制度背景与描述性事实先行，为识别策略铺垫",
    ),
    key_venues=(
        "American Economic Review",
        "Quarterly Journal of Economics",
        "Econometrica",
        "Journal of Political Economy",
        "Review of Economic Studies",
    ),
    units_and_formulas_notes=(
        "金额给币种与基期（实际 vs 名义，注明平减指数）",
        "弹性/半弹性解释口径（百分比变化 vs 百分点）写明",
        "系数表注明因变量单位与样本量（N）、R²",
        "工具变量报告一阶段 F 统计量（如 Kleibergen-Paap）",
        "事件研究图给出基期约定与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Python", "R", "Stata", "MATLAB"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar"),
)
