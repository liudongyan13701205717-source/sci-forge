"""休闲娱乐学科论文支持：户外休闲/公园/休闲行为体裁、APA 引用样式与休闲评估口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="recreation_and_leisure",
    aliases=(
        "recreation_and_leisure",
        "休闲娱乐",
        "休闲研究",
        "户外休闲",
        "Recreation and Leisure",
        "Leisure Studies",
        "户外休闲研究",
        "公园管理",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（调研与设计）", "results（使用率与满意度）", "discussion（休闲行为与应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（使用与评估）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；休闲研究与旅游常用 APA）",
    reporting_standards={
        "k1": "休闲评估须遵循 APLMA 标准",
        "k2": "可持续休闲须遵循 LEED 规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "调研方法与样本量须报告",
        "满意度评分给出量表与评分分布",
        "使用率给出分母口径",
        "地点类型与规模须说明",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Leisure Studies",
        "Journal of Park and Recreation Administration",
        "Parks and Recreation Journal",
        "Journal of Leisure Research",
        "Environmental Management",
    ),
    units_and_formulas_notes=(
        "使用率给出人次与占比",
        "满意度评分注明制式",
        "面积用 m² 或 km²",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("RecTrac", "Leisure Soft", "SPSS", "Excel", "R", "QGIS", "ArcGIS", "NVivo", "Tableau", "Power BI", "Qualtrics", "MATLAB", "Python", "SAS", "Stata", "JMP", "OpenRefine", "NetLogo", "Endnote", "Kobo Toolbox"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
