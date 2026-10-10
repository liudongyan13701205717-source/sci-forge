"""Climate Research 学科论文支持：气候研究/气候模拟/气候预测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="climate_research",
    aliases=(
        "Climate Research", "气候研究", "Climate Science",
        "Climate Modeling", "气候建模", "Climate Prediction",
        "气候预测", "Climate Modeling and Simulation",
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
        "data_format": "模式输出须采用 NetCDF/CDO 标准格式并附元数据",
    },
    conventions=(
        "使用 IPCC AR6 的术语与情景（CMIP6、SSP）",
        "引用气候模式时说明模式名称、版本与分辨率",
        "使用 ERA5、MERRA-2 等再分析资料时给出版本与时间跨度",
        "气候模式输出使用 NetCDF/CDO 格式",
        "使用 xarray、cf-xarray 等标准库进行数据处理",
    ),
    key_venues=(
        "Climate of the Past",
        "Climate Dynamics",
        "Journal of Geophysical Research: Atmospheres",
        "Journal of Geophysical Research: Oceans",
        "Environmental Research Letters",
        "Atmospheric Chemistry and Physics",
        "Journal of Climate",
        "Climate Research",
    ),
    units_and_formulas_notes=(
        "温度使用 K 或 °C；降水用 mm/day；气压用 hPa",
        "辐射通量用 W/m²；热含量用 J；海平面用 mm",
        "模式输出须标注分辨率、时间步长与物理参数化方案",
        "年代平均须给面积权重与样本数；趋势用每年斜率并附显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("WRF", "CESM", "MPI-ESM", "UKV", "CMIP6", "Python", "RStudio", "MATLAB", "Octave", "QGIS", "Google Earth Engine", "Copernicus Climate Data Store", "R", "MetPy", "Matplotlib", "Plotly", "NCL (NCAR Command Language)", "xarray", "GrADS", "Jupyter Notebook"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Copernicus"),
)
