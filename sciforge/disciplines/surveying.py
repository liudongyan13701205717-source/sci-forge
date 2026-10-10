"""Surveying 学科论文支持：大地测量/工程测量/变形监测/地理信息。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="surveying",
    aliases=(
        "surveying", "Surveying", "测量学",
        "大地测量", "工程测量", "测绘",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与测量问题）",
            "methods（测量方案与技术）",
            "results（精度与成果数据）",
            "discussion（讨论与工程应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（测区与工程背景）",
            "analysis（测量方案与实施）",
            "results（成果与精度）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（测量理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份；测绘学报规范）",
    reporting_standards={
        "precision": "测量精度须报告坐标精度、距离精度与角度精度",
        "instrument": "仪器型号、检定有效期与校准记录须报告",
        "coordinate_system": "坐标系、投影与高程基准须说明",
        "data_processing": "数据处理须报告平差方法、观测值数目与收敛条件",
    },
    conventions=(
        "坐标用经纬度（°N/°E）或投影坐标（m）",
        "距离精度用 mm 或 相对误差（1/xxx）",
        "高程基准须注明（如 1985 国家高程基准）",
        "仪器精度用 mm/km（距离）或 ″（角度）",
        "测量报告须含技术总结、成果图与精度评定",
    ),
    key_venues=(
        "Journal of Geodesy",
        "Journal of Surveying Engineering (ASCE)",
        "Survey Review",
        "Measurement Control",
        "测绘学报",
    ),
    units_and_formulas_notes=(
        "距离用 m 或 mm；高程用 m",
        "角度用 ″（角秒）或 °",
        "坐标精度用 mm 或 m",
        "平差残差用 mm 或 角秒",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("全站仪（徕卡/拓普康）", "GNSS RTK 接收机（Trimble/R3）", "水准仪（自动安平）", "三维激光扫描仪（Leica/Trimble）", "无人机（Drone，大疆/翼辰）", "倾斜摄影测量（Context Capture）", "GIS 软件（ArcGIS/QGIS）", "CAD 制图（AutoCAD Civil 3D）", "BIM 软件（Revit）", "GNSS 数据处理软件（Trimble Business Center）", "激光雷达点云处理（CloudCompare）", "三维激光扫描软件（Cyclone）", "无人机数据处理（DJI Terra）", "大地测量软件（GAMIT/GLOBK）", "变形监测系统（InSAR）", "水下测量设备（测深仪）", "卫星定位（GNSS）数据后处理", "工程测量软件（Civil 3D）", "CASS 成图软件", "三维激光扫描仪（Riegl/Leica RTC360）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
