"""大气污染防治学科论文支持：大气污染物扩散模型、清单构建与减排评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="air_pollution_control",
    aliases=(
        "Air pollution control",
        "大气污染防治",
        "大气污染控制",
        "大气环境工程",
        "air pollution prevention and control",
        "atmospheric pollution",
        "emission inventory",
        "air quality modelling",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（污染背景、清单或情景问题）",
            "methods（模型配置/清单构建/监测网/情景设计）",
            "results（浓度场、贡献源解析、减排效果）",
            "discussion（不确定性、与观测对比）",
            "conclusion（政策启示）",
            "references",
        ),
        "policy_report": (
            "abstract",
            "背景与目标",
            "现状评估",
            "减排路径",
            "效益分析",
            "实施建议",
            "参考文献",
        ),
    },
    citation_style="EPA/GB 规范样式（技术报告）或 ACS 样式（期刊论文）",
    reporting_standards={
        "inventory": "清单构建遵循 EPA NEI 框架或 UNF-CCC 规范，须给出活动水平与排放因子来源",
        "model_evaluation": "模型评价须报告 NMSE、BIAS、RMSE 等标准指标与观测站清单",
        "uncertainty": "不确定性分析须覆盖排放因子、气象参数与化学机制",
        "compliance": "引用 GB 3095、GB 16297、HJ 819 等现行标准的最新版本",
    },
    conventions=(
        "污染物浓度单位统一为 μg/m³（颗粒物）与 ppb（气态），必要时给出 mg/m³ 对照",
        "排放量单位用 kt/a 或 t/a，并明确统计年与空间分辨率",
        "排放清单表须区分 SO₂、NOₓ、CO、NMVOC、PM₁₀、PM₂.₅、氨、臭氧前体物等组分",
        "模型时段与步长（如 15 min 化学步长）须在方法节声明",
        "气象与地形数据源与版本须显式标注",
    ),
    key_venues=(
        "Atmospheric Environment",
        "Environmental Science & Technology",
        "Atmospheric Chemistry and Physics",
        "环境科学学报",
        "中国环境科学",
        "Journal of Environmental Management",
        "Environment International",
    ),
    units_and_formulas_notes=(
        "遵循 HJ 819—2017 大气污染源源强核算技术指南总则与分项指南",
        "排放因子标注来源（IPCC 默认值/行业实测/地方值）",
        "扩散模型结果与观测对比时须对齐时间步长与空间尺度",
        "PM₂.₅ 化学组成报告按 EC、OC、水溶性离子、地壳元素分类",
        "情景分析须给出基准年、目标年与主要驱动变量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPA AERMOD", "EPA AERSCREEN", "EPA ISCST3", "EPA CALINE5", "EPA SCRAM", "EPA AirToxScreen", "EPA BenMAP-2", "EPA BETA9", "EPA SCREEN3", "EPA CALPUFF", "EPA CALMET", "EPA AERVIEW", "EPA ODM", "EPA ODMGRID", "NOAA HYSPLIT", "NOAA CAMx", "NOAA WRF", "NOAA WRF-Chem", "NOAA M3NPCT", "US EPA CMAQ", "US EPA UAMQ", "US EPA UAMK", "US EPA UAMOC", "US EPA SOFV3", "US EPA KINEM", "US EPA ADMS", "US EPA APACHE", "EMEP", "GEOS-Chem", "LMDZ-ORCHADROME", "MOS-Chem", "EDGAR", "IPCC emission factors", "EPA AP-42", "EPA EDGAR (Fuglemen)", "EPA BenMAP-3", "HYSPLIT Web", "PyMAP3D", "COMSOL Multiphysics", "ANSYS FLUENT", "PHOENICS", "Fire Dynamics Simulator (FDS)", "KML", "QGIS", "ArcGIS", "PostgreSQL/PostGIS", "R", "MATLAB", "Python", "Gaussian plume", "Box model"),
    category="工学",
    databases=("CNEMS Air", "OpenAlex", "Crossref", "EPA AP-42", "UNFCCC EDGAR"),
)
