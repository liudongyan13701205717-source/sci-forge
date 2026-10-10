"""潜水学科论文支持：潜水技术、水下作业与海洋环境研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="diving",
    aliases=(
        "diving", "潜水", "潜水技术",
        "scuba diving", "水肺潜水",
        "commercial diving", "商业潜水",
        "deep diving", "深潜",
        "diving physiology", "潜水生理学",
        "underwater operations", "水下作业",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（潜水问题与背景）",
            "methodology（实验设计、数据采集、分析）",
            "results（生理/技术效果）",
            "discussion（安全改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（技术分析）",
            "outcome（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "safety comparison（安全对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experiment": "潜水条件须完整（深度、时间、气体组成）",
        "physiology": "生理指标须注明测量方法与时间",
        "safety": "潜水事故须按 DAN 分类报告",
    },
    conventions=(
        "深度用 m 表示（ATA 或 bar）",
        "时间用 min 表示",
        "气体组成用 % 表示",
        "生理指标须注明测量时机与方法",
        "潜水计划须注明减压方案与气体切换深度",
    ),
    key_venues=(
        "Undersea Hyperbaric Medicine",
        "Journal of Applied Physiology",
        "Diving and Hyperbaric Medicine",
        "Annals of Clinical and Translational Gastroenterology",
        "Hydrobiology",
    ),
    units_and_formulas_notes=(
        "深度用 m 表示",
        "压力用 ATA 或 bar 表示",
        "气体分压用 ATA 表示",
        "时间用 min 表示",
        "生理指标注明测量方法与参考范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Excel", "Diving Planning Software", "Dive Computer", "Decompression Tables", "Gas Analyzer", "Blood Oxygen Meter", "Pulse Oximeter", "Depth Gauge", "Pressure Gauge", "Water Temperature Sensor", "Visibility Meter", "Current Meter", "Salinity Meter", "pH Meter", "Dissolved Oxygen Meter", "Ultrasonic Thickness Gauge", "Video Analyzer", "Acoustic Doppler Current Profiler"),
    category="工学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
