"""休闲管理学科论文支持：休闲项目/公园/旅游管理体裁、APA 引用样式与项目评估口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="recreation_management",
    aliases=(
        "recreation_management",
        "休闲管理",
        "公园管理",
        "休闲项目",
        "Recreation Management",
        "Park Management",
        "休闲项目管理",
        "旅游目的地管理",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（调研与管理设计）", "results（绩效与评估）", "discussion（管理应用与改进）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（管理分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；休闲与旅游管理研究常用 APA）",
    reporting_standards={
        "k1": "项目评估须遵循 REAC 框架",
        "k2": "旅游管理须遵循 WTTC 规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "管理框架与 KPI 须说明",
        "调研方法与样本量须报告",
        "满意度评分给出量表",
        "绩效指标须给出计算口径",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Journal of Park and Recreation Administration",
        "Parks and Recreation Journal",
        "Tourism Management",
        "Journal of Sustainable Tourism",
        "International Journal of Contemporary Hospitality Management",
    ),
    units_and_formulas_notes=(
        "使用率给出人次与占比",
        "绩效指标注明计算口径",
        "面积用 m² 或 km²",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("RecTrac", "Leisure Soft", "SPSS", "Excel", "R", "QGIS", "ArcGIS", "NVivo", "Tableau", "Power BI", "Qualtrics", "MATLAB", "Python", "SAS", "Stata", "JMP", "OpenRefine", "NetLogo", "Endnote", "Kobo Toolbox"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
