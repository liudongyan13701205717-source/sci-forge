"""岩土工程学科论文支持：土力学、地基基础、边坡、基坑与岩石力学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geotechnical_engineering",
    aliases=(
        "geotechnical_engineering",
        "岩土工程",
        "soil_mechanics",
        "土力学",
        "foundation_engineering",
        "基础工程",
        "slope_engineering",
        "边坡工程",
        "rock_mechanics",
        "岩石力学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与岩土问题）",
            "methodology（试验、建模与参数）",
            "results（土性/变形数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程背景）",
            "analysis（设计与实施）",
            "results（施工监测与性能）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份；ASCE 期刊遵循 ASCE 规范）",
    reporting_standards={
        "experimental": "土工试验遵循 ASTM D 系列标准",
        "site_characterization": "场地勘察遵循 ISSMGE 建议方法",
        "numerical": "数值分析遵循 ISSMGE 数值方法规范",
    },
    conventions=(
        "土体分类（USCS）与物理指标须报告",
        "强度/变形参数须注明试验方法",
        "地下水位与孔压条件须说明",
        "安全系数与设计准则须明确",
        "监测项目与仪器须报告",
    ),
    key_venues=(
        "Journal of Geotechnical and Geoenvironmental Engineering",
        "Géotechnique",
        "Canadian Geotechnical Journal",
        "Soils and Foundations",
        "Computers and Geotechnics",
    ),
    units_and_formulas_notes=(
        "应力用 kPa/MPa；含水量用 %；重度用 kN/m³",
        "有效应力与固结方程须编号；公式用 amsmath",
        "数值结果给出均值 ± 不确定度与样本量",
        "渗透系数用 m/s 或 cm/s；压缩模量用 kPa/MPa",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PLAXIS", "PLAXIS 3D", "GEO5", "FLAC3D", "MIDAS GTS", "DIANA", "ABAQUS", "ANSYS", "MATLAB", "GeoStudio", "Slope/W", "Slide", "Seep/W", "QGIS", "ArcGIS", "PostGIS", "Python", "Surfer", "GOCAD", "TerraScope"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
