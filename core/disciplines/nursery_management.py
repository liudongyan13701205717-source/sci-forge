"""苗圃管理学科论文支持：园艺苗木培育/设施栽培体裁、APA 引用样式与栽培参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursery_management",
    aliases=(
        "nursery_management",
        "苗圃管理",
        "Nursery Management",
        "Horticulture Nursery",
        "Plant Nursery",
        "Greenhouse Management",
        "Propagation",
        "Seedling Production",
        "苗木培育",
    ),
    paper_types={
        "research": ("abstract", "introduction（研究背景与假设）", "methodology（栽培处理与观测指标）", "results（生长与产量数据）", "discussion（管理建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（苗圃概况）", "analysis（管理流程分析）", "results（经济与技术效益）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（栽培理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（园艺期刊主流样式）",
    reporting_standards={
        "field_trial": "田间试验遵循随机区组与区组重复规范",
        "economic": "经济分析遵循成本效益与敏感性分析规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "栽培参数按季节与品种记录（温度、湿度、光照、灌溉）",
        "试验设计说明区组、重复、样本量与随机化",
        "生长指标（株高、地径、冠幅）给测量时间与工具",
        "产量与商品率给定义与统计口径",
        "病虫害管理给出防治阈值与用药记录",
    ),
    key_venues=(
        "HortScience",
        "Acta Horticulturae",
        "Journal of the American Society for Horticultural Science",
        "Acta Horticulturae",
        "Scientia Horticulturae",
    ),
    units_and_formulas_notes=(
        "生长指标 cm/mm/g 为单位",
        "土壤含水率以 % 体积含水率给出",
        "光合作用参数 μmol m⁻² s⁻¹",
        "经济分析以元/亩为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NurseryLogix", "HortiTrax", "Farmbook", "PlantUPro", "VegTrak", "QGIS", "ArcGIS", "AutoCAD", "SketchUp", "Adobe Illustrator", "Microsoft Excel", "DHT22 温湿度传感器", "土壤湿度传感器", "自动灌溉控制器", "DJI Phantom 4 RTK", "Google Earth", "GPS 定位仪", "温室环境控制系统", "电子苗圃管理系统", "育苗软件"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
