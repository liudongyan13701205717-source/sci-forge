"""航海科学学科论文支持：航海研究/船舶导航体裁、航行规范与航海记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nautical_science",
    aliases=("nautical_science", "航海科学", "航海", "船舶驾驶",
             "航海技术", "船舶导航", "航海工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与航行问题）",
            "methodology（模拟/试验/分析方法）",
            "results（航行/导航结果）",
            "discussion（安全与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（航次/事件/船舶概况）",
            "analysis（航行决策与人为因素分析）",
            "results（案例结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（航海理论综述）",
            "evidence synthesis（多案例证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Ocean Engineering 遵循 Elsevier 规范）",
    reporting_standards={
        "navigation": "航行研究遵循 IMO 规范",
        "simulation": "模拟器试验遵循 IMO 模拟器规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "safety": "安全研究遵循 STCW 规范",
        "human_factors": "人为因素遵循 IMO 指南",
    },
    conventions=(
        "船舶主尺度须完整报告",
        "航海设备型号须注明",
        "模拟器型号与参数须说明",
        "试验条件（风、浪、流）须完整",
        "人为因素须符合 STCW",
    ),
    key_venues=(
        "Ocean Engineering",
        "Journal of Navigation",
        "International Journal of Naval Architecture and Ocean Engineering",
        "Journal of Marine Science and Technology",
        "Marine Policy",
    ),
    units_and_formulas_notes=(
        "航速用 kn；距离用 nmi；功率用 kW",
        "公式用 amsmath；航行方程须编号",
        "时间/位置须精确到秒/分位",
        "罗经差/磁差须注明",
        "气象数据须完整",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ECDIS（电子海图）", "雷达（ARPA）", "回声测深仪", "GPS 差分设备", "AIS（自动识别系统）", "磁罗经", "六分仪", "卫星通信（Inmarsat）", "气象传真机", "航行模拟器", "MaxSea（航行规划）", "MATLAB", "Python（NumPy）", "Excel", "LaTeX", "Sentinel（卫星遥感）", "Google Earth", "天气预测软件", "导航日志软件", "Navionics（电子海图）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
