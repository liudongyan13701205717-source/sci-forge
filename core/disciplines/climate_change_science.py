"""Climate Change Science 学科论文支持：气候科学/大气科学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="climate_change_science",
    aliases=(
        "Climate Change Science", "气候科学", "Climate Science",
        "气候变化科学", "Atmospheric Sciences", "大气科学",
        "Climate Dynamics", "气候动力学", "气候系统科学",
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
        "ipcc_ar6": "气候模式与情景须遵循 IPCC AR6 术语（CMIP6、SSP）",
        "model_documentation": "模式版本、分辨率与边界条件须完整声明",
        "reanalysis_data": "再分析资料须给出数据产品名、版本与时间跨度",
    },
    conventions=(
        "使用 IPCC AR6 的术语（CMIP6、SSP、RCP）",
        "引用气候模式时给出模式名称、版本与分辨率",
        "使用 ERA5、MERRA-2 等再分析资料时给出版本与时间跨度",
        "气候敏感度使用 ECS/ETTES 术语",
        "单位使用 SI，温标使用开尔文或摄氏度并标注",
    ),
    key_venues=(
        "Nature Climate Change",
        "Nature Geoscience",
        "Journal of Climate",
        "Geophysical Research Letters",
        "Climate Dynamics",
        "Atmospheric Chemistry and Physics",
        "Nature Communications",
        "Science",
    ),
    units_and_formulas_notes=(
        "温度使用 SI 单位 K 或 °C，须标注温标",
        "辐射通量用 W/m²，热含量用 J/m²，海平面用 mm",
        "气候敏感度须明确使用 ECS 或 ETTES 并给出估计值与误差",
        "异常距平基准期须声明（如 1991–2020），并给出面积权重",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CESM", "MPI-ESM", "HadCM3", "CMIP6", "Python", "RStudio", "MATLAB", "QGIS", "Google Earth Engine", "Copernicus Climate Data Store", "R", "MetPy", "Matplotlib", "Plotly", "NCL (NCAR Command Language)", "xarray", "ERA5", "ECMWF", "GrADS", "Jupyter Notebook"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Copernicus"),
)
