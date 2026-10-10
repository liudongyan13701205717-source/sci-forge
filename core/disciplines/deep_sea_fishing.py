"""Deep sea fishing 学科论文支持：深海捕捞/远洋渔业研究体裁、海洋渔业数据规范与探测工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="deep_sea_fishing",
    aliases=(
        "deep_sea_fishing", "深海捕捞", "远洋捕捞", "深海渔业",
        "远洋渔业", "deep sea fishing", "pelagic fishing", "demersal fishing",
        "offshore fishing", "long-distance fishing", "international fishing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与渔业问题）",
            "data and methods（数据来源、渔具参数与研究方法）",
            "results（渔获组成、资源评估与生态数据）",
            "discussion（管理与政策意义）",
            "conclusions",
            "references",
        ),
        "stock_assessment": (
            "abstract",
            "introduction",
            "data（渔获量、CPUE、调查数据）",
            "model（评估模型与参数设定）",
            "results（资源状态与参考点）",
            "sensitivity（敏感性分析）",
            "references",
        ),
        "methodology": (
            "abstract",
            "introduction",
            "equipment（渔具设计与参数）",
            "operations（作业方法与流程）",
            "catch_data（渔获数据分析）",
            "implications（资源管理与环境影响）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "catch": "渔获组成须按物种报告（拉丁名），体长/体重数据须注明采样方法",
        "gear": "渔具参数须完整报告（网目尺寸、网线径、网长、沉子重量等）",
        "assessment": "资源评估须声明模型类型（如VPA、Surplus Production）、参数设定与数据来源",
        "effort": "捕捞努力量须报告作业天数、航次数、渔具数量",
        "cpue": "CPUE（单位捕捞努力量渔获量）须注明标准化方法与置信区间",
    },
    conventions=(
        "渔具参数须完整报告（网目尺寸、网线径、网长、沉子重量等）",
        "捕捞位置须以经纬度与水深标注；调查航次须注明日期与船名",
        "渔获组成须按物种报告（拉丁名），体长/体重数据须注明采样方法",
        "资源评估须声明模型类型（如VPA、Surplus Production）、参数设定与数据来源",
        "统计须报告置信区间与样本量；时间序列须注明时间跨度与数据粒度",
    ),
    key_venues=(
        "ICES Journal of Marine Science",
        "Progress in Oceanography",
        "Deep-Sea Research Part I",
        "Deep-Sea Research Part II",
        "Marine and Freshwater Research",
        "Fisheries Oceanography",
        "Journal of Experimental Marine Biology and Ecology",
        "Fisheries Research",
    ),
    units_and_formulas_notes=(
        "水深用 m；水温用 ℃；盐度用 PSU",
        "渔获量用 t（吨）；CPUE 用 kg/day 或 kg/h",
        "网目尺寸用 mm；网线径用 mm；网长用 m",
        "纬度/经度用十进制度；水深用 m",
        "统计显著性用 α=0.05；95% 置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Multibeam Echo Sounder", "Sub-bottom Profiler", "Fish-Finding Sonar", "Fish Aggregating Device (FAD)", "ECDIS (Electronic Chart Display and Information System)", "AIS (Automatic Identification System)", "GPS (Global Positioning System)", "Hydroacoustic Survey System", "Trawling Equipment", "Purse Seine Net", "Longline System", "Pots and Traps", "Oceanographic Buoy", "CTD Sensor", "Doppler Velocity Profiler (DVP)", "Underwater Acoustic Modem", "ROV (Remotely Operated Vehicle)", "AUV (Autonomous Underwater Vehicle)", "VMS (Vessel Monitoring System)", "R (fishery analysis packages)"),
    category="农学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
