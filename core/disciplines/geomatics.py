"""测绘学学科论文支持：大地测量、摄影测量、遥感、地图学与测量工程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geomatics",
    aliases=(
        "geomatics",
        "测绘学",
        "surveying",
        "测量学",
        "geodesy",
        "大地测量",
        "photogrammetry",
        "摄影测量",
        "remote_sensing",
        "遥感",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（测量方案与方法）",
            "results（精度与成果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程背景）",
            "analysis（实施与分析）",
            "results（成果）",
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
    citation_style="IEEE 或 AGU（视方向而定）",
    reporting_standards={
        "measurement": "测量须报告仪器型号、精度、观测条件与不确定度",
        "coordinate": "坐标系、基准、投影与转换参数须显式说明",
        "precision": "精度评定须报告 RMSE、样本量、检验方法与显著性",
    },
    conventions=(
        "坐标系、投影、高程基准、时间基准须显式",
        "仪器型号与厂商写全；观测参数写清",
        "不确定度用 A/B 类评定；合成给 k 与置信度",
        "地图须含比例尺、指北针、图例与坐标系",
        "角度、长度、精度单位统一",
    ),
    key_venues=(
        "ISPRS Journal of Photogrammetry and Remote Sensing",
        "Journal of Geodesy",
        "Remote Sensing of Environment",
        "Photogrammetric Engineering and Remote Sensing",
        "ISPRS International Journal of Geo-Information",
    ),
    units_and_formulas_notes=(
        "长度用 m 或 mm；角度用 \" 或 mrad",
        "坐标用 m 或 °；高程用 m asl",
        "不确定度用 m 或 mm；相对精度给 1/N",
        "精度报告：RMSE、样本量、置信度、检验方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Leica TS 全站仪", "Trimble Total Station", "Leica GNSS Receiver", "Trimble GNSS Receiver", "RTK 测量系统", "DJI Phantom 无人机", "DJI Mavic 3E", "Agisoft Metashape", "Pix4D", "Leica ScanStation", "Trimble FX 三维激光", "Faro Laser Scanner", "GOM Inspect", "QGIS", "ArcGIS", "PostGIS", "MATLAB", "Python", "Jupyter Notebook", "Surfer"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
