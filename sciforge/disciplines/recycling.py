"""回收利用学科论文支持：废物分类/循环经济/资源化体裁、GB/T 引用样式与回收率口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="recycling",
    aliases=(
        "recycling",
        "回收利用",
        "废物回收",
        "循环经济",
        "Recycling",
        "Waste Recycling",
        "废物管理",
        "资源化利用",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（分类与工艺流程）", "results（回收率与环境影响）", "discussion（机理与循环意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（工艺与环境影响）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714 样式（中国文献规范）与英文文献采用数字编号",
    reporting_standards={
        "k1": "废物分类须遵循 GB/T 19095 分类规范",
        "k2": "碳足迹须遵循 ISO 14067 规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "废物类型与分类须说明",
        "回收率给出分子分母口径",
        "工艺参数（温度、压力、时间）须报告",
        "碳排放数据须给出计算边界",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Waste Management",
        "Resources Conservation and Recycling",
        "Journal of Cleaner Production",
        "Science of the Total Environment",
        "Environmental Science & Technology",
    ),
    units_and_formulas_notes=(
        "回收率用 %",
        "碳排放用 kgCO₂e",
        "处理量用 t 或 t/d",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Waste Management Inc", "Veolia", "Suez", "Terrafirma", "RecycleSoft", "Wastewise", "Circularis", "OpenLCA", "SimaPro", "GaBi", "Python", "MATLAB", "SPSS", "Excel", "R", "QGIS", "ArcGIS", "Tableau", "Endnote", "NetLogo"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
