"""Agriculture not elsewhere classified 学科论文支持：农业政策与农村发展综合体裁、APA/Elsevier 与政策分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_not_elsewhere_classified",
    aliases=(
        "agriculture not elsewhere classified",
        "农业政策",
        "农村发展",
        "agriculture NEC",
        "rural development",
        "agricultural policy",
        "农林牧渔其他",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "data and methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context",
            "data and method",
            "results",
            "implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "findings",
            "research gaps",
            "references",
        ),
    },
    citation_style="APA 7 或 Elsevier numbered（Food Policy 采用 Elsevier）",
    reporting_standards={
        "survey": "农户调查遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 AAAAM 惯例；效应量须报告",
        "policy": "政策评估须遵循 OECD DAC 效果框架",
    },
    conventions=(
        "农业术语全文一致：农户/家庭/规模/补贴/政策工具须明确定义",
        "数据来源须完整标注（FAOSTAT、USDA ERS、国家统计局、World Bank）并注明口径",
        "样本量、显著性水平、置信区间与效应量须完整报告",
        "名义与实际价格须区分并给出平减指数；汇率注明时点",
    ),
    key_venues=(
        "Food Policy",
        "Agricultural Economics",
        "Journal of Rural Studies",
        "World Development",
        "China Agricultural Economics Review",
        "Journal of Agricultural and Applied Economics",
        "Agriculture & Human Values",
    ),
    units_and_formulas_notes=(
        "价格/产量/面积用国际单位（USD、t、ha）并注明统计口径",
        "政策工具（补贴/关税/配额）须给出度量单位与年份",
        "效应量报告 Cohen's d、η²、R² 等标准指标",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "GAMS", "LEAP", "ECONOMICA", "AIMS", "ArcGIS", "QGIS", "Google Earth Engine", "SPSS", "NVivo", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "Microsoft Excel", "FAOSTAT", "USDA ERS", "World Bank WDI"),
    category="农学",
    databases=("OpenAlex", "CNKI", "万方", "SSRN", "FAOSTAT", "USDA ERS", "World Bank Open Data", "OECD iLibrary"),
)
