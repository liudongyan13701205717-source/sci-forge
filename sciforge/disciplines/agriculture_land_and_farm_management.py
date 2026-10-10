"""Agriculture, land and farm management 学科论文支持：农业土地与农场经营管理体裁、APA 与土地经济注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_land_and_farm_management",
    aliases=(
        "agriculture land and farm management",
        "农业土地与农场管理",
        "农场管理",
        "土地经济",
        "农业经营",
        "farm management",
        "land management",
        "farm business",
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
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
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
    },
    citation_style="APA 7 或 Elsevier numbered（AJAE 采用 Elsevier）",
    reporting_standards={
        "survey": "农户调查遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 AAAAM 惯例；效应量须报告",
    },
    conventions=(
        "土地权属、地类、面积单位（ha/亩）须明确；地权类型须定义",
        "农场账目遵循农业会计惯例（GA-FARM 或中国新会计制度）",
        "收入、成本、利润按可比年价折算并给出平减指数",
        "样本量、显著性水平、置信区间与效应量须完整报告",
    ),
    key_venues=(
        "Journal of Agricultural and Applied Economics",
        "Land Use Policy",
        "Journal of Rural Studies",
        "Food Policy",
        "International Journal of Agricultural Sustainability",
        "Journal of Agribusiness",
        "China Agricultural Economics Review",
    ),
    units_and_formulas_notes=(
        "土地面积用 ha 或 km²；亩换算 1 ha = 15 亩",
        "地租、地价用 USD/ha 或 CNY/亩并注明年份",
        "农场回报率（ROI、ROA）公式须给出并说明口径",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "GAMS", "ECONOMICA", "LEAP", "ArcGIS", "QGIS", "Google Earth", "Google Earth Engine", "SPSS", "NVivo", "MAXQDA", "Farm Business Management System AFS Enterprise", "Granular", "John Deere Operations Center", "FarmDrive", "SAP", "Oracle", "Coupa"),
    category="经济学",
    databases=("OpenAlex", "CNKI", "万方", "SSRN", "USDA ERS", "FAOSTAT", "World Bank WDI", "CAERS"),
)
