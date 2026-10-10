"""污染与控制论文支持：环境污染监测、污染物扩散模型、污染控制与治理技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pollution_and_contamination",
    aliases=("pollution_and_contamination", "污染与控制", "污染控制", "环境保护", "环境科学", "Environmental Science", "环境污染", "污染监测", "污染治理", "Pollution Control"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACS 样式",
    reporting_standards={"HJ 819": "大气污染源源强核算技术指南", "EPA NEI": "排放清单构建规范", "ISO 14064": "温室气体核算规范"},
    conventions=("污染物浓度单位统一为 μg/m³ 或 mg/L", "排放量单位用 kt/a 或 t/a", "模型评价须报告 NMSE、BIAS、RMSE", "排放因子须标注来源", "气象与地形数据源须显式标注"),
    key_venues=("Environmental Science & Technology", "Atmospheric Environment", "Water Research", "Journal of Hazardous Materials", "环境科学"),
    units_and_formulas_notes=("浓度 μg/m³（颗粒物）与 ppb（气态）", "排放量 kt/a 或 t/a", "扩散模型步长 15 min", "PM₂.₅ 化学组成按 EC、OC 分类"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPA AERMOD", "EPA CALINE5", "EPA BenMAP-3", "NOAA HYSPLIT", "NOAA WRF-Chem", "US EPA CMAQ", "US EPA CAMx", "EMEP", "GEOS-Chem", "PyMAP3D", "COMSOL Multiphysics", "ANSYS FLUENT", "QGIS", "ArcGIS Pro", "MATLAB", "Python", "R", "SPSS", "Hach Water Quality Tester", "EPA AP-42"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "Web of Science"),
)