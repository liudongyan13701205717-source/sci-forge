"""殡葬与墓葬科学学科论文支持：殡葬管理、遗体处理、殡葬文化与公墓规划。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="funeral_services_and_mortuary_science",
    aliases=("funeral_services_and_mortuary_science", "funeral services", "殡葬科学", "殡葬管理", "墓葬学", "殡葬文化", "公墓规划", "遗体处理"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "preservation": "遗体防腐须报告化学浓度、温度与处理时间",
        "management": "殡葬管理须报告标准流程与合规要求",
        "cultural_study": "殡葬文化研究须报告田野调查方法与样本"
    },
    conventions=(
        "防腐处理须标注化学品名称与浓度",
        "温度须注明测量点与仪器",
        "法律法规须引用最新版本",
        "殡葬仪式须尊重文化差异",
        "数据须匿名化处理以保护隐私"
    ),
    key_venues=(
        "Death Studies",
        "Mortality & Mortal Choice",
        "Journal of Death Education",
        "Journal of Thanatology",
        "Omega: Journal of Death and Dying"
    ),
    units_and_formulas_notes=(
        "浓度用 mg/L 或 %",
        "温度用 °C 或 K",
        "时间用 min 或 h",
        "防腐剂量用 mg/kg",
        "气体浓度用 ppm"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Funeral Management Software", "Mortuary Software", "Body Preservation Chemicals", "Temperature Monitor", "Environmental Monitor", "Body Care Software", "Death Records System", "Genealogy Software", "Cemetery Design Software", "Gravestone Carving Software", "Mausoleum Design Software", "Funeral Planning Tool", "Memorial Design Software", "Cemetery Management System", "Death Certificate Software", "Cremation Tracking System", "Funeral Cost Calculator", "Cremation Chamber Monitor", "Funeral Equipment Software", "Funeral Service Scheduling"),
    category="管理学",
    databases=("OpenAlex", "Crossref"),
)
