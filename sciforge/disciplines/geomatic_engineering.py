"""地理信息工程学科论文支持：测绘工程、空间数据采集与处理系统设计。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geomatic_engineering",
    aliases=(
        "geomatic_engineering",
        "地理信息工程",
        "geomatics_engineering",
        "地理信息工程",
        "geospatial_engineering",
        "地理空间工程",
        "surveying_and_mapping",
        "测绘工程",
        "spatial_engineering",
        "空间工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（设计与实现方法）",
            "results（精度验证与结果）",
            "discussion（性能与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程背景）",
            "analysis（设计与实施）",
            "results（成果与精度）",
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
    citation_style="IEEE 或 APA 7（视期刊而定）",
    reporting_standards={
        "measurement": "测量须报告仪器型号、精度等级、观测条件与不确定度",
        "system_design": "系统须报告架构、模块、数据流与接口协议",
        "validation": "精度验证须报告 RMSE、样本量、检验方法与显著性",
    },
    conventions=(
        "坐标系、投影、高程基准与时间基准须显式说明",
        "仪器型号与厂商写全；观测参数写清",
        "不确定度用 A 类/B 类评定，合成给 k 与置信度",
        "软件架构用 UML 图；流程图用统一符号",
        "算法报告复杂度、收敛判据与失败情形",
    ),
    key_venues=(
        "ISPRS Journal of Photogrammetry and Remote Sensing",
        "Journal of Geodesy",
        "Journal of Surveying Engineering",
        "Measurement",
        "International Journal of Applied Earth Observation and Geoinformation",
    ),
    units_and_formulas_notes=(
        "长度用 m 或 mm；角度用 \" 或 mrad；高度用 m",
        "坐标用 m 或 °；时间用 UTC 或 TT",
        "不确定度用 m 或 mm；相对精度给 1/N",
        "角度精度用 mrad 或 \"；测距精度用 mm + ppm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "PostGIS", "GDAL/OGR", "Leica TS 全站仪", "Trimble Total Station", "Leica GNSS Receiver", "Trimble GNSS Receiver", "RTK 测量系统", "DJI Phantom 无人机", "Agisoft Metashape", "Pix4D", "Leica ScanStation 三维激光", "Trimble FX 三维激光", "Faro Laser Scanner", "GOM Inspect", "Python", "MATLAB", "Jupyter Notebook", "OpenCV"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
