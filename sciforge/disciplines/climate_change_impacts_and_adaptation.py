"""Climate Change Impacts and Adaptation 学科论文支持：气候影响与适应。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="climate_change_impacts_and_adaptation",
    aliases=(
        "Climate Change Impacts and Adaptation", "气候变化影响与适应",
        "Climate Impacts", "气候影响评估", "Climate Adaptation",
        "气候适应", "Climate Risk", "气候风险管理",
        "Climate Change Impacts",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="AGU（American Geophysical Union）",
    reporting_standards={
        "ipcc_ar6": "影响评估术语与情景须遵循 IPCC AR6 框架",
        "climate_risk": "气候风险评估遵循 ISO 14091/14092",
        "adaptation_plan": "适应计划须包含情景、指标与不确定性分析",
    },
    conventions=(
        "使用 IPCC AR6 术语与影响分类（SOM、IAM、SSP）",
        "引用 SSP 情景时说明时间区间与区域",
        "影响评估遵循 ISO 14091 或 ISO 14092 规范",
        "适应措施应遵循 ISO 14091 气候风险评估",
        "影响评估须结合多变量与不确定性分析",
    ),
    key_venues=(
        "Nature Climate Change",
        "Nature Communications",
        "Environmental Research Letters",
        "Climate Dynamics",
        "Regional Environmental Change",
        "Wiley Interdisciplinary Reviews: Climate Change",
        "Global Environmental Change",
        "International Journal of Climate Change Strategy and Management",
    ),
    units_and_formulas_notes=(
        "温度使用 °C 或 K，气压使用 hPa，辐射使用 W/m²",
        "SSP/RCP 情景须给出情景名称、时间区间与区域",
        "影响评估须给出置信区间与显著性水平",
        "适应效益成本比 = 避免损失 / 实施成本，须给出货币与贴现率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Python", "QGIS", "ArcGIS Pro", "Google Earth Engine", "WRF", "CMAQ", "CESM", "CMIP6 Analysis", "Copernicus Climate Data Store", "Climate Data Online", "Matplotlib", "Plotly", "NCL (NCAR Command Language)", "DroughtAtlas", "CDO", "ERA5", "xarray", "Jupyter Notebook"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Copernicus"),
)
