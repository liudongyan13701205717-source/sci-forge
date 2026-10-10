"""伐木学科论文支持：伐木作业、森林经营、木材测量与安全研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tree_felling",
    aliases=("tree_felling", "伐木", "森林采伐", "林木采伐",
             "林业工程", "silviculture", "forest harvesting"),
    paper_types={
        "research": (
            "abstract",
            "introduction（伐木作业背景与研究问题）",
            "materials and methods（材料与方法）",
            "results（木材质量与安全数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（采伐案例）",
            "analysis",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "silviculture": "伐木作业遵循森林采伐规程",
        "safety": "伐木安全遵循 ISO 11513",
        "measurement": "木材测量遵循 EN 13565",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "材积单位 m³",
        "木材密度单位 kg/m³",
        "树木直径单位 cm",
        "木材等级遵循 EN 13565",
        "统计报告遵循 APA 7",
    ),
    key_venues=(
        "Forest Ecology and Management",
        "Canadian Journal of Forest Research",
        "Forestry and Forest Research Papers",
        "森林工程",
        "木材科学与技术",
    ),
    units_and_formulas_notes=(
        "材积单位 m³",
        "密度单位 kg/m³",
        "树木直径单位 cm",
        "伐木强度单位 m³/ha",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("链锯", "采伐联合机", "集材机", "集材拖拉机", "测树仪器", "树干直径卡尺", "倾角仪", "激光测距仪", "无人机", "LiDAR 扫描仪", "ArcGIS", "QGIS", "Python", "R", "Excel", "GNSS 导航仪", "木材分级机", "木材质量分析仪", "Forest Resource Assessment", "伐木安全装备"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
