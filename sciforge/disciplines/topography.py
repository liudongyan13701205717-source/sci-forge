"""地形测量学科论文支持：地形测绘/空间分析体裁、Photogrammetric Engineering 引用样式与测量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="topography",
    aliases=("topography", "地形测量", "地形测绘", "地形分析", "测绘学",
             "topographic surveying", "GIS", "地形制图", "数字高程模型"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与地形测量问题）",
            "methods（数据采集与处理方法）",
            "results（精度分析与可视化）",
            "discussion（误差分析与应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（测区案例）",
            "data processing（数据处理流程）",
            "results（地形产品与分析）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview",
            "main developments",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "coordinate_system": "坐标系与高程基准须明确（如 WGS-84 / 1985 国家高程基准）",
        "accuracy_report": "平面精度与高程精度须报告（中误差）",
        "control_network": "控制网平差方法与残差须说明",
        "data_uncertainty": "不确定性评估须遵循 ISO 21580 或 OGC 标准",
    },
    conventions=(
        "坐标单位：经度/纬度用度分秒（°'\"）或十进制度",
        "高程单位 m，注明基准面",
        "比例尺用 1:n 表示",
        "等高距（contour interval）须注明",
        "术语首次出现给出中英文对照",
    ),
    key_venues=(
        "Photogrammetric Engineering and Remote Sensing",
        "ISPRS Journal of Photogrammetry and Remote Sensing",
        "Journal of Geodesy",
        "Remote Sensing",
        "Geomatics World",
    ),
    units_and_formulas_notes=(
        "坐标：经纬度用度分秒或十进制度，平面坐标用 m",
        "高程单位 m，精度以中误差（cm/m）报告",
        "比例尺用 1:n 格式",
        "公式用 amsmath 排版；误差传播公式须明确写出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("全站仪", "GPS 接收机", "RTK 接收机", "无人机（UAV）", "激光雷达扫描仪", "水准仪", "全站仪测量机器人", "ArcGIS", "QGIS", "Global Mapper", "ERDAS Imagine", "OrbisWare", "Autodesk Civil 3D", "S Surv 4", "Leica Infinity", " Carlson Survey", "Pix4Dmapper", "Agisoft Metashape", "MATLAB", "Python"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
