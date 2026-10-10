"""Agricultural economics 学科论文支持：农业经济学/农户行为/农产品市场体裁、APA 引用样式与农业经济注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agricultural_economics",
    aliases=(
        "agricultural economics",
        "农业经济学",
        "农业经济",
        "农村经济",
        "农产品经济学",
        "agricultural and resource economics",
        "农经",
        "农业经济与管理",
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
        "survey": (
            "abstract",
            "introduction",
            "research design",
            "data collection",
            "empirical analysis",
            "findings",
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
    citation_style="APA 7（AJAE 与 Food Policy 遵循 Elsevier 数字样式）",
    reporting_standards={
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 AAAAM 惯例",
        "panel": "面板/时间序列须报告稳健标准误、固定效应与检验",
    },
    conventions=(
        "农业经济术语全文一致：农户/家庭/规模/补贴/价格/收入须明确定义",
        "数据来源须完整标注（USDA ERS、FAO、国家统计局、CEIC）并注明统计口径",
        "样本量、显著性水平、置信区间与效应量须完整报告；面板数据须说明 FE/RE/OLS/ARIMA",
        "名义与实际价格须区分并给出平减指数（CPI 或 WPI）；汇率注明时点",
    ),
    key_venues=(
        "American Journal of Agricultural Economics",
        "Agricultural Economics",
        "Agricultural Systems",
        "Food Policy",
        "Journal of Rural Studies",
        "Review of Agricultural Economics",
        "China Agricultural Economics Review",
    ),
    units_and_formulas_notes=(
        "价格/产量/面积用国际单位（USD、t、ha）并注明统计口径",
        "收入与成本按可比年价折算并给出平减因子",
        "效应量报告 Cohen's d、η²、R² 等标准指标",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "GAMS", "LEAP", "ECONOMICA", "MODSIM", "ArcGIS", "QGIS", "SPSS", "NVivo", "NVivo / MAXQDA", "FAOSTAT", "USDA ERS", "CEIC China Database", "World Bank WDI", "ILOSTAT", "OECD-AgriStat", "CNRI", "CAERS"),
    category="经济学",
    databases=("OpenAlex", "CNKI", "万方", "SSRN", "USDA ERS", "FAOSTAT", "World Bank Open Data"),
)
