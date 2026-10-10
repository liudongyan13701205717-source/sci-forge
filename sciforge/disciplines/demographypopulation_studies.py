"""Demography/population studies 学科论文支持：人口与人口学研究体裁、国际人口比较规范与人口预测工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="demographypopulation_studies",
    aliases=(
        "demographypopulation_studies", "人口学与人口研究", "人口与人口学研究",
        "population studies", "population research", "population and demography",
        "人口与社会", "population and society", "demographic research",
        "人口迁移研究", "population migration", "population policy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "data and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "comparative": (
            "abstract",
            "introduction",
            "comparative_framework（比较框架）",
            "data（多国/地区数据）",
            "findings（比较发现）",
            "implications（政策启示）",
            "references",
        ),
        "policy": (
            "abstract",
            "introduction",
            "background",
            "policy_analysis",
            "projections",
            "discussion",
            "conclusions",
            "references",
        ),
    },
    citation_style="APA 7（括号），如 (Author, Year)",
    reporting_standards={
        "fertility": "生育率须报告 TFR/CBR/GFR，区分时期指标与队列指标",
        "mortality": "死亡率须报告年龄别死亡率、期望寿命与婴儿死亡率",
        "migration": "迁移须报告迁移率、迁移流与净迁移",
        "projection": "预测须声明假设方案（高/中/低）、模型类型与数据来源",
        "comparison": "跨国比较须注明汇率与购买力平价调整方法",
    },
    conventions=(
        "人口统计指标须使用国际标准缩写（TFR/CBR/CDR/IMR），首次出现须给出全称",
        "生命表须用标准格式（年龄分组、存活率lx、死亡概率qx）",
        "人口预测须声明假设方案（高/中/低）、模型类型（队列法/矩阵法）与数据来源",
        "标准化率须声明标准人口（WHO/WHO2000/本国标准）",
        "跨国比较须注明汇率与购买力平价调整方法",
    ),
    key_venues=(
        "Demography",
        "Population Studies",
        "Population and Development Review",
        "European Journal of Population",
        "Demographic Research",
        "Population Research and Policy Review",
        "Journal of Population Economics",
        "Social Science & Medicine",
    ),
    units_and_formulas_notes=(
        "生育率 TFR 用 活产/妇女（无量纲）",
        "死亡率用 per 1,000 population（‰）",
        "期望寿命用 岁（years）",
        "人口增长率用 %/年 或 ‰/年",
        "总和生育率 TFR = Σfx（时期生育率之和）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "Python (pandas, pyarrow)", "Stata", "IBM SPSS Statistics", "SAS", "PopMod", "MxLab", "Spectra", "LaTeX", "ArcGIS", "QGIS", "Tableau", "Power BI", "PyHalo", "Demogratiser", "WHO Global Health Observatory", "UN DESA World Population Prospects", "Eurostat Database", "World Bank Data", "R package: period (period life tables)"),
    category="理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
