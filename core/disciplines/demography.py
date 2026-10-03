"""人口学论文支持：人口结构、生育率、死亡率、迁移、人口预测。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="demography",
    aliases=("demography", "demographics", "人口学", "人口统计学"),
    paper_types={
        "research": ("abstract", "introduction", "data and methods", "results", "discussion", "conclusions", "references"),
        "prospective": ("abstract", "introduction", "cohort description", "methods", "results", "discussion", "conclusions", "references"),
        "policy": ("abstract", "introduction", "background", "policy analysis", "projections", "discussion", "conclusions", "references"),
    },
    citation_style="APA 7（括号），如 (Author, Year)",
    reporting_standards={
        "fertility": "生育率须报告 TFR/CBR/GFR，区分时期指标与队列指标",
        "mortality": "死亡率须报告年龄别死亡率、期望寿命与婴儿死亡率",
        "migration": "迁移须报告迁移率、迁移流与净迁移",
        "projection": "预测须声明假设方案（高/中/低）、模型类型与数据来源",
    },
    conventions=(
        "生命表用标准格式（年龄分组、存活率、死亡概率）",
        "人口金字塔须用标准年龄分组（5岁一组）",
        "标准化率须声明标准人口（WHO/WHO2000/本国标准）",
        "时间序列用年份数据；预测区间用虚线或阴影",
        "人口统计指标用国际标准缩写（TFR/CBR/CDR/IMR）",
    ),
    key_venues=(
        "Demography",
        "Population Studies",
        "Population and Development Review",
        "European Journal of Population",
        "Demographic Research",
    ),
    units_and_formulas_notes=(
        "生育率 TFR 用 活产/妇女（无量纲）",
        "死亡率用 per 1,000 population（‰）",
        "期望寿命用 岁（years）",
        "人口增长率用 %/年 或 ‰/年",
        "总和生育率 TFR = Σfx（时期生育率之和）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("R", "Python", "Stata", "GIS", "LaTeX"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
