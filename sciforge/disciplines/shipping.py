"""航运学科论文支持：航运经济与管理、船舶调度与港口物流体裁及IMO海事规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="shipping",
    aliases=(
        "shipping",
        "航运",
        "航运管理",
        "航运经济",
        "海上运输",
        "Shipping",
        "Maritime Transport",
        "Maritime Business",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "data and sample（数据与样本）",
            "results（结果）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（航线/公司/港口案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份，Harvard）",
    reporting_standards={
        "archival": "档案研究须说明数据来源（波罗的海交易所、Lloyd's、Veson Navi）",
        "survey": "问卷研究遵循 AAPOR 报告规范",
        "simulation": "仿真研究须披露模型参数、随机种子与收敛标准",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "船舶尺度参数统一采用 IMO 定义（DWT、TEU、GT、NT），首次出现给出中英文",
        "汇率与运费按基准日期换算；燃油价格统一为 US$/bbl（Brent）",
        "碳排放强度用 EEOI 与 CEEOI 报告，遵循 IMO 2009/MEPC.1/Circ.677",
        "统计结果报告 M、SD、p 值与 95% CI；回归系数给出标准误",
        "样本量、时间跨度与样本筛选过程须说明",
    ),
    key_venues=(
        "Maritime Economics & Logistics",
        "Transportation Research Part E",
        "Maritime Policy & Management",
        "Journal of Shipping and Trade",
        "运输经济研究",
    ),
    units_and_formulas_notes=(
        "船舶尺度：DWT（吨）、TEU（二十尺等效箱）、载重吨与总吨分列",
        "运费用 US$/TWD（吨日租）或 US$/TEU 报告；燃油按 Bunker Adjustment Factor (BAF) 计价",
        "船舶周转率 V (km/d)、日租金 D (US$/day)、载货因数 STCW/Cargo Factor 明确单位",
        "碳排：EEOI = (ADT × CII_A) / E；CII = (ADT × CO₂) / (ADT)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MaxSea Route", "Voyage Planner (Voyis)", "Marpol 2", "MarineTraffic", "Kpler", "Veson Navi", "Baltic Exchange Online", "Drewry Containerized Freight Index", "GMS 航运版", "SeaWeb", "PortVision", "Navis N4", "WCA COSMOS", "Maersk Spot", "GEOBIA", "Borregales", "Python（Pandas/SciPy）", "R（dplyr/tidyverse）", "MATLAB", "AnyLogic"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "SSRN"),
)
