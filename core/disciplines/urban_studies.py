"""城市研究学科论文支持：城市/规划/治理体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="urban_studies",
    aliases=("urban_studies", "城市研究", "城市规划", "城市科学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例选择）",
            "data collection（数据收集）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context（政策背景）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Urban Studies 遵循 SAGE/APA 规范）",
    reporting_standards={
        "spatial_analysis": "空间分析遵循空间数据报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "研究范围与尺度须明确",
        "数据来源与时段须说明",
        "空间单元须定义",
        "政策背景须交代",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "Urban Studies",
        "Journal of Urban Affairs",
        "Cities",
        "Urban Affairs Review",
        "Journal of the American Planning Association",
        "Environment and Planning A",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "密度用 人/km² 或 户/km²",
        "回归系数给出标准误与显著性",
        "样本量须报告",
        "金额用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "报告"),
    tools=("ArcGIS Pro", "QGIS", "R（spdep 空间统计）", "Python（geopandas/UrbanSim）", "SPSS"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Zenodo"),
)