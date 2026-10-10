"""土地测量学科论文支持：测量技术、空间数据、地籍管理与工程放样。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="land_surveying",
    aliases=(
        "land_surveying",
        "土地测量",
        "Land Surveying",
        "Geomatics",
        "Engineering Surveying",
        "Cadastral Surveying",
        "Geospatial Engineering",
        "Spatial Data Systems",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="IEEE",
    reporting_standards={
        "k1": "GB/T 21418 卫星定位城市测量规范",
        "k2": "EN ISO 17123 测量仪器性能",
        "k3": "ACSM/ASPRS 精度标准",
    },
    conventions=(
        "坐标系统须明确注明（如CGCS2000/WGS84）与高程基准",
        "测量成果须报告残差与平差后的不确定度",
        "GNSS测量须注明接收机型号、天线高度与观测时长",
        "地形图须标明比例尺与等高线间隔",
        "地籍数据须注明权属来源与宗地编码规则",
    ),
    key_venues=(
        "Journal of Geodesy",
        "Journal of Surveying Engineering",
        "Photogrammetric Engineering & Remote Sensing",
        "Remote Sensing",
        "测绘学报",
    ),
    units_and_formulas_notes=(
        "坐标以度分秒或十进制度表示",
        "高程以米（m）为单位，精度到毫米",
        "面积以m²或公顷（hm²）表示",
        "角度以度分秒（°'\"）或弧度（rad）表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Leica TS16", "Leica TS15", "Trimble S7", "Trimble S6", "Topcon GTS-760", "Total Station Leica", "Trimble GPS", "Trimble GeoVision", "Trimble Field Maps", "Leica Infinity", "Leica GS", "Trimble Business Center", "AutoCAD Civil 3D", "ArcGIS", "QGIS", "Carlson Survey", "Toposuite", "DJI Terra", "CloudCompare", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
