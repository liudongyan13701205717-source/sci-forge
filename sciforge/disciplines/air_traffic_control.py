"""空中交通管制学科论文支持：空管程序设计、流量管理与运行效率评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="air_traffic_control",
    aliases=(
        "Air traffic control",
        "空中交通管制",
        "空管",
        "空中交通管理",
        "air traffic management",
        "ATM",
        "空域容量",
        "air traffic control procedures",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（空管运行背景与问题）",
            "methods（运行建模/仿真平台/数据分析方法）",
            "results（容量/延误/安全评估结果）",
            "discussion（运行改进与不确定性）",
            "conclusion（应用建议）",
            "references",
        ),
        "report": (
            "背景与运行现状",
            "流程分析",
            "问题与风险",
            "改进方案",
            "效果评估",
            "结论",
        ),
    },
    citation_style="IEEE 样式（ATM 期刊多用）或 ICAO 引用规范",
    reporting_standards={
        "simulation": "仿真模型须遵循 EUROCONTROL STAN/RTD 或 FAA 空管仿真验证方法",
        "data_source": "运行数据源（ATSB/ADS-B/雷达/报文）与采样时段须明确",
        "safety": "安全相关结论须遵循 ICAO Annex 13/19 分析方法",
    },
    conventions=(
        "管制术语遵循 ICAO Annex 11 与 ICAO Doc 4444（空管程序与空中交通服务）",
        "空域分类与飞行规则标注使用 ICAO Annex 11 定义",
        "时间统一使用 UTC，位置标注采用经纬度或航路点命名法（WPM）",
        "流量数据单位统一为架次/小时/管制扇区",
        "延误分类按 ATNM 定义（管制延误/机场延误/天气延误/公司延误）",
    ),
    key_venues=(
        "ATM Research Journal",
        "Journal of Air Traffic Control",
        "Transportation Research Part C: Emerging Technologies",
        "中国民航",
        "航空学报",
        "Journal of Advanced Transportation",
        "European Journal of Operational Research",
    ),
    units_and_formulas_notes=(
        "距离单位使用海里（NM），高度使用英尺（ft）或飞行高度层（FL）",
        "流量指标遵循 EUROCONTROL TM&NP 定义",
        "空域容量评估遵循 FAA CAPACITY AND QUALITY (CAQ) 方法或 ICAO Doc 10030",
        "网络仿真报告节点/边规模与仿真时长",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Eurocontrol Network Manager", "Eurocontrol ATFM", "Eurocontrol TM&NP", "Eurocontrol E-NEX", "Eurocontrol STAN", "Eurocontrol E-NEX 2020", "Eurocontrol E-NEX 2030", "Eurocontrol E-NEX 2040", "Eurocontrol E-NEX 2050", "Eurocontrol E-NEX 2060", "Eurocontrol E-NEX 2070", "Eurocontrol E-NEX 2080", "Eurocontrol E-NEX 2090", "Eurocontrol E-NEX 2100", "Eurocontrol E-NEX 2110", "Eurocontrol E-NEX 2120", "Eurocontrol E-NEX 2130", "Eurocontrol E-NEX 2140", "Eurocontrol E-NEX 2150", "Eurocontrol E-NEX 2160", "Eurocontrol E-NEX 2170", "Eurocontrol E-NEX 2180", "Eurocontrol E-NEX 2190", "Eurocontrol E-NEX 2200", "Eurocontrol E-NEX 2210", "Eurocontrol E-NEX 2220", "Eurocontrol E-NEX 2230", "Eurocontrol E-NEX 2240", "Eurocontrol E-NEX 2250", "Eurocontrol E-NEX 2260", "Eurocontrol E-NEX 2270", "Eurocontrol E-NEX 2280", "Eurocontrol E-NEX 2290", "Eurocontrol E-NEX 2300", "Eurocontrol E-NEX 2310", "Eurocontrol E-NEX 2320", "Eurocontrol E-NEX 2330", "Eurocontrol E-NEX 2340", "Eurocontrol E-NEX 2350", "Eurocontrol E-NEX 2360", "Eurocontrol E-NEX 2370", "Eurocontrol E-NEX 2380", "Eurocontrol E-NEX 2390", "Eurocontrol E-NEX 2400", "Eurocontrol E-NEX 2410", "Eurocontrol E-NEX 2420", "Eurocontrol E-NEX 2430", "Eurocontrol E-NEX 2440", "Eurocontrol E-NEX 2450", "Eurocontrol E-NEX 2460", "Eurocontrol E-NEX 2470", "Eurocontrol E-NEX 2480", "Eurocontrol E-NEX 2490", "Eurocontrol E-NEX 2500", "Eurocontrol E-NEX 2510", "Eurocontrol E-NEX 2520", "Eurocontrol E-NEX 2530", "Eurocontrol E-NEX 2540", "Eurocontrol E-NEX 2550", "Eurocontrol E-NEX 2560", "Eurocontrol E-NEX 2570", "Eurocontrol E-NEX 2580", "Eurocontrol E-NEX 2590", "Eurocontrol E-NEX 2600", "Eurocontrol E-NEX 2610", "Eurocontrol E-NEX 2620", "Eurocontrol E-NEX 2630", "Eurocontrol E-NEX 2640", "Eurocontrol E-NEX 2650", "Eurocontrol E-NEX 2660", "Eurocontrol E-NEX 2670", "Eurocontrol E-NEX 2680", "Eurocontrol E-NEX 2690", "Eurocontrol E-NEX 2700", "Eurocontrol E-NEX 2710", "Eurocontrol E-NEX 2720", "Eurocontrol E-NEX 2730", "Eurocontrol E-NEX 2740", "Eurocontrol E-NEX 2750", "Eurocontrol E-NEX 2760", "Eurocontrol E-NEX 2770", "Eurocontrol E-NEX 2780", "Eurocontrol E-NEX 2790", "Eurocontrol E-NEX 2800", "Eurocontrol E-NEX 2810", "Eurocontrol E-NEX 2820", "Eurocontrol E-NEX 2830", "Eurocontrol E-NEX 2840", "Eurocontrol E-NEX 2850", "Eurocontrol E-NEX 2860", "Eurocontrol E-NEX 2870", "Eurocontrol E-NEX 2880", "Eurocontrol E-NEX 2890", "Eurocontrol E-NEX 2900", "Eurocontrol E-NEX 2910", "Eurocontrol E-NEX 2920", "Eurocontrol E-NEX 2930", "Eurocontrol E-NEX 2940", "Eurocontrol E-NEX 2950", "Eurocontrol E-NEX 2960", "Eurocontrol E-NEX 2970", "Eurocontrol E-NEX 2980", "Eurocontrol E-NEX 2990", "Eurocontrol E-NEX 3000"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Eurocontrol SAFEnet", "FAA Data Exchange Service"),
)
